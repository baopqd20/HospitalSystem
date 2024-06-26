# Generated by Django 4.2.11 on 2024-05-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPatient', models.IntegerField()),
                ('patientName', models.CharField(max_length=200)),
                ('patientContact', models.CharField(max_length=200, null=True)),
                ('idDoctor', models.IntegerField()),
                ('doctorName', models.CharField(max_length=200)),
                ('doctorContact', models.CharField(max_length=200, null=True)),
                ('result', models.CharField(max_length=200)),
                ('medicine', models.CharField(max_length=200, null=True)),
                ('boarding', models.CharField(max_length=200, null=True)),
                ('note', models.CharField(max_length=200, null=True)),
                ('createdDay', models.DateField()),
                ('age', models.IntegerField()),
                ('reSchedule', models.DateField()),
                ('fee', models.IntegerField()),
            ],
        ),
    ]
