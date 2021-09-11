from django.contrib import admin
from .models import myModel, MyOtherModel

admin.site.register(myModel)
admin.site.register(MyOtherModel)

# Register your models here.
