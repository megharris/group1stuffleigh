# Generated by Django 2.2.7 on 2019-11-17 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField(blank=True)),
                ('course_subject', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=100)),
                ('room_capacity', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=100)),
                ('stud_address', models.CharField(max_length=200)),
                ('stud_city', models.CharField(max_length=50)),
                ('stud_zip', models.CharField(max_length=10)),
                ('stud_email', models.CharField(max_length=50)),
                ('stud_phone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tutor_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('tutor_name', models.CharField(max_length=50)),
                ('tutor_zip', models.CharField(max_length=10)),
                ('tutor_email', models.CharField(max_length=50)),
                ('tutor_phone', models.CharField(max_length=50)),
                ('tutor_sub_expertise', models.CharField(max_length=50)),
                ('tutor_bank', models.CharField(max_length=100)),
                ('tutor_rt_num', models.CharField(max_length=10)),
                ('tutor_acct_num', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_id', models.IntegerField()),
                ('schedule_date', models.DateField()),
                ('schedule_time', models.TimeField()),
                ('schedule_notes', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('schedule_course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='sis.Course')),
                ('schedule_room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='sis.Room')),
                ('schedule_tutor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedulelist', to='sis.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='schedules',
            field=models.ManyToManyField(blank=True, to='sis.Schedule'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
