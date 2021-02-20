from django.db import models

# Create your models here.

product_type = (
    ('1', 'LARGE'),
    ('0', 'SMALL'),
    ('2', 'ESPRESSO'),
)
coffee_machine_model = (
    ('1', 'base model'),
    ('2', 'premium model'),
    ('3', 'deluxe model')
)
coffee_pod_flavor = (
    ('0', 'vanilla'),
    ('1', 'caramel'),
    ('2', 'psl'),
    ('3', 'mocha'),
    ('4', 'hazelnut')
)
coffee_pod_pack_size = (
    ('1', '1 dozen'),
    ('3', '3 dozen'),
    ('5', '5 dozen'),
    ('7', '7 dozen'),
)


class CoffeeMachine(models.Model):
    name = models.CharField(max_length=10, blank=True)
    product_type = models.CharField(max_length=30, choices=product_type)
    model = models.CharField(max_length=30, choices=coffee_machine_model)
    water_line_compatible = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        name = "CM{}".format(self.product_type)

        if self.product_type == '2':
            name = "EM0"

        name += "0{}".format(self.model)

        self.name = name

        super(CoffeeMachine, self).save(*args, **kwargs)


class CoffeePod(models.Model):
    name = models.CharField(max_length=10, blank=True)
    product_type = models.CharField(max_length=30, choices=product_type)
    coffee_flavor = models.CharField(max_length=30, choices=coffee_pod_flavor)
    pack_size = models.CharField(max_length=30, choices=coffee_pod_pack_size)

    def save(self, *args, **kwargs):
        name = "CP{}".format(self.product_type)

        if self.product_type == '2':
            name = "EP0"

        name += "{}{}".format(self.coffee_flavor, self.pack_size)

        self.name = name

        super(CoffeePod, self).save(*args, **kwargs)
