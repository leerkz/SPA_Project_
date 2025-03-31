from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from users.models import Payments


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerializers(ModelSerializer):
    many_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_subscription(self, course):
        user = self.context['request'].user
        return Payments.objects.all().filter(user=user).filter(course=course).exists()

    def get_many_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'many_lessons', 'subscription')