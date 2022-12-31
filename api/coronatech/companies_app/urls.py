from rest_framework import routers
from .views import CompanyViewSet

cmy_router = routers.DefaultRouter()
cmy_router.register("companies", CompanyViewSet, basename="companies")
