# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _
from datetime import datetime, date
from datetime import datetime, timedelta
from odoo.exceptions import UserError

class medical_appointment(models.Model):
    _name = "medical.appointment"
    _description = "Cita Médica"
    _inherit = 'mail.thread'

    name = fields.Char(string="ID de Cita", readonly=True, copy=True)
    is_invoiced = fields.Boolean(copy=False, default=False)
    institution_partner_id = fields.Many2one('res.partner', domain=[('is_institution', '=', True)], string="Centro de Salud")
    inpatient_registration_id = fields.Many2one('medical.inpatient.registration', string="Registro de Internación")
    patient_status = fields.Selection([
        ('ambulatory', 'Ambulatorio'),
        ('outpatient', 'Paciente Externo'),
        ('inpatient', 'Paciente Internado'),
    ], string='Estado del Paciente', sort=False, default='outpatient')
    patient_id = fields.Many2one('medical.patient', string='Paciente', required=True)
    urgency_level = fields.Selection([
        ('a', 'Normal'),
        ('b', 'Urgente'),
        ('c', 'Emergencia Médica'),
    ], string='Nivel de Urgencia', sort=False, default="b")
    appointment_date = fields.Datetime(string='Fecha de la Cita', required=True, default=fields.Datetime.now)
    appointment_end = fields.Datetime(string='Fin de la Cita', required=True)
    doctor_id = fields.Many2one('medical.physician', string='Médico', required=True)
    no_invoice = fields.Boolean(string='Exento de Factura', default=True)
    validity_status = fields.Selection([
        ('invoice', 'Facturado'),
        ('tobe', 'Por Facturar'),
    ], string='Estado', sort=False, readonly=True, default='tobe')
    appointment_validity_date = fields.Datetime(string='Fecha de Validez')
    consultations_id = fields.Many2one('product.product', string='Servicio de Consulta', required=True)
    comments = fields.Text(string="Información Adicional")
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmada'),
        ('cancel', 'Cancelada'),
        ('done', 'Realizada')
    ], string="Estado", default='draft')
    invoice_to_insurer = fields.Boolean(string='Facturar a Aseguradora')
    medical_patient_psc_ids = fields.Many2many('medical.patient.psc', string='Lista de Síntomas Pediátricos')
    medical_prescription_order_ids = fields.One2many('medical.prescription.order', 'appointment_id', string='Prescripciones')
    insurer_id = fields.Many2one('medical.insurance', string='Aseguradora')
    duration = fields.Integer(string='Duración')

    def _valid_field_parameter(self, field, name):
        return name == 'sort' or super()._valid_field_parameter(field, name)

    @api.onchange('patient_id')
    def onchange_name(self):
        ins_obj = self.env['medical.insurance']
        ins_record = ins_obj.search([('medical_insurance_partner_id', '=', self.patient_id.patient_id.id)])
        if len(ins_record) >= 1:
            self.insurer_id = ins_record[0].id
        else:
            self.insurer_id = False

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('medical.appointment') or 'APT'
            msg_body = 'Cita creada'
            for msg in self:
                msg.message_post(body=msg_body)
        return super(medical_appointment, self).create(vals_list)

    @api.onchange('inpatient_registration_id')
    def onchange_patient(self):
        if not self.inpatient_registration_id:
            self.patient_id = ""
        inpatient_obj = self.env['medical.inpatient.registration'].browse(self.inpatient_registration_id.id)
        self.patient_id = inpatient_obj.id

    def confirm(self):
        self.write({'state': 'confirmed'})

    def done(self):
        self.write({'state': 'done'})

    def cancel(self):
        self.write({'state': 'cancel'})

    def print_prescription(self):
        return self.env.ref('basic_hms.report_print_prescription').report_action(self)

    def view_patient_invoice(self):
        self.write({'state': 'cancel'})

    def create_invoice(self):
        lab_req_obj = self.env['medical.appointment']
        account_invoice_obj = self.env['account.move']
        account_invoice_line_obj = self.env['account.move.line']
        lab_req = lab_req_obj
        if lab_req.is_invoiced:
            raise UserError(_('La factura ya existe.'))
        if not lab_req.no_invoice:
            res = account_invoice_obj.create({
                'partner_id': lab_req.patient_id.patient_id.id,
                'date_invoice': date.today(),
                'company_id': self.company_id.id,
                'journal_id': account_invoice_obj.journal_id.id,
                'account_id': lab_req.patient_id.patient_id.property_account_receivable_id.id,
            })
            res1 = account_invoice_line_obj.create({
                'product_id': lab_req.consultations_id.id,
                'product_uom': lab_req.consultations_id.uom_id.id,
                'name': lab_req.consultations_id.name,
                'product_uom_qty': 1,
                'price_unit': lab_req.consultations_id.lst_price,
                'account_id': lab_req.patient_id.patient_id.property_account_receivable_id.id,
                'invoice_id': res.id
            })

            if res:
                lab_req.write({'is_invoiced': True})
                imd = self.env['ir.model.data']
                action = self.env.ref('account.action_invoice_tree1')
                list_view_id = imd.sudo()._xmlid_to_res_id('account.view_order_form')
                result = {
                    'name': action.name,
                    'help': action.help,
                    'type': action.type,
                    'views': [[list_view_id, 'form']],
                    'target': action.target,
                    'context': action.context,
                    'res_model': action.res_model,
                    'res_id': res.id,
                }
                if res:
                    result['domain'] = "[('id','=',%s)]" % res.id
        else:
            raise UserError(_('La cita está exenta de facturación.'))
        return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
