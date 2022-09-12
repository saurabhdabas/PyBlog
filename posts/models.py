from django.db import models

# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=100)
  slug=models.SlugField()
  description=models.TextField()
  date=models.DateField(auto_now_add=True)

  def __str__(self):
    return self.title

  # Instance method that returns first 50 charatcters of post description
  def snippet(self):
    return self.description[:50] + '...'