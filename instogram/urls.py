
# > ------------------  URLS for instOgram ----------------------

from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from . import views

# for heruko
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html")),
    path('Get_Post', views.Get_Post, name='Get_Post'),
    path('Get_Videos', views.Get_Videos, name='Get_Videos'),
    path('Get_Profile_Pic', views.Get_Profile_Pic, name='Get_Profile_Pic')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
