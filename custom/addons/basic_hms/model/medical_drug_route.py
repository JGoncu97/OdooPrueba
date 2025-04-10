# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _

class medical_drug_route(models.Model):
    _name = 'medical.drug.route'
    _description = 'Vía de Administración del Medicamento'

    name = fields.Char(string="Vía", required=True)
    code = fields.Char(string="Código")
