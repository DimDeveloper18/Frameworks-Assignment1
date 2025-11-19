from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Comment(models.Model):
    comwriter = models.ForeignKey(User, on_delete=models.CASCADE)
    comname = models.CharField(max_length=100)
    comtext = models.TextField()
    commented_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comname