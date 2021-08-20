# coding: utf-8

"""
    APIs RISKAMERICA

    A continuación les presentamos la documentación las **APIs** **de** **RiskAmerica**, el cual es un servicio pagado ofrecido por RiskAmerica que se contrata por separado a nuestras otras ofertas de software.  Algunas consideraciones que debe tener al momento de usar las APIs: - El APIKEY o Token lo puede conseguir solicitándolo al equipo comercial de RiskAmerica - El request necesita ser enviado con el header **Accept:** **application/json** para que responda en formato **JSON** (de no ser enviado con esto se responderá en formato **XML**) - Todos los Servicios son **REST** y sus parametros pueden ser enviados tanto en **POST** como **GET** - El uso de las APIs puede llevar un cobro asociado según se pacte en el acuerdo comercial, por lo que le recomendamos ser cuidadosos en el uso de éstas para evitar sobre-cargos innecesarios. - RiskAmerica funciona con un mecanismo de **WhiteList** **de** **IPs** para las consultas de las API. Para habilitar o modificar la lista de IPs permitidas debe contactarse al mail **contacto@riskamerica.com**. - En caso de usar **Python** como lenguaje de programación puede visitar nuestro SKD disponible en [https://github.com/RiskAmerica/api-client-python](https://github.com/RiskAmerica/api-client-python) .  - En caso de usar otros lenguajes de programación puede usar el proyecto [https://github.com/swagger-api/swagger-codegen/tree/3.0.0](https://github.com/swagger-api/swagger-codegen/tree/3.0.0) para generar su propio SDK a partir del archivo [openapi.json](https://ra-public-files.s3-sa-east-1.amazonaws.com/wide-public/riam-api/openapi.json) . - Todas las APIs funcionan exclusivamente bajo el protocolo HTTPS usando TLS 1.2 o 1.3   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
# Importing related models
from .inline_response20027_message import InlineResponse20027Message




class InlineResponse20027(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'error': 'str',
        'message': 'list[InlineResponse20027Message]'
    }

    attribute_map = {
        'code': 'code',
        'error': 'error',
        'message': 'message'
    }

    def __init__(self, code=None, error=None, message=None):  # noqa: E501
        """InlineResponse20027 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._error = None
        self._message = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if error is not None:
            self.error = error
        if message is not None:
            self.message = message

    @property
    def code(self):
        """Gets the code of this InlineResponse20027.  # noqa: E501

        :return: The code of this InlineResponse20027.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse20027.


        :param code: The code of this InlineResponse20027.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def error(self):
        """Gets the error of this InlineResponse20027.  # noqa: E501

        :return: The error of this InlineResponse20027.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse20027.


        :param error: The error of this InlineResponse20027.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def message(self):
        """Gets the message of this InlineResponse20027.  # noqa: E501

        :return: The message of this InlineResponse20027.  # noqa: E501
        :rtype: list[InlineResponse20027Message]
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse20027.


        :param message: The message of this InlineResponse20027.  # noqa: E501
        :type: list[InlineResponse20027Message]
        """

        self._message = message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse20027, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20027):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
