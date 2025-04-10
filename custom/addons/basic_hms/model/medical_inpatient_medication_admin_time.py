# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _
from datetime import date, datetime

class medical_inpatient_medication_admin_time(models.Model):
    _name = 'medical.inpatient.medication.admin.time'
    _description = 'Horario de administración de medicamentos en hospitalización'

    admin_time = fields.Datetime(string='Fecha y hora de administración')
    dose = fields.Float(string='Dosis programada')
    remarks = fields.Text(string='Observaciones')
    medical_inpatient_admin_time_id = fields.Many2one('medical.physician', string='Profesional de salud')
    dose_unit = fields.Many2one('medical.dose.unit', string='Unidad de dosis')
    medical_inpatient_admin_time_medicament_id = fields.Many2one('medical.inpatient.medication', string='Medicamento asignado')
