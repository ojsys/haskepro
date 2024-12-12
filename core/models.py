from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class HeroSlide(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hero_slides/')
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Statistics(models.Model):
    title = models.CharField(max_length=255, default="Reaching Lives Across The Country")
    subtitle = models.CharField(max_length=255, default="Church Impact")
    stat_title1 = models.CharField(max_length=255, default="Our Statistics")
    stat_desc1 = models.CharField(max_length=255, default="An overview of the unreached people groups mostly in Nothern Nigeria")
    stat_title2 = models.CharField(max_length=255, default="Explore unreached people")
    stat_desc2 = models.CharField(max_length=255, default="Click on any colored state to see detailed statistics.")

    # Population Statistics
    total_population = models.IntegerField(default=0, help_text="Total estimated population")
    people_groups = models.IntegerField(default=0)
    # Minsitry Impact
    villages_reached = models.IntegerField(default=0)
    converts = models.IntegerField(default=0, help_text="Number of converts")
    film_attendees = models.IntegerField(default=0, help_text="Number of film showing attendees")
    people_reached = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    # Additional Impact Metrics
    bible_translations = models.IntegerField(default=0, help_text="Number of Bible translations")
    active_missionaries = models.IntegerField(default=0, help_text="Number of active missionaries")
    training_sessions = models.IntegerField(default=0, help_text="Number of training sessions conducted")
    
    class Meta:
        verbose_name = "Statistics Section"
        verbose_name_plural = "Statistics Sections"
    
    def __str__(self):
        return f"Stats {self.title}"

class Achievement(models.Model):
    villages = models.IntegerField(default=0)
    villages_description = models.TextField(default="We have reached several villages so far. We continue to reach several villages with the gospel of Jesus")
    
    people = models.IntegerField(default=0)
    people_description = models.TextField(default="People have accepted the salvation gospel to receive Christ through our outreach")
    
    reached = models.IntegerField(default=0)
    reached_description = models.TextField(default="People have been reached with the gospel and have been discipled to walk with the professional love")
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Achievement Stats (Updated: {self.updated_at.strftime('%Y-%m-%d')})"

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"



class MinistrySection(models.Model):
    title = models.CharField(max_length=200, default="Reaching Lives Across The Country")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='ministry_section/')

    class Meta:
        verbose_name = "Ministry Section"
        verbose_name_plural = "Ministry Sections"

    def __str__(self):
        return self.title

class Ministry(models.Model):
    title = models.CharField(max_length=200)  # e.g., "WE PRAY", "WE FELLOWSHIP"
    description = models.TextField()
    icon = models.ImageField(upload_to='ministry_icons/', blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Ministries"
        ordering = ['order']

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Galleries"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            from PIL import Image
            img = Image.open(self.image)
            self.width = img.width
            self.height = img.height
        super().save(*args, **kwargs)


class DemographicData(models.Model):

    STATE_CHOICES = [
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),        
        ('Anambra', 'Anambra'),      
        ('Bauchi', 'Bauchi'),     
        ('Bayelsa', 'Bayelsa'),      
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),    
        ('Ebonyi', 'Ebonyi'),     
        ('Edo', 'Edo'),  
        ('Ekiti', 'Ekiti'),    
        ('Enugu', 'Enugu'),    
        ('FCT', 'Abuja'),
        ('Gombe', 'Gombe'),    
        ('Imo', 'Imo'),  
        ('Jigawa', 'Jigawa'),     
        ('Kaduna', 'Kaduna'),     
        ('Kano', 'Kano'),   
        ('Katsina', 'Katsina'),      
        ('Kebbi', 'Kebbi'),    
        ('Kogi', 'Kogi'),   
        ('Kwara', 'Kwara'),    
        ('Lagos', 'Lagos'),    
        ('Nasarawa', 'Nasarawa'),       
        ('Niger', 'Niger'),    
        ('Ogun', 'Ogun'),   
        ('Ondo', 'Ondo'),   
        ('Osun', 'Osun'),   
        ('Oyo', 'Oyo'),  
        ('Plateau', 'Plateau'),      
        ('Rivers', 'Rivers'),     
        ('Sokoto', 'Sokoto'),     
        ('Taraba', 'Taraba'),     
        ('Yobe', 'Yobe'),   
        ('Zamfara', 'Zamfara'), 
        ]


    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    lga = models.CharField(max_length=100, verbose_name="L.G.A", null=True, blank=True)
    ward = models.CharField(max_length=100, null=True, blank=True)
    village = models.CharField(max_length=100, null=True, blank=True)
    christian_population = models.IntegerField(verbose_name="Christian Population", null=True, blank=True)
    muslim_population = models.IntegerField(verbose_name="Muslim Population", null=True, blank=True)
    traditional_population = models.IntegerField(verbose_name="Traditional People Population", null=True, blank=True)
    converts = models.IntegerField(null=True, blank=True)
    total_village_population = models.IntegerField(verbose_name="Total Village Population",null=True, blank=True)
    film_attendance = models.IntegerField(null=True, blank=True)
    people_group = models.CharField(max_length=100, null=True, blank=True)
    practiced_religion = models.CharField(max_length=100, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        unique_together = ['state', 'lga', 'ward', 'village']
        verbose_name_plural = "Demographic Data"
        # You might want to add indexes for frequently queried fields
        indexes = [
            models.Index(fields=['state']),
            models.Index(fields=['lga']),
        ]
        unique_together = ['state', 'lga', 'ward', 'village']

    def __str__(self):
        return f"{self.state}, {self.village}, {self.lga} "


class SiteLogo(models.Model):
    logo = models.ImageField(upload_to='logos/')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Site Logo"

    def __str__(self):
        return f"Logo updated on {self.updated_at}"
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    

#################### ABOUT PAGE MODEL ###################

class AboutPage(models.Model):
    title = models.CharField(max_length=200, default="ABOUT US")
    header_image = models.ImageField(upload_to='about/', help_text="Header image for about page")
    introduction = models.TextField(help_text="Main introduction text")
    ministry_goal = models.TextField(help_text="Main Goal", default="Our Goal")

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"
    
    def __str__(self):
        return f"{self.title}"

class AboutMinistry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to="about/min_img/", help_text="Ministry Image", null=True, blank=True)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "About Ministry"

    def __str__(self):
        return self.title

class MissionVision(models.Model):
    mission_title = models.CharField(max_length=200, default="Our Mission")
    mission_text = models.TextField()
    vision_title = models.CharField(max_length=200, default="Our Vision")
    vision_text = models.TextField()
    mission_image = models.ImageField(upload_to='about/', help_text="Image for Mission")
    vision_image = models.ImageField(upload_to='about/', help_text="Image for Vision")

    class Meta:
        verbose_name = "Mission and Vision"
        verbose_name_plural = "Mission and Vision"

    def __str__(self):
        return f"{self.mission_title} - {self.vision_title}"
    

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)
    challenge1_title = models.CharField(max_length=200, default="Reaching the Unreached in 10/40 Window")
    challenge1_desc = models.TextField()
    challenge1_image = models.ImageField(upload_to='about/challenge/', help_text="Challenge Image")
    challenge2_title = models.CharField(max_length=200, default="Praying for the Unreached")
    challenge2_desc = models.TextField()
    challenge2_image = models.ImageField(upload_to='about/challenge/', help_text="Challenge Image")
    challenge3_title = models.CharField(max_length=200, default="Supporting Education in Nigeria")
    challenge3_desc = models.TextField()
    challenge3_image = models.ImageField(upload_to='about/challenge/', help_text="Challenge Image")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class BoardMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='board/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']


    def __str__(self):
        return self.name
    

################## PROJECTS PAGE ###############
class ProjectPage(models.Model):
    title = models.CharField(max_length=200, default="HASKE PROJECTS")
    header_image = models.ImageField(upload_to='projects/', help_text="Header image for projects page")
    introduction = models.TextField(help_text="Introduction text below header")

    class Meta:
        verbose_name = "Project Page"
        verbose_name_plural = "Project Page"
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    order = models.IntegerField(default=0)
    
    # You might want to add these fields if they're relevant
    beneficiaries = models.IntegerField(default=0)
    location = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

################################################
################## Volunteer ####################
class VolunteerPage(models.Model):
    title = models.CharField(max_length=200, default="VOLUNTEER")
    header_image = models.ImageField(upload_to='volunteer/', help_text="Header image")
    introduction = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Volunteer Page"
        verbose_name_plural = "Volunteer Page"


class VolunteerApplication(models.Model):
    INTEREST_CHOICES = [
        ('go_team', 'Go-Team Member'),
        ('prayer', 'Prayer Partner'),
        ('medical', 'Medical Outreach'),
        ('education', 'Education Support'),
        ('community', 'Community Development'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    area_of_interest = models.CharField(max_length=50, choices=INTEREST_CHOICES)
    skills = models.TextField(help_text="Please list your relevant skills and experience")
    availability = models.TextField(help_text="When are you available to volunteer?")
    message = models.TextField(help_text="Additional message or questions", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.area_of_interest}"

    class Meta:
        ordering = ['-created_at']

class GoTeam(models.Model):
    title = models.CharField(max_length=200, default="Go-Teams")
    description = models.TextField()
    image = models.ImageField(upload_to='volunteer/teams/')
    

    def __str__(self):
        return self.title

class PrayerPartner(models.Model):
    title = models.CharField(max_length=200, default="Prayer Partners")
    description = models.TextField()
    image = models.ImageField(upload_to='volunteer/prayer/')
   
    def __str__(self):
        return self.title

class GiveSection(models.Model):
    title = models.CharField(max_length=200, default="Give")
    description = models.TextField()
    image = models.ImageField(upload_to='volunteer/give/')
    

    def __str__(self):
        return self.title

#################################################

#################  MEDIA  #######################
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    featured_image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    excerpt = models.TextField(help_text="Short description for preview", max_length=300)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-published_date']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_id = models.CharField(max_length=20, help_text="YouTube video ID from URL")
    published_date = models.DateTimeField()
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-published_date']
        
    def __str__(self):
        return self.title
    
    @property
    def embed_url(self):
        return f"https://www.youtube.com/embed/{self.video_id}"

class SpotifyPodcast(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    spotify_id = models.CharField(max_length=100, help_text="Spotify episode/track ID")
    published_date = models.DateTimeField()
    duration = models.CharField(max_length=10, help_text="Duration in format MM:SS")
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-published_date']
        
    def __str__(self):
        return self.title

class MediaPage(models.Model):
    title = models.CharField(max_length=200, default="Media Center")
    header_image = models.ImageField(upload_to='media/')
    blog_section_title = models.CharField(max_length=200, default="Latest Blog Posts")
    youtube_section_title = models.CharField(max_length=200, default="Video Messages")
    podcast_section_title = models.CharField(max_length=200, default="Audio Messages")
    
    class Meta:
        verbose_name = "Media Page"
        verbose_name_plural = "Media Page"
        
    def __str__(self):
        return self.title

#################################################

##################  Contact   #################

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
#################################################

################# Donations #####################
class DonationPage(models.Model):
    title = models.CharField(max_length=200, default="GIVE")
    header_image = models.ImageField(upload_to='donations/')
    description = models.TextField()
    bank_name = models.CharField(max_length=100, default="Zenith Bank Plc.")
    
    class Meta:
        verbose_name = "Donation Page"
        verbose_name_plural = "Donation Page"

    def __str__(self):
        return f"{self.title}"

class BankAccount(models.Model):
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)  # e.g., "MAIN ACCOUNT", "HUMANITARIAN"
    
    def __str__(self):
        return f"{self.account_number} - {self.description}"
    
#################################################
