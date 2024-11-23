from django.contrib import admin
from .models import HeroSlide, Statistics, Achievement, Ministry, MinistrySection, Gallery

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active',)
    ordering = ('order',)

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('total_people', 'villages_reached', 'people_reached', 'updated_at')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('villages', 'people', 'reached', 'updated_at')

    def has_add_permission(self, request):
        # Only allow one instance
        if self.model.objects.exists():
            return False
        return True


@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'created_at')
    list_editable = ('is_featured',)
    search_fields = ('title', 'description')
    list_filter = ('is_featured',)

@admin.register(MinistrySection)
class MinistrySectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')

    def has_add_permission(self, request):
        # Only allow one instance
        if self.model.objects.exists():
            return False
        return True
