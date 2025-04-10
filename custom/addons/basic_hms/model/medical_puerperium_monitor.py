# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_puerperium_monitor(models.Model):
    
    _name = 'medical.puerperium.monitor'
    _description = 'Monitor del Puerperio'
    
    pregnency_id = fields.Many2one('medical.patient.pregnency',string="Embarazo")
    date = fields.Datetime(string="Fecha y hora")
    systolic_pressure = fields.Integer(string="Presión sistólica")
    diastolic_pressure = fields.Integer(string="Presión diastólica")
    heart_freq = fields.Integer(string="Frecuencia cardiaca")
    temprature = fields.Integer(string="Temperatura")
    fundal_height = fields.Integer(string="Altura uterina")
    lochia_amount = fields.Selection([('n','Normal'),('a','Abundante'),('h','Hemorragia'),], string="Cantidad de loquios")
    lochia_color = fields.Selection([('r','Roja/Rubra'),('s','Serosa'),('a','Alba/Blanca')], string="Color de loquios")
    loicha_order = fields.Selection([('n','Normal'), ('o','Fétido/Maloliente')], string="Olor de loquios")


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: