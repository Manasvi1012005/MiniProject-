from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Hard reset
User.objects.filter(username='admin').delete()
User.objects.create_superuser('admin', 'admin@test.com', 'admin123')

# Test authentication
user = authenticate(username='admin', password='admin123')
if user is not None:
    print("TEST: Authentication SUCCESSFUL for 'admin' with 'admin123'")
    print(f"User is superuser: {user.is_superuser}")
else:
    print("TEST: Authentication FAILED for 'admin' with 'admin123'")
