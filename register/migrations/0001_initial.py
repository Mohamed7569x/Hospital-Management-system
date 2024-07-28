# Generated by Django 4.2 on 2024-07-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=255)),
                ('Phone', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Emergency_Contact', models.CharField(max_length=255)),
                ('Medical_History', models.CharField(max_length=255)),
            ],
        ),
    ]
