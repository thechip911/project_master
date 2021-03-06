# Generated by Django 3.2.5 on 2021-07-27 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Project Name')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Project is Archived or Not')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Project Create time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Project Update Time')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_creator', to=settings.AUTH_USER_MODEL)),
                ('project_admin', models.ManyToManyField(related_name='project_admin', to=settings.AUTH_USER_MODEL)),
                ('team', models.ManyToManyField(blank=True, related_name='project_team', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Project',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Task Name')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Task Due Date')),
                ('task_status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('to_be_reviewed', 'To Be Reviewed'), ('tested', 'Tested'), ('pending', 'Pending'), ('done', 'Done')], default='NEW', max_length=50)),
                ('task_priority', models.CharField(choices=[('normal', 'Normal'), ('lowest', 'Lowest'), ('low', 'Low'), ('high', 'High'), ('highest', 'Highest')], default='NORMAL', max_length=50)),
                ('is_archived', models.BooleanField(default=False, verbose_name='Task is Archived or Not')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Task Create Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Task Update Date')),
                ('assigned_to', models.ManyToManyField(related_name='task', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_creator', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='projects.project')),
            ],
            options={
                'verbose_name_plural': 'Task',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Task Start Time')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Task End Date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Task Create Date')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_sheet', to='projects.task')),
            ],
            options={
                'verbose_name_plural': 'Task Time Sheet',
                'ordering': ('-id',),
            },
        ),
    ]
