from django.db import models
from django.core import validators
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    telephone = models.IntegerField(validators=[validators.RegexValidator(r'1[345678]\d{9}')])
    def __str__(self):
        return self.username
