from odoo import models, fields, api

class profesor(models.Model):
    _name = 'profesor'
    _description = 'Clase Profesor'

    name = fields.Char(string='Nombre')
    email = fields.Char(string='Email')
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')

    colegio_id = fields.Many2one(comodel_name='colegio', string='Colegio')
    material_ids = fields.Many2many(comodel_name='material', string='Materiales')
    estudiante_id = fields.Many2many(comodel_name='estudiante',string='Estudiante')
    aulas_ids = fields.Many2many(comodel_name='aulas', string='Aulas')
    profesor_ids = fields.Many2one('profesor', string='Profesor')

