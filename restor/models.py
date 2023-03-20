from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'User {self.username}'


class Client(models.Model):
    name = models.CharField(max_length=20)
    card_number = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Клиент {self.name}'


class Worker(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Клиент {self.name}'


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField()

    def __str__(self):
        return f'{self.name} + {self.extra_price}'


class Food(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.ManyToManyField(Ingredient, related_name='foods', through='Order')
    start_price = models.IntegerField()

    def __str__(self):
        return f"Блюдо {self.name}"


class Order(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    Order_date_time = models.DateField()

    def __str__(self):
        return f"Ингередиент {self.ingredient.name} блюдо {self.food.name} заказал {self.client.name} оформил {self.worker.name}"
