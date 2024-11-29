# coding: utf-8

"""
    APIs RISKAMERICA

    A continuación les presentamos la documentación las **APIs** **de** **RiskAmerica**, el cual es un servicio pagado ofrecido por RiskAmerica que se contrata por separado a nuestras otras ofertas de software.  Algunas consideraciones que debe tener al momento de usar las APIs: - El APIKEY o Token lo puede conseguir solicitándolo al equipo comercial de RiskAmerica - El request necesita ser enviado con el header **Accept:** **application/json** para que responda en formato **JSON** (de no ser enviado con esto se responderá en formato **XML**) - Todos los Servicios son **REST** y sus parametros pueden ser enviados tanto en **POST** como **GET** - El uso de las APIs puede llevar un cobro asociado según se pacte en el acuerdo comercial, por lo que le recomendamos ser cuidadosos en el uso de éstas para evitar sobre-cargos innecesarios. - RiskAmerica funciona con un mecanismo de **WhiteList** **de** **IPs** para las consultas de las API. Para habilitar o modificar la lista de IPs permitidas debe contactarse al mail **contacto@riskamerica.com**. - En caso de usar **Python** como lenguaje de programación puede visitar nuestro SDK disponible en [https://github.com/RiskAmerica/api-client-python](https://github.com/RiskAmerica/api-client-python) .  - En caso de usar otros lenguajes de programación puede usar el proyecto [https://github.com/swagger-api/swagger-codegen/tree/3.0.0](https://github.com/swagger-api/swagger-codegen/tree/3.0.0) para generar su propio SDK a partir del archivo [openapi.json](https://ra-public-files.s3-sa-east-1.amazonaws.com/wide-public/riam-api/openapi.json) . - Todas las APIs funcionan exclusivamente bajo el protocolo HTTPS usando TLS 1.2 o 1.3   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
# Importing related models




class InlineResponse2007Message(object):
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
        'rut': 'int',
        'serie': 'str',
        'fecha': 'date',
        'tir_rfnclp': 'float',
        'tir_rfnuf': 'float'
    }

    attribute_map = {
        'rut': 'rut',
        'serie': 'serie',
        'fecha': 'fecha',
        'tir_rfnclp': 'tirRFNCLP',
        'tir_rfnuf': 'tirRFNUF'
    }

    def __init__(self, rut=None, serie=None, fecha=None, tir_rfnclp=None, tir_rfnuf=None):  # noqa: E501
        """InlineResponse2007Message - a model defined in Swagger"""  # noqa: E501
        self._rut = None
        self._serie = None
        self._fecha = None
        self._tir_rfnclp = None
        self._tir_rfnuf = None
        self.discriminator = None
        if rut is not None:
            self.rut = rut
        if serie is not None:
            self.serie = serie
        if fecha is not None:
            self.fecha = fecha
        if tir_rfnclp is not None:
            self.tir_rfnclp = tir_rfnclp
        if tir_rfnuf is not None:
            self.tir_rfnuf = tir_rfnuf

    @property
    def rut(self):
        """Gets the rut of this InlineResponse2007Message.  # noqa: E501
        Rut del Fondo (sin dígito verificador)  # noqa: E501

        :return: The rut of this InlineResponse2007Message.  # noqa: E501
        :rtype: int
        """
        return self._rut

    @rut.setter
    def rut(self, rut):
        """Sets the rut of this InlineResponse2007Message.

        Rut del Fondo (sin dígito verificador)  # noqa: E501

        :param rut: The rut of this InlineResponse2007Message.  # noqa: E501
        :type: int
        """

        self._rut = rut

    @property
    def serie(self):
        """Gets the serie of this InlineResponse2007Message.  # noqa: E501
        Código de la serie  # noqa: E501

        :return: The serie of this InlineResponse2007Message.  # noqa: E501
        :rtype: str
        """
        return self._serie

    @serie.setter
    def serie(self, serie):
        """Sets the serie of this InlineResponse2007Message.

        Código de la serie  # noqa: E501

        :param serie: The serie of this InlineResponse2007Message.  # noqa: E501
        :type: str
        """

        self._serie = serie

    @property
    def fecha(self):
        """Gets the fecha of this InlineResponse2007Message.  # noqa: E501
        Fecha de los valores entregados  # noqa: E501

        :return: The fecha of this InlineResponse2007Message.  # noqa: E501
        :rtype: date
        """
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        """Sets the fecha of this InlineResponse2007Message.

        Fecha de los valores entregados  # noqa: E501

        :param fecha: The fecha of this InlineResponse2007Message.  # noqa: E501
        :type: date
        """

        self._fecha = fecha

    @property
    def tir_rfnclp(self):
        """Gets the tir_rfnclp of this InlineResponse2007Message.  # noqa: E501
        TIR RFN en Pesos  # noqa: E501

        :return: The tir_rfnclp of this InlineResponse2007Message.  # noqa: E501
        :rtype: float
        """
        return self._tir_rfnclp

    @tir_rfnclp.setter
    def tir_rfnclp(self, tir_rfnclp):
        """Sets the tir_rfnclp of this InlineResponse2007Message.

        TIR RFN en Pesos  # noqa: E501

        :param tir_rfnclp: The tir_rfnclp of this InlineResponse2007Message.  # noqa: E501
        :type: float
        """

        self._tir_rfnclp = tir_rfnclp

    @property
    def tir_rfnuf(self):
        """Gets the tir_rfnuf of this InlineResponse2007Message.  # noqa: E501
        TIR RFN en UF  # noqa: E501

        :return: The tir_rfnuf of this InlineResponse2007Message.  # noqa: E501
        :rtype: float
        """
        return self._tir_rfnuf

    @tir_rfnuf.setter
    def tir_rfnuf(self, tir_rfnuf):
        """Sets the tir_rfnuf of this InlineResponse2007Message.

        TIR RFN en UF  # noqa: E501

        :param tir_rfnuf: The tir_rfnuf of this InlineResponse2007Message.  # noqa: E501
        :type: float
        """

        self._tir_rfnuf = tir_rfnuf

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
        if issubclass(InlineResponse2007Message, dict):
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
        if not isinstance(other, InlineResponse2007Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
