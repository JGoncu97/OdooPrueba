# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class medical_patient_evaluation(models.Model):
	_name = 'medical.patient.evaluation'
	_description = 'Evaluación médica del paciente'
	_rec_name = 'medical_patient_id' 
 
	patient_id = fields.Many2one('res.partner', domain=[('is_patient','=',True)], string="Contacto paciente")
	medical_patient_id = fields.Many2one('medical.patient', string="Paciente", required=True)
	start_evaluation = fields.Datetime(string="Inicio de evaluación")
	physician_partner_id = fields.Many2one('res.partner', domain=[('is_doctor','=',True)], string="Médico")
	end_evaluation = fields.Datetime(string="Fin de evaluación")
	evaluation_type = fields.Selection([
			('a', 'Ambulatorio'),
			('e', 'Emergencia'),
			('i', 'Hospitalizado'),
			('pa', 'Cita programada'),
			('pc', 'Control periódico'),
			('p', 'Llamada telefónica'),
			('t', 'Telemedicina'),
		], string='Tipo')
	chief_complaint = fields.Char(string='Motivo de consulta')
	information_source = fields.Char(string='Fuente')
	reliable_info = fields.Boolean(string='Confiable')
	present_illness = fields.Text(string='Enfermedad actual')
   
	weight = fields.Float(string='Peso (kg)', help='Peso en kilogramos')
	height = fields.Float(string='Altura (cm)')
	abdominal_circ = fields.Float(string='Circunferencia abdominal')
	hip = fields.Float(string='Cadera')
	bmi = fields.Float(string='Índice de masa corporal')
	whr = fields.Float(string='ICC (Índice cintura-cadera)')
	head_circumference = fields.Float(string='Circunferencia de la cabeza')
	malnutrition = fields.Boolean(string='Desnutrición')
	dehydration = fields.Boolean(string='Deshidratación')
	tag = fields.Integer(
			string='Últimos triglicéridos',
			help='Nivel de triacilglicerol (triglicéridos). Puede ser aproximado'
		)
	is_tremor = fields.Boolean(
			string='Temblor',
			help='Marque esta casilla si el paciente muestra signos de temblores',
		)
	mood = fields.Selection([
			('n', 'Normal'),
			('s', 'Triste'),
			('f', 'Temeroso'),
			('r', 'Rabioso'),
			('h', 'Feliz'),
			('d', 'Disgusto'),
			('e', 'Euforia'),
			('fl', 'Plano'),
		], string='Estado de ánimo')
	glycemia = fields.Float(
			string='Glucemia',
			help='Último nivel de glucosa en sangre. Puede ser aproximado.')
	evaluation_summary = fields.Text(string='Resumen de evaluación')
	temperature = fields.Float(string='Temperatura (celsius)',
									help='Temperatura en grados Celsius')
	osat = fields.Integer(string='Saturación de oxígeno',
							   help='Saturación de oxígeno (arterial).')
	bpm = fields.Integer(string='Frecuencia cardíaca',
							  help='Frecuencia cardíaca expresada en latidos por minuto')
	loc_eyes = fields.Selection([
			('1', 'No abre los ojos'),
			('2', 'Abre los ojos en respuesta a estímulos dolorosos'),
			('3', 'Abre los ojos en respuesta a la voz'),
			('4', 'Abre los ojos espontáneamente'),
		], string='Glasgow - Ojos')
	loc_verbal = fields.Selection([
			('1', 'No emite sonidos'),
			('2', 'Sonidos incomprensibles'),
			('3', 'Palabras inapropiadas'),
			('4', 'Confuso, desorientado'),
			('5', 'Orientado, conversa normalmente'),
		], string='Glasgow - Verbal')
	loc_motor = fields.Selection([
			('1', 'No se mueve'),
			('2', 'Extensión a estímulos dolorosos (respuesta decorticada)'),
			('3', 'Flexión anormal a estímulos dolorosos (respuesta decorticada)'),
			('4', 'Flexión/Retirada a estímulos dolorosos'),
			('5', 'Localiza estímulos dolorosos'),
			('6', 'Obedece órdenes'),
		], string='Glasgow - Motor')
	violent = fields.Boolean(string='Comportamiento violento')
	orientation = fields.Boolean(string='Orientación')
	memory = fields.Boolean(string='Memoria')
	knowledge_current_events = fields.Boolean(string='Conocimiento de eventos actuales')
	judgment = fields.Boolean(string='Juicio')
	symptom_proctorrhagia = fields.Boolean(string='Polifagia')
	abstraction = fields.Boolean(string='Abstracción')
	vocabulary = fields.Boolean(string='Vocabulario')
	symptom_pain = fields.Boolean(string='Dolor')
	symptom_pain_intensity = fields.Integer(string='Intensidad del dolor')
	symptom_arthralgia = fields.Boolean(string='Artralgia')
	symptom_abdominal_pain = fields.Boolean(string='Dolor abdominal')
	symptom_thoracic_pain = fields.Boolean(string='Dolor torácico')
	symptom_pelvic_pain = fields.Boolean(string='Dolor pélvico')
	symptom_hoarseness = fields.Boolean(string='Ronquera')
	symptom_sore_throat = fields.Boolean(string='Dolor de garganta')
	symptom_ear_discharge = fields.Boolean(string='Secreción del oído')
	symptom_chest_pain_excercise = fields.Boolean(string='Dolor en el pecho solo con ejercicio')
	symptom_astenia = fields.Boolean(string='Astenia')
	symptom_weight_change = fields.Boolean(string='Cambio repentino de peso')
	symptom_hemoptysis = fields.Boolean(string='Hemoptisis')
	symptom_epistaxis = fields.Boolean(string='Epistaxis')
	symptom_rinorrhea = fields.Boolean(string='Rinorrea')
	symptom_vomiting = fields.Boolean(string='Vómito')
	symptom_polydipsia = fields.Boolean(string='Polidipsia')
	symptom_polyuria = fields.Boolean(string='Poliuria')
	symptom_vesical_tenesmus = fields.Boolean(string='Tenesmo vesical')
	symptom_dysuria = fields.Boolean(string='Disuria')
	symptom_myalgia = fields.Boolean(string='Mialgia')
	symptom_cervical_pain = fields.Boolean(string='Dolor cervical')
	symptom_lumbar_pain = fields.Boolean(string='Dolor lumbar')
	symptom_headache = fields.Boolean(string='Dolor de cabeza')
	symptom_odynophagia = fields.Boolean(string='Odinofagia')
	symptom_otalgia = fields.Boolean(string='Otalgia')
	symptom_chest_pain = fields.Boolean(string='Dolor en el pecho')
	symptom_orthostatic_hypotension = fields.Boolean(string='Hipotensión ortostática')
	symptom_anorexia = fields.Boolean(string='Anorexia')
	symptom_abdominal_distension = fields.Boolean(string='Distensión abdominal')
	symptom_hematemesis = fields.Boolean(string='Hematemesis')
	symptom_gingival_bleeding = fields.Boolean(string='Sangrado gingival')
	symptom_nausea = fields.Boolean(string='Náuseas')
	symptom_dysphagia = fields.Boolean(string='Disfagia')
	symptom_polyphagia = fields.Boolean(string='Polifagia')
	symptom_nocturia = fields.Boolean(string='Nicturia')
	symptom_pollakiuria = fields.Boolean(string='Polaquiuria')
	symptom_mood_swings = fields.Boolean(string='Cambios de humor')
	symptom_pruritus = fields.Boolean(string='Prurito')
	symptom_disturb_sleep = fields.Boolean(string='Trastornos del sueño')
	symptom_orthopnea = fields.Boolean(string='Ortopnea')
	symptom_paresthesia = fields.Boolean(string='Parestesia')
	symptom_dizziness = fields.Boolean(string='Mareos')
	symptom_tinnitus = fields.Boolean(string='Tinnitus')
	symptom_eye_glasses = fields.Boolean(string='Anteojos')
	symptom_diplopia = fields.Boolean(string='Diplopia')
	symptom_dysmenorrhea = fields.Boolean(string='Dismenorrea')
	symptom_metrorrhagia = fields.Boolean(string='Metrorragia')
	symptom_vaginal_discharge = fields.Boolean(string='Flujo vaginal')
	symptom_diarrhea = fields.Boolean(string='Diarrea')
	symptom_rectal_tenesmus = fields.Boolean(string='Tenesmo rectal')
	symptom_sexual_dysfunction = fields.Boolean(string='Disfunción sexual')
	symptom_stress = fields.Boolean(string='Estrés')
	symptom_insomnia = fields.Boolean(string='Insomnio')
	symptom_dyspnea = fields.Boolean(string='Disnea')
	symptom_amnesia = fields.Boolean(string='Amnesia')
	symptom_paralysis = fields.Boolean(string='Parálisis')
	symptom_vertigo = fields.Boolean(string='Vértigo')
	symptom_syncope = fields.Boolean(string='Síncope')
	symptom_blurry_vision = fields.Boolean(string='Visión borrosa')
	symptom_photophobia = fields.Boolean(string='Fotofobia')
	symptom_amenorrhea = fields.Boolean(string='Amenorrea')
	symptom_menorrhagia = fields.Boolean(string='Menorragia')
	symptom_urethral_discharge = fields.Boolean(string='Secreción uretral')
	symptom_constipation = fields.Boolean(string='Estreñimiento')
	symptom_melena = fields.Boolean(string='Melena')
	symptom_xerostomia = fields.Boolean(string='Xerostomía')
	calculation_ability = fields.Boolean(string='Capacidad de cálculo')
	object_recognition = fields.Boolean(string='Reconocimiento de objetos')
	praxis = fields.Boolean(string='Praxis')
	edema = fields.Boolean(string='Edema')
	petechiae = fields.Boolean(string='Petequias')
	acropachy = fields.Boolean(string='Acropaquia')
	miosis = fields.Boolean(string='Miosis')
	cough = fields.Boolean(string='Tos')
	arritmia = fields.Boolean(string='Arritmias')
	heart_extra_sounds = fields.Boolean(string='Sonidos cardíacos extras')
	ascites = fields.Boolean(string='Ascitis')
	bronchophony = fields.Boolean(string='Broncofonía')
	cyanosis = fields.Boolean(string='Cianosis')
	hematoma = fields.Boolean(string='Hematomas')
	nystagmus = fields.Boolean(string='Nistagmo')
	mydriasis = fields.Boolean(string='Midriasis')
	palpebral_ptosis = fields.Boolean(string='Ptosis palpebral')
	heart_murmurs = fields.Boolean(string='Soplos cardíacos')
	jugular_engorgement = fields.Boolean(string='Temblor')
	lung_adventitious_sounds = fields.Boolean(string='Ruidos adventicios pulmonares')
	increased_fremitus = fields.Boolean(string='Frémito aumentado')
	jaundice = fields.Boolean(string='Ictericia')
	breast_lump = fields.Boolean(string='Bultos mamarios')
	nipple_inversion = fields.Boolean(string='Inversión del pezón')
	peau_dorange = fields.Boolean(string='Piel de naranja')
	hypotonia = fields.Boolean(string='Hipotonía')
	masses = fields.Boolean(string='Masas')
	goiter = fields.Boolean(string='Bocio')
	xerosis = fields.Boolean(string='Xerosis')
	decreased_fremitus = fields.Boolean(string='Frémito disminuido')
	lynphadenitis = fields.Boolean(string='Linfadenitis')
	breast_asymmetry = fields.Boolean(string='Asimetría mamaria')
	nipple_discharge = fields.Boolean(string='Secreción del pezón')
	gynecomastia = fields.Boolean(string='Ginecomastia')
	hypertonia = fields.Boolean(string='Hipertonía')
	pressure_ulcers = fields.Boolean(string='Úlceras por presión')
	alopecia = fields.Boolean(string='Alopecia')
	erithema = fields.Boolean(string='Eritema')
	diagnosis_id = fields.Many2one('medical.pathology', string='Diagnóstico presuntivo')
	ldl = fields.Integer(
			string='Último LDL',
			help='Última lectura de colesterol LDL. Puede ser aproximado'
		)
	visit_type = fields.Selection([
			('new','Nueva condición de salud'),
			('follow','Seguimiento'),
			('chronic','Control de condición crónica'),
			('child','Control de niño sano'),
			('women','Control de mujer sana'),
			('man','Control de hombre sano')
		], string="Tipo de visita")
	urgency = fields.Selection([
			('a', 'Normal'), 
			('b', 'Urgente'), 
			('c', 'Emergencia médica')
		], string='Urgencia')
	systolic = fields.Integer(string='Presión sistólica')
	diastolic = fields.Integer(string='Presión diastólica')
	respiratory_rate = fields.Integer(string='Frecuencia respiratoria')
	signs_and_symptoms_ids = fields.One2many('medical.signs.and.sympotoms', 'patient_evaluation_id', string='Signos y síntomas')
	hba1c = fields.Float(string='Hemoglobina glicosilada')
	cholesterol_total = fields.Integer(string='Último colesterol total')
	hdl = fields.Integer(string='Último HDL')
	ldl = fields.Integer(string='Último LDL')
	tags = fields.Integer(string='Últimos triglicéridos')
	loc = fields.Integer(string='Nivel de consciencia')
	info_diagnosis = fields.Text(string='Información del diagnóstico')
	directions = fields.Text(string='Plan de tratamiento')
	user_id = fields.Many2one('res.users', string='ID de usuario del médico', readonly=True)
	medical_appointment_date_id = fields.Many2one('medical.appointment', string='Fecha de la cita')
	next_appointment_id = fields.Many2one('medical.appointment', string='Próxima cita')
	derived_from_physician_id = fields.Many2one('medical.physician', string='Derivado por el médico')
	derived_to_physician_id = fields.Many2one('medical.physician', string='Derivado al médico')
	secondary_conditions_ids = fields.One2many('medical.secondary_condition', 'patient_evaluation_id', string='Condiciones secundarias')
	diagnostic_hypothesis_ids = fields.One2many('medical.diagnostic_hypotesis', 'patient_evaluation_id', string='Procedimientos')
	procedure_ids = fields.One2many('medical.directions', 'patient_evaluation_id', string='Procedimientos')