"""_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.catalog.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),

    path('catalog/', include('apps.catalog.urls')),
    path('products/', include('apps.products.urls')),
    path('order/', include('apps.payments.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('selections/', include('apps.selections.urls')),
    path('search/', include('apps.search.urls')),


    #
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
