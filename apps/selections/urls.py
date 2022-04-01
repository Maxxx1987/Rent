from django.urls import path

from apps.selections.views import (
    SelectionCreateView,
    SelectionListView,
    SelectionDeleteView,
    ProductSelectionListView,
    ProductSelectionCreateView,
    ProductSelectionDeleteView,
)

urlpatterns = [
    path('', SelectionListView.as_view()),
    path('add/', SelectionCreateView.as_view()),
    path('<int:pk>/', ProductSelectionListView.as_view()),
    path('<int:pk>/delete/', SelectionDeleteView.as_view()),
    path('<int:pk>/products/add/', ProductSelectionCreateView.as_view()),
    path('<int:sel_pk>/products/<int:pk>/delete/', ProductSelectionDeleteView.as_view())
    #path('<int:pk>/update/', UserSelectionUpdateView.as_view()),
]
