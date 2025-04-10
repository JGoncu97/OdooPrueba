# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _

class medical_insurance_plan(models.Model):
    _name = 'medical.insurance.plan'
    _description = 'Plan de seguro médico'
    _rec_name = 'insurance_product_id'

    insurance_product_id = fields.Many2one(
        'product.product',
        string='Plan',
        domain="[('type', '=', 'service')]"
    )
    is_default = fields.Boolean(string='Plan predeterminado')
    company_partner_id = fields.Many2one(
        'res.partner',
        domain=[('is_insurance_company', '=', True)],
        string='Compañía aseguradora'
    )
    notes = fields.Text(string='Información adicional')
