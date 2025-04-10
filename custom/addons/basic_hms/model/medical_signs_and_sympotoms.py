# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_signs_and_sympotoms(models.Model):
    _name = 'medical.signs.and.sympotoms'
    _description = 'medical signs and sympotoms'
    _rec_name = 'pathology_id'

    patient_evaluation_id = fields.Many2one('medical.patient.evaluation', string="Evaluación del paciente")
    pathology_id = fields.Many2one('medical.pathology',string="Hallazgo clínico")
    sign_or_symptom = fields.Selection([
            ('sign', 'Signo'),
            ('symptom', 'Síntoma'),
        ], string="Tipo de hallazgo")
    comments = fields.Char(string="Comentarios")