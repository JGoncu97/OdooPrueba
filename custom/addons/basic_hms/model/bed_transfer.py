# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _
from datetime import date

class bed_transfer(models.Model):
    _name = 'bed.transfer'
    _description = "Transferencia de Cama"

    name = fields.Char(string="Nombre")
    date = fields.Datetime(string='Fecha')
    bed_from = fields.Char(string='Desde la cama')
    bed_to = fields.Char(string='Hacia la cama')
    reason = fields.Text(string='Motivo de la Transferencia')
    inpatient_id = fields.Many2one('medical.inpatient.registration', string='ID de Internación')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
