from django.urls import path
from django.conf import settings
from .views import StateDemographicView, DemographicsMapView
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    #path('<slug:slug>/', views.page_detail, name='page_detail'),

    path('api/demographics/<str:state_name>/', StateDemographicView.as_view(), name='state-demographics'),
    path('demographics-map/', DemographicsMapView.as_view(), name='demographics-map'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)