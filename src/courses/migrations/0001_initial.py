# Generated by Django 4.0.1 on 2022-01-14 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('allowed_memberships', models.ManyToManyField(to='memberships.Membership')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('position', models.IntegerField()),
                ('video_url', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
            ],
        ),
    ]
