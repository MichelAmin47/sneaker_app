from django.contrib import admin

from .models import Question
from .models import Shoe

admin.site.register(Question)
admin.site.register(Shoe)

