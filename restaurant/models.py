from django.db import models

class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    # Removed the default so a password must be provided (and hashed) when creating a user.
    password = models.CharField(max_length=255)
    school = models.CharField(max_length=255, default="NYU")
    grade = models.CharField(max_length=20, default="Freshman")

    def __str__(self):
        return self.name


class Discounts(models.Model):
    discount_id = models.BigAutoField(primary_key=True)
    discount_type = models.CharField(max_length=255)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    # Uncomment and add valid_from/valid_until if needed:
    # valid_from = models.DateTimeField()
    # valid_until = models.DateTimeField()

    def __str__(self):
        return self.discount_type


class Restaurants(models.Model):
    restaurant_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    cuisine_type = models.CharField(max_length=255, blank=True, null=True)
    open_hours = models.CharField(max_length=255, blank=True, null=True)
    google_place_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    discounts_id = models.ForeignKey(Discounts, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Menus(models.Model):
    menu_id = models.BigAutoField(primary_key=True)
    restaurant_id = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name="menus")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        # Note: Using restaurant_id's related Restaurants object's name.
        return f"{self.name} - {self.restaurant_id.name}"


class Reviews(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="reviews")
    restaurant_id = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name="reviews")
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_id.name} for {self.restaurant_id.name}"