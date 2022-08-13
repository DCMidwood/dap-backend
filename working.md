Requirements

```bash
pip freeze > requirements.txt
```

3. Create virtual environment virtualenv specifying the Python version (3.10.4)
   ```bash
   python -m virtualenv -p python3.10.4 venv
   ```
4. Activate the virtual environment

   ```bash
    venv\Scripts\activate
   ```

5. install required modules
   ```bash
    pip install -r requirements.txt
   ```

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

python manage.py startapp api
