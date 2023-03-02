# Generated by Django 4.1.7 on 2023-03-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('apelido', models.CharField(max_length=100)),
                ('sexo', models.BooleanField()),
                ('tipodoc', models.CharField(max_length=200)),
                ('nrdoc', models.CharField(max_length=200)),
                ('dataadmissao', models.DateField()),
                ('cargo', models.CharField(max_length=200)),
                ('formacaoacademica', models.CharField(max_length=200)),
                ('nivelacademico', models.CharField(max_length=200)),
                ('nuit', models.IntegerField()),
                ('estadocivil', models.CharField(max_length=200)),
                ('localnasc', models.CharField(max_length=200)),
                ('telefone', models.IntegerField()),
                ('telefone1', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('observacao', models.CharField(max_length=200)),
                ('estadodelete', models.BooleanField()),
            ],
        ),
    ]