from django.db import models


class Author(models.Model):
    """
        Author Model 
    """

    name = models.CharField(max_length=150, unique=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.name

