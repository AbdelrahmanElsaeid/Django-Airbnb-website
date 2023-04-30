from django.contrib import admin
from .models import Property,Place,PropertyBook,PropertyImages,PropertyReview,Category
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Property, SomeModelAdmin)
admin.site.register(Place)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)