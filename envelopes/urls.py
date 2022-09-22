from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base'),
    path('output/', views.ViewPDF.as_view(), name='output'),
    path('pdf_download/', views.DownloadPDF.as_view(), name='pdf_download'),
]
