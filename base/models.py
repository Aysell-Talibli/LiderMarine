from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

class ServiceCategory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    @property
    def count(self):
        return self.services.all().count()
    class Meta:
        verbose_name_plural = "Xidmet kategoriyalari"

class Service(models.Model):
    slug=models.SlugField(null=True, unique=True)
    category=models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    name=models.CharField(max_length=100)
    image=models.ImageField(null=True)
    is_main = models.BooleanField(_("Ana sehifede gorunsun?"), default=False)
    description=models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Xidmetler"
    
    @property
    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"slug": self.slug})

class ProductCategory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Mehsul Kategoriyalari"

class Product(models.Model):
    slug=models.SlugField(null=True, unique=True)
    category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name=models.CharField(max_length=100)
    description=models.TextField()
    is_main = models.BooleanField(_("Ana sehifede gorunsun?"), default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Mehsullar"

class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    image=models.ImageField()

class About(models.Model):
    text=models.TextField()
    image=models.ImageField(null=True)

    class Meta:
        verbose_name_plural = "Haqqimizda"

class Partner(models.Model):
    image=models.ImageField(null=True)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return f'{self.name, self.surname}'

class Main(models.Model):
    header_logo=models.ImageField(null=True, blank=True)
    footer_logo=models.ImageField(null=True, blank=True)
    footer_text=models.TextField()
    footer_image=models.ImageField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Esas Melumatlar"

class MainContact(models.Model):
    main=models.ForeignKey(Main,  on_delete=models.SET_NULL, null=True, blank=True, related_name='main_contact' )
    address=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(max_length=70, null=True, blank=True)
    phone=models.CharField(max_length=20, null=True, blank=True)
     
    
class HomeImage(models.Model):
    name = models.CharField(_("Adi"), max_length=200)
    image=models.ImageField(null=True)

    def __str__(self):
        if self.name:
            return self.name
        return self.id
    class Meta:
        verbose_name_plural = "Ana Sehife Sekiller"

class Slider(models.Model):
    title=models.CharField(max_length=50)
    text=models.CharField(max_length=80)
    image=models.ImageField()
    def __str__(self):
        return self.title
    
class Map(models.Model):
    link=models.TextField()

class BackgroundImage(models.Model):
    about=models.ImageField(_("Haqqimizda arxa plan sekil"),null=True, blank=True)
    services=models.ImageField(_("Xidmetler arxa plan sekil"),null=True, blank=True)
    products=models.ImageField(_("Mehsullar arxa plan sekil"),null=True, blank=True)
    contact=models.ImageField(_("Elaqe arxa plan sekil"),null=True, blank=True)
    class Meta:
        verbose_name_plural = "Arxa plan sekilleri"

class HomeApply(models.Model):
    email=models.EmailField(max_length=70)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Ana sehife muracietler"

class ProductApply(models.Model):
    product=models.ForeignKey(Product,on_delete= models.CASCADE, null=True )
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    phone=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name , self.product.name}'
    class Meta:
        verbose_name_plural = "Mehsul sifarisleri"

class SocialMedia(models.Model):
    class SocialChoices(models.TextChoices):
        INSTAGRAM = "insta", "Instagram"
        FACEBOOK = "fb", "Facebook"
        TIKTOK = "tiktok", "Tiktok"
        WHATSAPP = "wp", "Whatsapp"
        LINKEDIN = "linkedin", "Linkedin"
        TWITTER = "twitter", "Twitter"
    app=models.CharField(max_length=100, choices=SocialChoices.choices)
    link=models.TextField(null=True)
    def __str__(self):
        return self.app
    