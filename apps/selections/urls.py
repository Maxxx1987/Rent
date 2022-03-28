from django.urls import path

from apps.selections.views import (
    SelectionCreateView,
    SelectionListView, SelectionDeleteView, SelectionDetailView,
)

urlpatterns = [
    path('', SelectionListView.as_view()),
    path('add/', SelectionCreateView.as_view()),
    path('<int:pk>/', SelectionDetailView.as_view()),
    path('<int:pk>/delete/', SelectionDeleteView.as_view()),
    #path('<int:pk>/update/', UserSelectionUpdateView.as_view()),
]
