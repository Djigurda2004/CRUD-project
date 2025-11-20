from django.urls import path
from . import views

urlpatterns = [
    path('',views.newapp_home,name="newapp_home"),
    path('addapp',views.addapp,name="addapp"),
    path('<int:pk>',views.NewappDetailView.as_view(),name = 'newapp-detail'),
    path('<int:pk>/update',views.NewappUpdateView.as_view(),name = 'newapp-update'),
    path('<int:pk>/delete',views.NewappDeleteView.as_view(),name = 'newapp-delete')
]