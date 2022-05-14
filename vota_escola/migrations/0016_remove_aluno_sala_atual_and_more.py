# Generated by Django 4.0.4 on 2022-05-09 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vota_escola', '0015_escola_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='sala_atual',
        ),
        migrations.AlterUniqueTogether(
            name='candidato',
            unique_together={('ano', 'candidato', 'turma')},
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='sala',
        ),
        migrations.DeleteModel(
            name='Sala',
        ),
    ]