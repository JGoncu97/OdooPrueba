# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_patient_pregnency(models.Model):
    _name = 'medical.patient.pregnency'
    _description = 'Embarazo del paciente'

    gravida = fields.Integer(string='Número de embarazo')
    lmp = fields.Integer(string='FUM (Fecha Última Menstruación)')
    pdd = fields.Date(string='Fecha probable de parto')
    patient_id = fields.Many2one('medical.patient', string='Paciente')
    current_pregnency = fields.Boolean(string='Embarazo actual')
    medical_patient_evolution_prental_ids = fields.One2many('medical.patient.prental.evoultion', 'pregnency_id', string='Evaluaciones prenatales')
    medical_perinatal_ids = fields.One2many('medical.preinatal', 'pregnency_id', string='Registros perinatales')
    puerperium_perental_ids = fields.One2many('medical.puerperium.monitor', 'pregnency_id', string='Monitoreo del puerperio')
    fetuses = fields.Boolean(string='Fetos múltiples')
    monozygotic = fields.Boolean(string='Monocigótico')
    igur = fields.Selection([('s','Simétrico'),('a','Asimétrico')], string='RCIU (Restricción de Crecimiento Intrauterino)')
    warn = fields.Boolean(string='Advertencia')
    result = fields.Char(string='Resultado')
    pregnancy_end_date = fields.Date(string='Fecha de finalización del embarazo')
    pregnancy_end_result = fields.Char(string='Resultado del parto')


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: