# Generated by Django 4.2.4 on 2024-02-19 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_taskgroup_task_taskgroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['due_date']},
        ),
        migrations.AlterField(
            model_name='task',
            name='taskgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.taskgroup'),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('name', 'due_date')},
        ),
    ]
