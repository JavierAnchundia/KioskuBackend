# Generated by Django 3.1 on 2021-07-08 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tipo', models.CharField(max_length=20)),
                ('pct_dscto', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=200, null=True, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('evaluador', 'evaluador'), ('final', 'final'), ('final', 'final')], default='final', max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=2)),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mibackendapp.ciudad')),
                ('membresia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mibackendapp.membresia')),
                ('provincia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mibackendapp.provincia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ciudad',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mibackendapp.provincia'),
        ),
    ]
