# Generated by Django 3.2 on 2021-08-18 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='note',
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.CharField(default=1234, max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=250, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=250, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=250, verbose_name='message'),
        ),
    ]