from django.contrib.auth.views import login, logout
from django.urls import path, reverse_lazy, include
from speedvisionx.views import HomePageView, MatrixDetailsView

from rest_framework import routers
router = routers.DefaultRouter()
# router.register(r'matrixshow', MatrixViewSet.as_view(), base_name="matrixshow")

urlpatterns =[
    path('login/', login, {'template_name':'login.html'}, name='login'),
    path('logout/', logout, {'next_page': reverse_lazy('login')}, name='logout'),
    path('block/', MatrixDetailsView.as_view(), name='block'),
    path('home/', HomePageView.as_view(), name='home'),
    path('', include(router.urls)),
]

