# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# classes under cofigration menu of laboratry 

class medical_test_type(models.Model):

    _name  = 'medical.test_type'
    _description = 'medical test type'

    name = fields.Char( string='Nombre', required = True)
    code  =  fields.Char( string='Código', required = True)
    seq = fields.Integer(string='Secuencia', default=1)
    critearea_ids = fields.One2many('medical_test.critearea', 'medical_test_type_id', string='Criterio de evaluación')
    service_product_id = fields.Many2one('product.product', string='Servicio', required = True)
    info  = fields.Text(string='Información extra')
