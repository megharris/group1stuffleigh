from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    stud_name = models.CharField(max_length=100)
    stud_address = models.CharField(max_length=200)
    stud_city = models.CharField(max_length=50)
    stud_zip = models.CharField(max_length=10)
    stud_email = models.CharField(max_length=50)
    stud_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.stud_name)

class Tutor(models.Model):
    tutor_id = models.IntegerField(primary_key=True, default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tutor_name = models.CharField(max_length=50)
    # tutor_name = models.ForeignKey('Profile', related_name='contents', on_delete=models.CASCADE)
    tutor_zip = models.CharField(max_length=10)
    tutor_email = models.CharField(max_length=50)
    tutor_phone = models.CharField(max_length=50)
    tutor_sub_expertise = models.CharField(max_length=50)
    tutor_bank = models.CharField(max_length=100)
    tutor_rt_num = models.CharField(max_length=10)
    tutor_acct_num = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.tutor_name)

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True, default=0)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(blank=True)
    course_subject = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.course_name)

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True, default=0)
    room_number = models.CharField(max_length=100)
    room_capacity = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.room_number)


class Schedule(models.Model):
    schedule_id = models.IntegerField()
    #schedule_course_name = models.CharField(max_length=100)
    schedule_course_name = models.ForeignKey(Course, related_name='contents', on_delete=models.CASCADE)
    schedule_room_number = models.ForeignKey(Room, related_name='contents', on_delete=models.CASCADE)
    schedule_tutor_name = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='schedulelist', on_delete=models.CASCADE)
    # tutor_email = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='email', on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    schedule_notes = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)
#    max_seat = models.IntegerField()


    def created(self):
        self.created = timezone.now()
        self.save()

    def updated(self):
        self.updated = timezone.now()
        self.save()

    def __str__(self):
        return str(self.schedule_course_name)

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    schedules = models.ManyToManyField(Schedule, blank=True)

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
