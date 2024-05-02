# Generated by Django 5.0.4 on 2024-05-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('contact_details', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('vendor_code', models.CharField(db_index=True, max_length=255, unique=True)),
                ('on_time_delivery_rate', models.FloatField(db_index=True)),
                ('quality_rating_avg', models.FloatField(db_index=True)),
                ('average_response_time', models.FloatField(db_index=True)),
                ('fulfillment_rate', models.FloatField(db_index=True)),
            ],
            options={
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
    ]