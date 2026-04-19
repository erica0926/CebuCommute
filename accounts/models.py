from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    types = ((1, 'Regular'), (2, 'Student'), (3, 'Senior'), (4, 'PWD/Pregnant'))
    user_type = models.IntegerField(choices=types)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# ['first_name', 'last_name', 'username', 'email', 'password', 'user_type']