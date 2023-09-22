from django.db import models

# Create your models here.
class user_roles(models.Model):
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
class patient_info(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    medical_history = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.f_name + " " + self.l_name
