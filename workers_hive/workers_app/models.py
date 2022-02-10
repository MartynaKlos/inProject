from django.db import models

OCCUPATIONS = [
    (1, "manager"),
    (2, "junior specialist"),
    (3, "specialist"),
    (4, "senior specialist"),
    (5, "consultant"),
    (6, "assistant")
]

class Worker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    age = models.IntegerField()
    occupation = models.IntegerField(choices=OCCUPATIONS)
    photo = models.ImageField(upload_to='photos/', verbose_name='Photo', null=True)

class OccupationAgeAvg(models.Model):
    unique_id = models.IntegerField(primary_key=True)
    occupation = models.IntegerField()
    avg_age = models.FloatField()

    class Meta:
        managed = False
        db_table = 'report'
