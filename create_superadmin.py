from django.contrib.auth.models import User
from django.contrib.auth import authenticate

username = 'superadmin'
password = 'superadmin123'

# Hard reset
User.objects.filter(username=username).delete()
User.objects.create_superuser(username, 'superadmin@onlinemaid.com', password)
print(f"DEBUG: Superuser '{username}' has been CREATED with password '{password}'.")

# Test authentication
auth_user = authenticate(username=username, password=password)
if auth_user:
    print(f"DEBUG: AUTH SUCCESS for '{username}' in shell")
else:
    print(f"DEBUG: AUTH FAILED for '{username}' in shell")
