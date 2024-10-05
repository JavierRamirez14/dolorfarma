# Generated by Django 5.0.4 on 2024-07-28 11:21

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='None', max_length=100)),
                ('duracion', models.CharField(default='None', max_length=100)),
                ('documento', models.TextField(blank=True, default='None', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='None', max_length=100)),
                ('dolor', models.CharField(default='None', max_length=100)),
                ('cuerpo', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dolor', models.CharField(default='None', max_length=100)),
                ('cuerpo', models.CharField(default='None', max_length=100)),
                ('patologia', models.CharField(default='None', max_length=200)),
                ('intensidad', models.CharField(default='None', max_length=100)),
                ('duracion', models.CharField(default='None', max_length=100)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]