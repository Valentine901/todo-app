from django.db import models 
from django.contrib.auth.models import User


class Todo(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', default='default')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['-created']