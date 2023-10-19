from odoo import models, fields

class colegio_modify(models.TransientModel):
    _name = 'colegio_modify'
    _description = 'Modificar Colegio Wizard'

    name = fields.Char(string='Nombre')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    
    profesor_ids = fields.One2many('profesor', inverse_name='colegio_id', string='Profesores')
    ampa_ids = fields.One2many(comodel_name='ampa', inverse_name='colegio_id', string='AMPA')
    material_ids = fields.One2many(comodel_name='material', inverse_name='colegio_id', string='Materiales')
    estudiante_ids = fields.One2many(comodel_name='estudiante', inverse_name='colegio_id', string='Estudiantes')
    aulas_ids = fields.One2many(comodel_name='aulas', inverse_name='colegio_id', string='Aulas')
    colegio_id = fields.Many2one('colegio', string= 'Colegio')
 
    def modify_colegio_ids(self):
        if self.colegio_id:
            self.colegio_id.write({
                'name': self.name,
                'direccion': self.direccion,
                'telefono': self.telefono,
                'profesor_ids': self.profesor_ids.ids,
                'estudiante_ids': [(6, 0, self.estudiante_ids.ids)],
                'ampa_ids': self.ampa_ids.ids,
                'material_ids': self.material_ids.ids,
                'aulas_ids': self.aulas_ids.ids
            })