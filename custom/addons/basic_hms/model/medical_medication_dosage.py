# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _

class medical_medication_dosage(models.Model):
    _name = 'medical.medication.dosage'
    _description = 'dosificación de medicación médica'

    name = fields.Char(string="Frecuencia", required=True)
    abbreviation = fields.Char(string="Abreviatura")
    code = fields.Char(string="Código")
