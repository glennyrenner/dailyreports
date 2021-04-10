from django.shortcuts import render
from django.http.response import JsonResponse
from main.models import *
import datetime
import json


def home(request):
    return render(request, 'main/home.html')


def cdd(request):
    if request.method == "POST":
        try:
            # get the date and bring the data and send again
            date = request.POST.get('date')
            prev_r = PrevReport.objects.filter(date=date).first()
            if not prev_r:
                prev_r = PrevReport()

            interv_r = IntervReport.objects.filter(date=date).first()
            if not interv_r:
                interv_r = IntervReport()

            env_r = EnvReport.objects.filter(date=date).first()
            if not env_r:
                env_r = EnvReport()

            medic_r = MedicReport.objects.filter(date=date).first()
            if not medic_r:
                medic_r = MedicReport()

            adv_r = AdvReport.objects.filter(date=date).first()
            if not adv_r:
                adv_r = AdvReport()

            prev_a = PrevActivity.objects.filter(report=prev_r)
            interv_a = IntervActivity.objects.filter(report=interv_r)
            env_a = EnvActivity.objects.filter(report=env_r)
            medic_a = MedicActivity.objects.filter(report=medic_r)
            adv_a = AdvActivity.objects.filter(report=adv_r)


            # not stored as zeros make then zeros in case needed
            try:
                if prev_r.so_sc_24_prev:
                    prev_rso_sc_24_prev = int(prev_r.so_sc_24_prev)
                else : 
                    prev_rso_sc_24_prev = 0

                if interv_r.so_sc_24:
                    interv_rso_sc_24 = int(interv_r.so_sc_24)
                else : 
                    interv_r.so_sc_24 = 0

                if env_r.so_sc_24:
                    env_rso_sc_24 = int(env_r.so_sc_24)
                else : 
                    env_rso_sc_24 = 0

                if medic_r.so_sc_24:
                    medic_rso_sc_24 = int(medic_r.so_sc_24)
                else : 
                    medic_rso_sc_24 = 0

                if prev_r.so_sc_24_jv:
                    prev_rso_sc_24_jv = int(prev_r.so_sc_24_jv)
                else : 
                    prev_rso_sc_24_jv = 0
                

                total_24 = prev_rso_sc_24_prev + interv_rso_sc_24 + \
                    env_rso_sc_24 + medic_rso_sc_24 + \
                    prev_rso_sc_24_jv
                

                if prev_r.so_sc_mtd_prev:
                    prev_rso_sc_mtd_prev = int(prev_r.so_sc_mtd_prev)
                else : 
                    prev_rso_sc_mtd_prev = 0

                if interv_r.so_sc_mtd:
                    interv_rso_sc_mtd = int(interv_r.so_sc_mtd)
                else : 
                    interv_rso_sc_mtd = 0

                if env_r.so_sc_mtd:
                    env_rso_sc_mtd = int(env_r.so_sc_mtd)
                else : 
                    env_rso_sc_mtd = 0

                if medic_r.so_sc_mtd:
                    medic_rso_sc_mtd = int(medic_r.so_sc_mtd)
                else : 
                    medic_rso_sc_mtd = 0

                if prev_r.so_sc_mtd_jv:
                    prev_rso_sc_mtd_jv = int(prev_r.so_sc_mtd_jv)
                else : 
                    prev_rso_sc_mtd_jv = 0

                total_mtd = prev_rso_sc_mtd_prev + interv_rso_sc_mtd \
                    + env_rso_sc_mtd + medic_rso_sc_mtd + prev_rso_sc_mtd_jv

            except Exception as e:
                total_mtd = "Invalid inputs!"
                total_24 = "Invalid inputs!"

            context = {
                'date': date,
                'prev_r': prev_r,
                'interv_r': interv_r,
                'env_r': env_r,
                'medic_r': medic_r,
                'adv_r': adv_r,
                'prev_a': prev_a,
                'interv_a': interv_a,
                'env_a': env_a,
                'medic_a': medic_a,
                'adv_a': adv_a,
                'total_24': total_24,
                'total_mtd': total_mtd
            }

            print(context['env_r'].solid_waste)
            return render(request, 'main/cdd.html', context)
        except Exception as e:
            print(f'FUCKED UP EHRE : {e}')
    else:
        context = {
            'date': '...',
            'prev_r': '...',
            'interv_r': '...',
            'env_r': '...',
            'medic_r': '...',
            'adv_r': '...',
            'prev_a': '...',
            'interv_a': '...',
            'env_a': '...',
            'medic_a': '...',
            'adv_a': '...',
            'total_24': '...',
            'total_mtd': '...'
        }
        return render(request, 'main/cdd.html', context)


def medic(request):
    return render(request, 'main/medic.html')


def prev(request):
    return render(request, 'main/prev.html')


def adv(request):
    return render(request, 'main/adv.html')


def env(request):
    return render(request, 'main/env.html')


def interv(request):
    return render(request, 'main/interv.html')


def submit_adv(request):
    data = json.loads(request.GET.get('data'))
    date = data['date']
    name = data['name']
    sosc_24 = data['sosc_24h']
    sosc_mtd = data['sosc_mtd']
    activities = data['activities']

    report = AdvReport(date=date, name=name,
                       so_sc_24=sosc_24, so_sc_mtd=sosc_mtd)
    report.save()

    for r in activities:
        a = AdvActivity(report=report, name=r['name'],
                        day=r['day'], number=r['number'], act_type=r['type'])
        a.save()

    return JsonResponse({
        'state': 'good'
    })


def submit_prev(request):
    data = json.loads(request.GET.get('data'))

    date = data['date']
    name = data['name']
    so_sc_24_prev = data['so_sc_24_prev']
    so_sc_24_jv = data['so_sc_24_jv']
    so_sc_mtd_prev = data['so_sc_mtd_prev']
    so_sc_mtd_jv = data['so_sc_mtd_jv']
    incident_24 = data['incident_24']
    incident_mtd_rec = data['incident_mtd_rec']
    incident_mtd_all = data['incident_mtd_all']
    incident_ytd_rec = data['incident_ytd_rec']
    incident_ytd_all = data['incident_ytd_all']
    manpower_cds = data['manpower_cds']
    manpower_eng = data['manpower_eng']
    manpower_insp = data['manpower_insp']
    manpower_tech = data['manpower_tech']
    inspection_audit_prev = data['inspection_audit_prev']
    inspection_audit_jv = data['inspection_audit_jv']
    num_ptw_cpf = data['num_ptw_cpf']
    num_ptw_projdeb = data['num_ptw_projdeb']
    num_ptw_log = data['num_ptw_log']
    num_ptw_total = data['num_ptw_total']
    gasdet_avail = data['gasdet_avail']
    gasdet_issued = data['gasdet_issued']
    gasdet_outofserv = data['gasdet_outofserv']

    activities = data['activities']

    report = PrevReport(
        date=date,
        name=name,
        so_sc_24_prev=so_sc_24_prev,
        so_sc_24_jv=so_sc_24_jv,
        so_sc_mtd_prev=so_sc_mtd_prev,
        so_sc_mtd_jv=so_sc_mtd_jv,
        incident_24=incident_24,
        incident_mtd_rec=incident_mtd_rec,
        incident_mtd_all=incident_mtd_all,
        incident_ytd_rec=incident_ytd_rec,
        incident_ytd_all=incident_ytd_all,
        manpower_cds=manpower_cds,
        manpower_eng=manpower_eng,
        manpower_insp=manpower_insp,
        manpower_tech=manpower_tech,
        inspection_audit_prev=inspection_audit_prev,
        inspection_audit_jv=inspection_audit_jv,
        num_ptw_cpf=num_ptw_cpf,
        num_ptw_projdeb=num_ptw_projdeb,
        num_ptw_log=num_ptw_log,
        num_ptw_total=num_ptw_total,
        gasdet_avail=gasdet_avail,
        gasdet_issued=gasdet_issued,
        gasdet_outofserv=gasdet_outofserv
    )

    report.save()

    for r in activities:
        a = PrevActivity(report=report, name=r['name'],
                         day=r['day'], number=r['number'], act_type=r['type'])
        a.save()

    return JsonResponse({
        'state': 'good'
    })


def submit_medic(request):
    data = json.loads(request.GET.get('data'))

    date = data['date']
    so_sc_24 = data['so_sc_24']
    so_sc_mtd = data['so_sc_mtd']
    incident = data['incident']
    doc = data['doc']
    cpf = data['cpf']
    bdv_jour = data['bdv_jour']
    bdv_nuit = data['bdv_nuit']
    iacp_jour = data['iacp_jour']
    iacp_nuit = data['iacp_nuit']
    toyota = data['toyota']
    renault = data['renault']
    mercedes = data['mercedes']
    mercedes4x4 = data['mercedes4x4']
    equip_hors_serv = data['equip_hors_serv']
    cons_jv = data['cons_jv']
    cons_extra = data['cons_extra']
    embauche_jv = data['embauche_jv']
    embauche_extra = data['embauche_extra']
    periodique = data['periodique']
    soins_genereux = data['soins_genereux']

    activities = data['activities']

    report = MedicReport(
        date=date,
        so_sc_24=so_sc_24,
        so_sc_mtd=so_sc_mtd,
        incident=incident,
        doc=doc,
        cpf=cpf,
        bdv_jour=bdv_jour,
        bdv_nuit=bdv_nuit,
        iacp_jour=iacp_jour,
        iacp_nuit=iacp_nuit,
        toyota=toyota,
        renault=renault,
        mercedes=mercedes,
        mercedes4x4=mercedes4x4,
        equip_hors_serv=equip_hors_serv,
        cons_jv=cons_jv,
        cons_extra=cons_extra,
        embauche_jv=embauche_jv,
        embauche_extra=embauche_extra,
        periodique=periodique,
        soins_genereux=soins_genereux
    )

    report.save()

    for r in activities:
        a = MedicActivity(report=report, name=r['name'],
                          day=r['day'], number=r['number'], act_type=r['type'])
        a.save()

    return JsonResponse({
        'state': 'good'
    })


def submit_interv(request):
    data = json.loads(request.GET.get('data'))

    date = data['date']
    so_sc_24 = data['so_sc_24']
    so_sc_mtd = data['so_sc_mtd']
    etat_rescue = data['etat_rescue']
    etat_fire_fighting = data['etat_fire_fighting']
    etat_vma45 = data['etat_vma45']
    etat_silvani = data['etat_silvani']
    etat_landrover = data['etat_landrover']
    etat_others = data['etat_others']
    pers_cmt = data['pers_cmt']
    pers_ce = data['pers_ce']
    pers_tech = data['pers_tech']
    pers_cond = data['pers_cond']
    pers_agt = data['pers_agt']
    pers_total = data['pers_total']
    inspec_cpf = data['inspec_cpf']
    inspec_bdv = data['inspec_bdv']
    inspec_cc = data['inspec_cc']
    inspec_iacp = data['inspec_iacp']
    inspec_airstrip = data['inspec_airstrip']
    perm_jour = data['perm_jour']
    perm_nuit = data['perm_nuit']
    alarms = data['alarms']

    activities = data['activities']

    report = IntervReport(
        date=date,
        so_sc_24=so_sc_24,
        so_sc_mtd=so_sc_mtd,
        etat_rescue=etat_rescue,
        etat_fire_fighting=etat_fire_fighting,
        etat_vma45=etat_vma45,
        etat_silvani=etat_silvani,
        etat_landrover=etat_landrover,
        etat_others=etat_others,
        pers_cmt=pers_cmt,
        pers_ce=pers_ce,
        pers_tech=pers_tech,
        pers_cond=pers_cond,
        pers_agt=pers_agt,
        pers_total=pers_total,
        inspec_cpf=inspec_cpf,
        inspec_bdv=inspec_bdv,
        inspec_cc=inspec_cc,
        inspec_iacp=inspec_iacp,
        inspec_airstrip=inspec_airstrip,
        perm_jour=perm_jour,
        perm_nuit=perm_nuit,
        alarms=alarms
    )

    report.save()

    for r in activities:
        a = IntervActivity(report=report, name=r['name'],
                           day=r['day'], number=r['number'], act_type=r['type'])
        a.save()

    return JsonResponse({
        'state': 'good'
    })


def submit_env(request):
    data = json.loads(request.GET.get('data'))

    date = data['date']
    name = data['name']
    so_sc_24 = data['so_sc_24']
    so_sc_mtd = data['so_sc_mtd']
    incident_24 = data['incident_24']
    incident_mtd = data['incident_mtd']
    incident_ytd = data['incident_ytd']
    solid_waste = data['solid_waste']
    domestic_water_quality = data['domestic_water_quality']
    waste_water_quality_cpf = data['waste_water_quality_cpf']
    waste_water_quality_iacp = data['waste_water_quality_iacp']
    waste_water_quality_sarpi = data['waste_water_quality_sarpi']
    waste_water_quality_military = data['waste_water_quality_military']
    swimming_pool = data['swimming_pool']

    activities = data['activities']

    report = EnvReport(
        date=date,
        name=name,
        so_sc_24=so_sc_24,
        so_sc_mtd=so_sc_mtd,
        incident_24=incident_24,
        incident_mtd=incident_mtd,
        incident_ytd=incident_ytd,
        solid_waste=solid_waste,
        domestic_water_quality=domestic_water_quality,
        waste_water_quality_cpf=waste_water_quality_cpf,
        waste_water_quality_iacp=waste_water_quality_iacp,
        waste_water_quality_sarpi=waste_water_quality_sarpi,
        waste_water_quality_military=waste_water_quality_military,
        swimming_pool=swimming_pool
    )

    report.save()

    for r in activities:
        a = EnvActivity(report=report, name=r['name'],
                        day=r['day'], number=r['number'], act_type=r['type'])
        a.save()

    return JsonResponse({
        'state': 'good'
    })
