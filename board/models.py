from django.db import models

# Create your models here.
class Posting(models.Model):
    name = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name + ':' + self.title

class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    text = models.CharField(max_length=200, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        ordering = ['created_date']
        return self.name + ':' + self.text
