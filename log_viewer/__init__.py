from django.contrib.auth.models import User
users = User.objects.all()
print(users.values_list('username', flat=True))
