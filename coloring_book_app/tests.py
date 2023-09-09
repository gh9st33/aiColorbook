```python
from django.test import TestCase, Client
from django.urls import reverse
from .models import ImageUpload
from .forms import ImageUploadForm, SettingsForm
import os

class ImageUploadTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.upload_url = reverse('upload')

    def test_image_upload(self):
        with open('coloring_book_app/tests/test_image.jpg', 'rb') as img:
            response = self.client.post(self.upload_url, {'image': img}, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ImageUpload.objects.exists())

class ImageUploadFormTestCase(TestCase):
    def test_valid_form(self):
        with open('coloring_book_app/tests/test_image.jpg', 'rb') as img:
            form = ImageUploadForm(files={'image': img})
        self.assertTrue(form.is_valid())

class SettingsFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {'conversion_method': 'method1', 'adjustment_level': 3}
        form = SettingsForm(data=form_data)
        self.assertTrue(form.is_valid())

class ConversionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.settings_url = reverse('settings')

    def test_conversion(self):
        with open('coloring_book_app/tests/test_image.jpg', 'rb') as img:
            self.client.post(reverse('upload'), {'image': img}, format='multipart')
        response = self.client.post(self.settings_url, {'conversion_method': 'method1', 'adjustment_level': 3})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists('coloring_book_app/static/coloring_book_app/pdf/test_image.pdf'))
```