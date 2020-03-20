from django.test import TestCase

# Create your tests here.

from courses.models import Category
from courses.models import Course
from courses.models import Branch
from courses.models import Contact


class CategoryModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name='Fishing',
            imgpath='FlipFlap',
        )
        course = Course.objects.create(
            name='Rod',
            description='For hook to fish',
            category=category,
            logo='Kek',
        )
        Branch.objects.create(
            latitude='1456987423',
            longitude='745596545',
            address='Baikal Lake',
            course=course
        )
        Contact.objects.create(
            type='FACEBOOK',
            value='Baikallake',
            course=course,
        )

    def test_category_creation(self):
        category = Category.objects.get(name='Fishing', imgpath='FlipFlap')
        self.assertEqual(category.name, 'Fishing')
        self.assertEqual(category.imgpath, 'FlipFlap')

    def test_course_creation(self):
        course = Course.objects.get(name='Rod', logo='kek')
        self.assertEqual(course.name, 'Rod')
        self.assertEqual(course.logo, 'kek')

    def test_branch_creation(self):
        branch = Branch.objects.get(latitude='1456987423', address='Baikal Lake')
        self.assertEqual(branch.address, "Baikal Lake")
        self.assertEqual(branch.latitude, "1456987423")

    def test_contact_creation(self):
        contact = Contact.objects.get(type='FACEBOOK', value='Baikallake',)
        self.assertEqual(contact.value, 'Baikallake')
        self.assertEqual(contact.type, 'FACEBOOK')
