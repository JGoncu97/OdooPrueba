# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime

class medical_preinatal(models.Model):
    
    _name = 'medical.preinatal'
    _description = 'Prenatal'
    
    pregnency_id = fields.Many2one('medical.patient.pregnency', string="Embarazo")
    gestational_weeks = fields.Integer(string="Semanas de gestación")
    admission_date = fields.Date(string="Fecha de ingreso")
    code = fields.Char(string="Código")
    labour_mode = fields.Selection([('n','Normal'),('i','Inducido'),('c','Cesárea')], string="Tipo de parto")
    fetus_presentation = fields.Selection([('n','Correcta'),
                                         ('o','Occipucio / Cefálica Posterior'),
                                         ('fb','Pelviana Incompleta'),
                                         ('cb','Pelviana Completa'),
                                         ('tl','Transversa'),
                                         ('fu','Podálica (pies)')], string="Presentación fetal")
    monitor_ids = fields.One2many('medical.perinatal.monitor','medical_perinatal_id',string="Monitoreo")
    dystocia = fields.Boolean(string="Distocia")
    episiotomy = fields.Boolean(string="Episiotomía")
    lacerations = fields.Selection([('p', 'Perineal'),
                                    ('v', 'Vaginal'),
                                    ('c', 'Cervical'),
                                    ('bl', 'Ligamento Ancho'),
                                    ('vl', 'Vulvar'),
                                    ('r', 'Rectal'),
                                    ('br', 'Vesical'),
                                    ('u', 'Ureteral'),  ], string="Laceraciones")
    
    
    hematoma = fields.Selection([('v','Vaginal'), ('vl','Vulvar'),('r','Retroperitoneal')], string="Hematoma")
    plancenta_incomplete = fields.Boolean(string="Placenta incompleta")
    retained_placenta = fields.Boolean(string="Retención placentaria")
    abruptio_placentae = fields.Boolean(string="Desprendimiento prematuro de placenta")
    
       
    notes = fields.Text(string="Observaciones")


# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: