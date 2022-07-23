# Generated by Django 4.0.6 on 2022-07-23 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=60, null=True, verbose_name='First Name')),
                ('lname', models.CharField(blank=True, max_length=60, null=True, verbose_name='Last Name')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Age')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('joining_date', models.DateField(blank=True, null=True, verbose_name='Joining Date')),
                ('designation', models.CharField(blank=True, choices=[('Software Engineer', 'Software Engineer'), ('Quality Analyst', 'Quality Analyst'), ('Product Manager', 'Product Manager')], max_length=100, null=True, verbose_name='Designation')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.BooleanField(default=False, verbose_name='Task Attended')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('task', models.TextField(blank=True, null=True, verbose_name='Task')),
                ('death_line', models.DateField(blank=True, null=True, verbose_name='Last Date For Submiting')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]