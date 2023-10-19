from odoo import models, fields

class WizardCrearAula(models.TransientModel):
    _name = 'crear.wizard'
    _description = 'Wizard de prueba'

    colegio_id = fields.Many2one('colegio', string='Colegio')
    aulas_ids = fields.Many2one('aulas', string='Aulas', domain="[('colegio_id','=',colegio_id)]")
    estudiante_id = fields.Many2many('estudiante', string='Estudiante', domain="[('colegio_id','=',colegio_id)]")

    def crear_aulas(self):
        ModeloCrear = self.env['aulas']
        for colegio in self.colegio_id:
            registro = 'Aula para ' + colegio.name
            aulas_existentes = ModeloCrear.search([('name', 'ilike', registro + '%')])
            num_aulas = len(aulas_existentes) + 1
            aula_name = registro + ' ' + str(num_aulas)
            registro = ModeloCrear.create({'name': aula_name, 'colegio_id': colegio.id, 'estudiante_id': self.estudiante_id.id})
        return registro

    def add_estudiantes(self):
        aula = self.aulas_ids
        if aula:
            aula.write({'estudiante_id': [(4, estudiante_id) for estudiante_id in self.estudiante_id.ids]})

        # return{
        #     'type': 'ir.actions.client',
        #     'tag': 'display_notification',
        #     'params': {
        #         'title': 'Cambios completados',
        #         'message': 'Se han agregado los estudiantes a el aula correspondiente.',
        #         'sticky': False,
        #     }
        # }