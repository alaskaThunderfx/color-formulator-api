from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Client(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  date_added = models.DateField()
  starting_level = models.IntegerField(
      default=5,
      validators=[MaxValueValidator(10), MinValueValidator(1)]
  )
  colored = models.BooleanField()
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The client named '{self.first_name}' was added {self.date_added}. Their starting level is {self.starting_level}. It is colored: {self.colored}"

  def as_dict(self):
    """Returns dictionary version of Client models"""
    return {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'date_added': self.date_added,
        'starting_level': self.starting_level,
        'colored': self.colored
    }
