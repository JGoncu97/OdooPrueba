# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date, datetime

class medical_vaccination(models.Model):
    _name = 'medical.vaccination'
    _description = 'Vacunación médica'

    vaccine_product_id = fields.Many2one('product.product', string='Nombre de la vacuna', required=True)
    institution_partner_id = fields.Many2one('res.partner', domain=[('is_institution','=',True)], string='Entidad de salud', required=True)
    next_dose_date = fields.Datetime(string='Fecha de próxima dosis')
    vaccine_expiration_date = fields.Datetime(string='Fecha de vencimiento', required=True)
    observations = fields.Char(string='Anotaciones')
    dose = fields.Integer(string='Número de dosis aplicada', required=True)
    date = fields.Datetime(string='Fecha de aplicación', required=True)
    vaccine_lot = fields.Char(string='Número de lote de la vacuna')
    medical_patient_vaccines_id = fields.Many2one('medical.patient', string='Paciente')