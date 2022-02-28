#? Static Files Config in Development mode
from django.conf import settings
from django.conf.urls.static import static

#! Built-in Imports
from django.contrib import admin
from django.urls import path, include

#! Local Apps Imports
from mainapp.views import LandingPageView

urlpatterns = [
    #? Local urls
    path('', LandingPageView.as_view(), name='landing-view'),
    path('accounts/', include('mainapp.urls')),

    #?Third-party urls
    path('__debug__/', include('debug_toolbar.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

    #? System urls
    path('admin/', admin.site.urls),
]

#! Configures Static files urls
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 