from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user}"
