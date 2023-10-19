from odoo import models, fields
from odoo.exceptions import ValidationError

class colegio_delete(models.TransientModel):

    _name = 'colegio_delete'
    _description= 'Borrar Colegio Wizard'

    colegio_id = fields.Many2one('colegio', string='Colegio')

    def unlink_colegio(self):
        if self.colegio_id:
            self.colegio_id.unlink()
        else:
            raise ValidationError('No se ha podido borrar el registro.')