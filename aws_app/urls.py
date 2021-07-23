


from django.urls import path
from . import views
from .views import DemoView,PhotoListAV



urlpatterns = [
    # path('add/',views.addPhoto,name='addphoto'),
    path('demo/',DemoView.as_view()),
    path('photo-add/',PhotoListAV.as_view()),
]