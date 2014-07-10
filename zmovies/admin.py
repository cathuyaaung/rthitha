from django.contrib import admin
from zmovies.models import Movie, UserProfile

def make_ACTIVE(modeladmin, request, queryset):
	queryset.update(active=True)
make_ACTIVE.short_description = "ACTIVE"

def make_INACTIVE(modeladmin, request, queryset):
	queryset.update(active=False)
make_INACTIVE.short_description = "INACTIVE"

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    ordering = ['title']
    actions = [make_ACTIVE, make_INACTIVE]

admin.site.register(Movie, MovieAdmin)



from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'UserProfile'

# Define a new User admin
class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)