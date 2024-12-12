from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, Widget
from django.core.exceptions import ValidationError
from .models import DemographicData

class DemographicDataResource(resources.ModelResource):
    from import_export import resources

class DemographicDataResource(resources.ModelResource):
    class Meta:
        model = DemographicData
        import_id_fields = ['state', 'lga', 'ward', 'village']
        fields = [
            'state', 
            'lga', 
            'ward', 
            'village',
            'total_village_population',
            'christian_population',
            'muslim_population',
            'traditional_population',
            'converts',
            'film_attendance',
            'people_group',
            'practiced_religion'
        ]
        skip_unchanged = True
        report_skipped = False
        use_bulk = False  # Disable bulk create to handle duplicates properly

    def before_import_row(self, row, **kwargs):
        """Clean and validate row data"""
        # Ensure required fields are not empty
        required_fields = ['state', 'lga', 'ward', 'village']
        for field in required_fields:
            if not row.get(field):
                raise ValueError(f"{field} cannot be empty")
        
        # Clean empty strings to None for optional fields
        for key, value in row.items():
            if key not in required_fields and value == '':
                row[key] = None
        return row

    def get_or_init_instance(self, instance_loader, row):
        """
        Either fetches an existing instance or initializes a new one.
        """
        try:
            instance = self._meta.model.objects.get(
                state=row['state'],
                lga=row['lga'],
                ward=row['ward'],
                village=row['village']
            )
            return instance, False
        except self._meta.model.DoesNotExist:
            return self._meta.model(), True

    def save_instance(self, instance, is_create, **kwargs):
        """
        Custom save method to handle both creates and updates
        """
        try:
            # If it's an update, save instance
            if not is_create:
                instance.save()
            # If it's a new record, validate and save
            else:
                if all([
                    instance.state,
                    instance.lga,
                    instance.ward,
                    instance.village
                ]):
                    instance.save()
                else:
                    raise ValueError("Required fields cannot be empty")
            return True
        except Exception as e:
            print(f"Error saving instance: {str(e)}")
            return False