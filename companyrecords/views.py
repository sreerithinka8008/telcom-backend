from rest_framework import generics, filters
from .serializers import CompanySerializer, SwitchIPSerializer, FollowUPSerializer
from .models import Company, SwitchIP, FollowUp


class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter(is_deleted=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ["company_name", "switchip__ip"]

class CompanyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter(is_deleted=False)
    lookup_field = "id"
    

class SwitchIPListCreateView(generics.ListCreateAPIView):
    serializer_class = SwitchIPSerializer
    
    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        return SwitchIP.objects.filter(company__id=company_id, is_deleted=False)
    
    def perform_create(self, serializer):
        company_id = self.kwargs.get('company_id')
        company = Company.objects.get(id=company_id)
        serializer.save(company=company)

class SwitchIPRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SwitchIPSerializer
    queryset = SwitchIP.objects.filter(is_deleted=False)
    lookup_field = "id"

class FollowUpListCreateView(generics.ListCreateAPIView):
    serializer_class = FollowUPSerializer

    def get_queryset(self):
        comapny_id = self.kwargs.get('company_id')
        return FollowUp.objects.filter(company__id=comapny_id, is_deleted=False)
    
    def perform_create(self, serializer):
        company_id = self.kwargs.get('company_id')
        company = Company.objects.get(id=company_id)
        serializer.save(company=company)

class FollowUpRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FollowUPSerializer
    queryset = FollowUp.objects.filter(is_deleted=False)
    lookup_field = "id"
