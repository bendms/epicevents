# Generated by Django 4.1.7 on 2023-02-22 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=25)),
                ('lastname', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('company_name', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('sales_contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PLANNED', 'Planifié'), ('ACCOMPLISHED', 'Réalisé')], max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('attendees', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('notes', models.CharField(max_length=500)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('event_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.eventstatus')),
                ('support_contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('amount', models.FloatField()),
                ('payment_due', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('sales_contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
