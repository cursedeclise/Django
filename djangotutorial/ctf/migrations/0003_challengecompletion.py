# Generated by Django 4.2.20 on 2025-04-23 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0002_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.challenge')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.participant')),
            ],
        ),
    ]
