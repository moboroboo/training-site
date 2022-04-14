from django.db import models

class Paper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image = models.ImageField()
    # category = models.one_to_many()
    # tag = 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)