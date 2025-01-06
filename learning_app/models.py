from django.db import models

# Create your models here.


class UserLogin(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]
    email = models.EmailField()
    name=models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on save
    is_deleted = models.BooleanField(default=False)  # Soft delete flag


class ContentUpload(models.Model):
    user = models.ForeignKey('UserLogin', on_delete=models.CASCADE, related_name='content_uploads')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on save
    is_deleted = models.BooleanField(default=False)  # Soft delete flag