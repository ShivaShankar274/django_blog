from django.db import models
from datetime import datetime

class Blog(models.Model):
    title=models.CharField(max_length=50) 
    description=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    


    
