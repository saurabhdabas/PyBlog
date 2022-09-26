from django.db import models

# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=100)
  slug=models.SlugField()
  description=models.TextField()
  date=models.DateField(auto_now_add=True)
  thumbnail=models.ImageField(default='default.png',blank=True)

  def __str__(self):
    return self.title

  # Instance method that returns first 50 charatcters of post description
  def snippet(self):
    return self.description[:50] + '...'

  # Instance method to Calculate the Read time by assuming a human reads 200 words per minute
  def readtime(self):
    wordsArray = self.description.split()
    readingtime = len(wordsArray)/200
    return round(readingtime,1)
