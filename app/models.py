from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# Custom User model
class Student(AbstractUser):
    # Remove default fields
    first_name = None
    last_name = None
    username = None

    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Additional fields for mental health project
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email + password are enough

    def __str__(self):
        return self.email


# card model 
from django.db import models

class DailyPositiveCard(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='positive_cards/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# journal model 
class JournalEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='journal_entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.student.email}"   

# mood suggestion model 
class EmotionPrompt(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    prompt_text = models.TextField()

    def __str__(self):
        return self.title
     