# Generated by Django 3.0.8 on 2020-12-30 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.Tree')),
            ],
        ),
    ]