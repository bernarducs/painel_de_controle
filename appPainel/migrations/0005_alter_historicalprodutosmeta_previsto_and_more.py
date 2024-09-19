# Generated by Django 4.2.4 on 2024-09-19 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPainel', '0004_alter_eixo_options_alter_historicaleixo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprodutosmeta',
            name='previsto',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')], verbose_name='Previsto'),
        ),
        migrations.AlterField(
            model_name='historicalprodutosmeta',
            name='realizado',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')], verbose_name='Realizado'),
        ),
        migrations.AlterField(
            model_name='produtosmeta',
            name='previsto',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')], verbose_name='Previsto'),
        ),
        migrations.AlterField(
            model_name='produtosmeta',
            name='realizado',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')], verbose_name='Realizado'),
        ),
    ]
