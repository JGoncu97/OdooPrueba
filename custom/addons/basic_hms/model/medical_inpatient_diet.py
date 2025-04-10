# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _

class medical_inpatient_diet(models.Model):
    _name = 'medical.inpatient.diet'
    _description = 'Dieta en hospitalización'

    diet_id = fields.Many2one('medical.diet.therapeutic', string='Dieta terapéutica', required=True)
    remarks = fields.Text(string='Observaciones / Indicaciones')
    medical_inpatient_registration_id = fields.Many2one('medical.inpatient.registration', string='Registro de hospitalización')
