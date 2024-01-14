from rest_framework import status, viewsets
from rest_framework.response import Response

from images.serializers import ImageSerializer
from images.models import Image


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        image_data = request.data.get('image')
        serializer = self.get_serializer(data=image_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'image': serializer.data},
                        headers=headers,
                        status=status.HTTP_201_CREATED)
