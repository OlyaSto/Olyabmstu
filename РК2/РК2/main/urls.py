
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.master, name='master'),
    path('<int:cr_id>/', views.detail, name='detail'),
    path('<int:cr_id>/cans/', views.can, name='cann'),
    path('rep/', views.report, name='report'),
    path('create/', views.create, name='create'),
    path('<int:cr_id>/update/', views.update, name='update'),
    path('<int:cr_id>/delete/', views.delete, name='delete'),
    path('<int:cr_id>/cans/create/', views.create1, name='create1'),
    path('update/<int:cr_id>/', views.update1),
    path('delete/<int:cr_id>/', views.delete1)

]