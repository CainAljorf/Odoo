from odoo import models, fields

class ampa_create(models.TransientModel):

    _name = 'ampa_create'
    _description = 'Crear Ampa Wizard'

    name = fields.Char(string='Nombre')
    colegio_id = fields.Many2one(comodel_name='colegio', string='Colegio')
    estudiante_id = fields.Many2many('estudiante', string='Estudiante', domain="[('colegio_id','=',colegio_id)]")

    def action_crear_ampa(self):
        ModeloCrear = self.env['ampa']
        registro = ModeloCrear.create({'name': self.name, 'colegio_id': self.colegio_id.id, 'estudiante_id': self.estudiante_id.ids})
        return registro