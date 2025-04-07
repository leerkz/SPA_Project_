from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import youtube_only_validator
from users.models import Payments


class CourseSerializer(ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.subscription_set.filter(user=user).exists()
        return False


class LessonSerializer(ModelSerializer):
    link = serializers.URLField(validators=[youtube_only_validator])
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