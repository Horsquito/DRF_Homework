# Generated by Django 2.1.2 on 2019-04-08 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DRF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('OP', 'Open'), ('I_P', 'In process'), ('I_T', 'In test'), ('DO', 'Done')], default='OP', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='performer',
            name='task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='DRF.Task'),
        ),
    ]
