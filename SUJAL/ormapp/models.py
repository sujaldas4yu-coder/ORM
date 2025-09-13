
from django.db import models
from django.contrib import admin
class CarsRR_DB(models.Model):
      Car_model=models.CharField(max_length=20)
      Series=models.CharField()
      Color=models.CharField(max_length=15)
      Price=models.IntegerField(primary_key=True) 
      Fancy_number=models.IntegerField()  
class CarsRR_DBAdmin(admin.ModelAdmin):
      list_display=["Car_model","Series","Color","Price","Fancy_number"] 
