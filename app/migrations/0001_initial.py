# Generated by Django 4.0.5 on 2022-07-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_de_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
