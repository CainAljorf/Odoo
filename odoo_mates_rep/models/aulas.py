from odoo import models, fields, api

class aulas(models.Model):
    _name = 'aulas'
    _description = 'Clase Aulas'

    name = fields.Char(string='Nombre')

    colegio_id = fields.Many2one(comodel_name='colegio', string='Colegio')
    estudiante_id = fields.Many2many(comodel_name='estudiante',  string='Estudiante')
    profesor_id = fields.Many2many(comodel_name='profesor', string='Profesor')