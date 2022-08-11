Ensure virtualenv is installed 
   ```bash
    pip install virtualenv
   ```
   ```bash
   pip freeze > requirements.txt
   ```

3. Create virtual environment pipenv
   ```bash
   python -m virtualenv venv
   ```
4. Activate the virtual environment 
   ```bash
    venv\Scripts\activate
   ```

5. install required modules
   ```bash
    pip install -r requirements.txt
   ```
5. pip install django

django-admin startproject dap_backend_api .
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser

pip install djangorestframework
Fixes the problem

python manage.py makemigrations drinks
python manage.py migrate

INSTALLED_APPS = [
    'rest_framework'
    'drinks',
    'django.contrib