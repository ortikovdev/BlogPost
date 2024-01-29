# Generated by Django 5.0.1 on 2024-01-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_comment_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/')),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]