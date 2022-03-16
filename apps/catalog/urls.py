from django.urls import path

from apps.catalog.views import CategoryListView, SectionListView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<slug:slug>/', SectionListView.as_view()),
]
