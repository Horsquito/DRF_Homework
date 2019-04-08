from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    OPEN = 'OP'
    IN_PROCESS = 'I_P'
    IN_TEST = 'I_T'
    DONE = 'DO'
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (IN_PROCESS, 'In process'),
        (IN_TEST, 'In test'),
        (DONE, 'Done'),
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=OPEN,
    )

class Performer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=None)
