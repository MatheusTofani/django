from django.urls import path

from blog import views

urlpatterns = [
    path('admin/', views.PostView.as_view(), name='home'),
]