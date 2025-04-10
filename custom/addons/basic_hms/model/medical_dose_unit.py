# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _

class medical_dose_unit(models.Model):
    _name = 'medical.dose.unit'
    _description = 'Unidad de Dosis Médica'

    name = fields.Char(string="Unidad", required=True)
    description = fields.Char(string="Descripción")
