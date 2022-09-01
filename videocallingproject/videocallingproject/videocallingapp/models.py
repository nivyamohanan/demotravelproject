from django.db import models
#Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to="pics")
    desc= models.TextField()
    def __str__(self):
        return self.name
class team(models.Model):
    team_img=models.ImageField(upload_to="team_pics")
    team_name=models.CharField(max_length=250)
    team_desc=models.TextField()
    def __str__(self):
        return self.team_name