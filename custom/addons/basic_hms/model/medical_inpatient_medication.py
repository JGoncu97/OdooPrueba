# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _
from datetime import date, datetime

class medical_inpatient_medication(models.Model):
    _name = 'medical.inpatient.medication'
    _description = 'Medicamento administrado durante hospitalización'
    _rec_name = 'medical_medicament_id'

    medical_medicament_id = fields.Many2one('medical.medicament', string='Medicamento', required=True)
    is_active = fields.Boolean(string='Activo')
    start_treatment = fields.Datetime(string='Inicio del tratamiento', required=True)
    course_completed = fields.Boolean(string="Tratamiento completado")
    medical_inpatient_medication_physician_id = fields.Many2one('medical.physician', string='Médico tratante')
    medical_pathology_id = fields.Many2one('medical.pathology', string='Indicación')
    end_treatment = fields.Datetime(string='Fin del tratamiento', required=True)
    discontinued = fields.Boolean(string='Suspendido')
    medical_drug_route_id = fields.Many2one('medical.drug.route', string="Vía de administración")
    dose = fields.Float(string='Dosis')
    qty = fields.Integer(string='Cantidad (X)')
    medical_dose_unit_id = fields.Many2one('medical.dose.unit', string='Unidad de dosis')
    duration = fields.Integer(string="Duración del tratamiento")
    duration_period = fields.Selection([
        ('minutes', 'Minutos'),
        ('hours', 'Horas'),
        ('days', 'Días'),
        ('months', 'Meses'),
        ('years', 'Años'),
        ('indefine', 'Indefinido')
    ], string='Periodo de duración')
    medical_medication_dosage_id = fields.Many2one('medical.medication.dosage', string='Frecuencia')
    admin_times = fields.Char(string='Horas de administración')
    frequency = fields.Integer(string='Frecuencia')
    frequency_unit = fields.Selection([
        ('seconds', 'Segundos'),
        ('minutes', 'Minutos'),
        ('hours', 'Horas'),
        ('days', 'Días'),
        ('weeks', 'Semanas'),
        ('wr', 'Cuando se requiera')
    ], string='Unidad de frecuencia')
    adverse_reaction = fields.Text(string='Notas / Reacciones adversas')
    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration', string='Registro de hospitalización')
    inpatient_admin_times_ids = fields.One2many('medical.inpatient.medication.admin.time', 'medical_inpatient_admin_time_medicament_id', string='Administración')
    inpatient_log_history_ids = fields.One2many('medical.inpatient.medication.log', 'medical_inaptient_log_medicament_id', string='Historial de administración')
