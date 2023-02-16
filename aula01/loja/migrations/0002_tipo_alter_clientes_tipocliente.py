# Generated by Django 4.1.6 on 2023-02-09 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cliente', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tipoCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.tipo'),
        ),
    ]