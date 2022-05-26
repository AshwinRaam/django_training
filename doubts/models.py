from django.db import models

GENDER = [
    ('F', 'Female'),
    ('M', 'Male')
]


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    contact_no = models.CharField(max_length=13)
    gender = models.CharField(max_length=1, choices=GENDER)
    subject = models.CharField(max_length=30)


class Trainee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    contact_no = models.CharField(max_length=13)
    gender = models.CharField(max_length=1, choices=GENDER)
    exp = models.PositiveSmallIntegerField()


class doubts(models.Model):
    name = models.CharField(max_length=20)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    question_from = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    answer_by = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    when_asked = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
