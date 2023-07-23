
from django.contrib import admin
from django.urls import path, include, re_path, translate_url
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def set_language(request, lang_code):
    lang=request.META.get('HTTP_REFERER', None)
    response=redirect(translate_url(lang, lang_code))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('set_language/<str:lang_code>/', set_language, name="set_lang"),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)