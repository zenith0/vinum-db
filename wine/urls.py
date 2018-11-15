from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.WineList.as_view()), name='wine-list'),
    path('<slug:slug>/', login_required(views.WineDetailView.as_view()), name='wine-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)