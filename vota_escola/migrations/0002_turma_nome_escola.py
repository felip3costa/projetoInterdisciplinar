# Generated by Django 4.0.4 on 2022-04-28 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vota_escola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='nome_escola',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vota_escola.escola'),
            preserve_default=False,
        ),
    ]