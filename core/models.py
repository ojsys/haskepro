from django.db import models
from django.utils.text import slugify

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
    lga = models.CharField(max_length=100, verbose_name="L.G.A")
    ward = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    christian_population = models.IntegerField(verbose_name="Christian Population")
    muslim_population = models.IntegerField(verbose_name="Muslim Population")
    traditional_population = models.IntegerField(verbose_name="Traditional People Population")
    converts = models.IntegerField()
    total_village_population = models.IntegerField(verbose_name="Total Village Population")
    film_attendance = models.IntegerField()
    people_group = models.CharField(max_length=100)
    practiced_religion = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
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

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"
    
    def __str__(self):
        return f"{self.title}"

class AboutMinistry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
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
    mission_image = models.ImageField(upload_to='about/', height_field="Image for Mission")
    vision_image = models.ImageField(upload_to='about/', height_field="Image for Vision")

    class Meta:
        verbose_name = "Mission and Vision"
        verbose_name_plural = "Mission and Vision"

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
    

