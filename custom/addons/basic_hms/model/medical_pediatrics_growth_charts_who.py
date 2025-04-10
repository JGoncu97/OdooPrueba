# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_pediatrics_growth_charts_who(models.Model):
    _name = 'medical.pediatrics.growth.charts.who'
    _description = 'Gráficas de crecimiento pediátrico (OMS)'
    
    name = fields.Selection([
                             ('l/h-f-a','Longitud/Talla para la edad'),
                             ('w-f-a','Peso para la edad'),
                             ('bmi-f-a','IMC para la edad')],
                            string='Indicador')
    sex = fields.Selection([('m','Masculino'),('f','Femenino')],string='Sexo')
    measure = fields.Selection([('p','Percentil'),('z','Puntaje Z')],string='Medida')
    type = fields.Char(string="Tipo")
    month = fields.Integer(string="Mes")
    value = fields.Float(string='Valor')