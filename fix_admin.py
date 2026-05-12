from django.contrib.auth.models import User
from django.contrib.auth import authenticate

username = 'admin'
password = 'admin123'

# Check if exists
user = User.objects.filter(username=username).first()
if user:
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()
    print(f"DEBUG: Password for '{username}' has been RESET to '{password}'.")
else:
    User.objects.create_superuser(username, 'admin@onlinemaid.com', password)
    print(f"DEBUG: Superuser '{username}' has been CREATED with password '{password}'.")

# Double check authentication in shell
auth_user = authenticate(username=username, password=password)
if auth_user:
    print(f"DEBUG: AUTH SUCCESS for '{username}' with '{password}' in shell")
else:
    print(f"DEBUG: AUTH FAILED for '{username}' with '{password}' in shell")
