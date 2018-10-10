from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'date', 'username')
    list_display_links = ('id', 'question')
    search_fields = ('question', 'username')
    list_per_page = 50
    readonly_fields = ['id', 'date']

    def has_add_permission(self, request):
        return False