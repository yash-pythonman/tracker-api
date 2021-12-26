from django.db import models


class BaseModel(models.Model):
    """
    Model created to add common field in all tables.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(BaseModel):
    """
    Model created to store details of organization's address.
    """
    type = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    county = models.CharField(max_length=100)

    class Meta:
        abstract = True
