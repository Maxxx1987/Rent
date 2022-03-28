from django.urls import path, include

from apps.products.views import ProductDetailView
from apps.reviews.views import ReviewCreateView

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view()),
    path('<int:pk>/add_review/', ReviewCreateView.as_view()),
]
