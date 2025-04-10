# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _
from datetime import date, datetime

class medical_icu_glasgow(models.Model):
    _name = 'medical.icu.glasgow'
    _description = 'Escala de Glasgow en UCI'
    _rec_name = 'medical_inpatient_registration_id'

    medical_inpatient_registration_id = fields.Many2one(
        'medical.inpatient.registration',
        string="Código de Registro",
        required=True
    )
    evaluation_date = fields.Datetime(string="Fecha de Evaluación", required=True)
    glasgow_eyes = fields.Selection([
        ('1', '1 : No abre los ojos'),
        ('2', '2 : Abre los ojos ante estímulo doloroso'),
        ('3', '3 : Abre los ojos ante estímulo verbal'),
        ('4', '4 : Abre los ojos espontáneamente')],
        string="Respuesta Ocular"
    )
    glasgow_verbal = fields.Selection([
        ('1', '1 : No emite sonidos'),
        ('2', '2 : Sonidos incomprensibles'),
        ('3', '3 : Palabras inapropiadas'),
        ('4', '4 : Confuso o desorientado'),
        ('5', '5 : Orientado, conversa normalmente')],
        string="Respuesta Verbal"
    )
    glasgow_motor = fields.Selection([
        ('1', '1 : No realiza movimientos'),
        ('2', '2 : Extensión ante estímulo doloroso (respuesta descerebrada)'),
        ('3', '3 : Flexión anormal ante estímulo doloroso (respuesta de decorticación)'),
        ('4', '4 : Retira ante estímulo doloroso'),
        ('5', '5 : Localiza el estímulo doloroso'),
        ('6', '6 : Obedece órdenes')],
        string="Respuesta Motora"
    )
    glasgow = fields.Integer(string="Puntaje Glasgow", compute='get_glas_score')

    @api.depends('glasgow_motor', 'glasgow_verbal', 'glasgow_eyes')
    def get_glas_score(self):
        """Calcula subtotales"""
        count = int(self.glasgow_eyes) + int(self.glasgow_motor) + int(self.glasgow_verbal)
        self.glasgow = count

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
