# Generated by Django 4.1.3 on 2022-12-15 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='image title')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('place_title', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='place.placetitle')),
            ],
            options={
                'verbose_name': 'place image',
                'verbose_name_plural': 'places images',
                'ordering': ['title', 'id'],
            },
        ),
    ]