# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_prescription_line(models.Model):
    _name = "medical.prescription.line"
    _description = 'medical prescription line'

    name = fields.Many2one('medical.prescription.order', string="Número de fórmula")
    medicament_id = fields.Many2one('medical.medicament', string="Medicamento")
    indication = fields.Char(string="Indicación")
    allow_substitution = fields.Boolean(string="Permitir sustitución")
    form = fields.Char(string="Forma farmacéutica")
    prnt = fields.Boolean(string="Imprimir")
    route = fields.Char(string="Vía de administración")    
    end_treatement = fields.Datetime(string="Finalización") 
    dose = fields.Float(string="Dosis")
    dose_unit_id = fields.Many2one('medical.dose.unit', string="Unidad de dosis")
    qty = fields.Integer(string="Multiplicador")
    medication_dosage_id = fields.Many2one('medical.medication.dosage', string="Posología")
    admin_times = fields.Char(size=128, string="Horarios de toma")
    frequency = fields.Integer(string="Intervalo")
    frequency_unit = fields.Selection([('seconds','Segundos'),('minutes','Minutos'),('hours','Horas'),('days','Días'),('weeks','Semanas'),('wr','Cuando se requiera')], string="Unidad de intervalo")
    duration = fields.Integer(string="Duración")
    duration_period = fields.Selection([('minutes','Minutos'),('hours','Horas'),('days','Días'),('months','Meses'),('years','Años'),('indefine','Indefinido')], string="Periodo")
    quantity = fields.Integer(string="Unidades a entregar")
    review = fields.Datetime(string="Control")
    refills = fields.Integer(string="Reposiciones")
    short_comment = fields.Char(size=128, string="Nota adicional")
    end_treatment = fields.Datetime(string="Fecha fin")
    start_treatment = fields.Datetime(string="Fecha inicio")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: