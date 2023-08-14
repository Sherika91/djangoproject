from django.contrib import admin

from catalog.models import Student

# admin.site.register(Students)


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'surname',)

