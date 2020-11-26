from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

