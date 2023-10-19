from odoo import models, fields
from odoo.exceptions import ValidationError

class ampa_delete(models.TransientModel):

    _name = 'ampa_delete'
    _description= 'Borrar AMPA Wizard'

    ampa_ids = fields.Many2one('ampa', string='AMPA')

    def unlink_ampa(self):
        if self.ampa_ids:
            self.ampa_ids.unlink()
        else:
            raise ValidationError('No se ha podido borrar el registro.')