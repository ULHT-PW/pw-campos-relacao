# Generated by Django 4.0.5 on 2023-05-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campos_relacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('alunos', models.ManyToManyField(to='campos_relacao.aluno')),
            ],
        ),
    ]