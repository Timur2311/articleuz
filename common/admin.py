from django.contrib import admin

# Register your models here.
from .models import User, Author

admin.site.register(User)
admin.site.register(Author)