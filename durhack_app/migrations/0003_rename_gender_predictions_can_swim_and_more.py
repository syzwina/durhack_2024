# Generated by Django 5.1.2 on 2024-11-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('durhack_app', '0002_rename_petal_length_predictions_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictions',
            old_name='gender',
            new_name='can_swim',
        ),
        migrations.RenameField(
            model_name='predictions',
            old_name='sick',
            new_name='sex',
        ),
        migrations.RemoveField(
            model_name='predictions',
            name='went_to_lifeboat',
        ),
        migrations.AddField(
            model_name='predictions',
            name='pclass',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='predictions',
            name='age',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
