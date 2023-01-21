# Generated by Django 4.1.5 on 2023-01-20 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curator', '0001_initial'),
        ('discipline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('curator', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='direction', to='curator.curator', verbose_name='Куратор')),
                ('disciplines', models.ManyToManyField(related_name='directions', to='discipline.discipline', verbose_name='Дисциплины')),
            ],
            options={
                'verbose_name': 'Направление подготовки',
                'verbose_name_plural': 'Направления подготовки',
                'ordering': ['-name'],
            },
        ),
    ]
