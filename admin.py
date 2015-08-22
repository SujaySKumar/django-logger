from django.contrib import admin

# Register your models here.

class SujayLoggerAdmin(admin.ModelAdmin):
    def log_addition(self, request, object, message):
        from django.contrib.admin.models import LogEntry, ADDITION
        LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=force_text(object),
            action_flag=ADDITION,
            change_message="Object has been added",
        )
