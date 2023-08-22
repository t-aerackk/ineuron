from django.db import models
from .utils import generate_tid

# Create your models here.
class Appointment(models.Model):
    tid = models.CharField(max_length=6 , unique=True)    
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField(default='12:00')
    department=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    message=models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.tid:
            self.tid = generate_tid()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Appointment for {self.id} of {self.name} - {self.department} on {self.date} at {self.time}"

# class ImageHandler(models.Model):
#     img = models.ImageField(upload_to='images',blank=True,null=True)
    