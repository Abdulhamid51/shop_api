from django.db import models
from django.contrib.auth.models import User

# User profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.BooleanField("Jinsi(True=erkak)")
    brithday = models.DateField("Tug'ilgan kuni")
    phone = models.PositiveIntegerField("Tel raqami")
    cart = models.ForeignKey("api.Cart", related_name="owner", on_delete=models.PROTECT, blank=True)
    adress = models.ForeignKey("api.Adress", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user.username


# User profile details
class Cart(models.Model):
    carts = models.ManyToManyField("api.Carts", blank=True)
    all_price = models.DecimalField("jami narxi", max_digits=5, decimal_places=2, default=0)
    all_pieces = models.PositiveIntegerField("jami soni")
    payment_method = models.ForeignKey("api.PayMethod", verbose_name="kredit kartasi", on_delete=models.PROTECT, blank=True)

class Carts(models.Model):
    product = models.ForeignKey("api.Product", verbose_name="mahsulot", on_delete=models.CASCADE)
    pieces = models.PositiveIntegerField("soni")

class PayMethod(models.Model):
    card_num = models.PositiveIntegerField("karta raqami")
    card_date = models.CharField("sanasi", max_length=5)
    card_name = models.CharField("ismi", max_length=150)

    def __str__(self):
        return self.card_name

class Adress(models.Model):
    REGIONS = (
        ('Andijon','Andijon'),
        ('Namangan','Namangan'),
        ('Farg`ona','Farg`ona'),
        ('Toshkent','Toshkent'),
        ('Jizzax','Jizzax'),
        ('Samarqand','Samarqand'),
        ('Qashqadaryo','Qashqadaryo'),
        ('Surxondaryo','Surxondaryo'),
        ('Navoiy','Navoiy'),
        ('Buxoro','Buxoro'),
        ('Sirdaryo','Sirdaryo'),
        ('Xorazm','Xorazm'),
        ('Qoraqalpog`iston','Qoraqalpog`iston'),
    )
    region = models.CharField(choices=REGIONS, max_length=50)
    district = models.CharField("tuman", max_length=50)


# Product details
class Categories(models.Model):
    title = models.CharField("Nomi", max_length=50)
    icon = models.ImageField("rasmi", upload_to='category_img/')

    def __str__(self):
        return self.title


class Colors(models.Model):
    name = models.CharField("Rang nomi", max_length=50)
    code = models.CharField("Rang kodi", max_length=50)

    def __str__(self):
        return self.name


class Sizes(models.Model):
    number = models.CharField("razmeri", max_length=50)

    def __str__(self):
        return self.number


class Images(models.Model):
    image = models.ImageField("rasmi", upload_to='product_images')

# Product 
class Product(models.Model):
    images = models.ManyToManyField("api.Images")
    title = models.CharField("Nomi", max_length=150)
    price = models.DecimalField("narxi", max_digits=5, decimal_places=2)
    price_off = models.DecimalField("aksiya %", max_digits=5, decimal_places=2)
    shipping = models.DecimalField("elitib berish", max_digits=5, decimal_places=2)
    sizes = models.ManyToManyField("api.Sizes", verbose_name="olchami")
    colors = models.ManyToManyField("api.Colors", verbose_name="rangi")
    category = models.ForeignKey("api.Categories", verbose_name="Kategoriyasi", on_delete=models.CASCADE)
    style = models.CharField("styli", max_length=50, blank=True)
    info = models.TextField("malumoti", blank=True)
    date = models.DateField("sanasi", auto_now_add=True)

    def __str__(self):
        return self.title

# Product reviews
class Reviews(models.Model):
    product = models.ForeignKey("api.Product", related_name="rate", on_delete=models.CASCADE)
    user = models.ForeignKey("api.UserProfile", related_name="reviews", on_delete=models.CASCADE)
    stars = models.PositiveIntegerField("max 5")
    message = models.TextField("fikr")
    date = models.DateTimeField("sanasi", auto_now_add=True)