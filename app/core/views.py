from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from core.models import Upload


def image_upload(request):
    if request.method == "POST":
        pass
    return render(request, "upload.html")
