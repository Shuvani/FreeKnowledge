from django.shortcuts import render
from .models import *
from django.utils.datastructures import OrderedSet
# from .forms import AnswerForm


def topics_for_section(section_id, grade):
    learning_block = Videos.objects.raw('SELECT * FROM learning_videos '
                                        'INNER JOIN learning_sections ls '
                                        'ON ls.id = learning_videos.section_id AND ls.id = %s '
                                        'INNER JOIN learning_topics lt '
                                        'ON lt.id = learning_videos.topic_id '
                                        'WHERE learning_videos.study_year = %s',
                                        [section_id, grade])

    if len(learning_block) == 0:
        return {
            'empty': True
        }

    return {
        'empty': False,
        'section': learning_block[0].section.title,
        'topics': learning_block
    }


def learning_topics(request, grade):
    blocks = list(map(
        lambda x: topics_for_section(x.id, int(grade)),
        Sections.objects.all()
    ))
    print(blocks)
    context = {
        "blocks": blocks
    }

    return render(request, 'learning/learning.html', context)


def learning_content(request, content_id):
    row = Videos.objects.raw('SELECT * FROM learning_videos '
                             'INNER JOIN learning_sections ls '
                             'ON ls.id = learning_videos.section_id '
                             'INNER JOIN learning_topics lt '
                             'ON lt.id = learning_videos.topic_id '
                             'WHERE learning_videos.id = %s', [content_id])

    section = row[0].section_id
    topic = row[0].topic_id
    study_year = row[0].study_year

    tasks = Tasks.objects.raw('SELECT * FROM learning_tasks '
                              'WHERE learning_tasks.section_id = %s '
                              'AND learning_tasks.topic_id = %s '
                              'AND learning_tasks.study_year = %s', [section, topic, study_year])

    # if request.method == 'POST':
    #     form = AnswerForm(request.POST)
    #     if form.is_valid():
    #         answer = form.cleaned_data['answer']
    #         print(answer)
    # else:
    #     form = AnswerForm()
    context = {
        'row': row,
        'tasks': tasks,
        # 'form': form
    }

    return render(request, 'learning/content.html', context)
