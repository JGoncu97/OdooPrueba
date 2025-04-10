# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

class medical_patient(models.Model):
    
    _name = 'medical.patient'
    _description = 'Paciente'
    _rec_name = 'patient_id'

    @api.onchange('patient_id')
    def _onchange_patient(self):
        '''
        The purpose of the method is to define a domain for the available
        purchase orders.
        '''
        address_id = self.patient_id
        self.partner_address_id = address_id

    def print_report(self):
        return self.env.ref('basic_hms.report_print_patient_card').report_action(self)

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    patient_id = fields.Many2one('res.partner',domain=[('is_patient','=',True)],string="Paciente", required= True)
    name = fields.Char(string='Documento', readonly=True)
    last_name = fields.Char(string="Apellidos")
    date_of_birth = fields.Date(string="Fecha de nacimiento")
    sex = fields.Selection([('m', 'Masculino'),('f', 'Femenino')], string="Sexo")
    age = fields.Char(compute=onchange_age,string="Edad del paciente",store=True)
    critical_info = fields.Text(string="Información crítica")
    photo = fields.Binary(string="Fotografía")
    blood_type = fields.Selection([('A', 'A'),('B', 'B'),('AB', 'AB'),('O', 'O')], string="Grupo sanguíneo")
    rh = fields.Selection([('-+', '+'),('--', '-')], string="Factor RH")
    marital_status = fields.Selection([('s','Soltero(a)'),('m','Casado(a)'),('w','Viudo(a)'),('d','Divorciado(a)'),('x','Separado(a)')],string='Estado civil')
    deceased = fields.Boolean(string='Fallecido')
    date_of_death = fields.Date(string="Fecha de fallecimiento")
    cause_of_death = fields.Char(string='Causa de fallecimiento')
    receivable = fields.Float(string="Saldo pendiente", readonly=True)
    current_insurance_id = fields.Many2one('medical.insurance',string="EPS actual")
    partner_address_id = fields.Many2one('res.partner', string="Dirección")

    street = fields.Char(related='patient_id.street', readonly=False)
    street2 = fields.Char(related='patient_id.street2', readonly=False)
    zip_code = fields.Char(related='patient_id.zip', readonly=False)
    city = fields.Char(related='patient_id.city', readonly=False)
    state_id = fields.Many2one("res.country.state", related='patient_id.state_id', readonly=False)
    country_id = fields.Many2one('res.country', related='patient_id.country_id', readonly=False)
    
    primary_care_physician_id = fields.Many2one('medical.physician', string="Médico de cabecera")
    patient_status = fields.Char(string="Estado de hospitalización",readonly=True)
    patient_disease_ids = fields.One2many('medical.patient.disease','patient_id',string="Enfermedades del paciente")
    patient_psc_ids = fields.One2many('medical.patient.psc','patient_id',string="Problemas de salud")
    excercise = fields.Boolean(string='Realiza ejercicio')
    excercise_minutes_day = fields.Integer(string="Minutos por día")
    sleep_hours = fields.Integer(string="Horas de sueño")
    sleep_during_daytime = fields.Boolean(string="Duerme durante el día")
    number_of_meals = fields.Integer(string="Comidas por día")
    coffee = fields.Boolean(string="Consume café")
    coffee_cups = fields.Integer(string='Tazas por día')
    eats_alone = fields.Boolean(string="Come solo")
    soft_drinks = fields.Boolean(string="Consume gaseosas")
    salt = fields.Boolean(string="Consume sal")
    diet = fields.Boolean(string="Actualmente en dieta")
    diet_info = fields.Integer(string='Información de dieta')
    general_info = fields.Text(string="Información general")
    lifestyle_info = fields.Text(string="Estilo de vida")
    smoking = fields.Boolean(string="Fumador")
    smoking_number = fields.Integer(string="Cigarrillos al día")
    ex_smoker = fields.Boolean(string="Ex-fumador")
    second_hand_smoker = fields.Boolean(string="Fumador pasivo")
    age_start_smoking = fields.Integer(string="Edad inicio de fumar")
    age_quit_smoking = fields.Integer(string="Edad dejó de fumar")
    drug_usage = fields.Boolean(string='Consumo de drogas')
    drug_iv = fields.Boolean(string='Drogas intravenosas')
    ex_drug_addict = fields.Boolean(string='Ex adicto a drogas')
    age_start_drugs = fields.Integer(string='Edad inicio consumo drogas')
    age_quit_drugs = fields.Integer(string="Edad dejó las drogas")
    alcohol = fields.Boolean(string="Consume alcohol")
    ex_alcohol = fields.Boolean(string="Ex alcohólico")
    age_start_drinking = fields.Integer(string="Edad inicio consumo alcohol")
    age_quit_drinking = fields.Integer(string="Edad dejó el alcohol")
    alcohol_beer_number = fields.Integer(string="Cervezas por día")
    alcohol_wine_number = fields.Integer(string="Copas de vino por día")
    alcohol_liquor_number = fields.Integer(string="Tragos por día")
    cage_ids = fields.One2many('medical.patient.cage','patient_id',string="Evaluación CAGE (alcohol/drogas)")
    sex_oral = fields.Selection([('0','Ninguno'),
                                 ('1','Activo'),
                                 ('2','Pasivo'),
                                 ('3','Ambos')],string='Sexo oral')
    sex_anal = fields.Selection([('0','Ninguno'),
                                 ('1','Activo'),
                                 ('2','Pasivo'),
                                 ('3','Ambos')],string='Sexo anal')
    prostitute = fields.Boolean(string='Trabajador(a) sexual')
    sex_with_prostitutes = fields.Boolean(string='Relaciones con trabajadores sexuales')
    sexual_preferences = fields.Selection([
            ('h', 'Heterosexual'),
            ('g', 'Homosexual'),
            ('b', 'Bisexual'),
            ('t', 'Transexual'),
        ], string="Orientación sexual", sort=False)
    sexual_practices = fields.Selection([
            ('s', 'Sexo seguro / protegido'),
            ('r', 'Sexo riesgoso / sin protección'),
        ], string="Prácticas sexuales", sort=False)
    sexual_partners = fields.Selection([
            ('m', 'Monógamo'),
            ('t', 'Polígamo'),
        ], string="Relaciones sexuales", sort=False)
    sexual_partners_number = fields.Integer(string="Número de parejas sexuales")
    first_sexual_encounter = fields.Integer(string="Edad primera relación sexual")
    anticonceptive = fields.Selection([
            ('0', 'Ninguno'),
            ('1', 'Píldora / Minipíldora'),
            ('2', 'Preservativo masculino'),
            ('3', 'Vasectomía'),
            ('4', 'Ligadura de trompas'),
            ('5', 'Dispositivo intrauterino (DIU)'),
            ('6', 'Coito interrumpido'),
            ('7', 'Método del ritmo'),
            ('8', 'Inyección anticonceptiva'),
            ('9', 'Parche anticonceptivo'),
            ('10', 'Preservativo femenino'),
        ], string="Método anticonceptivo", sort=False)
    sexuality_info = fields.Text(string="Información adicional de sexualidad")
    motorcycle_rider = fields.Boolean(string="Conduce motocicleta", help="El/la paciente conduce motocicletas")
    helmet = fields.Boolean(string="Usa casco", help="El/la paciente usa casco adecuado para motocicleta")
    traffic_laws = fields.Boolean(string="Respeta normas de tránsito", help="Marcar si el/la paciente es un conductor/a responsable")
    car_revision = fields.Boolean(string="Revisión técnico-mecánica", help="Mantenimiento del vehículo. Revisiones periódicas - llantas, frenos...")
    car_seat_belt = fields.Boolean(string="Usa cinturón de seguridad", help="Medidas de seguridad al conducir: cinturón")
    car_child_safety = fields.Boolean(string="Seguridad infantil en vehículo", help="Medidas de seguridad al conducir : sillas de seguridad, cinturón de seguridad adecuado, no sentarse en el asiento delantero, ....")
    home_safety = fields.Boolean(string="Seguridad en el hogar", help="Medidas de seguridad en cocina, productos químicos, etc.")
    fertile = fields.Boolean(string="Fértil")
    menarche = fields.Integer(string="Edad de la menarquia")
    menopausal = fields.Boolean(string="Menopausia")
    menopause = fields.Integer(string="Edad de la menopausia")
    menstrual_history_ids = fields.One2many('medical.patient.menstrual.history','patient_id')
    breast_self_examination = fields.Boolean(string="Autoexamen de seno")
    mammography = fields.Boolean(string="Mamografía")
    pap_test = fields.Boolean(string="Citología")
    last_pap_test = fields.Date(string="Última citología")
    colposcopy = fields.Boolean(string="Colposcopia")
    mammography_history_ids = fields.One2many('medical.patient.mammography.history','patient_id' ,string="Historial de mamografías")
    pap_history_ids = fields.One2many('medical.patient.pap.history','patient_id' ,string="Historial de citologías")
    colposcopy_history_ids = fields.One2many('medical.patient.colposcopy.history','patient_id' ,string="Historial de colposcopias")
    pregnancies = fields.Integer(string="Embarazos")
    premature = fields.Integer(string="Prematuros")
    stillbirths = fields.Integer(string="Mortinatos")
    abortions = fields.Integer(string="Abortos")
    pregnancy_history_ids = fields.One2many('medical.patient.pregnency','patient_id' ,string="Historial de embarazos")
    family_history_ids = fields.Many2many('medical.family.disease',string="Historial familiar de enfermedades")
    perinatal_ids = fields.Many2many('medical.preinatal' ,string="Historial perinatal")
    ex_alcoholic = fields.Boolean(string="Ex alcohólico")
    currently_pregnant = fields.Boolean(string="Embarazo actual")
    born_alive = fields.Integer(string="Nacidos vivos")
    gpa = fields.Char(string="GPA")
    works_at_home = fields.Boolean(string="Trabaja en casa")
    colposcopy_last = fields.Date(string="Última colposcopia")
    mammography_last = fields.Date(string="Última mamografía")
    ses = fields.Selection([
            ('None', ''),
            ('0', 'Bajo'),
            ('1', 'Medio-bajo'),
            ('2', 'Medio'),
            ('3', 'Medio-alto'),
            ('4', 'Alto'),
        ], string="Estrato socioeconómico", help="Estrato socioeconómico del/la paciente", sort=False)
    education = fields.Selection([('o','Ninguno'),('1','Primaria incompleta'),
                                  ('2','Primaria completa'),
                                  ('3','Bachillerato incompleto'),
                                  ('4','Bachillerato completo'),
                                  ('5','Educación superior')],string='Nivel educativo')
    housing = fields.Selection([
            ('None', ''),
            ('0', 'Vivienda con condiciones sanitarias deficientes'),
            ('1', 'Vivienda pequeña pero con buenas condiciones sanitarias'),
            ('2', 'Vivienda cómoda con buenas condiciones sanitarias'),
            ('3', 'Vivienda amplia con excelentes condiciones sanitarias'),
            ('4', 'Vivienda lujosa con excelentes condiciones sanitarias'),
        ], string="Condiciones de vivienda", help="Condiciones de vivienda y sanitarias", sort=False)
    works = fields.Boolean(string="Trabaja")
    hours_outside = fields.Integer(string="Horas fuera de casa", help="Número de horas al día que la paciente pasa fuera de la casa")
    hostile_area = fields.Boolean(string="Vive en zona de riesgo")
    notes = fields.Text(string="Observaciones adicionales")
    sewers = fields.Boolean(string="Alcantarillado")
    water = fields.Boolean(string="Agua potable")
    trash = fields.Boolean(string="Recolección de basura")
    electricity = fields.Boolean(string="Servicio de electricidad")
    gas = fields.Boolean(string="Servicio de gas")
    telephone = fields.Boolean(string="Servicio telefónico")
    television = fields.Boolean(string="Televisión")
    internet = fields.Boolean(string="Internet")
    single_parent = fields.Boolean(string="Familia monoparental")
    domestic_violence = fields.Boolean(string="Violencia intrafamiliar")
    working_children = fields.Boolean(string="Trabajo infantil")
    teenage_pregnancy = fields.Boolean(string="Embarazo adolescente")
    sexual_abuse = fields.Boolean(string="Abuso sexual")
    drug_addiction = fields.Boolean(string="Drogadicción")
    school_withdrawal = fields.Boolean(string="Deserción escolar")
    prison_past = fields.Boolean(string="Antecedentes carcelarios")
    prison_current = fields.Boolean(string="Actualmente en prisión")
    relative_in_prison = fields.Boolean(string="Familiar en prisión", help="Algún familiar directo ha estado o está en prisión")
    fam_apgar_help = fields.Selection([
            ('None', ''),
            ('0', 'Ninguno'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], string='Ayuda familiar',
            help="¿Está satisfecho con la ayuda familiar ante un problema?", sort=False)
    fam_apgar_discussion = fields.Selection([
            ('None', ''),
            ('0', 'Ninguna'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], string='Toma de decisiones',
            help="¿Está satisfecho con cómo se toman decisiones importantes como grupo?", sort=False)
    fam_apgar_decisions = fields.Selection([
            ('None', ''),
            ('0', 'None'),
            ('1', 'Moderately'),
            ('2', 'Very much'),
        ], string='Decision making',
            help="Is the patient satisfied with the level of making important decisions as a group ?", sort=False)
    fam_apgar_timesharing = fields.Selection([
            ('None', ''),
            ('0', 'Ninguna'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], string='Tiempo en familia',
            help="¿Está satisfecho con el tiempo que pasan juntos?", sort=False)
    fam_apgar_affection = fields.Selection([
            ('None', ''),
            ('0', 'Ninguna'),
            ('1', 'Moderadamente'),
            ('2', 'Mucho'),
        ], string="Afecto familiar",
            help="¿Está satisfecho con el afecto que recibe de su familia?", sort=False)
    fam_apgar_score = fields.Integer(string="Puntuación", help="7-10: Familia funcional; 4-6: Disfunción moderada; 0-3: Disfunción severa")
    lab_test_ids = fields.One2many('medical.patient.lab.test','patient_id',string='Exámenes de laboratorio')
    fertile = fields.Boolean(string="Fértil")
    menarche_age = fields.Integer(string="Edad de la menarquia")
    menopausal = fields.Boolean(string="Menopausia")
    pap_test_last = fields.Date(string="Última citología")
    colposcopy = fields.Boolean(string="Colposcopia")
    gravida = fields.Integer(string="Embarazos")
    medical_vaccination_ids = fields.One2many('medical.vaccination','medical_patient_vaccines_id',string="Vacunas")
    medical_appointments_ids = fields.One2many('medical.appointment','patient_id',string='Citas médicas')
    lastname = fields.Char(string="Apellido")
    report_date = fields.Date(string="Fecha del reporte", default=datetime.today().date())
    medication_ids = fields.One2many('medical.patient.medication1','medical_patient_medication_id',string="Medicamentos")
    deaths_2nd_week = fields.Integer(string="Fallecidos después de 2da semana")
    deaths_1st_week = fields.Integer(string="Fallecidos después de 1ra semana")
    full_term = fields.Integer(string="A término")
    ses_notes = fields.Text(string="Notas socioeconómicas")

    def _valid_field_parameter(self, field, name):
        return name == 'sort' or super()._valid_field_parameter(field, name)

    @api.model_create_multi
    def create(self,vals_list):
        for val in vals_list:
            appointment = self._context.get('appointment_id')
            res_partner_obj = self.env['res.partner']
            if appointment:
                val_1 = {'name': self.env['res.partner'].browse(val['patient_id']).name}
                patient= res_partner_obj.create(val_1)
                val.update({'patient_id': patient.id})
            if val.get('date_of_birth'):
                dt = val.get('date_of_birth')
                d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                age = str(rd.years) + "y" +" "+ str(rd.months) + "m" +" "+ str(rd.days) + "d"
                val.update({'age':age} )

            patient_id  = self.env['ir.sequence'].next_by_code('medical.patient')
            if patient_id:
                val.update({
                            'name':patient_id,
                           })
           
        return super(medical_patient, self).create(vals_list)

    @api.constrains('date_of_death')
    def _check_date_death(self):
        for rec in self:
            if rec.date_of_birth:
                if rec.deceased == True :
                    if rec.date_of_death <= rec.date_of_birth :
                      raise UserError(_('Date Of Death Can Not Less Than Date Of Birth.' ))

    def copy(self, default=None):
        for rec in self:
            raise UserError(_('You Can Not Duplicate Patient.' ))

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: