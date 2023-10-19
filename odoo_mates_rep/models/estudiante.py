from odoo import models, fields, api

class estudiante(models.Model):
    _name = 'estudiante'
    _description = 'Clase Estudiante'

    name = fields.Char(string='Nombre')
    edad = fields.Integer(string='Edad')
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')

    colegio_id = fields.Many2one(comodel_name='colegio', string='Colegio')
    ampa_ids = fields.Many2one(comodel_name='ampa', string='AMPA')
    aulas_ids = fields.Many2many(comodel_name='aulas', string='Aulas')
    profesor_ids = fields.Many2many(comodel_name='profesor', string='Profesor')
    estudiante_ids= fields.Many2one('estudiante', string= 'Estudiante')