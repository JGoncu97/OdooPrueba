# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_cage(models.Model):
    _name = 'medical.patient.cage'
    _description = 'Evaluación CAGE del paciente'
    _rec_name = 'patient_id'

    @api.onchange('cage_c', 'cage_a', 'cage_g', 'cage_e')
    def get_score(self):
        self.cage_score = int(self.cage_c) + int(self.cage_a) + int(self.cage_g) + int(self.cage_e)
         
    patient_id = fields.Many2one('medical.patient', string='Paciente')
    evaluation_date = fields.Datetime(string='Fecha de evaluación')
    cage_c = fields.Boolean(string='C - ¿Ha sentido alguna vez que debe beber menos?', default=False)
    cage_a = fields.Boolean(string='A - ¿Le ha molestado que la gente lo critique por su forma de beber?', default=False)
    cage_g = fields.Boolean(string='G - ¿Se ha sentido mal o culpable por su forma de beber?', default=False)
    cage_e = fields.Boolean(string='E - ¿Ha necesitado beber por la mañana para calmar los nervios?', default=False)
    cage_score = fields.Integer(string='Puntaje CAGE', default=0)


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: