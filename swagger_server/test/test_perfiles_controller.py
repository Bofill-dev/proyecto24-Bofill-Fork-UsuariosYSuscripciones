# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.perfil import Perfil  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPerfilesController(BaseTestCase):
    """PerfilesController integration test stubs"""

    def test_usuarios_id_usuario_perfiles_get(self):
        """Test case for usuarios_id_usuario_perfiles_get

        Obtener todos los perfiles asociados a un usuario
        """
        response = self.client.open(
            '/usuarios/{id_usuario}/perfiles'.format(id_usuario=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_perfiles_id_delete(self):
        """Test case for usuarios_perfiles_id_delete

        Eliminar un perfil dada un ID
        """
        response = self.client.open(
            '/usuarios/perfiles/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_perfiles_id_get(self):
        """Test case for usuarios_perfiles_id_get

        Obtener un perfil por la ID del perfil
        """
        response = self.client.open(
            '/usuarios/perfiles/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_perfiles_post(self):
        """Test case for usuarios_perfiles_post

        Crear un perfil de usuario asociado a un usuario
        """
        body = Perfil()
        response = self.client.open(
            '/usuarios/perfiles',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_perfiles_put(self):
        """Test case for usuarios_perfiles_put

        Actualizar un perfil dada la ID del objeto pasado
        """
        body = Perfil()
        response = self.client.open(
            '/usuarios/perfiles',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
