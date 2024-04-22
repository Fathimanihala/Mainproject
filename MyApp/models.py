from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)


class Route(models.Model):
    routename=models.CharField(max_length=50)
    fromplace=models.CharField(max_length=50)
    toplace=models.CharField(max_length=50)

class Bus(models.Model):
    busregno = models.CharField(max_length=50)
    busmodel = models.CharField(max_length=50)
    chasisnumber=models.CharField(max_length=50)
    manufacturename = models.CharField(max_length=50)
    ROUTE=models.ForeignKey(Route,on_delete=models.CASCADE)

class Driver(models.Model):
    name = models.CharField(max_length=50,default='')
    image = models.CharField(max_length=250)
    email = models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=100,default='')
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default='')

class Allocate(models.Model):
    BUS=models.ForeignKey(Bus,on_delete=models.CASCADE)
    DRIVER=models.ForeignKey(Driver,on_delete=models.CASCADE)


class Busstop(models.Model):
    ROUTE = models.ForeignKey(Route, on_delete=models.CASCADE)
    placename = models.CharField(max_length=50)
    longitude=models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)

class Schedule(models.Model):
    BUS = models.ForeignKey(Bus, on_delete=models.CASCADE)
    BUSSTOP = models.ForeignKey(Busstop, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    trip=models.CharField(max_length=50)



class Notification(models.Model):
    notification = models.CharField(max_length=50)
    date = models.DateField()

class  EmergencyNotification(models.Model):
    notification = models.CharField(max_length=50)
    date = models.DateField()

class Location(models.Model):
    BUS = models.ForeignKey(Bus, on_delete=models.CASCADE)
    placename = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)


class User(models.Model):
    LOOGIN=models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phoneno = models.BigIntegerField()
    email = models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    pincode=models.IntegerField()
    district=models.CharField(max_length=50)
    idproof=models.CharField(max_length=500)






