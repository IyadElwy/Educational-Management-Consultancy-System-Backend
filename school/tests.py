from django.test import TestCase
from .models import School, Location, ContactPerson
from django.db.utils import IntegrityError


class SchoolTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        contact_person_1 = ContactPerson.objects.create(
            name='Jane Doe', email='jane_doe@gmail.com', phone='0232242324'
        )
        contact_person_1.save()

        location_1 = Location.objects.create(
            description='Near south 90', country='Egypt', city='Cairo',
            district='Tagamoo', lat=23.232233, lon=355.33242
        )
        location_1.save()

        school_1 = School.objects.create(
            name='Europa Schule Kairo', location=location_1, contact_person=contact_person_1,
            school_description='One of only three german schools in cairo.'
        )
        school_1.save()

    def test_school_data(self):
        school = School.objects.get(id=1)
        self.assertEqual(school.name, 'Europa Schule Kairo')
        self.assertEqual(school.school_description, 'One of only three german schools in cairo.')
        self.assertEqual(school.location.description, 'Near south 90')
        self.assertEqual(school.location.country, 'Egypt')
        self.assertEqual(school.location.city, 'Cairo')
        self.assertEqual(school.location.district, 'Tagamoo')
        self.assertEqual(int(school.location.lat), int(23.232233))
        self.assertEqual(int(school.location.lon), int(355.33242))

    def test_create_school_with_existing_location_and_contact_info(self):
        school_1 = School.objects.get(id=1)
        try:
            School.objects.create(name='Deutsche Evangelische Oberschule',
                                  location=school_1.location,
                                  contact_person=school_1.contact_person,
                                  school_description='The first ever German school in Egypt.')
            raise Exception('The test case of "Creating a school with the same location and contact-info data passed, '
                            'but it should have failed"')
        except IntegrityError as e:
            pass
