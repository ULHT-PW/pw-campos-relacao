# Generated by Django 4.0.5 on 2023-05-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campos_relacao', '0002_aluno_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='alunos',
            field=models.ManyToManyField(related_name='disciplinas', to='campos_relacao.aluno'),
        ),
    ]
