```python
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .utils.image_to_coloring_page import convert_image_to_coloring_page

def index(request):
    return render(request, 'coloring_book_app/index.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            return redirect('settings', image_id=image.id)
    else:
        form = ImageUploadForm()
    return render(request, 'coloring_book_app/upload.html', {'form': form})

def adjust_settings(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            settings = form.save()
            return redirect('convert', image_id=image.id, settings_id=settings.id)
    else:
        form = SettingsForm()
    return render(request, 'coloring_book_app/settings.html', {'form': form, 'image': image})

def convert_image(request, image_id, settings_id):
    image = get_object_or_404(Image, id=image_id)
    settings = get_object_or_404(Settings, id=settings_id)
    coloring_page = convert_image_to_coloring_page(image, settings)
    return redirect('download', coloring_page_id=coloring_page.id)

def download_coloring_page(request, coloring_page_id):
    coloring_page = get_object_or_404(ColoringPage, id=coloring_page_id)
    return render(request, 'coloring_book_app/download.html', {'coloring_page': coloring_page})
```