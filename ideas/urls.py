from rest_framework import routers
from django.urls import include, path
from .views import VoteViewSet, IdeaViewSet

router = routers.DefaultRouter()
router.register(f'ideas', IdeaViewSet)
router.register(f'votes', VoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]