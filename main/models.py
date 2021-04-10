from django.db import models
import datetime

# Create your models here.

class MedicReport(models.Model):
    date = models.CharField(max_length=128, default="0")
    so_sc_24 = models.CharField(max_length=512, default="0")
    so_sc_mtd = models.CharField(max_length=512, default="0")
    incident = models.CharField(max_length=512, default="/")
    doc = models.CharField(max_length=512, default="/")
    cpf = models.CharField(max_length=512, default="/")
    bdv_jour = models.CharField(max_length=512, default="/")
    bdv_nuit = models.CharField(max_length=512, default="/")
    iacp_jour = models.CharField(max_length=512, default="/")
    iacp_nuit = models.CharField(max_length=512, default="/")
    toyota = models.CharField(max_length=512, default="/")
    renault = models.CharField(max_length=512, default="/")
    mercedes = models.CharField(max_length=512, default="/")
    mercedes4x4 = models.CharField(max_length=512, default="/")
    equip_hors_serv = models.CharField(max_length=512, default="/")
    cons_jv = models.CharField(max_length=512, default="/")
    cons_extra = models.CharField(max_length=512, default="/")
    embauche_jv = models.CharField(max_length=512, default="/")
    embauche_extra = models.CharField(max_length=512, default="/")
    periodique = models.CharField(max_length=512, default="/")
    soins_genereux = models.CharField(max_length=512, default="/")
    
    def __str__(self):
        return self.date

class PrevReport(models.Model):
    date = models.CharField(max_length=128, default="0")
    name = models.CharField(max_length=1024, default="unnamed")
    so_sc_24_prev = models.CharField(max_length=512, default="0")
    so_sc_24_jv = models.CharField(max_length=512, default="0")
    so_sc_mtd_prev = models.CharField(max_length=512, default="0")
    so_sc_mtd_jv = models.CharField(max_length=512, default="0")
    incident_24 = models.CharField(max_length=512, default="/")
    incident_mtd_rec = models.CharField(max_length=512, default="/")
    incident_mtd_all = models.CharField(max_length=512, default="/")
    incident_ytd_rec = models.CharField(max_length=512, default="/")
    incident_ytd_all = models.CharField(max_length=512, default="/")
    manpower_cds = models.CharField(max_length=512, default="/")
    manpower_eng = models.CharField(max_length=512, default="/")
    manpower_insp = models.CharField(max_length=512, default="/")
    manpower_tech = models.CharField(max_length=512, default="/")
    inspection_audit_prev = models.CharField(max_length=512, default="/")
    inspection_audit_jv = models.CharField(max_length=512, default="/")
    num_ptw_cpf = models.CharField(max_length=64, default="/")
    num_ptw_projdeb = models.CharField(max_length=64, default="/")
    num_ptw_log = models.CharField(max_length=64, default="/")
    num_ptw_total = models.CharField(max_length=64, default="/")
    gasdet_avail = models.CharField(max_length=64, default="/")
    gasdet_issued = models.CharField(max_length=64, default="/")
    gasdet_outofserv = models.CharField(max_length=64, default="/")
    def __str__(self):
        return self.date

class AdvReport(models.Model):
    date = models.CharField(max_length=128, default="0")
    name = models.CharField(max_length=1024, default="/")
    so_sc_24 = models.CharField(max_length=512, default="0")
    so_sc_mtd = models.CharField(max_length=512, default="0")
    def __str__(self):
        return self.date
        
class EnvReport(models.Model):
    date = models.CharField(max_length=128, default="0")
    name = models.CharField(max_length=1024, default="/")
    so_sc_24 = models.CharField(max_length=512, default="0")
    so_sc_mtd = models.CharField(max_length=512, default="0")
    incident_24 = models.CharField(max_length=64, default="/")
    incident_mtd = models.CharField(max_length=64, default="/")
    incident_ytd = models.CharField(max_length=64, default="/")
    solid_waste = models.CharField(max_length=64, default="/")
    domestic_water_quality = models.CharField(max_length=64, default="/")
    waste_water_quality_cpf = models.CharField(max_length=64, default="/")
    waste_water_quality_iacp = models.CharField(max_length=64, default="/")
    waste_water_quality_sarpi = models.CharField(max_length=64, default="/")
    waste_water_quality_military = models.CharField(max_length=64, default="/")
    swimming_pool = models.CharField(max_length=64, default="/")
    def __str__(self):
        return self.date
        
class IntervReport(models.Model):
    date = models.CharField(max_length=128, default="0")
    so_sc_24 = models.CharField(max_length=512, default="0")
    so_sc_mtd = models.CharField(max_length=512, default="0")
    etat_rescue = models.CharField(max_length=64, default="/")
    etat_fire_fighting = models.CharField(max_length=64, default="/")
    etat_vma45 = models.CharField(max_length=64, default="/")
    etat_silvani = models.CharField(max_length=64, default="/")
    etat_landrover = models.CharField(max_length=64, default="/")
    etat_others = models.CharField(max_length=64, default="/")
    pers_cmt = models.CharField(max_length=64, default="/")
    pers_ce = models.CharField(max_length=64, default="/")
    pers_tech = models.CharField(max_length=64, default="/")
    pers_cond = models.CharField(max_length=64, default="/")
    pers_agt = models.CharField(max_length=64, default="/")
    pers_total = models.CharField(max_length=64, default="/")
    inspec_cpf = models.CharField(max_length=64, default="/")
    inspec_bdv = models.CharField(max_length=64, default="/")
    inspec_cc = models.CharField(max_length=64, default="/")
    inspec_iacp = models.CharField(max_length=64, default="/")
    inspec_airstrip = models.CharField(max_length=64, default="/")
    perm_jour = models.CharField(max_length=64, default="/")
    perm_nuit = models.CharField(max_length=64, default="/")
    alarms = models.CharField(max_length=64, default="/")
    def __str__(self):
        return self.date

class MedicActivity(models.Model):
    report = models.ForeignKey(MedicReport, on_delete=models.CASCADE)
    day = models.CharField(max_length=128, default="today")
    number = models.IntegerField(default=0)
    act_type = models.CharField(max_length=512, default="act-type")
    name = models.CharField(max_length=128, default="today")

class PrevActivity(models.Model):
    report = models.ForeignKey(PrevReport, on_delete=models.CASCADE)
    day = models.CharField(max_length=128, default="today")
    number = models.IntegerField(default=0)
    act_type = models.CharField(max_length=512, default="act-type")
    name = models.CharField(max_length=128, default="today")


class AdvActivity(models.Model):
    report = models.ForeignKey(AdvReport, on_delete=models.CASCADE)
    day = models.CharField(max_length=128, default="today")
    number = models.IntegerField(default=0)
    act_type = models.CharField(max_length=512, default="act-type")
    name = models.CharField(max_length=128, default="today")


class EnvActivity(models.Model):
    report = models.ForeignKey(EnvReport, on_delete=models.CASCADE)
    day = models.CharField(max_length=128, default="today")
    number = models.IntegerField(default=0)
    act_type = models.CharField(max_length=512, default="act-type")
    name = models.CharField(max_length=128, default="today")


class IntervActivity(models.Model):
    report = models.ForeignKey(IntervReport, on_delete=models.CASCADE)
    day = models.CharField(max_length=128, default="today")
    number = models.IntegerField(default=0)
    act_type = models.CharField(max_length=512, default="act-type")
    name = models.CharField(max_length=128, default="today")




