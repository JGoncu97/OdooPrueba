# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _

class medical_icu_chest_drainage(models.Model):
    _name = 'medical.icu.chest_drainage'
    _description = 'Drenaje Torácico en UCI'

    location = fields.Selection([
        ('rl', 'Pleura Derecha'),
        ('ll', 'Pleura Izquierda'),
        ('mediastinum', 'Mediastino')],
        string='Ubicación'
    )
    suction = fields.Boolean(string="Con Succión")
    suction_pressure = fields.Integer(string="Presión de Succión (cm H2O)")
    fluid_volumme = fields.Integer(string="Volumen del Fluido")
    fluid_aspect = fields.Selection([
        ('serous', 'Seroso'),
        ('bloody', 'Sanguinolento'),
        ('chylous', 'Quiloso'),
        ('purulent', 'Purulento')],
        string="Aspecto del Fluido"
    )
    oscillation = fields.Boolean(string='Oscilación')
    air_leak = fields.Boolean(string='Fuga de Aire')
    remarks = fields.Char(string="Observaciones")
    medical_patient_rounding_chest_drainage_id = fields.Many2one(
        'medical.patient.rounding',
        string="Ronda Médica"
    )
