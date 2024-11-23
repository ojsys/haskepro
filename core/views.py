from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.views.generic import TemplateView
from .models import HeroSlide, Statistics, Achievement, Ministry, MinistrySection, Gallery, DemographicData
from .serializers import DemographicDataSerializer

class StateDemographicView(generics.RetrieveAPIView):
    serializer_class = DemographicDataSerializer

    def get(self, request, state_name):
        # get aggregated data for the state
        state_data = DemographicData.objects.filter(state__iexact=state_name).aggregate(
            total_christian = Sum('christian_population'),
            total_muslim = Sum('muslim_population'),
            total_traditional=Sum('traditional_population'),
            total_converts=Sum('converts'),
            total_population=Sum('total_village_population'),
            total_film_attendance=Sum('film_attendance'),
            village_count=Count('village', distinct=True),
            people_groups=Count('people_group', distinct=True)
        )
        
        response_data = {
            'state': state_name,
            'statistics': state_data
        }
        
        return Response(response_data)
    

class DemographicsMapView(TemplateView):
    template_name = 'demographics_map.html'


def home(request):
    context = {
        'slides': HeroSlide.objects.filter(is_active=True).order_by('order'),
        'statistics': Statistics.objects.first(),
        'achievement': Achievement.objects.first(),
        'ministry_section': MinistrySection.objects.first(),
        'ministries': Ministry.objects.all(),
        'gallery_items': Gallery.objects.filter(is_featured=True)[:6],
    }
    return render(request, 'core/home.html', context)