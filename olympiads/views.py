from django.shortcuts import render
from datetime import datetime
from django.utils.datastructures import OrderedSet
from .models import *


def index(request):
    # main page
    # three nearest olympiads from the timetable
    events = Timetable.objects.raw('SELECT * FROM olympiads_olympiads AS oo '
                                   'INNER JOIN olympiads_timetable ot ON oo.id = ot.olympiad_id '
                                   'WHERE ot.start_date IS NOT NULL '
                                   'AND ot.start_date >= %s '
                                   'ORDER BY ot.start_date '
                                   'LIMIT 3', [datetime.now()])

    # new news
    news = News.objects.filter(show=True)

    context = {
        'events': events,
        'news': news
    }
    return render(request, 'olympiads/index.html', context)


def materials_for_olympiad(olympiad_id, grade):
    # helped function for materials()
    # materials for the special olympiad and study_year
    olympiad_materials = Materials.objects.raw('SELECT * FROM olympiads_materials '
                                               'INNER JOIN olympiads_olympiads oo '
                                               'ON oo.id = olympiads_materials.olympiad_id AND oo.id = %s '
                                               'INNER JOIN olympiads_stages os '
                                               'ON os.id = olympiads_materials.stage_id '
                                               'WHERE olympiads_materials.study_year = %s '
                                               'ORDER BY olympiads_materials.year DESC, os.id ASC',
                                               [olympiad_id, grade])

    # if there is no content for this olympiad
    if len(olympiad_materials) == 0:
        return {
            'empty': True
        }

    # add field year and stage.title to olympiad
    years = list(OrderedSet(map(lambda el: el.year, olympiad_materials)))
    stages = list(OrderedSet(map(lambda el: el.stage.title, olympiad_materials)))

    materials = {}

    # create a matrix with materials sorted by years and stages
    for year in years:
        materials[year] = {}
        for stage in stages:
            materials[year][stage] = []
            for mat in olympiad_materials:
                if mat.year == year and mat.stage.title == stage:
                    materials[year][stage].append(mat)

    return {
        'empty': False,
        'olympiad': olympiad_materials[0].olympiad.title,
        'short_olympiad_name': olympiad_materials[0].olympiad.short_name,
        'stages': stages,
        'years': years,
        'materials': materials
    }


def materials(request, grade):
    # olympiads materials page
    # for each olympiad find the materials
    tables = list(map(
        lambda x: materials_for_olympiad(x.id, int(grade)),
        Olympiads.objects.all()
    ))

    context = {
        "tables": tables
    }

    return render(request, 'olympiads/materials.html', context)


def timetable(request):
    # main olympiads page
    # rows for the table of this year olympiads
    rows = Timetable.objects.raw('SELECT * FROM olympiads_timetable '
                                 'INNER JOIN olympiads_olympiads oo '
                                 'ON oo.id = olympiads_timetable.olympiad_id '
                                 'WHERE olympiads_timetable.finished = False')
    mapping = {}
    # group rows by olympiads
    for row in rows:
        if row.olympiad.title in mapping:
            mapping[row.olympiad.title].append(row)
        else:
            mapping[row.olympiad.title] = [row]

    context = {
        'rows': mapping
    }
    return render(request, 'olympiads/timetable.html', context)
