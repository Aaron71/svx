from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework import viewsets, generics

from speedvisionx.models import RaceMatrix
from speedvisionx.serializers import RaceMatrixViewDetails


class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "base.html"

class MatrixDetailsView(generics.ListCreateAPIView):
    queryset = RaceMatrix.objects.all()
    serializer_class = RaceMatrixViewDetails
    print(queryset)