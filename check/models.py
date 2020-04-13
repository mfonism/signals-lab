from django.db import models


class Fluffy(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"A fluffy creature called '{self.name}'"
