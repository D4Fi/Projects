# Generated by Django 4.2.5 on 2023-09-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=2)),
                ('estoque', models.IntegerField()),
                ('img_produto', models.ImageField(upload_to='')),
            ],
        ),
    ]