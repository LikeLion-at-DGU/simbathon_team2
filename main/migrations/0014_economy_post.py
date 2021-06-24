# Generated by Django 3.2.4 on 2021-06-22 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_management_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='economy_Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
