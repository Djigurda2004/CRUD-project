from django.urls import path
from . import views

urlpatterns = [
    path('',views.arts,name="arts"),
    path('addart',views.add_art,name="add-art"),
    path('<int:pk>',views.ArtDetailView.as_view(),name = 'art-detail'),
    path('<int:pk>/update',views.ArtUpdateView.as_view(),name = 'art-update'),
    path('<int:pk>/delete',views.ArtDeleteView.as_view(),name = 'art-delete')
]