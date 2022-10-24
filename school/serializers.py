from rest_framework import serializers
from .models import Location, ContactPerson, School


class LocationSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'description',
                  'country',
                  'city',
                  'district',
                  'lat',
                  'lon',)
        model = Location


class ContactPersonSerializer_NO_ID(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'name',
                  'email',
                  'phone',)
        model = ContactPerson


class SchoolSerializer_NO_ID(serializers.ModelSerializer):
    location = LocationSerializer_NO_ID(read_only=False)
    contact_person = ContactPersonSerializer_NO_ID(read_only=False)

    class Meta:
        fields = ('id',
                  'school_description',
                  'name',
                  'location',
                  'contact_person',
                  )
        model = School

    def create(self, validated_data):
        location_data = dict(validated_data['location'])
        contact_person_data = dict(validated_data['contact_person'])

        location = Location.objects.create(description=location_data['description'],
                                           country=location_data['country'],
                                           city=location_data['city'],
                                           district=location_data['district'],
                                           lat=location_data['lat'],
                                           lon=location_data['lon'])

        contact_person = ContactPerson.objects.create(name=contact_person_data['name'],
                                                      email=contact_person_data['email'],
                                                      phone=contact_person_data['phone'])

        school = School.objects.create(name=validated_data['name'],
                                       location=location,
                                       contact_person=contact_person,
                                       school_description=validated_data['school_description'])

        return school


####################################################################################################

class LocationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'description',
                  'country',
                  'city',
                  'district',
                  'lat',
                  'lon',)
        model = Location


class ContactPersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = ('id',
                  'name',
                  'email',
                  'phone',)
        model = ContactPerson


class SchoolSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=False)
    contact_person = ContactPersonSerializer(read_only=False)

    id = serializers.IntegerField(read_only=False)

    class Meta:
        fields = (
            'id',
            'school_description',
            'name',
            'location',
            'contact_person',)
        model = School

    def update(self, instance, validated_data):
        location_data = dict(validated_data['location'])
        contact_person_data = dict(validated_data['contact_person'])

        Location.objects.filter(id=location_data['id']).update(description=location_data['description'],
                                                               country=location_data['country'],
                                                               city=location_data['city'],
                                                               district=location_data['district'],
                                                               lat=location_data['lat'],
                                                               lon=location_data['lon'])

        ContactPerson.objects.filter(id=contact_person_data['id']).update(
            name=contact_person_data['name'],
            email=contact_person_data['email'],
            phone=contact_person_data['phone'])

        School.objects.filter(id=validated_data['id']).update(name=validated_data['name'],
                                                              school_description=validated_data[
                                                                  'school_description'])

        return School.objects.get(id=validated_data['id'])
