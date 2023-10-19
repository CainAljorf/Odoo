from odoo import models, fields, api

class material(models.Model):
    _name = 'material'
    _description = 'Clase Material'

    name = fields.Char(string='Nombre')
    descripcion = fields.Char(string='Descripción')
    cantidad = fields.Float(string='Cantidad')

    colegio_id = fields.Many2one(comodel_name='colegio', string='Colegio')
    profesor_id = fields.Many2many(comodel_name='profesor',  string='Profesor')
    material_ids = fields.Many2one('material', string= 'Material')

