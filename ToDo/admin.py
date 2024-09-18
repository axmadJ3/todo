from django.contrib import admin


from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'update_at', 'is_done')
    list_editable = ['is_done']
    list_filter = ('created_at', 'update_at', 'is_done')
    actions = ['mark_is_done_true', 'mark_is_done_false']
    search_fields = ['title__startswith']
    list_per_page = 3

    @admin.action(description='Пометить как выполненные')
    def mark_is_done_true(self, request, queryset):
        count = queryset.update(is_done=True)
        self.message_user(request, f"{count} задачи помечены как выполненные.")
    
    @admin.action(description='Пометить как не выполненные')
    def mark_is_done_false(self, request, queryset):
        count = queryset.update(is_done=False)
        self.message_user(request, f"{count} задачи помечены как не выполненные.")
        
        
admin.site.register(Todo, TodoAdmin)
