
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.master, name='master'),
    path('<int:cr_id>/', views.detail, name='detail'),
    path('<int:cr_id>/cans/', views.can, name='cann')

]
