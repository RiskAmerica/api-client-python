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




class InlineResponse20041Message(object):
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
        'id': 'int',
        'rut': 'int',
        'nombre': 'str',
        'identificador_cliente': 'str'
    }

    attribute_map = {
        'id': 'id',
        'rut': 'rut',
        'nombre': 'nombre',
        'identificador_cliente': 'identificadorCliente'
    }

    def __init__(self, id=None, rut=None, nombre=None, identificador_cliente=None):  # noqa: E501
        """InlineResponse20041Message - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._rut = None
        self._nombre = None
        self._identificador_cliente = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if rut is not None:
            self.rut = rut
        if nombre is not None:
            self.nombre = nombre
        if identificador_cliente is not None:
            self.identificador_cliente = identificador_cliente

    @property
    def id(self):
        """Gets the id of this InlineResponse20041Message.  # noqa: E501
        Identificador del fondo  # noqa: E501

        :return: The id of this InlineResponse20041Message.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20041Message.

        Identificador del fondo  # noqa: E501

        :param id: The id of this InlineResponse20041Message.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def rut(self):
        """Gets the rut of this InlineResponse20041Message.  # noqa: E501
        RUT  # noqa: E501

        :return: The rut of this InlineResponse20041Message.  # noqa: E501
        :rtype: int
        """
        return self._rut

    @rut.setter
    def rut(self, rut):
        """Sets the rut of this InlineResponse20041Message.

        RUT  # noqa: E501

        :param rut: The rut of this InlineResponse20041Message.  # noqa: E501
        :type: int
        """

        self._rut = rut

    @property
    def nombre(self):
        """Gets the nombre of this InlineResponse20041Message.  # noqa: E501
        Nombre del fondo  # noqa: E501

        :return: The nombre of this InlineResponse20041Message.  # noqa: E501
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        """Sets the nombre of this InlineResponse20041Message.

        Nombre del fondo  # noqa: E501

        :param nombre: The nombre of this InlineResponse20041Message.  # noqa: E501
        :type: str
        """

        self._nombre = nombre

    @property
    def identificador_cliente(self):
        """Gets the identificador_cliente of this InlineResponse20041Message.  # noqa: E501
        Identificador personalizado  # noqa: E501

        :return: The identificador_cliente of this InlineResponse20041Message.  # noqa: E501
        :rtype: str
        """
        return self._identificador_cliente

    @identificador_cliente.setter
    def identificador_cliente(self, identificador_cliente):
        """Sets the identificador_cliente of this InlineResponse20041Message.

        Identificador personalizado  # noqa: E501

        :param identificador_cliente: The identificador_cliente of this InlineResponse20041Message.  # noqa: E501
        :type: str
        """

        self._identificador_cliente = identificador_cliente

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
        if issubclass(InlineResponse20041Message, dict):
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
        if not isinstance(other, InlineResponse20041Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
