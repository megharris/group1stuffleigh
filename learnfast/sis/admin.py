from django.contrib import admin
from .models import Student, Course, Room, Schedule, Profile, Tutor
from django.core.mail import send_mail


class StudentList(admin.ModelAdmin):
    list_display = ('stud_name', 'stud_email', 'stud_phone')
    list_filter = ('stud_name')
    search_fields = ('stud_name')
    ordering = ['stud_name']

@admin.register(Tutor)
class TutorList(admin.ModelAdmin):
    list_display = ('tutor_name', 'tutor_sub_expertise', 'tutor_email')
    list_filter = ('tutor_name', 'tutor_sub_expertise')
    search_fields = ('tutor_name', 'tutor_sub_expertise')
    ordering = ['tutor_name']
    actions = ['send_email_html']

    def send_email_html(selfmodeladmin, request, queryset):
        for profile in queryset:
            send_mail(subject="Schedules Prepared", message="Schedules for next week are prepared. Please check your dashboard.\n\nSincerely,\n\nLearnFast Administration", from_email='learnfasttutoring@gmail.com', recipient_list=[profile.tutor_email])

@admin.register(Course)
class CourseList(admin.ModelAdmin):
    list_display = ('course_name', 'course_subject')
    list_filter = ('course_name', 'course_subject')
    search_fields = ('course_name', 'course_subject')
    ordering = ['course_name']

@admin.register(Room)
class RoomList(admin.ModelAdmin):
    list_display = ('room_number', 'room_capacity')
    list_filter = ('room_number', 'room_capacity')
    search_fields = ('room_number', 'room_capacity')
    ordering = ['room_number']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['schedule_course_name', 'schedule_tutor_name', 'slug', 'price',
                    'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('schedule_course_name',)}
    actions = ['send_email_html']

    def send_email_html(selfmodeladmin, request, queryset):
        for profile in queryset:
            send_mail(subject="Schedules Prepared",
                      message="Schedules for next week are prepared. Please check your dashboard.\n\nSincerely,\n\nLearnFast Administration",
                      from_email='learnfasttutoring@gmail.com', recipient_list=[profile.schedule_tutor_name])


admin.site.register(Student)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Profile, UserProfileAdmin)