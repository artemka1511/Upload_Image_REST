from django.core.exceptions import ValidationError
from rest_framework import serializers
from image.models import Image


def file_size(value):
    limit = 0.2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f' Размер {value.name} превышает 200кб. Загрузка всех файлов отменена')


class ImageDetailSerializer(serializers.Serializer):
    image = serializers.ListField(child=serializers.ImageField(validators=[file_size]))

    def create(self, validated_data):
        image = validated_data.pop('image')
        for img in image:
            image = Image.objects.create(image=img)
        return image

    class Meta:
        model = Image
        fields = ('image', )


class ImageListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

