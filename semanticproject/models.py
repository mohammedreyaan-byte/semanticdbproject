from django.db import models


class SemanticModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name
