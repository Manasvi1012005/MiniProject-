from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@onlinemaid.com', 'admin123')
    print("Superuser created: username=admin, password=admin123")
else:
    u = User.objects.get(username='admin')
    u.set_password('admin123')
    u.is_superuser = True
    u.is_staff = True
    u.save()
    print("Admin password updated to 'admin123'")
