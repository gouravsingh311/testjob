from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True,unique=True)
    contact_number=models.CharField(max_length=10)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True,unique=True)
    weight=models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.name


class Order(models.Model):
    order_number=models.CharField(max_length=255,null=True,blank=True,unique=True)
    customer=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE,related_name='customer_order') 
    order_date=models.DateField(auto_now_add=True)
    addres=models.CharField(max_length=1050)

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.order_by('-id').first()
            new_order_number = "ORD{:05d}".format(last_order.id + 1) if last_order else "ORD00001"
            self.order_number = new_order_number

        super().save(*args, **kwargs)

 
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,null=True,blank=True,on_delete=models.CASCADE,related_name='order_item')
    product=models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE,related_name='product_order_item')
    quantity=models.PositiveIntegerField()

    
    def __str__(self):
        return self.quantity

