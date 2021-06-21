# Generated by Django 2.2.9 on 2021-06-18 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Сообщества',
                'verbose_name_plural': 'Сообщества',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликованно'),
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='posts.Group', verbose_name='Сообщество'),
        ),
    ]
