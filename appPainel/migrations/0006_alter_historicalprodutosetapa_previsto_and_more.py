# Generated by Django 4.2.4 on 2024-09-19 14:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPainel', '0005_alter_historicalprodutosmeta_previsto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprodutosetapa',
            name='previsto',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')], verbose_name='Previsto'),
        ),
        migrations.AlterField(
            model_name='historicalprodutosetapa',
            name='realizado',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')], verbose_name='Realizado'),
        ),
        migrations.AlterField(
            model_name='produtosetapa',
            name='previsto',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')], verbose_name='Previsto'),
        ),
        migrations.AlterField(
            model_name='produtosetapa',
            name='realizado',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')], verbose_name='Realizado'),
        ),
    ]
