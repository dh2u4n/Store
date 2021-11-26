from django.db import models


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=100)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=400, null=True)

    def getAddress(self):
        return self.street + ', ' + self.ward.name + ', ' + self.district.name + ', ' + self.city.name

    def numCart(self):
        return len(Order.objects.filter(customer=self, status="incart"))

    def __str__(self):
        return self.name


class Product(models.Model):
    type = models.CharField(max_length=100, choices=[('iphone', 'iphone'), (
        'ipad', 'ipad'), ('mac', 'mac'), ('watch', 'watch'), ], default='iphone')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantityInStock = models.IntegerField()
    showcasedImg = models.ImageField(null=True)
    id = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return self.name


class Product_img(models.Model):
    id = models.AutoField(primary_key=True)
    productID = models.CharField(max_length=32)
    img = models.ImageField(null=True)
    color = models.CharField(max_length=10, null=True)


class Product_color(models.Model):
    id = models.AutoField(primary_key=True)
    productID = models.CharField(max_length=32)
    color = models.CharField(max_length=10)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    stt = (
        ('incart', 'Trong giỏ hàng'),
        ('processing', 'Đang xử lý'),
        ('done', 'Đã hoàn thành'),
    )
    status = models.CharField(max_length=20, choices=stt, default='inCart')

    def __str__(self):
        return str(self.id)
