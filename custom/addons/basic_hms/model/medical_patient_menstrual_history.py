# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_menstrual_history(models.Model):

    _name = 'medical.patient.menstrual.history'
    _description = 'Historial menstrual del paciente'
    
    patient_id = fields.Many2one('medical.patient', string='Paciente')
    evolution_id = fields.Many2one('medical.patient.evaluation', string='Evaluación')
    evoultion_date = fields.Date(string='Fecha')
    lmp = fields.Integer(string='FUM', required=True)
    lmp_length = fields.Integer(string='Duración de la FUM', required=True)
    is_regular = fields.Boolean(string='Es regular')
    dysmenorrhea = fields.Boolean(string='Dismenorrea')
    frequency = fields.Selection([('amenorrhea','Amenorrea'),
                                  ('oligomenorrhea','Oligomenorrea'),
                                  ('eumenorrhea','Eumenorrea'),
                                  ('pollymenohea','Polimenorrea')], 
                                string='Frecuencia')
    volume = fields.Selection([('hopomenorrhea','Hipomenorrea'),
                               ('normal','Normal'),
                               ('menorrhagia','Menorragia')],
                             string='Volumen')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: