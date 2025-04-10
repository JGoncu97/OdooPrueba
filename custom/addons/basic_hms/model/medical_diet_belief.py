# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _

class medical_diet_belief(models.Model):
    _name = 'medical.diet.belief'
    _description = 'Creencias Dietéticas Médicas'

    code = fields.Char(string='Código', required=True)
    description = fields.Text(string='Descripción', required=True)
    name = fields.Char(string='Creencia')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:s
