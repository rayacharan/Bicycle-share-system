# Generated by Django 3.2.19 on 2023-06-01 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_use', models.BooleanField(default=False)),
                ('is_faulty', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Bikes',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(default='', max_length=100)),
                ('station_latitude', models.FloatField(null=True)),
                ('station_longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('check_out_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_amount', models.FloatField(default=0.0)),
                ('fix_amount', models.FloatField(default=0.0)),
                ('is_complete', models.BooleanField(default=False)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BikeShare.bike')),
                ('end_station', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='BikeShare.station')),
                ('start_station', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='startstation', to='BikeShare.station')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BikeShare.station'),
        ),
    ]
