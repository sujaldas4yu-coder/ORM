# Ex02 Django ORM Web Application
## Date: 13/09/2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py


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


admin.py

from Django.contrib import admin
from .models import CarsRR_DB,CarsRR_DBAdmin
admin.site.register(CarsRR_DB,CarsRR_DBAdmin)

```
## OUTPUT
![alt text](<Screenshot 2025-09-13 142625.png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
