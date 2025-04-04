from django.contrib import admin
from cartapp import models

admin.site.register(models.ProductModel)
admin.site.register(models.OrdersModel)
admin.site.register(models.DetailModel)
admin.site.register(models.temperature_db)
