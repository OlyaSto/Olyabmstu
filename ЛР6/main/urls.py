
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from . import views as stock_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'stocks', stock_views.StockViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.master, name='master'),
    path('<int:cr_id>/', views.detail, name='detail'),
    path('<int:cr_id>/cans/', views.can, name='cann')

]