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
    total_people = models.IntegerField(default=0)
    villages_reached = models.IntegerField(default=0)
    people_reached = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Statistics"

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