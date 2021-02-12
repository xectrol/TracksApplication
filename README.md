# Tracks App

According to the genre typed by the user, this application randomly selects one of the artists of that selected music genre and lists the 5 most popular songs of that artist.

## To run application

Before running the application make sure you correctly set genre.json's absolute file path where addresses to localProjectDirectory\djangoProject\genre.json.
After downloading the app to your local machine, you can start the application with the command below. If you are using PyCharm you can also run "djangoProject" from the toolbar.

```bash
localProjectDirectory\djangoProject\ python manage.py runserver
```
Application starts at localhost:8000/tracks


## External Libs

```python
import responses
```
Used for mocking the  http requests

