from rest_framework import routers
from .views import reports_viewset

router = routers.DefaultRouter()
router.register('reports', reports_viewset)