from django.contrib.auth.models import User
superusers = User.objects.filter(is_superuser=True)
if superusers.exists():
    print("Existing superusers:")
    for user in superusers:
        print(f"- {user.username}")
else:
    print("No superusers found.")
