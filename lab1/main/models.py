from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    POSITION_CHOICES = {
        ('secretary', 'Secretary'),
        ('associate director', 'Associate Director'),
        ('director', 'Director'),
    }
    user = models.ForeignKey(User, on_delete = models.PROTECT, null=True)
    name = models.CharField(max_length = 50, verbose_name = "Name")
    surname = models.CharField(max_length = 50, verbose_name = "Surname")
    position = models.CharField(max_length = 150, choices = POSITION_CHOICES)
    address = models.CharField(max_length = 50, verbose_name = "Address")
    phone = models.CharField(max_length = 14)
    
    def __str__(self):
        return 'Name - {0}, Surname - {1}, Position - {2}'.format(self.name, self.surname, self.position)