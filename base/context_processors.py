from .models import *

def base_data(request):
    main_info=Main.objects.last()
    product_categories=ProductCategory.objects.all()
    service_categories=ServiceCategory.objects.all()
    apps=SocialMedia.objects.all()
    sliders=Slider.objects.all()
    images=BackgroundImage.objects.last()
    map=Map.objects.last()
    return {'product_categories': product_categories, 'apps':apps,'sliders':sliders,'map':map,
            'service_categories': service_categories, 'main_info':main_info, 'images':images}