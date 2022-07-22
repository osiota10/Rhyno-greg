# Generated by Django 4.0.5 on 2022-07-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0004_ourproject_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaHandle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('font_awesome_class', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('font_awesome_class', models.CharField(max_length=30)),
                ('stat_figure', models.IntegerField()),
                ('stat_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='ourproject',
            name='project_status',
        ),
        migrations.AlterField(
            model_name='ourproject',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('In Development', 'In Development')], max_length=20),
        ),
    ]
