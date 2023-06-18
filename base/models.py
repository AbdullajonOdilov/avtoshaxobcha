from django.db import models

# Create your models here.

class Mahsulot_filter(models.Model):
    name = models.CharField(max_length=100, help_text="mahsulot filteri")

    def __str__(self):
        return self.name

class Mahsulot(models.Model):
    product_name = models.CharField(max_length=100, help_text="mahsulot nomi")
    filter = models.ForeignKey(Mahsulot_filter, on_delete=models.CASCADE)
    buy_price = models.FloatField(help_text="kelish narxi")
    sell_price = models.FloatField(help_text="sotish narxi")
    miqdori = models.IntegerField()
    izoh = models.CharField(max_length=500, blank=True, null=True, help_text="litri, brandi....")
    time = models.DateTimeField()

    def __str__(self):
        return self.product_name

class Oluvchi(models.Model):
    name = models.CharField(max_length=100, help_text="mashina nomi")
    car_number = models.CharField(max_length=20, help_text="mashina raqami")
    total_cost = models.FloatField(help_text="umumiy narx")
    time = models.DateTimeField()

    def __str__(self):
        return self.name

class Savdo(models.Model):
    product = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    cost = models.FloatField()
    oluvchi = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True, related_name="savdolar")

    def __str__(self):
        return self.name

class Chiqim(models.Model):
    money = models.FloatField(help_text='pul miqdori')
    comment = models.CharField(max_length=500, help_text='nima uchun sarflandi')
    person = models.CharField(max_length=200, help_text='kim sarfladi', blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.comment




