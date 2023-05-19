from django.db import models

# Create your models here.

class MedicineModel(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    exp_date = models.DateField()

    def __str__(self):
        return self.name
    