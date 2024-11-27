from django.urls import path
from search import views

urlpatterns = [
    path('', views.SearchView.as_view(), name='root'),
    path('details/<int:id>/', views.SearchDetails.as_view(), name="details"),
]
