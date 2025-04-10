# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_mammography_history(models.Model):

    _name = 'medical.patient.mammography.history'
    _description = 'Historial de mamografías del paciente'
    
    patient_id = fields.Many2one('medical.patient', string='Paciente')
    evolution_id = fields.Many2one('medical.patient.evaluation', string='Evaluación')
    evolution_date = fields.Date(string='Fecha')
    last_mamography_date = fields.Date(string='Fecha de la última mamografía')
    result = fields.Selection([('normal','Normal'),
                              ('abnormal','Anormal')],
                             string='Resultado')
    remark = fields.Char(string='Comentarios')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: