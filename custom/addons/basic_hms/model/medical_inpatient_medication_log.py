# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _
from datetime import date, datetime

class medical_inpatient_medication_log(models.Model):
    _name = 'medical.inpatient.medication.log'
    _description = 'Registro de administración de medicamentos en hospitalización'

    admin_time = fields.Datetime(string='Fecha y hora de administración', readonly=True)
    dose = fields.Float(string='Dosis administrada')
    remarks = fields.Text(string='Observaciones')
    medical_inpatient_medication_log_id = fields.Many2one('medical.physician', string='Profesional de salud', readonly=True)
    medical_dose_unit_id = fields.Many2one('medical.dose.unit', string='Unidad de dosis')
    medical_inaptient_log_medicament_id = fields.Many2one('medical.inpatient.medication', string='Historial del medicamento')
