# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class medical_rounding_procedure(models.Model):
    _name = 'medical.rounding_procedure'
    _description = 'medical rounding procedure'

    notes = fields.Text(string="Observaciones") 
    medical_patient_rounding_procedure_id = fields.Many2one('medical.patient.rounding',string="Procedimiento de redondeo del paciente")