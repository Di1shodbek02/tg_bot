from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='pics/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
