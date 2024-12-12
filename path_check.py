import os
import sys
import django
from django.conf import settings

# Setup Django environment
sys.path.append('/var/www/haske')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'haske_pro.settings')
django.setup()

# Diagnostic Print Statements
print("--- Static File Diagnostic Report ---")
print(f"BASE_DIR: {settings.BASE_DIR}")
print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
print(f"STATIC_URL: {settings.STATIC_URL}")
print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")

# Verify file existence
test_file_path = os.path.join(settings.STATIC_ROOT, 'js', 'nigeria_map.geojson')
print(f"\nTest File Path: {test_file_path}")
print(f"File Exists: {os.path.exists(test_file_path)}")

# List files in STATIC_ROOT
print("\nStatic Root Contents:")
for root, dirs, files in os.walk(settings.STATIC_ROOT):
    for file in files:
        print(os.path.join(root, file))