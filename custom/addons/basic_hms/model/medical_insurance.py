# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _

class medical_insurance(models.Model):
    _name = 'medical.insurance'
    _description = 'Seguro médico'
    _rec_name = 'insurance_compnay_id'

    number = fields.Char(string='Número')
    medical_insurance_partner_id = fields.Many2one('res.partner', string='Titular', required=True)
    patient_id = fields.Many2one('res.partner', string='Paciente')
    type = fields.Selection([
        ('state', 'Público'),
        ('private', 'Privado'),
        ('labour_union', 'Sindicato / Gremio')
    ], string='Tipo de seguro')
    member_since = fields.Date(string='Miembro desde')
    insurance_compnay_id = fields.Many2one(
        'res.partner',
        domain=[('is_insurance_company', '=', True)],
        string='Compañía aseguradora'
    )
    category = fields.Char(string='Categoría')
    notes = fields.Text(string='Información adicional')
    member_exp = fields.Date(string='Fecha de expiración')
    medical_insurance_plan_id = fields.Many2one('medical.insurance.plan', string='Plan de seguro')
