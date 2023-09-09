```python
from django.db import models

class Image(models.Model):
    original_image = models.ImageField(upload_to='original_images/')
    converted_image = models.FileField(upload_to='converted_images/', blank=True, null=True)
    conversion_method = models.CharField(max_length=50, default='method1')
    settings = models.JSONField(default=dict)

    def __str__(self):
        return f"Image {self.id}"
```