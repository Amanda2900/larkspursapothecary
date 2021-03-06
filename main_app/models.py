from django.db import models
from django.urls import reverse
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

  # creates an easy way to refer to the elements in the db
  def __str__(self):
    return self.name

  # alphabetizes the herb list
  class Meta:
    ordering = ['name']


class Remedy(models.Model):
  name = models.CharField(max_length=100)
  herbs = models.ManyToManyField(Herb, help_text="Hold down “Control”, or “Command” on a Mac, to select more than one.")
  type = models.CharField(
    max_length=1,
    choices=TYPES,
    default=TYPES[0][0]
  )
  description = models.TextField(max_length=500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('remedy_detail', kwargs={'remedy_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=250)
  remedy = models.OneToOneField(Remedy, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for remedy_id: {self.remedy_id} @{self.url}"


