from django.db import models
from django.contrib.auth.models import User

TYPES = (
  ("T", "Tonic"),
  ("P", "Poultice"),
  ("S", "Sachet")
)

RARITY = (
  ("U", "Uncommon"),
  ("C", "Common")
)

class Herb(models.Model):
  name = models.CharField(max_length=100)
  rarity = models.CharField(
    max_length=1,
    choices=RARITY,
    default=RARITY[0][0]
  )
  info = models.TextField(max_length=250)
  uses = models.TextField(max_length=500)

  def __str__(self):
    return self.name


class Remedy(models.Model):
  name = models.CharField(max_length=100)
  herbs = models.ManyToManyField(Herb)
  type = models.CharField(
    max_length=1,
    choices=TYPES,
    default=TYPES[0][0]
  )
  description = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

