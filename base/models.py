from django.db import models

# Create your models here.

class Mahsulot_filter(models.Model):
    name = models.CharField(max_length=100, help_text="mahsulot filteri", verbose_name="Mahsulot filteri")

    def __str__(self):
        return self.name

class Mahsulot(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="Mahsulot nomi", help_text="mahsulot nomi")
    filter = models.ForeignKey(Mahsulot_filter, verbose_name="Filteri", on_delete=models.CASCADE)
    buy_price = models.FloatField(verbose_name="Kelish narxi", help_text="kelish narxi")
    sell_price = models.FloatField(verbose_name="Sotish narxi", help_text="sotish narxi")
    miqdori = models.IntegerField(verbose_name="Miqdori")
    izoh = models.TextField(max_length=500, blank=True, null=True, verbose_name="Litri, brendi....", help_text="litri, brendi....")
    time = models.DateTimeField(verbose_name="Vaqti")

    def __str__(self):
        return self.product_name

class Oluvchi(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mashina nomi", help_text="mashina nomi")
    car_number = models.CharField(max_length=20, verbose_name="Mashina raqami", help_text="mashina raqami")
    total_cost = models.FloatField(verbose_name="Umumiy narx", help_text="umumiy narx")
    time = models.DateTimeField()

    def __str__(self):
        return self.name

class Savdo(models.Model):
    product = models.ForeignKey(Mahsulot, verbose_name="Mahsulot", on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(verbose_name="Miqdori")
    cost = models.FloatField(verbose_name="Narxi")
    oluvchi = models.ForeignKey(Oluvchi, on_delete=models.SET_NULL, verbose_name="Oluvchi", null=True, related_name="savdolar")

    def __str__(self):
        return self.name

class Chiqim(models.Model):
    money = models.FloatField(verbose_name="Pul miqdori", help_text='pul miqdori')
    comment = models.CharField(max_length=500, verbose_name="Nima uchun sarflandi'", help_text='nima uchun sarflandi')
    person = models.CharField(max_length=200, verbose_name="Kim sarfladi", help_text='kim sarfladi', blank=True, null=True)
    date = models.DateTimeField(verbose_name="Vaqti")

    def __str__(self):
        return self.comment




