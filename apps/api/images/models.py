import os
import uuid
from django.db import models
import cloudinary.uploader
from haishoku.haishoku import Haishoku
from PIL import Image as PILImage, ImageStat


class ConvertRgbToHexMixin:
    @staticmethod
    def rgb_to_hex(rgb):
        ##
        rgb = tuple(rgb)
        return '#%02x%02x%02x' % rgb


class Image(models.Model, ConvertRgbToHexMixin):
    id = models.UUIDField(primary_key=True, unique=True, editable=False,
                          default=uuid.uuid4, verbose_name='Public identifier')
    description = models.TextField()
    img_size = models.DecimalField(max_digits=20, decimal_places=3)
    dominant_color = models.CharField(max_length=20)
    average_color = models.CharField(max_length=20)
    img_pallete = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=255)

    def _get_img_size(self, img_url):
        return os.stat(img_url).st_size

    def _get_dominant_color(self, img_url):
        haiskoku_img = Haishoku.loadHaishoku(img_url)
        return self.rgb_to_hex(haiskoku_img.dominant)

    def _get_pallete(self, img_url):
        haiskoku_img = Haishoku.loadHaishoku(img_url)
        pallete = haiskoku_img.palette
        hex_array = [self.rgb_to_hex(x[1]) for x in pallete]
        return str(hex_array)

    def _get_average_color(self, img_url):
        pillow_img = PILImage.open(img_url)
        image_stats = ImageStat.Stat(pillow_img)
        return self.rgb_to_hex(image_stats.median)

    def set_image(self, img_url):
        self.img_size = self._get_img_size(img_url)
        self.dominant_color = self._get_dominant_color(img_url)
        self.img_pallete = self._get_pallete(img_url)
        self.average_color = self._get_average_color(img_url)
        self.url = cloudinary.uploader.upload(img_url)['url']

    def __str__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return 'img <%s:%s>' % (self.description, public_id)
