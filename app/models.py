"""
Definition of models.
"""

from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

class Pregunta(models.Model):
     question_theme = models.CharField(max_length=200)
     question_text = models.CharField(max_length=200)
     pub_date = models.DateTimeField('date published')

class Opcion(models.Model):
    question = models.ForeignKey(Pregunta)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)

class Usuario(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)