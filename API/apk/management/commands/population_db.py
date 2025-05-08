import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from apk.models import Product, Order, OrderItem
from apk.models import CustomUser as User

class Command(BaseCommand):
    help = 'Creaytes application data'

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username = 'admin', password='test')

        products = [
            Product(name="A Scanner Darkly", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=4),
            Product(name="Coffee Machine",description=lorem_ipsum.paragraph(), price=Decimal('70.99'), stock =6),
            Product(name="Velvet Underground & Nitco", description=lorem_ipsum.paragraph(), price=Decimal('15.99'), stock=11),
            Product(name="Enter the Wu-Tang(36 Chambers)", description=lorem_ipsum.paragraph(), price=Decimal('17.99'), stock=2),
            Product(name="Digital Camera", description=lorem_ipsum.paragraph(), price=Decimal('350.99'), stock=4),
            Product(name="Watch", description=lorem_ipsum.paragraph(), price=Decimal('500.05'), stock=0),
        ]

        Product.objects.bulk_create(products)
        products = Product.objects.all()

        # create some dummy orders tied to the supruser
        for _ in range(3):
            order = Order.objects.create(user=user)
            for product in random.sample(list(products), 2):
                OrderItem.objects.create(
                    order=order, product = product, quantity = random.randint(1,3)
                )



