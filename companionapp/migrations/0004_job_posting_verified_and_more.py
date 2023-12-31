# Generated by Django 4.2.2 on 2023-11-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companionapp', '0003_job_posting_companyid'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_posting',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='Is Verified'),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='company_profile',
            field=models.TextField(blank=True, default='Nil', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='department',
            field=models.CharField(blank=True, default='Nil', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='employment_type',
            field=models.CharField(blank=True, default='Nil', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='industry',
            field=models.CharField(blank=True, default='Nil', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='job_benefits',
            field=models.TextField(blank=True, default='Nil', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='job_description',
            field=models.TextField(blank=True, default='Nil', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='job_function',
            field=models.CharField(blank=True, default='Nil', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='job_requirements',
            field=models.TextField(blank=True, default='Nil', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='job_title',
            field=models.CharField(blank=True, default='Nil', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='location_job',
            field=models.CharField(blank=True, default='Nil', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='required_education',
            field=models.CharField(blank=True, default='Nil', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='required_experience',
            field=models.CharField(blank=True, default='Nil', max_length=255, null=True),
        ),
    ]
