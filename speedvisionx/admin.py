from django.contrib import admin

# Register your models here.
from speedvisionx.models import RaceMatrix

class RaceMatrixDetails(admin.ModelAdmin):
    search_fields = ["media_id"]
    list_display = ["index", "media_id", "video_url"]
    readonly_fields = ["index"]
    #
    # fieldsets = (
    #     ('Block Info', {"fields": ("index", "media_id", "video_url", "")}),
    #     # ('Transaction Data', {"fields": ("transaction", "timestamp")}),
    # )

    # add_fieldsets = (
    #     ('Transaction Data', {"fields": ("media_id",)}),
    # )
    #
    # def get_fieldsets(self, request, obj=None):
    #     if not obj:
    #         return self.add_fieldsets
    #     return super().get_fieldsets(request, obj)
    # def get_readonly_fields(self, request, obj=None):
    #     if not obj:
    #         return ["index", "hash", "previous_hash", "timestamp"]
    #     return self.readonly_fields


admin.site.register(RaceMatrix, RaceMatrixDetails)