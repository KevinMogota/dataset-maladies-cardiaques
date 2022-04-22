from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'sbp', 'tobacco', 'ldl', 'adiposity', 'famhist', 'type', 'obesity', 'alcohol', 'age', 'predictions')

admin.site.register(Data, DataAdmin)
