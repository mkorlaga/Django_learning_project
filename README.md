# Django learning path project

In this repository I'm storing my progress over learning Django framework. <br>
There is a LOT to learn.

## Reproduction steps

1. Clone repository:
``` git clone https://github.com/mkorlaga/Django_learning_project.git```
    > Due to safety issues to run project properly you need to add your SECRET_KEY in settings.py
2. Make yourself a stable and save virtual environment:
    ```
    cd Django_learning_project
    pyhton -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. Prepare database (default is SQLite3):

    ```
    python manage.py migrate
    python manage.py createsuperuser
    ```
    > Due to your lack of populated database you might not see items in your views.<br>
    > You can always add your items.

4. Run server:
` python manage.py runserver`

