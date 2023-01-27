from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import random

#admin
#wrapupprojects

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile-pictures/', null=True, blank=True)
    githubProfileUrl = models.URLField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        if(self.user.first_name):
            return self.user.first_name
        else:
            return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def create_projectCode():
    not_unique = True
    while not_unique:
        unique_code = random.randint(100000000, 999999999)
        if not Project.objects.filter(projectCode=unique_code):
            not_unique = False
        return unique_code


class Project(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)
    githubRepositoryUrl = models.URLField(null=True, blank=True)
    projectAdmin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    projectCode = models.PositiveIntegerField(unique=True, default=create_projectCode)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)+'-'+str(self.project.title)
        

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=1024, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_started = models.BooleanField(default=False)
    started_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='task_started_by')
    is_completed = models.BooleanField(default=False)
    completed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='task_completed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.title)+'-'+str(self.project.id)


class Meeting(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=1024, null=True, blank=True) 
    description = models.TextField(null=True, blank=True)
    meetingUrl = models.URLField(null=True, blank=True)
    agendas = models.FileField(upload_to='meeting-agendas/', null=True, blank=True)
    notes = models.FileField(upload_to='meeting-notes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    
    




