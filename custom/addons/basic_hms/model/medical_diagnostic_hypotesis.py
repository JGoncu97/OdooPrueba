# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _

class medical_diagnostic_hypotesis(models.Model):
    _name = 'medical.diagnostic_hypotesis'
    _description = 'Hipótesis Diagnóstica Médica'
    _rec_name = 'diagnostic_pathology_id'

    diagnostic_pathology_id = fields.Many2one('medical.pathology', string='Procedimiento')
    patient_evaluation_id = fields.Many2one('medical.patient.evaluation', string='Evaluación del Paciente')
    comments = fields.Char(string='Comentarios')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
