from django.urls import path
from django.conf import settings
from .views import StateDemographicView, DemographicsMapView
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # about
    path('about/', views.about, name='about'),
    # projects
    path('projects/', views.projects, name='projects'),
    # volunteers
    path('volunteer/', views.volunteer, name='volunteer'),
    # volunteers Apply
    path('volunteer/apply/', views.volunteer_apply, name='volunteer-apply'),

    path('api/demographics/<str:state_name>/', StateDemographicView.as_view(), name='state-demographics'),
    path('demographics-map/', DemographicsMapView.as_view(), name='demographics-map'),
    path('api/state-data/', views.get_state_data, name='state-data'),
    path('api/state-data/<str:state_name>/', views.get_state_detail, name='state-detail'),
     
    path('state/<str:state_name>/', views.state_detail, name='state_detail'),
    # Subscribe
    path('subscribe/', views.subscribe, name='subscribe'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)