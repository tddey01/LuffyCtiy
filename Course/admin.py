from django.contrib import admin

# Register your models here.
from Course import models

for table in models.__all__:
    admin.site.register(getattr(models, table))