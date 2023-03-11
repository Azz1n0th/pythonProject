from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=1000, primary_key=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self):
        return self.sku


class PhysicalProduct(Product):
    name = models.CharField(max_length=1000)


class ServiceProduct(Product):
    name = models.CharField(max_length=1000)


class Customer(models.Model):
    name = models.CharField(max_length=1000, primary_key=True)
    customer_number = models.CharField(max_length=200)


class InvoiceInbound(models.Model):
    invoice_number = models.CharField(max_length=100)
    products = models.ManyToManyField("self")
    total_price = models.DecimalField(max_digits=200, decimal_places=2)


class InvoiceOutbound(models.Model):
    invoice_number = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self):
        return self.invoice_number


class FiscalNote(models.Model):
    invoice_number = models.CharField(max_length=100)
    products = models.ManyToManyField("self")
    total_price = models.DecimalField(max_digits=200, decimal_places=2)


class AccessAccount(models.Model):
    username = models.CharField(max_length=500, primary_key=True)
    password = models.CharField(max_length=2000)
    email = models.EmailField()


class Vendor(models.Model):
    name = models.CharField(max_length=2000)
    VAT_Number = models.CharField(max_length=2000)


class Tax(models.Model):
    name = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=200, decimal_places=2)

    class Meta:
        verbose_name_plural = "Taxes"


class Fee(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=200, decimal_places=2)


class ExpenseItem(models.Model):
    item_name = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=200, decimal_places=2)


class Employee(models.Model):
    first_name = models.CharField(max_length=2000)
    middle_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=2000)


