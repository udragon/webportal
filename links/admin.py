from django.contrib import admin
from models import Link, Category

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    name = 'Categories'
    pass

# Registrations #
admin.site.register(Link, LinkAdmin)
admin.site.register(Category, CategoryAdmin)
