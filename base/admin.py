from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

class ImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Product


class AddContactAdmin(admin.StackedInline):
	model = MainContact
	
class MainAdmin(admin.ModelAdmin):
	inlines = [AddContactAdmin]
        

class ContactAdmin(admin.ModelAdmin):
    list_display_links = [
        "name",
        "surname",
        "email",
        "phone"
    ]
    
    list_display = (
        "name",
        "surname",
        "email",
        "phone"
    )



admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)
admin.site.register(BackgroundImage)
admin.site.register(Main, MainAdmin)
admin.site.register(About)
admin.site.register(Partner)
admin.site.register(Contact, ContactAdmin)
admin.site.register(HomeImage)
admin.site.register(Slider)
admin.site.register(SocialMedia)
admin.site.register(ProductApply)
admin.site.register(HomeApply)
