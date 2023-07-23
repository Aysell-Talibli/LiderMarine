from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title','text')
