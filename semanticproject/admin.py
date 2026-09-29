from django.contrib import admin
from .models import SemanticModel

@admin.register(SemanticModel)
class SemanticModelAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'description')


