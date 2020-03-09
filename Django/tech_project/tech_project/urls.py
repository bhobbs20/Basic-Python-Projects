from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('admin_console/', include('products.urls')),
]

urlpatterns += staticfiles_urlpatterns()