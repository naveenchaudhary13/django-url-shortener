from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ShortURL(models.Model):
    """
        Represents a shortened URL.
        
        Attributes:
            user (User): The user who created the URL.
            long_url (str): The original long URL.
            short_code (str): The generated short code for the URL.
            click_count (int): The number of times the URL has been clicked.
            expires_at (datetime): The timestamp when the URL expires.
            created_at (datetime): The timestamp when the URL was created.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    click_count = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_expired(self):
        return self.expires_at and timezone.now() > self.expires_at
    
    def __str__(self):
        return self.short_code
