# coding: utf-8

"""
    APIs RISKAMERICA

    A continuación les presentamos la documentación las **APIs** **de** **RiskAmerica**, el cual es un servicio pagado ofrecido por RiskAmerica que se contrata por separado a nuestras otras ofertas de software.  Algunas consideraciones que debe tener al momento de usar las APIs: - El APIKEY o Token lo puede conseguir solicitándolo al equipo comercial de RiskAmerica - El request necesita ser enviado con el header **Accept:** **application/json** para que responda en formato **JSON** (de no ser enviado con esto se responderá en formato **XML**) - Todos los Servicios son **REST** y sus parametros pueden ser enviados tanto en **POST** como **GET** - El uso de las APIs puede llevar un cobro asociado según se pacte en el acuerdo comercial, por lo que le recomendamos ser cuidadosos en el uso de éstas para evitar sobre-cargos innecesarios. - RiskAmerica funciona con un mecanismo de **WhiteList** **de** **IPs** para las consultas de las API. Para habilitar o modificar la lista de IPs permitidas debe contactarse al mail **contacto@riskamerica.com**.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import riam_api_client
from riam_api_client.models.inline_response200_message_fondo import InlineResponse200MessageFondo  # noqa: E501
from riam_api_client.rest import ApiException


class TestInlineResponse200MessageFondo(unittest.TestCase):
    """InlineResponse200MessageFondo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse200MessageFondo(self):
        """Test InlineResponse200MessageFondo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = riam_api_client.models.inline_response200_message_fondo.InlineResponse200MessageFondo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
