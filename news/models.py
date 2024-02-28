from django.db import models

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        db_table = 'contact'

class New(AbstractBaseModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.title

# models.py
class Advertise(AbstractBaseModel):
    title = models.CharField(max_length=128)
    body = models.TextField()
    brand = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Advertise'
        verbose_name_plural = 'Advertises'
        db_table = 'advertise'

    def __str__(self):
        return self.title







