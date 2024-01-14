from rest_framework import serializers

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('url', 'description', 'img_size', 'img_pallete',
                  'dominant_color', 'average_color', 'created_at')
        read_only_fields = ['img_size', 'img_pallete', 'dominant_color',
                            'average_color', 'created_at']

    def create(self, validated_data):
        img_url = validated_data.pop('url')
        image = Image(
            **validated_data
        )
        image.set_image(img_url)
        image.save()
        return image
