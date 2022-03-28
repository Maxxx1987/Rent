from django.urls import path

from apps.reviews.views import ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('<int:pk>/update/', ReviewUpdateView.as_view()),
    path('<int:pk>/delete/', ReviewDeleteView.as_view()),
]
