from odoo import models, fields, api

class colegio(models.Model):
    _name = 'colegio'
    _description = 'Clase Colegio'

    name = fields.Char(string='Nombre')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    
    profesor_ids = fields.One2many('profesor', inverse_name='colegio_id', string='Profesores')
    ampa_ids = fields.One2many(comodel_name='ampa', inverse_name='colegio_id', string='AMPA')
    material_ids = fields.One2many(comodel_name='material', inverse_name='colegio_id', string='Materiales')
    estudiante_ids = fields.One2many(comodel_name='estudiante', inverse_name='colegio_id', string='Estudiantes')
    aulas_ids = fields.One2many(comodel_name='aulas', inverse_name='colegio_id', string='Aulas')
    colegio_id = fields.Many2one('colegio', string= 'Colegio')