
from restor.models import *
user1 = User.objects.create(username="nikname21", password="defender42")
client = Client.objects.create(name="Azat Sokolov", card_number="4147565798789009", user=user1)
user2 = User.objects.create(username="altywa1998", password="nono34")
worker = Worker(name="Altynai ALieva", position="Operator kassi", user=user2)
cheese = Ingredient.objects.create(name="СЫР", extra_price=10)
chicken = Ingredient.objects.create(name="курица", extra_price=70)
beef = Ingredient.objects.create(name="говядина", extra_price=80)
salat = Ingredient.objects.create(name="салат", extra_price=15)
free = Ingredient.objects.create(name="фри", extra_price=15)
burger = Food.objects.create(name="Гамбургер", start_price = 25)
shawerma = Food.objects.create(name="Шаурма", start_price = 50)
burger.ingredients.add(chicken, throught_defaults={'extra_price':70})
burger.ingredients.add(salat, throught_defaults={'extra_price':15})
shawerma.ingredients.add(beef, throught_defaults={'extra_price':70})
shawerma.ingredients.add(cheese, throught_defaults={'extra_price':10})
shawerma.ingredients.add(salat, throught_defaults={'extra_price':15})
shawerma.ingredients.add(free, throught_defaults={'extra_price':15})


