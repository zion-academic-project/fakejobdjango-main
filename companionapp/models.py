from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    #Common fields
    is_admin = models.BooleanField(default=False, verbose_name='Is Admin')

    is_company = models.BooleanField(default=False, verbose_name='Is Job Provider')
    is_customer = models.BooleanField(default=False, verbose_name='Is Job Seeker')
    name = models.CharField(max_length=100, default='User')
    mobile_number = models.CharField(max_length=20, default='Nil')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    verified = models.BooleanField(default=False, verbose_name='Is Verified')

    #Job Seeker fields
    aboutme = models.TextField(max_length=1000, default='Nil')
    resume_file = models.FileField(upload_to='resumes', blank=True, null=True)


    @property
    def imageURL(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''
        return  url
    
    def __str__(self):
        return self.username
    

class Job_posting(models.Model):
    companyid = models.IntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    location_job = models.CharField(max_length=300, default='Nil', blank=True, null=True)
    department = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    company_profile = models.TextField(max_length=1000, default='Nil', blank=True, null=True)
    job_description = models.TextField(max_length=1000, default='Nil', blank=True, null=True)
    job_requirements = models.TextField(max_length=1000, default='Nil', blank=True, null=True)
    job_benefits = models.TextField(max_length=1000, default='Nil', blank=True, null=True)
    employment_type = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    required_experience = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    required_education = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    industry = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    job_function = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    verified = models.BooleanField(default=False, verbose_name='Is Verified')

    def __str__(self):
        return self.job_title
    

class Applications(models.Model):
    postingid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    companyid = models.IntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    location_job = models.CharField(max_length=300, default='Nil', blank=True, null=True)
    department = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    company_profile = models.TextField(max_length=1000, default='Nil', blank=True, null=True)
    job_description = models.TextField(max_length=1000, default='Nil', blank=True, null=True)
    job_requirements = models.TextField(max_length=1000, default='Nil', blank=True, null=True)
    job_benefits = models.TextField(max_length=1000, default='Nil', blank=True, null=True)
    employment_type = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    required_experience = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    required_education = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    industry = models.CharField(max_length=255, default='Nil', blank=True, null=True)
    job_function = models.CharField(max_length=255, default='Nil', blank=True, null=True)    
    application_status = models.BooleanField(default=False, verbose_name='Application Status')
    application_messsage = models.TextField(max_length=1000, default='Nil', blank=True, null=True)


    def __str__(self):
        return self.job_title
    