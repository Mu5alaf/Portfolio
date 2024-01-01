from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    about = models.TextField(max_length=300,null=True)
    picture = models.ImageField(upload_to="media",blank=True, null=True,help_text="Upload an image file (JPEG, PNG, etc.)")
    github_url = models.URLField(max_length=200, blank=True, null=True, help_text="Enter the website URL")
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, help_text="Enter the website URL")
    def __str__(self):
        return self.name


class Skills(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    skill= models.CharField(max_length=255,default="Your skills ")
    experience = models.CharField(max_length=255,default="Your experience years ")
    def __str__(self):
        return self.skill
    
class Project (models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    picture_snap = models.ImageField(upload_to="media/project",blank=True, null=True,help_text="Upload an image file (JPEG, PNG, etc.)")
    name = models.CharField(max_length=255,default="Your project ")
    tools = models.CharField(max_length=255,default="Project tools")
    project_url = models.URLField(max_length=200, blank=True, null=True, help_text="Enter the project URL")
    def __str__(self):
        return self.name