from django.contrib import admin
from .models import Property,Place,PropertyBook,PropertyImages,PropertyReview,Category
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name','price', 'get_avg_rating', 'check_availability']

class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property', 'in_progress']

admin.site.register(Property, SomeModelAdmin)
admin.site.register(Place)
admin.site.register(PropertyBook, PropertyBookAdmin)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)