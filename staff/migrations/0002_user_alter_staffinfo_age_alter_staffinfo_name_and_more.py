# Generated by Django 5.0.7 on 2024-07-19 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='staffinfo',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='staffinfo',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staffinfo',
            name='sex',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
