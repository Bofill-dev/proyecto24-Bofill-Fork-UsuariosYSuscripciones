# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.plan import Plan  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPlanesController(BaseTestCase):
    """PlanesController integration test stubs"""

    def test_planes_get(self):
        """Test case for planes_get

        Obtener lista de planes de suscripción que se enucuentren en la base de datos
        """
        response = self.client.open(
            '/planes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_planes_id_plan_delete(self):
        """Test case for planes_id_plan_delete

        Eliminar una suscripción por ID
        """
        response = self.client.open(
            '/planes/{id_plan}'.format(id_plan=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_planes_post(self):
        """Test case for planes_post

        Crear un nuevo plan de suscripción
        """
        body = Plan()
        response = self.client.open(
            '/planes',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_planes_put(self):
        """Test case for planes_put

        Actualizar una suscripción existente por ID
        """
        body = Plan()
        response = self.client.open(
            '/planes',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
