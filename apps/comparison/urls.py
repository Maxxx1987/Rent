from django.urls import path

from apps.comparison.views import (
    ComparisonProductListView,
    ComparisonProductDeleteView,
    ComparisonProductCreateView,
    ComparisonDeleteView,
)

urlpatterns = [
    path('', ComparisonProductCreateView.as_view()),
    path('list/', ComparisonProductListView.as_view()),
    path('<int:pk>/delete/', ComparisonProductDeleteView.as_view()),
    path('user/<int:pk>/delete/', ComparisonDeleteView.as_view()),
]
