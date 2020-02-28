from rest_framework import serializers
from courses.models import *


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address')


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'imgpath')


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)
    branches = BranchSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Course
        fields = ('name', 'description', 'category', 'logo', 'branches', 'contacts')

    def create(self, validated_data):
        branches_data = validated_data.pop('branches')
        contacts_data = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)

        for branch in branches_data:
            branch, created = Branch.objects.get_or_create(address=branch['address'])
            course.branches.add(branch)

        for contact in contacts_data:
            contact, created = Contact.objects.get_or_create(value=contact['value'])
            course.contacts.add(contact)
        return course


class CoursesDetalSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Course
        fields = "__all__"


