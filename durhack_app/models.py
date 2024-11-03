from django.db import models
from django.utils import timezone

# Create your models here.


class Predictions(models.Model):
    # The possible predictions the model can make in the 'predictions' field
    # defined by: (<database name>, <human readible name>)
    PREDICT_OPTIONS = [
        ('survives', 'Survives'),
        ('dead', 'Dead')
    ]

    # Prediction table fields (or columns) are defined by creating attributes
    # and assigning them to field instances such as models.CharField()
    predict_datetime = models.DateTimeField(default=timezone.now)
    age = models.PositiveIntegerField()
    gender = models.DecimalField(decimal_places=2, max_digits=3)
    sick = models.DecimalField(decimal_places=2, max_digits=3)
    went_to_lifeboat = models.DecimalField(decimal_places=2, max_digits=3)
    prediction = models.CharField(choices=PREDICT_OPTIONS, max_length=10)