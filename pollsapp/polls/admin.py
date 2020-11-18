from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Pollsapp Admin"
admin.site.site_title = "Pollsapp Admin"
admin.site.index_title = "Pollsapp Admin"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['text']}),
        ('Date', {'fields': ['published'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)