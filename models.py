from django.db import models
from django.contrib.auth.models import AbstractUser


class UserCustModel(AbstractUser):
    
    def __str__(self):
            return self.username
    

class PersonalInfoModel(models.Model):
      user = models.OneToOneField(UserCustModel, on_delete=models.CASCADE)
      name = models.CharField(max_length=51, null=True, blank=True)
      address = models.TextField(null=True, blank=True)
      phone = models.CharField(max_length=20, blank=True, null=True)
      proffesion = models.CharField(max_length=520, blank=True, null=True)
      bio = models.CharField(max_length=120, blank=True, null=True)
      additionalink = models.CharField(max_length=150,null=True)
      about = models.TextField(null=True, blank=True)
      image = models.ImageField(upload_to='media/image', blank=True, null=True)

      def __srt__(self):
            return self.name


class ProjectModel(models.Model):
      titel = models.CharField(max_length=250, null=True, blank= True)
      discription = models.TextField(null=True, blank=True)
      image = models.ImageField(upload_to='media/project',null=True, blank=True)
      technology_used = models.CharField(max_length=250, null=True, blank=True)
      github_link = models.CharField(max_length=250, blank=True, null=True)
      live_demo = models.CharField(max_length=200,blank=True, null=True)
      create_at = models.DateField(auto_now_add=True,null=True,blank=True)

      def __srt__(self):
            return self.titel
      

class TechnicalModel(models.Model):
      skiil_name = models.CharField(max_length=200,null=True,blank=True)
      discription = models.TextField(null=True,blank=True)
      level = models.FloatField(null=True,blank=True)
      languase = models.CharField(max_length=250, blank=True, null=True)

      def __str__(self):
            return f"{self.skiil_name}"
      

class ExprinceModel(models.Model):
      company_name = models.CharField(max_length=250, blank=True, null=True)
      job_position = models.CharField(max_length=250, blank=True, null=True)
      job_titel = models.CharField(max_length=250, blank=True, null=True)
      start_date = models.DateField(auto_now_add=True, null=True, blank=True)
      end_date = models.DateField(auto_now_add=True, null=True, blank=True)
      achivments =models.TextField(null=True, blank=True)


      def __str__(self):
            return f'{self.company_name}'
      
class EducationModel(models.Model):
      University = models.CharField(max_length=250, blank=True, null=True)
      Department = models.CharField(max_length=250,blank=True, null=True)
      passing_yaer = models.DateField(auto_now_add=True, null=True, blank=True)
      result = models.FloatField(null=True, blank=True)


      def __str__(self):
            return  f"{self.University}"
