from rest_framework.viewsets import ModelViewSet
from .models import Company
from .serializers import CompanySerializer
from rest_framework.pagination import PageNumberPagination

class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_updated")
    pagination_class = PageNumberPagination