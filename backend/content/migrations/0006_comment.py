# Generated by Django 4.0.5 on 2022-07-02 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0005_alter_article_rating_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(blank=True, default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_article_name', to='content.article')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_creator', to=settings.AUTH_USER_MODEL)),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.comment')),
            ],
        ),
    ]
