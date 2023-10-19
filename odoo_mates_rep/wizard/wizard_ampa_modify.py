from odoo import models, fields, api

class aulas_modify(models.TransientModel):

    _name = 'ampa_modify'
    _description = 'Modificar AMPA Wizard'

    name = fields.Char(string='Nombre')

    colegio_id = fields.Many2one(comodel_name='colegio', string='Colegio')
    estudiante_id = fields.Many2many('estudiante', string='Estudiante', domain="[('colegio_id','=',colegio_id)]")
    ampa_ids = fields.Many2one('ampa', string = 'AMPA')
 
    def modify_ampa_ids(self):
        if self.ampa_ids:
            self.ampa_ids.write({
                'name': self.name,
                'colegio_id': self.colegio_id.id,
                'estudiante_id': [(6, 0, self.estudiante_id.ids)]
            })