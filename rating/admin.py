from django.contrib import admin
from .models import MLScore, StudentRating, CoordinatorRating

admin.site.register(MLScore)
admin.site.register(StudentRating)
admin.site.register(CoordinatorRating)
