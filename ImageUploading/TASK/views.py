from django.shortcuts import render, redirect
from django.views import View
from .models import UploadedImage
from .forms import UploadImageForm

class UploadImageView(View):
    template_name = 'upload_image.html'

    def get(self, request):
        form = UploadImageForm()
        images = UploadedImage.objects.all()
        return render(request, self.template_name, {'form': form, 'images': images})

    def post(self, request):
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
        return render(request, self.template_name, {'form': form})

def list_images(request):
    images = UploadedImage.objects.all()
    return render(request, 'list_images.html', {'images': images})