from django.contrib import admin

# from .models import Restaurants, Menus, Discounts

from .models import Users, Restaurants, Menus, Discounts, Reviews


@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "rating",
    )
    list_editable = ("rating",)


admin.site.register(Users)
# admin.site.register(Restaurants)
admin.site.register(Menus)
admin.site.register(Discounts)
admin.site.register(Reviews)

# python manage.py createsuperuser if want to see these as admin http://127.0.0.1:8000/admin/
