# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
 
from odoo import api, fields, models, _
 
class medical_patient_rounding(models.Model):
    _name = "medical.patient.rounding"
    _description ='Ronda médica del paciente'
    _rec_name = 'medical_inpatient_registration'

    @api.onchange('right_pupil','left_pupil')
    def onchange_duration(self):
        if self.left_pupil == self.right_pupil:
            self.anisocoria = False
        else:
            self.anisocoria = True
      
    medical_inpatient_registration = fields.Many2one('medical.inpatient.registration', string="Código de registro", required=True)
    health_physician_id = fields.Many2one('medical.physician', string="Profesional de salud", readonly=True)
    evaluation_start = fields.Datetime(string="Inicio", required=True)
    evaluation_end = fields.Datetime(string="Fin", required=True)
    environmental_assessment = fields.Char(string='Entorno')
    icu_patient = fields.Boolean(string='UCI')
    warning = fields.Boolean(string='Advertencia')
    pain = fields.Boolean(string='Dolor')
    potty = fields.Boolean(string='Necesidades')
    position = fields.Boolean(string='Posición')
    proximity = fields.Boolean(string='Proximidad')
    pump = fields.Boolean(string='Bombas')
    personal_needs = fields.Boolean(string='Necesidades personales')
    temperature = fields.Float(string='Temperatura')
    systolic = fields.Integer(string="Presión sistólica")
    diastolic = fields.Integer(string='Presión diastólica')
    bpm = fields.Integer(string='Frecuencia cardíaca')
    respiratory_rate = fields.Integer(string="Frecuencia respiratoria")
    osat = fields.Integer(string="Saturación de oxígeno")
    diuresis = fields.Integer(string="Diuresis")
    urinary_catheter = fields.Boolean(string="Catéter urinario")
    glycemia = fields.Integer(string="Glucemia")
    depression = fields.Boolean(string="Signos de depresión")
    evolution = fields.Selection([('n','Estado actual'),
                                  ('i','Mejorando'),
                                  ('w','Empeorando')],
                                 string="Evolución")
    round_summary = fields.Text(string="Resumen de la ronda")
    gcs = fields.Many2one("medical.icu.glasgow", string="Escala de Glasgow")
    right_pupil = fields.Integer(string="Pupila derecha")
    pupillary_reactivity = fields.Selection([('brisk','Activa'),
                                             ('sluggish','Lenta'),
                                             ('nonreactive','No reactiva')],
                                            string="Reactividad pupilar")
    pupil_dilation = fields.Selection([('normal','Normal'),
                                       ('miosis','Miosis'),
                                       ('mydriasis','Midriasis')],
                                      string="Dilatación pupilar")
    left_pupil = fields.Integer(string="Pupila izquierda")
    anisocoria = fields.Boolean(string="Anisocoria")
    pupil_consensual_resp = fields.Boolean(string="Respuesta consensual")
    oxygen_mask = fields.Boolean(string='Máscara de oxígeno')
    respiration_type = fields.Selection([('regular','Regular'),
                                         ('deep','Profunda'),
                                         ('shallow','Superficial'),
                                         ('labored','Dificultosa'),
                                         ('intercostal','Intercostal')],
                                        string="Respiración")
    peep = fields.Boolean(string='PEEP')
    sce = fields.Boolean(string='SCE')
    lips_lesion = fields.Boolean(string="Lesión labial")
    fio2 = fields.Integer(string="FiO2")
    trachea_alignment = fields.Selection([('midline','Línea media'),
                                           ('right','Desviada a la derecha'),
                                           ('left','Desviada a la izquierda')],
                                          string='Alineación traqueal')
    oral_mucosa_lesion = fields.Boolean(string='Lesión en mucosa oral')
    chest_expansion = fields.Selection([('symmentric','Simétrica'),
                                        ('asymmentric','Asimétrica')],
                                       string="Expansión torácica")
    paradoxical_expansion = fields.Boolean(string="Paradójica")
    tracheal_tug = fields.Boolean(string='Tiraje traqueal')
    xray = fields.Binary(string="Radiografía")
    chest_drainages = fields.One2many('medical.icu.chest_drainage','medical_patient_rounding_chest_drainage_id', string="Drenajes torácicos")
    ecg = fields.Many2one('medical.icu.ecg', string="ECG")
    venous_access = fields.Selection([('none','Ninguno'),
                                      ('central','Catéter central'),
                                      ('peripheral','Periférico')],
                                     string="Acceso venoso")
    swan_ganz = fields.Boolean(string='Swan Ganz')
    arterial_access = fields.Boolean(string='Acceso arterial')
    dialysis = fields.Boolean(string="Diálisis")
    edema = fields.Selection([('none','Ninguno'),
                              ('peripheral','Periférico'),
                              ('anasarca','Anasarca')],
                             string='Edema')
    bacteremia = fields.Boolean(string="Bacteremia")
    ssi = fields.Boolean(string='Infección del sitio quirúrgico')
    wound_dehiscence = fields.Boolean(string='Dehiscencia de herida')
    cellulitis = fields.Boolean(string="Celulitis")
    necrotizing_fasciitis = fields.Boolean(string='Fascitis necrotizante')
    vomiting = fields.Selection([('none','Ninguno'),
                                 ('vomiting','Vómito'),
                                 ('hematemesis','Hematemesis')],
                                string="Vómito")
    bowel_sounds = fields.Selection([('normal','Normal'),
                                     ('increased','Aumentados'),
                                     ('decreased','Disminuidos'),
                                     ('absent','Ausentes')],
                                    string="Ruidos intestinales")
    stools = fields.Selection([('normal','Normal'),
                               ('constipation','Estreñimiento'),
                               ('diarrhea','Diarrea'),
                               ('melena','Melena')],
                              string="Deposiciones")
    peritonitis = fields.Boolean(string="Peritonitis")
    procedures_ids = fields.One2many('medical.rounding_procedure','medical_patient_rounding_procedure_id', string="Procedimientos")
    hospital_location_id = fields.Many2one('stock.location', string='Ubicación hospitalaria')
    medicaments_ids = fields.One2many('medical.patient.rounding.medicament','medical_patient_rounding_medicament_id', string="Medicamentos")
    medical_supplies_ids = fields.One2many('medical.patient.rounding.medical_supply','medical_patient_rounding_medical_supply_id', string='Insumos médicos')
    vaccines_ids = fields.One2many('medical.patient.rounding.vaccine','medical_patient_rounding_vaccine_id', string='Vacunas')
    state = fields.Selection([('draft','Borrador'),
                              ('done','Completado')],
                             string="Estado")