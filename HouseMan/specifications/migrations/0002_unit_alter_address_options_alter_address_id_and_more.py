# Generated by Django 5.1.4 on 2025-01-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address'},
        ),
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='building',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
