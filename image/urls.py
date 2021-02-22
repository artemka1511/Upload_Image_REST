from django.urls import path
from image.views import ImageCreateView, ImageListView


urlpatterns = [
    path('image/create', ImageCreateView.as_view()),
    path('all/', ImageListView.as_view()),
]