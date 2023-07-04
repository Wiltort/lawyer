# Generated by Django 4.2.2 on 2023-06-30 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_client_service_alter_client_email_alter_service_pers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='pers',
            field=models.CharField(choices=[('n', 'Физическое лицо'), ('l', 'Юридическое лицо')], max_length=1, verbose_name='юр/физ лицо'),
        ),
    ]