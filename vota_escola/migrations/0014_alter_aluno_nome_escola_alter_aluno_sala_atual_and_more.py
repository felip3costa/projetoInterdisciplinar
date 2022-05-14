# Generated by Django 4.0.4 on 2022-05-07 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vota_escola', '0013_alter_escola_unique_together_alter_escola_bairro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nome_escola',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vota_escola.escola'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='sala_atual',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vota_escola.sala'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turma_atual',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vota_escola.turma'),
        ),
    ]
