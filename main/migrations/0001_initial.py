# Generated by Django 3.0.3 on 2021-02-27 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='DATE', max_length=128)),
                ('name', models.CharField(default='unnamed', max_length=1024)),
                ('so_sc_24', models.CharField(default='so/sc 24h', max_length=512)),
                ('so_sc_mtd', models.CharField(default='so/sc mtd', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='EnvReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='DATE', max_length=128)),
                ('name', models.CharField(default='unnamed', max_length=1024)),
                ('so_sc_24', models.CharField(default='so/sc 24h', max_length=512)),
                ('so_sc_mtd', models.CharField(default='so/sc mtd', max_length=512)),
                ('incident_24', models.CharField(default='unidentified', max_length=64)),
                ('incident_mtd', models.CharField(default='unidentified', max_length=64)),
                ('incident_ytd', models.CharField(default='unidentified', max_length=64)),
                ('solid_waste', models.CharField(default='unidentified', max_length=64)),
                ('domestic_water_quality', models.CharField(default='unidentified', max_length=64)),
                ('waste_water_quality_cpf', models.CharField(default='unidentified', max_length=64)),
                ('waste_water_quality_iacp', models.CharField(default='unidentified', max_length=64)),
                ('waste_water_quality_sarpi', models.CharField(default='unidentified', max_length=64)),
                ('waste_water_quality_military', models.CharField(default='unidentified', max_length=64)),
                ('swimming_pool', models.CharField(default='unidentified', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='IntervReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='DATE', max_length=128)),
                ('so_sc_24', models.CharField(default='so/sc 24h', max_length=512)),
                ('so_sc_mtd', models.CharField(default='so/sc mtd', max_length=512)),
                ('etat_rescue', models.CharField(default='unidentified', max_length=64)),
                ('etat_fire_fighting', models.CharField(default='unidentified', max_length=64)),
                ('etat_vma45', models.CharField(default='unidentified', max_length=64)),
                ('etat_silvani', models.CharField(default='unidentified', max_length=64)),
                ('etat_landrover', models.CharField(default='unidentified', max_length=64)),
                ('etat_others', models.CharField(default='unidentified', max_length=64)),
                ('pers_cmt', models.CharField(default='unidentified', max_length=64)),
                ('pers_ce', models.CharField(default='unidentified', max_length=64)),
                ('pers_tech', models.CharField(default='unidentified', max_length=64)),
                ('pers_cond', models.CharField(default='unidentified', max_length=64)),
                ('pers_agt', models.CharField(default='unidentified', max_length=64)),
                ('pers_total', models.CharField(default='unidentified', max_length=64)),
                ('inspec_cpf', models.CharField(default='unidentified', max_length=64)),
                ('inspec_bdv', models.CharField(default='unidentified', max_length=64)),
                ('inspec_cc', models.CharField(default='unidentified', max_length=64)),
                ('inspec_iacp', models.CharField(default='unidentified', max_length=64)),
                ('inspec_airstrip', models.CharField(default='unidentified', max_length=64)),
                ('perm_jour', models.CharField(default='unidentified', max_length=64)),
                ('perm_nuit', models.CharField(default='unidentified', max_length=64)),
                ('alarms', models.CharField(default='unidentified', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MedicReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='DATE', max_length=128)),
                ('so_sc_24', models.CharField(default='so/sc 24h', max_length=512)),
                ('so_sc_mtd', models.CharField(default='so/sc mtd', max_length=512)),
                ('incident', models.CharField(default='unidentified', max_length=512)),
                ('doc', models.CharField(default='unidentified', max_length=512)),
                ('cpf', models.CharField(default='unidentified', max_length=512)),
                ('bdv_jour', models.CharField(default='unidentified', max_length=512)),
                ('bdv_nuit', models.CharField(default='unidentified', max_length=512)),
                ('iacp_jour', models.CharField(default='unidentified', max_length=512)),
                ('iacp_nuit', models.CharField(default='unidentified', max_length=512)),
                ('toyota', models.CharField(default='unidentified', max_length=512)),
                ('renault', models.CharField(default='unidentified', max_length=512)),
                ('mercedes', models.CharField(default='unidentified', max_length=512)),
                ('mercedes4x4', models.CharField(default='unidentified', max_length=512)),
                ('equip_hors_serv', models.CharField(default='unidentified', max_length=512)),
                ('cons_jv', models.CharField(default='unidentified', max_length=512)),
                ('cons_extra', models.CharField(default='unidentified', max_length=512)),
                ('embauche_jv', models.CharField(default='unidentified', max_length=512)),
                ('embauche_extra', models.CharField(default='unidentified', max_length=512)),
                ('periodique', models.CharField(default='unidentified', max_length=512)),
                ('soins_genereux', models.CharField(default='unidentified', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='PrevReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='DATE', max_length=128)),
                ('name', models.CharField(default='unnamed', max_length=1024)),
                ('so_sc_24_prev', models.CharField(default='so/sc 24h', max_length=512)),
                ('so_sc_24_jv', models.CharField(default='so/sc 24h', max_length=512)),
                ('so_sc_mtd_prev', models.CharField(default='so/sc mtd', max_length=512)),
                ('so_sc_mtd_jv', models.CharField(default='so/sc mtd', max_length=512)),
                ('incident_24', models.CharField(default='unidentified', max_length=512)),
                ('incident_mtd_rec', models.CharField(default='unidentified', max_length=512)),
                ('incident_mtd_all', models.CharField(default='unidentified', max_length=512)),
                ('incident_ytd_rec', models.CharField(default='unidentified', max_length=512)),
                ('incident_ytd_all', models.CharField(default='unidentified', max_length=512)),
                ('manpower_cds', models.CharField(default='unidentified', max_length=512)),
                ('manpower_eng', models.CharField(default='unidentified', max_length=512)),
                ('manpower_insp', models.CharField(default='unidentified', max_length=512)),
                ('manpower_tech', models.CharField(default='unidentified', max_length=512)),
                ('inspection_audit_prev', models.CharField(default='unidentified', max_length=512)),
                ('inspection_audit_jv', models.CharField(default='unidentified', max_length=512)),
                ('num_ptw_cpf', models.CharField(default='unidentified', max_length=64)),
                ('num_ptw_projdeb', models.CharField(default='unidentified', max_length=64)),
                ('num_ptw_log', models.CharField(default='unidentified', max_length=64)),
                ('num_ptw_total', models.CharField(default='unidentified', max_length=64)),
                ('gasdet_avail', models.CharField(default='unidentified', max_length=64)),
                ('gasdet_issued', models.CharField(default='unidentified', max_length=64)),
                ('gasdet_outofserv', models.CharField(default='unidentified', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PrevActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='today', max_length=128)),
                ('number', models.IntegerField(default=0)),
                ('act_type', models.CharField(default='act-type', max_length=512)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PrevReport')),
            ],
        ),
        migrations.CreateModel(
            name='MedicActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='today', max_length=128)),
                ('number', models.IntegerField(default=0)),
                ('act_type', models.CharField(default='act-type', max_length=512)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.MedicReport')),
            ],
        ),
        migrations.CreateModel(
            name='IntervActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='today', max_length=128)),
                ('number', models.IntegerField(default=0)),
                ('act_type', models.CharField(default='act-type', max_length=512)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.IntervReport')),
            ],
        ),
        migrations.CreateModel(
            name='EnvActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='today', max_length=128)),
                ('number', models.IntegerField(default=0)),
                ('act_type', models.CharField(default='act-type', max_length=512)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.EnvReport')),
            ],
        ),
        migrations.CreateModel(
            name='AdvActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='today', max_length=128)),
                ('number', models.IntegerField(default=0)),
                ('act_type', models.CharField(default='act-type', max_length=512)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.AdvReport')),
            ],
        ),
    ]