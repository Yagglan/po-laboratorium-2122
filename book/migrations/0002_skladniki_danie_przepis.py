# Generated by Django 4.0.4 on 2022-04-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='skladniki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_skladnika', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='danie',
            name='przepis',
            field=models.ManyToManyField(to='book.skladniki'),
        ),
    ]