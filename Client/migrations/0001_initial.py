# Generated by Django 4.0.7 on 2024-04-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_id', models.CharField(max_length=15, null=True)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('product', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('manganese_Comp', models.CharField(default=None, max_length=100, null=True)),
                ('manganese_form', models.CharField(default=None, max_length=100, null=True)),
                ('manganese_size', models.CharField(default=None, max_length=100, null=True)),
                ('manganese_mass', models.CharField(default=None, max_length=100, null=True)),
                ('mang_admin_approve', models.BooleanField(default=False)),
                ('app_process', models.BooleanField(default=False)),
                ('app_admin_approve', models.BooleanField(default=False)),
                ('material_volume', models.CharField(default=None, max_length=100, null=True)),
                ('fin_porosity_value', models.BooleanField(default=False)),
                ('porsity_value', models.CharField(default=None, max_length=100, null=True)),
                ('mercury_intuduced', models.CharField(default=None, max_length=100, null=True)),
                ('prediction', models.CharField(default=None, max_length=100, null=True)),
                ('porosity_result', models.CharField(default=None, max_length=100, null=True)),
                ('porosity_fin_report', models.BooleanField(default=False)),
                ('por_rep_admin_approve', models.BooleanField(default=False)),
                ('por_rep_admin_reject', models.BooleanField(default=False)),
                ('client_payment', models.BooleanField(default=False)),
                ('amount', models.CharField(default=None, max_length=100, null=True)),
                ('dispatch', models.BooleanField(default=False)),
                ('porosity_test', models.BooleanField(default=False)),
                ('maxi', models.CharField(default=None, max_length=100, null=True)),
                ('mercury', models.CharField(default=None, max_length=100, null=True)),
                ('porosity_upload', models.BooleanField(default=False)),
                ('fintest', models.BooleanField(default=False, null=True)),
                ('res', models.CharField(default=None, max_length=100, null=True)),
                ('graph', models.FileField(null=True, upload_to='media/')),
                ('report_pdf', models.FileField(max_length=5000, null=True, upload_to='media/')),
                ('retest', models.BooleanField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('consumer_id', models.CharField(max_length=100, null=True, unique=True)),
                ('cl_admin_lg', models.BooleanField(default=False)),
            ],
        ),
    ]
