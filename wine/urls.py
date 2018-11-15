from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.WineList.as_view(), name='wine-list'),
    path('<slug:slug>/', views.WineDetailView.as_view(), name='wine-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)