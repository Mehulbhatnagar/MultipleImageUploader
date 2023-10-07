from django.db import models
import uuid

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    caption = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
