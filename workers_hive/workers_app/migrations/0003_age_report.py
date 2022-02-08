from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("workers_app", "0002_alter_worker_occupation")
    ]

    operations = [
        migrations.CreateModel(
            name='OccupationAgeAvg',
            fields=[
                ('unique_id', models.IntegerField(primary_key=True, serialize=False)),
                ('occupation', models.IntegerField()),
                ('avg_age', models.FloatField())
            ],
            options={
                'db_table': 'report',
                'managed': False,
            },
        ),
         migrations.RunSQL(
            """
            CREATE MATERIALIZED VIEW report (avg_age, occupation, unique_id) 
            AS SELECT DISTINCT ON (occupation)
            AVG(age),
            occupation,  
            occupation
            FROM workers_app_worker
            GROUP BY occupation;
            """
        )
    ]