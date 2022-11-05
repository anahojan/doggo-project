from django.db import models
from django.contrib.auth.models import User

#create detabase tables. We are creating python class to represent a database table
#class name is the name of the database
# attributes inside the class are column names
#id is the id of the database are rows of the database
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name






class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #null = True means that the database can null
    #participants = 
    updated = models.DateTimeField(auto_now_add=True)
    # updated takes a snapshot of the database and updates the database accordingly (everytime we save)
    created = models.DateTimeField(auto_now_add=True)
    #created saves the timestamp of the database when creating. It doesn't change.

    def __str__(self):
        return self.name

#when we add a model the first thing we need to do is make migrations $ python3 manage.py makemigrations
# it creates a file under migrations which includes the sql code for the database
# *(base) anahojan@HojanPC:~/Documents/DOGGO/DOGGO-project$ python3 manage.py makemigrations
# Migrations for 'base':
#   base/migrations/0001_initial.py
#     - Create model Room
# (base) anahojan@HojanPC:~/Documents/DOGGO/DOGGO-project$ python3 manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, base, contenttypes, sessions
# Running migrations:
#   Applying base.0001_initial... OK #

# creating admin to view the database
# (env) anahojan@HojanPC:~/Documents/DOGGO/DOGGO-project$ python3 manage.py createsuperuser
# Username (leave blank to use 'anahojan'): 
# Email address: 89191228@student.upr.si
# Password: 
# Password (again): 
# Superuser created successfully.


class Message(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #if a room gets deleted all of the messages inside this room will be deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)
    # updated takes a snapshot of the database and updates the database accordingly (everytime we save)
    created = models.DateTimeField(auto_now_add=True)
    #created saves the timestamp of the database when creating. It doesn't change.

    def __str__(self):
        return self.body[0:50]
        # in the preview we want first 50 charachter.