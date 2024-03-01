from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50)
    name1=models.CharField(max_length=50)
    instagram=models.CharField(max_length=250)
    fb=models.CharField(max_length=250)
    image=models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.name




class About(models.Model):
    name=models.CharField(max_length=50)
    name1=models.CharField(max_length=50)
    instagram=models.CharField(max_length=250)
    fb=models.CharField(max_length=250)
    image=models.ImageField(upload_to='media')

class School(models.Model):
    name=models.CharField(max_length=50)
    name1=models.CharField(max_length=50)
    instagram=models.CharField(max_length=250)
    fb=models.CharField(max_length=250)
    image=models.ImageField(upload_to='media')


    def __str__(self):
        return self.name
    
class Contact(models.Model):
        Full_Name=models.CharField(max_length=50)
        email=models.CharField(max_length=50)
        Subject=models.IntegerField()
        Message=models.CharField(max_length=50)


        def __str__(self):
            return self.Full_Name
        