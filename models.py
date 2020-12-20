from django.db import models
# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField(max_length=50,primary_key=True)
    user_password=models.CharField(max_length=50)
    user_mobile=models.IntegerField()
    class Meta:
        db_table='user'
class Car(models.Model):
    car_number=models.CharField(max_length=50,primary_key=True)
    user_email=models.EmailField(max_length=50)
    car_model=models.CharField(max_length=50)
    car_seats=models.IntegerField()
    car_source=models.CharField(max_length=50)
    car_destination=models.CharField(max_length=50)
    car_depttime=models.CharField(max_length=50)
    car_retntime=models.CharField(max_length=50)
    
    class Meta:
        db_table='user_car'

