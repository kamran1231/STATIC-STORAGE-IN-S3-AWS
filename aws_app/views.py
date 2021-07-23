from django.shortcuts import render,redirect
from .models import Photo
# Create your views here.


def addPhoto(request):
    if request.method == 'POST':
        data = request.POST['uname']
        image = request.FILES.get('image')
        photo = Photo.objects.create(name=data,image=image)

        return redirect('addphoto')
    return render(request,'home.html')