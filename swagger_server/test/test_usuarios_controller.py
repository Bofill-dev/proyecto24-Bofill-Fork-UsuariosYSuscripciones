# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.usuario import Usuario  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsuariosController(BaseTestCase):
    """UsuariosController integration test stubs"""

    def test_login_get(self):
        """Test case for login_get

        Iniciar sesión
        """
        query_string = [('username', 'username_example'),
                        ('password', 'password_example')]
        response = self.client.open(
            '/login',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_get(self):
        """Test case for usuarios_get

        Obtener lista de usuarios que se encuentra en la base de datos
        """
        response = self.client.open(
            '/usuarios',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_delete(self):
        """Test case for usuarios_id_delete

        Eliminar un usuario según la ID pasada
        """
        response = self.client.open(
            '/usuarios/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_get(self):
        """Test case for usuarios_id_get

        Obtener un usuario por la ID pasada
        """
        response = self.client.open(
            '/usuarios/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_post(self):
        """Test case for usuarios_post

        Crear un nuevo usuario en la pagina web
        """
        body = Usuario()
        response = self.client.open(
            '/usuarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_put(self):
        """Test case for usuarios_put

        Actualizar un usuario segun la ID pasada en el objeto usuario
        """
        body = Usuario()
        response = self.client.open(
            '/usuarios',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
