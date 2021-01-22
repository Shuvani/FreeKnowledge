## Структура приложения
* deploy - скрипты и файлы для деплоя приложения на сервер
* freeknowledge - основные файлы django приложения (автоматически создаются при создании нового приложения)
* learning - Все для страницы "Обучение"
* olympiads - Все для страницы "Главная" и "Олимпиады"
* templates - базовые шаблоны всего приложения

## Установка на новый сервер:
* freeknowledge/settings.py -> изменить первый ip-address в ALLOWED_HOSTS на public ip вашего сервера
* deploy/default -> в строке с комментарием вставить свой ip-address   
* in GitHub select deploy/deploy.sh file -> click on Raw -> copy the URL-> in the server's command line enter the folwing comand 
    ```html
      curl -sL <your_url> | sudo bash -
    ```

## Перезалить на сервер
* push changes to the GitHub
* 
    ```html
      cd /opt/venv/freeknowledge/
      sudo sh ./deploy/update.sh
    ```