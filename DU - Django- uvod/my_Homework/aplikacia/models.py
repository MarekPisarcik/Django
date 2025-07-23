from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
