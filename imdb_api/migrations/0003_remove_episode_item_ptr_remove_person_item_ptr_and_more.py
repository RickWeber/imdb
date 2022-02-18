# Generated by Django 4.0.2 on 2022-02-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_api', '0002_item_remove_episode_episode_remove_episode_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='item_ptr',
        ),
        migrations.RemoveField(
            model_name='person',
            name='item_ptr',
        ),
        migrations.RemoveField(
            model_name='title',
            name='item_ptr',
        ),
        migrations.AddField(
            model_name='episode',
            name='data',
            field=models.JSONField(default=0, verbose_name='json data'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episode',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episode',
            name='last_update',
            field=models.DateTimeField(default=0, verbose_name='last update'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='data',
            field=models.JSONField(default=0, verbose_name='json data'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_update',
            field=models.DateTimeField(default=0, verbose_name='last update'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='data',
            field=models.JSONField(default=0, verbose_name='json data'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='last_update',
            field=models.DateTimeField(default=0, verbose_name='last update'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
