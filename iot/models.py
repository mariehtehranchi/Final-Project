from django.db import models
from django.db.models.base import Model

# Create your models here.
class Data(models.Model):
    Temp = models.PositiveIntegerField()
    Humid = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at"]
    
class Control(models.Model):
    ki = models.PositiveIntegerField()
    kp = models.PositiveIntegerField()
    kd = models.PositiveIntegerField()
    auto = models.BooleanField(default=True)
    setpoint = models.PositiveIntegerField()

class Led(models.Model):
    on = models.BooleanField(default=True)
