from django.db import models

# Create your models here.
class BikeUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    mobile = models.CharField(max_length=12, default='',null=True)
    password = models.CharField(max_length=255, default='')

    class Meta:
        managed = True
        db_table = 'bikeuser'


class BikeData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default='')
    subtitle = models.CharField(max_length=500, default='')
    details = models.TextField(default='')
    feature_image = models.CharField(max_length=500, default='')
    author = models.CharField(max_length=255, default='')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'bikedata'