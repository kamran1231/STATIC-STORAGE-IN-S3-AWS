from django.shortcuts import render,redirect
from rest_framework import viewsets
from .serializers import PhotoSerializer
from .models import Photo
from rest_framework.permissions import BasePermission,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print(request.user)
        return Response({'Success: You are authenticated'})


#Basic-function for add photo
# def addPhoto(request):
#     if request.method == 'POST':
#         data = request.POST['uname']
#         image = request.FILES.get('image')
#         photo = Photo.objects.create(name=data,image=image)
#
#         return redirect('addphoto')
#     return render(request,'home.html')


class PhotoListAV(APIView):
    def get(self,request):
        photo = Photo.objects.all()
        serializer = PhotoSerializer(photo,many=True)
        return Response(serializer.data)

    permission_classes = [IsAuthenticated]
    def post(self,request):

        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer
#
#
#     def upload_docs(request):
#         try:
#             file = request.data['file']
#         except KeyError:
#             raise ParseError('Request has no resource file attached')
#         product = Product.objects.create(image=file, ....)