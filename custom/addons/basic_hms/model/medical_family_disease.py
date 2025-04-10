# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _

class medical_family_disease(models.Model):
    _name = 'medical.family.disease'
    _description = 'Antecedente Familiar de Enfermedad'
    _rec_name = 'medical_pathology_id'

    medical_pathology_id = fields.Many2one(
        'medical.pathology',
        string='Enfermedad',
        required=True
    )
    relative = fields.Selection([
        ('m', 'Madre'),
        ('f', 'Padre'),
        ('b', 'Hermano'),
        ('s', 'Hermana'),
        ('a', 'Tía'),
        ('u', 'Tío'),
        ('ne', 'Sobrino'),
        ('ni', 'Sobrina'),
        ('gf', 'Abuelo'),
        ('gm', 'Abuela')],
        string="Pariente"
    )
    metrnal = fields.Selection([
        ('m', 'Materno'),
        ('p', 'Paterno')],
        string="Línea Familiar"
    )
