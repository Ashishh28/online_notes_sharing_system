from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='notes_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)  # ✅ NEW

    def __str__(self):
        return self.title
