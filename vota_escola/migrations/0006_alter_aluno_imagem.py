# Generated by Django 4.0.4 on 2022-04-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vota_escola', '0005_alter_aluno_ra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='imagem',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]