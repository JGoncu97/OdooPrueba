# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _
# Clases bajo el menú de configuración del laboratorio

class medical_lab_test_units(models.Model):

    _name = 'medical.lab.test.units'
    _description = 'Unidades de prueba de laboratorio médico'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código')
