from django.urls import path
from .views import GenerateComparisonTableView

urlpatterns = [
    path("generate-comparison-table/", GenerateComparisonTableView.as_view(), name="generate-comparison-table"),
]