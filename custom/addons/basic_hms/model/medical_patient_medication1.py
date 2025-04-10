# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_medication1(models.Model):
    _name = 'medical.patient.medication1'
    _description = 'Medicación del paciente'
    _rec_name = 'medical_patient_medication_id'

    medical_medicament_id = fields.Many2one('medical.medicament', string='Medicamento', required=True)
    medical_patient_medication_id = fields.Many2one('medical.patient', string='Paciente')
    is_active = fields.Boolean(string='Activo', default=True)
    start_treatment = fields.Datetime(string='Inicio del tratamiento', required=True)
    course_completed = fields.Boolean(string="Tratamiento completado")
    doctor_physician_id = fields.Many2one('medical.physician', string='Médico')
    indication_pathology_id = fields.Many2one('medical.pathology', string='Indicación')
    end_treatment = fields.Datetime(string='Fin del tratamiento', required=True)
    discontinued = fields.Boolean(string='Discontinuado')
    drug_route_id = fields.Many2one('medical.drug.route', string="Vía de administración")
    dose = fields.Float(string='Dosis')
    qty = fields.Integer(string='X')
    dose_unit_id = fields.Many2one('medical.dose.unit', string='Unidad de dosis')
    duration = fields.Integer(string="Duración del tratamiento")
    duration_period = fields.Selection([('minutes','Minutos'),
                                        ('hours','Horas'),
                                        ('days','Días'),
                                        ('months','Meses'),
                                        ('years','Años'),
                                        ('indefine','Indefinido')], string='Periodo de tratamiento')
    medication_dosage_id = fields.Many2one('medical.medication.dosage', string='Frecuencia')
    admin_times = fields.Char(string='Horas de administración')
    frequency = fields.Integer(string='Frecuencia')
    frequency_unit = fields.Selection([('seconds','Segundos'),
                                       ('minutes','Minutos'),
                                       ('hours','Horas'),
                                       ('days','Días'),
                                       ('weeks','Semanas'),
                                       ('wr','Cuando se requiera')], string='Unidad')
    notes = fields.Text(string='Notas')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: