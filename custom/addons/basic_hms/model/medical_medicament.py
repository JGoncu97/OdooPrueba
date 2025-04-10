# -*- coding: utf-8 -*-
# Parte de BrowseInfo. Consulta el archivo LICENSE para más detalles sobre derechos de autor y licencias.

from odoo import api, fields, models, _

class medical_medicament(models.Model):

    _name = 'medical.medicament'
    _description = 'Medicamento médico'
    _rec_name = 'medical_name'

    @api.depends('product_id')
    def onchange_product(self):
        for each in self:
            if each:
                self.qty_available = self.product_id.qty_available
                self.price = self.product_id.lst_price
            else:
                self.qty_available = 0
                self.price = 0.0

    medical_name = fields.Text(string='Nombre')
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    therapeutic_action = fields.Char(string='Efecto terapéutico', help='Acción terapéutica')
    price = fields.Float(compute=onchange_product, string='Precio', store=True)
    qty_available = fields.Integer(compute=onchange_product, string='Cantidad disponible', store=True)
    indications = fields.Text(string='Indicaciones')
    active_component = fields.Char(string='Componente activo')
    presentation = fields.Text(string='Presentación')
    composition = fields.Text(string='Composición')
    dosage = fields.Text(string='Instrucciones de dosificación')
    pregnancy = fields.Text(string='Embarazo')
    overdosage = fields.Text(string='Sobredosis')
    pregnancy_warning = fields.Boolean(string='Advertencia de embarazo')
    pregnancy_category = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('x', 'X'),
        ('n', 'N')
    ], string='Categoría de embarazo', help="""** Categorías de embarazo según la FDA **

CATEGORÍA A: Estudios adecuados y bien controlados en humanos no han demostrado riesgo para el feto durante el primer trimestre (ni en los trimestres posteriores).

CATEGORÍA B: Los estudios en animales no han demostrado riesgo fetal y no existen estudios adecuados y bien controlados en mujeres embarazadas O los estudios en animales han mostrado algún efecto adverso, pero estudios adecuados en mujeres no han demostrado riesgo en ningún trimestre.

CATEGORÍA C: Los estudios en animales han mostrado efectos adversos y no existen estudios adecuados en humanos, pero los beneficios potenciales pueden justificar el uso en mujeres embarazadas.

CATEGORÍA D: Hay evidencia positiva de riesgo fetal humano, basada en datos de reacciones adversas, pero los beneficios potenciales pueden justificar su uso en mujeres embarazadas.

CATEGORÍA X: Estudios en animales o humanos han demostrado anormalidades fetales o riesgo fetal humano, y los riesgos superan claramente los beneficios potenciales.

CATEGORÍA N: No clasificado aún.""")

    adverse_reaction = fields.Text(string='Reacciones adversas')
    storage = fields.Text(string='Condiciones de almacenamiento')
    notes = fields.Text(string='Información adicional')
