# Generated by Django 2.1.2 on 2018-10-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListeElecteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120, null=True)),
                ('prenom', models.CharField(max_length=120, null=True)),
                ('numero_electeur', models.CharField(max_length=120, null=True)),
                ('numero_identite', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonElecteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120, null=True)),
                ('prenom', models.CharField(max_length=120, null=True)),
                ('numero_electeur', models.CharField(max_length=120, null=True)),
                ('numero_identite', models.CharField(max_length=120, null=True)),
                ('region', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
