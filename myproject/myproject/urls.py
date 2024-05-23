# myproject/urls.py
from django.contrib import admin
from django.urls import path
from graphics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/', views.create_graphic, name='create_graphic'),
    path('api/graphic/<int:graphic_id>/<int:value>/', views.get_graphic, name='get_graphic'),
    path('api/get/imageurl/', views.getImageUrl, name='getImageUrl')
]
