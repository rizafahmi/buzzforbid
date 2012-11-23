from travel_agent.models import Agent
from django.contrib import admin


class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', )
    pass

admin.site.register(Agent, AgentAdmin)
