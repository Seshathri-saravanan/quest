from django.db import models

class Train(models.Model):
    no = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    source = models.CharField(max_length=20)
    days = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    arrival = models.CharField(max_length=20)
    departure = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class TrainRoutes(models.Model):
    no = models.CharField(max_length=10)
    source1 = models.CharField(max_length=10)
    source2 = models.CharField(max_length=10)
    source3 = models.CharField(max_length=10)
    source4 = models.CharField(max_length=10)
    source5 = models.CharField(max_length=10)
    source6 = models.CharField(max_length=10)
    source7 = models.CharField(max_length=10)
    source8 = models.CharField(max_length=10)
    source9 = models.CharField(max_length=10)
    source10 = models.CharField(max_length=10)
    source11 = models.CharField(max_length=10)
    source12 = models.CharField(max_length=10)
    time1 = models.CharField(max_length=20)
    time2 = models.CharField(max_length=20)
    time3 = models.CharField(max_length=20)
    time4 = models.CharField(max_length=20)
    time5 = models.CharField(max_length=20)
    time6 = models.CharField(max_length=20)
    time7 = models.CharField(max_length=20)
    time8 = models.CharField(max_length=20)
    time9 = models.CharField(max_length=20)
    time10 = models.CharField(max_length=20)
    time11 = models.CharField(max_length=20)
    time12 = models.CharField(max_length=20)

