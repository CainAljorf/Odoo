from odoo import models, fields, api

class ampa(models.Model):

    _name = 'ampa'
    _description = 'Clase AMPA'

    name = fields.Char(string='Nombre')

    colegio_id = fields.Many2one(comodel_name='colegio', string='Colegio')
    estudiante_id = fields.Many2many('estudiante', string='Estudiante')