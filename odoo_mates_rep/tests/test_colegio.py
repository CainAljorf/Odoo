
#Código para evitar tener que instalar el módulo en el entorno python para ejecutar el test.
import logging


from odoo.tests.common import TransactionCase
_logger = logging.getLogger(__name__)

class TestColegio(TransactionCase):

    def setUp(self):
        # Crear registros para el test
        super(TestColegio, self).setUp()
        self.colegio_obj = self.env['colegio']
        self.colegio = self.colegio_obj.create({'name': 'Mi Colegio'})
        _logger.info('Test Record OK')

    def test_crear_colegio(self):
        # Testeamos que se pueda crear un colegio correctamente
        colegio = self.colegio_obj.create({'name': 'Nuevo Colegio'})
        self.assertTrue(colegio)
        _logger.info('Test Create OK')

    def test_editar_colegio(self):
        # Testeamos que se pueda editar el nombre de un colegio correctamente
        self.colegio.write({'name': 'Mi Nuevo Colegio'})
        self.assertEqual(self.colegio.name, 'Mi Nuevo Colegio')
        _logger.info('Test Write OK')

    def test_eliminar_colegio(self):
        # Testeamos que se pueda eliminar un colegio correctamente
        self.colegio.unlink()
        self.colegio_obj.browse(self.colegio.id)
        _logger.info('Test Unlink OK')

# Ejecutar este comando en la terminal para iniciar el test.
# /opt/odoo16/odoo-bin -c /etc/odoo16.conf --test-enable --test-tags=odoo_mates_rep --test-file=/opt/odoo16/custom/odoo_mates_rep/tests/test_colegio.py
