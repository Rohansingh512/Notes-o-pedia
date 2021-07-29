from django.db import models
#from .models import Contact
# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=100)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'massage from ' + self.name + '-' + self.email

class Books(models.Model):
    sno = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    teacher=models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    file=models.FileField(upload_to='static', blank=True)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'massage from ' + self.name + '-' + self.email









