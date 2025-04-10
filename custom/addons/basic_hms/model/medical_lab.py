# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _
from datetime import datetime

# Clase para el menú de laboratorio

class medical_lab(models.Model):

    _name = 'medical.lab'
    _description = 'Laboratorio médico'

    name = fields.Char(string="ID")
    test_id = fields.Many2one('medical.test_type', string='Tipo de examen', required=True)
    date_analysis = fields.Datetime(string='Fecha del análisis', default=datetime.now())
    patient_id = fields.Many2one('medical.patient', string='Paciente', required=True)
    date_requested = fields.Datetime(string='Fecha solicitada', default=datetime.now())
    medical_lab_physician_id = fields.Many2one('medical.physician', string='Patólogo')
    requestor_physician_id = fields.Many2one('medical.physician', string='Médico solicitante', required=True)
    critearea_ids = fields.One2many('medical_test.critearea', 'medical_lab_id', string='Criterios')
    results = fields.Text(string='Resultados')
    diagnosis = fields.Text(string='Diagnóstico')
    is_invoiced = fields.Boolean(string='Facturado', copy=False, default=False)

    @api.model_create_multi
    def create(self, vals_list):
        result = super(medical_lab, self).create(vals_list)
        for val in vals_list:
            val['name'] = self.env['ir.sequence'].next_by_code('ltest_seq')
            if val.get('test_id'):
                critearea_obj = self.env['medical_test.critearea']
                criterea_ids = critearea_obj.search([('test_id', '=', val['test_id'])])
                for criterio in criterea_ids:
                    critearea_obj.write({'medical_lab_id': result})
        return result
