# Generated by Django 4.2.6 on 2023-10-30 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('pass_seria', models.CharField(max_length=55)),
                ('pass_num', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='house_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.house'),
        ),
        migrations.AddField(
            model_name='order',
            name='profile_id',
            field=models.ManyToManyField(to='api.profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order_status'),
        ),
        migrations.AddField(
            model_name='house_photo',
            name='house_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.house'),
        ),
    ]
