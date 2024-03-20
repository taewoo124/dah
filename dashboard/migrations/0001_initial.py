# Generated by Django 4.2.11 on 2024-03-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('description', models.TextField(verbose_name='설명')),
                ('body', models.TextField(verbose_name='본문')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]