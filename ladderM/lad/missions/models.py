from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    
    name = models.CharField(max_length=255)
    
    surname = models.CharField(max_length=255)

    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    
    yas = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.username)


class Mission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missions')

    title = models.CharField(max_length=255)

    mission_desc = models.TextField(blank=True, null=True)

    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)

    mission_Finished = models.BooleanField(default=False)
   
    def __str__(self):
        return str(self.title)