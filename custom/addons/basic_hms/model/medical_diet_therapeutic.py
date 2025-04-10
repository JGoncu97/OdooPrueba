# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _

class medical_diet_therapeutic(models.Model):
    _name = 'medical.diet.therapeutic'
    _description = 'Dieta Terapéutica Médica'

    name = fields.Char(string='Tipo de Dieta', required=True)
    code = fields.Char(string='Código', required=True)
    description = fields.Text(string='Descripción', required=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
