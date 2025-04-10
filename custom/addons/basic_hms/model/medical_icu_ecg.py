# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _
from datetime import date, datetime

class medical_icu_ecg(models.Model):
    _name = 'medical.icu.ecg'
    _description = 'ECG en UCI'
    _rec_name = 'medical_inpatient_registration_id'

    ecg_date = fields.Datetime(string="Fecha del ECG", required=True)
    medical_inpatient_registration_id = fields.Many2one(
        'medical.inpatient.registration',
        string="Código de Registro",
        required=True
    )
    lead = fields.Selection([
        ('i', '|'),
        ('ii', '||'),
        ('iii', '|||'),
        ('avf', 'aVF'),
        ('avr', 'aVR'),
        ('avl', 'aVL'),
        ('v1', 'V1'),
        ('v2', 'V2'),
        ('v3', 'V3'),
        ('v4', 'V4'),
        ('v5', 'V5'),
        ('v6', 'V6')],
        string="Derivación"
    )
    axis = fields.Selection([
        ('normal', 'Normal'),
        ('left', 'Desviación Izquierda'),
        ('right', 'Desviación Derecha'),
        ('extreme_right', 'Desviación Extrema Derecha')],
        string="Eje Eléctrico",
        required=True
    )
    rate = fields.Integer(string="Frecuencia Cardiaca", required=True)
    pacemaker = fields.Selection([
        ('sa', 'Nódulo Sinusal'),
        ('av', 'Auriculoventricular'),
        ('pk', 'Fibras de Purkinje')],
        string="Marcapasos",
        required=True
    )
    rhythm = fields.Selection([
        ('regular', 'Regular'),
        ('irregular', 'Irregular')],
        string="Ritmo",
        required=True
    )
    pr = fields.Integer(string="Intervalo PR", required=True)
    qrs = fields.Integer(string="Complejo QRS", required=True)
    qt = fields.Integer(string="Intervalo QT", required=True)
    st_segment = fields.Selection([
        ('normal', 'Normal'),
        ('depressed', 'Descendido'),
        ('elevated', 'Elevado')],
        string="Segmento ST",
        required=True
    )
    twave_inversion = fields.Boolean(string="Inversión de Onda T")
    interpretation = fields.Char(string="Interpretación", required=True, size=256)

    def ecg_date(self, field, name):
        return name == 'sort' or super().ecg_date(field, name)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
