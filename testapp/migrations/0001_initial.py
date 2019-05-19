# Generated by Django 2.2.1 on 2019-05-19 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_creator', to='testapp.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='NFCTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tag_no', models.CharField(max_length=100, unique=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag_creator', to='testapp.Employee')),
                ('whose_tag', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whose_tag', to='testapp.Employee')),
            ],
        ),
    ]
