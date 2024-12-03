from django.contrib import admin

# Register your models here.
from .models import Team, Person

admin.site.register(Team)

class PersonAdmin(admin.ModelAdmin):
    @admin.display(description = "shirt size (id)")
    def team_with_id(self,obj):
        if obj.team :
            return f'{obj.team} ({obj.team.id})'
        return 'No team'

    list_display = ["name", "nickname", "shirt_size", "month_added", "team_with_id"]

admin.site.register(Person, PersonAdmin)