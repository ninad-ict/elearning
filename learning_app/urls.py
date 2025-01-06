from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginViewSet,ContentUploadViewSet

# Create a router and register the UserLoginViewSet
router = DefaultRouter()
router.register(r'userlogins', UserLoginViewSet),
router.register(r'content-uploads', ContentUploadViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]