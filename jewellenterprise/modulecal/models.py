from django.db import models

# Create your models here.


class ModuleData(models.Model):

    serial_no = models.CharField(max_length=50)
    v0 = models.FloatField(null=True, blank=True)
    v180 = models.FloatField(null=True, blank=True)
    v30p_initial = models.FloatField(null=True, blank=True)  # before drawdown
    v30p_final = models.FloatField(null=True, blank=True)  # before drawdown
    v30n_initial = models.FloatField(null=True, blank=True)  # after drawdown
    v30n_final = models.FloatField(null=True, blank=True)  # after drawdown
    test = models.CharField(max_length=50)
    user = models.CharField(max_length=50)


class MobaData(models.Model):

    serial_no = models.CharField(max_length=50)
    v0 = models.FloatField(null=True, blank=True)
    v180 = models.FloatField(null=True, blank=True)
    v90p_initial = models.FloatField(null=True, blank=True)
    v90n_initial = models.FloatField(null=True, blank=True)
    v90p_final = models.FloatField(null=True, blank=True)
    v90n_final = models.FloatField(null=True, blank=True)
    test = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
