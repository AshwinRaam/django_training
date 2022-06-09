
from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    contact_no = models.CharField(max_length=13)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Trainee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    contact_no = models.CharField(max_length=13)
    exp = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Doubts(models.Model):
    name = models.CharField(max_length=20)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    question_from = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    answer_by = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    when_asked = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=20)
