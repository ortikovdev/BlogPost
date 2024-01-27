# Generated by Django 5.0.1 on 2024-01-25 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_created_date_article_modified_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.article'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subarticle',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.article'),
            preserve_default=False,
        ),
    ]