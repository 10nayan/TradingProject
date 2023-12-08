# Nifty Price Tracker App using Django Python
![Screenshot from 2023-12-08 22-34-55](https://github.com/10nayan/TradingProject/assets/88362758/5bcad675-1333-41d3-9acd-2e33484513a5)
## Introduction
This website is built with Django which is a python framework for web development.
This app has basic feature of uploading a CSV file of Nifty price data and this returns a JSON file with price candle data within the user entered timeframe
## Files in the project
- **/MainApp/views.py**: This is the app file that contains the logic of all the view functions in the backend which generate dynamic contents to HTML template.
- **/MainApp/forms.py**: python app file  required for creatingform in this appliation.
- **/MainApp/urls.py**: python app file  required for url mapping to all the view functions.
- **/MainApp/admin.py**: python app file  required for registering to django-administration of this appliation.
- **/MainApp/apps.py**: python app file  required for registering the MainApp app to django TradingProject of this appliation.
- **/TradingProject/**: python main project folder in which MainApp app is created.
- **requirements.txt**: list of Python packages installed (also required for Heroku)
- **MainApp/templates/**: folder with all HTML files
- **MainApp/static/**: for all JS scripts and CSS files
## Usage
### Clone/Modify app
1. Modify MainApp folder or create a new app in the main TradingProject project folder.

    For modifying existance code or creating new app, These lines need to be edited in TradingProject/settings.py are shown below:
```python
SECRET_KEY ='<your secret key>'
ALLOWED_HOSTS = ['<your allowed host>']
DATABASES = {<your database settings>}
```
2. Run makemigrations and migrate command from the terminal to create the table with the link to your database.

3. Run createsuperuser command to register to django admin panel.

4. Create new app in TradingProject project folder using following command,
    
```console
C:\<path to TradingProject>\python manage.py startapp <your app name>
```