from PIL import Image

from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class NotebookAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red;">При загрузке изображение с разрешением больше {}x{} оно будет обрезано!</span>
            """.format(
                *Product.MIN_RESOLUTION
            )
        )

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     img = Image.open(image)
    #     min_height, min_width = Product.MIN_RESOLUTION
    #     max_height, max_width = Product.MAX_RESOLUTION
    #     if image.size > Product.MAX_IMAGE_SIZE:
    #         raise ValidationError('Размер изображения не должен привышать 3MB!')
    #     if img.height < min_height or img.width < min_width:
    #         raise ValidationError('Разрешение изображения меньше минимального!')
    #     if img.height > max_height or img.width > max_width:
    #         raise ValidationError('Разрешение изображения больше максимального!')
    #     return image


admin.site.register(Category)
admin.site.register(Notebook)
admin.site.register(Smartphone)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
