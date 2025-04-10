# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_perinatal_monitor(models.Model):
    
    _name = 'medical.perinatal.monitor'
    _description = 'Monitoreo perinatal'
    
    medical_perinatal_id = fields.Many2one('medical.perinatal.monitor',string="Control perinatal")
    date = fields.Date(string="Fecha")
    systolic = fields.Integer(string="Presión sistólica")
    diastolic = fields.Integer(string="Presión diastólica")
    mothers_heart_freq = fields.Integer(string="Frecuencia cardiaca materna")
    consentration = fields.Integer(string="Concentración")
    cervix_dilation = fields.Integer(string="Dilatación cervical")  
    fundel_height = fields.Integer(string="Altura uterina")
    fetus_presentation = fields.Selection([('n','Correcta'),
                                         ('o','Occipucio / Cefálica posterior'),
                                         ('fb','Presentación de nalgas incompleta'),
                                         ('cb','Presentación de nalgas completa'),
                                         ('tl','Transversa'),
                                         ('fu','Podálica')], string="Presentación fetal")
    f_freq = fields.Integer(string="Frecuencia cardiaca fetal")
    bleeding = fields.Boolean(string="Sangrado")
    meconium = fields.Boolean(string="Meconio")
    notes = fields.Char(string="Observaciones")


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: