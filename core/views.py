from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.views.generic import TemplateView
from .models import HeroSlide, Statistics, Achievement, Ministry, MinistrySection, Gallery, DemographicData, SiteLogo, AboutPage, AboutMinistry, MissionVision, Challenge, BoardMember
from .models import Project, ProjectPage, VolunteerPage, GoTeam, PrayerPartner, GiveSection, VolunteerApplication
from .serializers import DemographicDataSerializer
from .forms import SubscriberForm



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

################ MAP VIEWs ######################
"""Get States with Data"""
def get_state_data(request):
    """Get all states with data summary"""
    states_with_data = DemographicData.objects.values('state').annotate(
        village_count=Count('village', distinct=True),
        total_converts=Sum('converts'),
        total_population=Sum('total_village_population')
    ).order_by('state')
    
    return JsonResponse({
        'states': list(states_with_data)
    })



def get_state_detail(request, state_name):
    """Get detailed data for a specific state"""
    state_data = DemographicData.objects.filter(state=state_name).aggregate(
        village_count=Count('village', distinct=True),
        total_converts=Sum('converts'),
        total_population=Sum('total_village_population'),
        total_christian=Sum('christian_population'),
        total_muslim=Sum('muslim_population'),
        total_traditional=Sum('traditional_population'),
        film_attendance=Sum('film_attendance')
    )
    
    return JsonResponse({
        'state': state_name,
        'statistics': state_data
    })


def state_detail(request, state_name):
    
    
    # Get all data for this state
    state_data = DemographicData.objects.filter(state=state_name)
    
    # Calculate summary with all required fields for charts
    summary = {
        'village_count': state_data.count(),
        'total_population': state_data.aggregate(Sum('total_village_population'))['total_village_population__sum'] or 0,
        'total_converts': state_data.aggregate(Sum('converts'))['converts__sum'] or 0,
        'film_attendance': state_data.aggregate(Sum('film_attendance'))['film_attendance__sum'] or 0,
        'total_christian': state_data.aggregate(Sum('christian_population'))['christian_population__sum'] or 0,
        'total_muslim': state_data.aggregate(Sum('muslim_population'))['muslim_population__sum'] or 0,
        'total_traditional': state_data.aggregate(Sum('traditional_population'))['traditional_population__sum'] or 0,
    }
    
    detailed_data = DemographicData.objects.filter(state=state_name).order_by('lga', 'ward', 'village')
    
    context = {
        'state_name': state_name,
        'summary': summary,
        'detailed_data': detailed_data,
        'logo': SiteLogo.objects.last(),
    }
    print(f"Number of detailed records: {detailed_data.count()}")
    return render(request, 'core/state_detail.html', context)

######################################
def home(request):
    context = {
        'slides': HeroSlide.objects.filter(is_active=True).order_by('order'),
        'statistics': Statistics.objects.last(),
        'achievement': Achievement.objects.first(),
        'ministry_section': MinistrySection.objects.first(),
        'ministries': Ministry.objects.all(),
        'gallery_items': Gallery.objects.filter(is_featured=True)[:6],
        'logo': SiteLogo.objects.last(),
    }
    return render(request, 'core/home.html', context)


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({
                    'status': 'success',
                    'message': 'Thank you for subscribing!'
                })
            except:
                return JsonResponse({
                    'status': 'error',
                    'message': 'This email is already subscribed.'
                })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Please enter a valid email address.'
            })
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


##################### About Page ######################

def about(request):
    context = {
        'about': AboutPage.objects.first(),
        'ministries': AboutMinistry.objects.all(),
        'mission_vision': MissionVision.objects.first(),
        'challenge': Challenge.objects.first(),
        'board_members': BoardMember.objects.all(),
        'logo': SiteLogo.objects.last(),
    }
    return render(request, 'core/about.html', context)

###########################################

############## PROJECTS Page ###############
def projects(request):
    context = {
        'page': ProjectPage.objects.first(),
        'projects': Project.objects.all(),
        'logo': SiteLogo.objects.last(),
    }
    return render(request, 'core/projects.html', context)


###########################################
############## Volunteer Page ###############
def volunteer(request):
    context = {
        'page': VolunteerPage.objects.first(),
        'go_team': GoTeam.objects.first(),
        'prayer_partner': PrayerPartner.objects.first(),
        'give_section': GiveSection.objects.first(),
        'logo': SiteLogo.objects.last(),
    }
    return render(request, 'core/volunteer.html', context)


def volunteer_apply(request):
    if request.method == 'POST':
        try:
            application = VolunteerApplication.objects.create(
                full_name=request.POST.get('full_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                area_of_interest=request.POST.get('area_of_interest'),
                skills=request.POST.get('skills'),
                availability=request.POST.get('availability'),
                message=request.POST.get('message', '')
            )
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you for your interest! We will contact you soon.'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'There was an error submitting your application. Please try again.'
            })
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


###########################################

############## Media Page ###############



###########################################

############## Contact Page ###############



###########################################