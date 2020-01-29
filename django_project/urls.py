from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from core import views


router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, basename='customer-router')
router.register(r'professions', views.ProfessionViewSet)
router.register(r'data-sheet', views.DataSheetViewSet)
router.register(r'documents', views.DocumentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls'))
]
