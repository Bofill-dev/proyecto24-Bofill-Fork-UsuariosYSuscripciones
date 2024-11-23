# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.suscripcion import Suscripcion  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSuscripcionesController(BaseTestCase):
    """SuscripcionesController integration test stubs"""

    def test_suscripciones_id_subscription_delete(self):
        """Test case for suscripciones_id_subscription_delete

        Eliminar una suscripción de usuario
        """
        response = self.client.open(
            '/suscripciones/{id_subscription}'.format(id_subscription=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suscripciones_id_subscription_get(self):
        """Test case for suscripciones_id_subscription_get

        Obtener las suscripciones de un usuario
        """
        response = self.client.open(
            '/suscripciones/{id_subscription}'.format(id_subscription=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suscripciones_post(self):
        """Test case for suscripciones_post

        Crear una nueva suscripción de usuario
        """
        body = Suscripcion()
        response = self.client.open(
            '/suscripciones',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_suscripciones_put(self):
        """Test case for suscripciones_put

        Actualizar los detalles de la suscripción de usuario
        """
        body = Suscripcion()
        response = self.client.open(
            '/suscripciones',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_usuario_suscripcion_get(self):
        """Test case for usuarios_id_usuario_suscripcion_get

        Obtener el nombre del plan de suscripción de un usuario
        """
        response = self.client.open(
            '/usuarios/{id_usuario}/suscripcion'.format(id_usuario=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuarios_id_usuario_suscripcion_post(self):
        """Test case for usuarios_id_usuario_suscripcion_post

        Crear una nueva suscripción para un usuario
        """
        body = Suscripcion()
        response = self.client.open(
            '/usuarios/{id_usuario}/suscripcion'.format(id_usuario=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
