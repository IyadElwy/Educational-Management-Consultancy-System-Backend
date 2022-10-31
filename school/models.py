from django.db import models


class Location(models.Model):
    description = models.CharField(max_length=500)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f'{self.lat}-{self.lon}'


class ContactPerson(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class School(models.Model):
    # info
    name = models.CharField(max_length=100)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    contact_person = models.OneToOneField(ContactPerson, on_delete=models.CASCADE)
    school_description = models.TextField()
    # dev
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
