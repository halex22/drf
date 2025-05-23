from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MessageViewSet, CreateUserView

api_router = DefaultRouter()
api_router.register(r'messages', viewset=MessageViewSet)


urlpatterns = [
    path('v1/', include((api_router.urls, 'v1'))),
    path('sign-up', CreateUserView.as_view(), name='sign-up')
]