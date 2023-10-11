# Generated by Django 3.2.22 on 2023-10-11 14:51

from django.db import migrations, models
import healtheat.apps.base.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('day', models.PositiveSmallIntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], unique=True, verbose_name='День недели')),
                ('breakfast', healtheat.apps.base.models.BlankCharField(blank=True, max_length=255, null=True, verbose_name='Завтрак')),
                ('elevenses', healtheat.apps.base.models.BlankCharField(blank=True, max_length=255, null=True, verbose_name='Второй завтрак')),
                ('lunch', healtheat.apps.base.models.BlankCharField(blank=True, max_length=255, null=True, verbose_name='Обед')),
                ('afternoon_tea', healtheat.apps.base.models.BlankCharField(blank=True, max_length=255, null=True, verbose_name='Полдник')),
                ('dinner', healtheat.apps.base.models.BlankCharField(blank=True, max_length=255, null=True, verbose_name='Ужин')),
            ],
            options={
                'verbose_name': 'Ежедневное меню',
                'verbose_name_plural': 'Ежедневное меню',
                'ordering': ['day'],
            },
        ),
    ]