# Generated by Django 5.0.7 on 2024-07-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(upload_to='movies')),
            ],
        ),
    ]
