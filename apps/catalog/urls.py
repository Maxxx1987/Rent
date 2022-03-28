from django.urls import path, include

from apps.catalog.views import CategoryListView, SectionListView
from apps.products.views import ProductListView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<slug:slug>/', SectionListView.as_view()),
    path('<slug:foo>/<slug:bar>/', ProductListView.as_view()),
]
