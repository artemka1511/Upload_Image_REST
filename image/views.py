from rest_framework import generics, permissions
from image.serializers import ImageDetailSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from image.models import Image
from image.serializers import ImageListDetailSerializer


class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageDetailSerializer
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = [permissions.IsAuthenticated]


class ImageListView(generics.ListAPIView):
    serializer_class = ImageListDetailSerializer
    queryset = Image.objects.all()
