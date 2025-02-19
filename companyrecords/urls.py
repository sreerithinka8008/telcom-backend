from django.urls import path
from .views import CompanyListCreateView, CompanyRetrieveUpdateDeleteView, SwitchIPListCreateView, SwitchIPRetrieveUpdateDeleteView, FollowUpListCreateView, FollowUpRetrieveUpdateDeleteView
urlpatterns = [
    path("company/", CompanyListCreateView.as_view() ),
    path("company/<id>", CompanyRetrieveUpdateDeleteView.as_view()),
    path("switchips/<int:company_id>", SwitchIPListCreateView.as_view() ),
    path("switchip/<int:id>", SwitchIPRetrieveUpdateDeleteView.as_view()),    
    path("followups/<int:company_id>", FollowUpListCreateView.as_view() ),
    path("followup/<int:id>", FollowUpRetrieveUpdateDeleteView.as_view()),
]
