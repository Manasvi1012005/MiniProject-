from home.models import Maid
Maid.objects.get_or_create(name='Alice', age=25, experience=3, location='Mumbai', phone='9876543210', address='123 Mumbai Street', salary=5000, service_type='home_cleaning', description='Expert in home cleaning')
Maid.objects.get_or_create(name='Bob', age=30, experience=5, location='Delhi', phone='9876543211', address='456 Delhi Road', salary=7000, service_type='cooking', description='Professional cook')
Maid.objects.get_or_create(name='Charlie', age=28, experience=4, location='Bangalore', phone='9876543212', address='789 Bangalore Ln', salary=6000, service_type='babysitting', description='Caring babysitter')
Maid.objects.get_or_create(name='Daisy', age=35, experience=8, location='Pune', phone='9876543213', address='101 Pune Avenue', salary=8000, service_type='elder_care', description='Patient elder care professional')
Maid.objects.get_or_create(name='Edward', age=26, experience=2, location='Chennai', phone='9876543214', address='202 Chennai Blvd', salary=4500, service_type='laundry', description='Efficient laundry services')
Maid.objects.get_or_create(name='Fiona', age=29, experience=6, location='Kolkata', phone='9876543215', address='303 Kolkata Street', salary=5500, service_type='balcony_cleaning', description='Detailed balcony cleaning')
Maid.objects.get_or_create(name='George', age=32, experience=5, location='Hyderabad', phone='9876543216', address='404 Hyderabad Rd', salary=6500, service_type='kitchen_cleaning', description='Specialized kitchen deep cleaning')
print("More sample maids with details created")


