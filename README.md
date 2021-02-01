## Структура приложения
* deploy - скрипты и файлы для деплоя приложения на сервер
* freeknowledge - основные файлы django приложения (автоматически создаются при создании нового приложения)
* learning - Все для страницы "Обучение"
* olympiads - Все для страницы "Главная" и "Олимпиады"
* templates - базовые шаблоны всего приложения

## Установка на новый сервер:
* freeknowledge/settings.py -> изменить первый ip-address в ALLOWED_HOSTS на public ip вашего сервера
* deploy/default -> в строке с комментарием вставить свой ip-address
* подключиться к серверу и подключить дополнительный жестуий диск (для AWS EC2)
  ```html
      lsblk <!--Чтобы посмотреть какие жесткие диски подключены к инстансу-->
      sudo file -s /dev/xvdb 
      sudo mkfs -t ext4 /dev/xvdb <!--Создать файловую систему на этом диске-->
      sudo mkdir /data <!--Создаем директорию на сервере-->
      sudo mount /dev/xvdb /data <!--Маунтим туда диск-->
      lsblk <!--Проверяем что все сработало-->
      <!--Поменяем конфиг так, чтобы маунтить этот диск автоматически после каждого ребута-->
      sudo cp /etc/fstab /etc/fstab.orig
      sudo vim /etc/fstab
        <!--Написать это в файл-->
        LABEL=cloudimg-rootfs	/	 ext4	defaults,discard	0 0
        /dev/xvdb /data ext4 defaults,nofail 0 2
      sudo file -s /dev/xvdb
    ```
* in GitHub select deploy/deploy.sh file -> click on Raw -> copy the URL-> in the server's command line enter the folwing comand 
    ```html
      curl -sL <your_url> | sudo bash -
    ```

## Перезалить на сервер
* push changes to the GitHub
* 
    ```html
      sudo bash /data/venv/freeknowledge/deploy/update.sh
    ```
  
## Удалить с сервера
```html
  sudo umount /data
```

## Если вдруг не выходит зайти в админку
```html
  chown nobody /data/venv/freeknowledge/
  chown nobody /data/venv/freeknowledge/db.sqlite3
```

## Обновить сертификат 2 мая 
```html
    sudo letsencrypt certonly --webroot -w /data/venv/freeknowledge -d knowfree.ru
```
