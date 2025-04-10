# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _
from datetime import date, datetime

class medical_icu_ventilation(models.Model):
    _name = 'medical.icu.ventilation'
    _description = 'Ventilación en UCI'
    _rec_name = 'ventilation'

    current_mv = fields.Boolean(string="Actual", required=True, default=True)
    mv_start = fields.Datetime(string="Desde", required=True)
    mv_end = fields.Datetime(string="Hasta", required=True)
    mv_period = fields.Char(string="Duración", size=128, required=True)
    ventilation = fields.Selection([
        ('none', 'Ninguna - Ventilación espontánea'),
        ('nppv', 'Presión positiva no invasiva (NPPV)'),
        ('ett', 'Tubo endotraqueal (ETT)'),
        ('tracheostomy', 'Traqueostomía')
    ], string="Tipo de ventilación")
    remarks = fields.Char(string="Observaciones")
