"""
URL configuration for bankstatements project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transform/', include('transform.urls')),
    
    path('', include('transform.urls')), # empty path
    # path('/', include('transform.urls')), # empty path
    # path('bankstatementtransformer.azurewebsites.net', include('transform.urls')), # bankstatementtransformer.azurewebsites.net
    # path('bankstatementtransformer.azurewebsites.net/', include('transform.urls')), # bankstatementtransformer.azurewebsites.net
    # path('$', include('transform.urls')), # $
    # path('$/', include('transform.urls')), # $


    # # path('transform', include('transform.urls')),
    # path('/transform/', include('transform.urls')),
    # path('bankstatementtransformer.azurewebsites.net/transform/', include('transform.urls')),
]  + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
