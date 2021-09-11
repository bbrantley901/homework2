from django.db import models

class myModel(models.Model):
    name = models.CharField(max_length=45)
    number = models.IntegerField(default =0)

class MyOtherModel(models.Model):
    name = models.ForeignKey(to = myModel, default = 0, on_delete = models.SET_DEFAULT)
    
# Create your models here.
