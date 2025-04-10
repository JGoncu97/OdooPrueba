# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import models, fields, api, _
from datetime import date, datetime

class medical_inpatient_registration(models.Model):
    _name = 'medical.inpatient.registration'
    _description = 'Registro de hospitalización'

    name = fields.Char(string="Código de registro", copy=False, readonly=True, index=True)
    patient_id = fields.Many2one('medical.patient', string="Paciente", required=True)
    hospitalization_date = fields.Datetime(string="Fecha de hospitalización", required=True)
    discharge_date = fields.Datetime(string="Fecha estimada de alta", required=True)
    attending_physician_id = fields.Many2one('medical.physician', string="Médico tratante")
    operating_physician_id = fields.Many2one('medical.physician', string="Médico cirujano")
    admission_type = fields.Selection([
        ('routine', 'Rutina'),
        ('maternity', 'Maternidad'),
        ('elective', 'Electiva'),
        ('urgent', 'Urgente'),
        ('emergency', 'Emergencia')
    ], required=True, string="Tipo de admisión")
    medical_pathology_id = fields.Many2one('medical.pathology', string="Motivo de ingreso")
    info = fields.Text(string="Información adicional")
    bed_transfers_ids = fields.One2many('bed.transfer', 'inpatient_id', string='Transferencias de cama')
    medical_diet_belief_id = fields.Many2one('medical.diet.belief', string='Preferencia alimentaria')
    therapeutic_diets_ids = fields.One2many('medical.inpatient.diet', 'medical_inpatient_registration_id', string='Dietas terapéuticas')
    diet_vegetarian = fields.Selection([
        ('none', 'Ninguna'),
        ('vegetarian', 'Vegetariana'),
        ('lacto', 'Lacto vegetariana'),
        ('lactoovo', 'Lacto-ovo vegetariana'),
        ('pescetarian', 'Pescetariana'),
        ('vegan', 'Vegana')
    ], string="Tipo de dieta")
    nutrition_notes = fields.Text(string="Notas/direcciones nutricionales")
    state = fields.Selection([
        ('free', 'Libre'),
        ('confirmed', 'Confirmado'),
        ('hospitalized', 'Hospitalizado'),
        ('cancel', 'Cancelado'),
        ('done', 'Finalizado')
    ], string="Estado", default="free")
    nursing_plan = fields.Text(string="Plan de enfermería")
    discharge_plan = fields.Text(string="Plan de alta")
    icu = fields.Boolean(string="UCI")
    medication_ids = fields.One2many('medical.inpatient.medication', 'medical_inpatient_registration_id', string='Medicamentos')

    @api.model
    def default_get(self, fields):
        result = super(medical_inpatient_registration, self).default_get(fields)
        patient_id = self.env['ir.sequence'].next_by_code('medical.inpatient.registration')
        if patient_id:
            if 'name' in fields:
                result.update({'name': patient_id})
        return result

    def registration_confirm(self):
        self.write({'state': 'confirmed'})

    def registration_admission(self):
        self.write({'state': 'hospitalized'})

    def registration_cancel(self):
        self.write({'state': 'cancel'})

    def patient_discharge(self):
        self.write({'state': 'done'})
