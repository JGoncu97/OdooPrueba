# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _
from datetime import date, datetime

class medical_neomatal_apgar(models.Model):
    _name = 'medical.neomatal.apgar'
    _description = 'evaluación Apgar neonatal'
    _rec_name = 'apgar_appearance'

    apgar_activity = fields.Selection([
        ('0', 'Ninguna'),
        ('1', 'Algo de flexión'),
        ('2', 'Extremidades flexionadas')
    ], string='Actividad')

    apgar_appearance = fields.Selection([
        ('0', 'Cianosis central'),
        ('1', 'Acrocianosis'),
        ('2', 'Sin cianosis')
    ], string='Apariencia')

    apgar_grimace = fields.Selection([
        ('0', 'Sin respuesta al estímulo'),
        ('1', 'Mueca al ser estimulado'),
        ('2', 'Llora o se retira al ser estimulado')
    ], string='Respuesta refleja')

    apgar_minute = fields.Integer(string='Minuto', required=True)

    apgar_respiration = fields.Selection([
        ('0', 'Ausente'),
        ('1', 'Débil / Irregular'),
        ('2', 'Fuerte')
    ], string='Respiración')

    apgar_pulse = fields.Selection([
        ('0', 'Ausente'),
        ('1', '< 100'),
        ('2', '> 100')
    ], string='Pulso')

    apgar_scores = fields.Integer(string='Puntaje Apgar')

    @api.onchange('apgar_activity', 'apgar_appearance', 'apgar_grimace', 'apgar_minute', 'apgar_respiration', 'apgar_pulse')
    def on_change_selection(self):
        self.apgar_scores = (
            int(self.apgar_activity)
            + int(self.apgar_appearance)
            + int(self.apgar_grimace)
            + int(self.apgar_minute)
            + int(self.apgar_respiration)
            + int(self.apgar_pulse)
        )
