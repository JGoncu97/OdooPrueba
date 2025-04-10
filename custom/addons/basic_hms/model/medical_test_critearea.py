# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
# clases bajo el menú de configuración de laboratorio

class medical_test_critearea(models.Model):
    _name  = 'medical_test.critearea'
    _description = 'medical test critearea'

    test_id = fields.Many2one('medical.test_type', string='Examen médico')
    name = fields.Char(string="Nombre")
    seq = fields.Integer(string="Secuencia")
    medical_test_type_id = fields.Many2one('medical.test_type', string='Tipo de examen', inverse_name='critearea_ids')
    medical_lab_id = fields.Many2one('medical.lab', string='Resultado del laboratorio')
    warning = fields.Boolean(string="Alerta")
    excluded = fields.Boolean(string="Excluido")
    lower_limit = fields.Float(string="Valor mínimo")
    upper_limit = fields.Float(string="Valor máximo")
    lab_test_unit_id = fields.Many2one('medical.lab.test.units', string="Unidades")
    result = fields.Float(string="Resultado")
    result_text = fields.Char(string="Resultado en texto")
    normal_range = fields.Char(string="Rango normal")
    remark = fields.Text(string="Observaciones")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: