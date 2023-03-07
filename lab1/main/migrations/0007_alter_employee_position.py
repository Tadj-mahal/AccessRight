# Generated by Django 4.1.7 on 2023-03-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_employee_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('secretary', 'Secretary'), ('associate director', 'Associate Director'), ('director', 'Director')], max_length=150),
        ),
    ]