# Generated by Django 4.0.4 on 2022-05-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vota_escola', '0012_alter_candidato_sala'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='escola',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='escola',
            name='bairro',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='escola',
            name='cidade',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='escola',
            name='complemento',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='escola',
            name='estado',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
    ]