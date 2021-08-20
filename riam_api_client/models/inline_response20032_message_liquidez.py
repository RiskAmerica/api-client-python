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




class InlineResponse20032MessageLiquidez(object):
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
        'fecha': 'date',
        'cantidad_outstanding': 'float',
        'monto_outstanding_clp': 'float',
        'cantidad_trans_mes': 'float',
        'rotacion_mes': 'float',
        'cantidad_trans_trimestre': 'float',
        'rotacion_trimestre': 'float',
        'cantidad_trans_anual': 'float',
        'rotacion_anual': 'float'
    }

    attribute_map = {
        'fecha': 'fecha',
        'cantidad_outstanding': 'cantidadOutstanding',
        'monto_outstanding_clp': 'montoOutstandingCLP',
        'cantidad_trans_mes': 'cantidadTransMes',
        'rotacion_mes': 'rotacionMes',
        'cantidad_trans_trimestre': 'cantidadTransTrimestre',
        'rotacion_trimestre': 'rotacionTrimestre',
        'cantidad_trans_anual': 'cantidadTransAnual',
        'rotacion_anual': 'rotacionAnual'
    }

    def __init__(self, fecha=None, cantidad_outstanding=None, monto_outstanding_clp=None, cantidad_trans_mes=None, rotacion_mes=None, cantidad_trans_trimestre=None, rotacion_trimestre=None, cantidad_trans_anual=None, rotacion_anual=None):  # noqa: E501
        """InlineResponse20032MessageLiquidez - a model defined in Swagger"""  # noqa: E501
        self._fecha = None
        self._cantidad_outstanding = None
        self._monto_outstanding_clp = None
        self._cantidad_trans_mes = None
        self._rotacion_mes = None
        self._cantidad_trans_trimestre = None
        self._rotacion_trimestre = None
        self._cantidad_trans_anual = None
        self._rotacion_anual = None
        self.discriminator = None
        if fecha is not None:
            self.fecha = fecha
        if cantidad_outstanding is not None:
            self.cantidad_outstanding = cantidad_outstanding
        if monto_outstanding_clp is not None:
            self.monto_outstanding_clp = monto_outstanding_clp
        if cantidad_trans_mes is not None:
            self.cantidad_trans_mes = cantidad_trans_mes
        if rotacion_mes is not None:
            self.rotacion_mes = rotacion_mes
        if cantidad_trans_trimestre is not None:
            self.cantidad_trans_trimestre = cantidad_trans_trimestre
        if rotacion_trimestre is not None:
            self.rotacion_trimestre = rotacion_trimestre
        if cantidad_trans_anual is not None:
            self.cantidad_trans_anual = cantidad_trans_anual
        if rotacion_anual is not None:
            self.rotacion_anual = rotacion_anual

    @property
    def fecha(self):
        """Gets the fecha of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Última fecha en custodia  # noqa: E501

        :return: The fecha of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: date
        """
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        """Sets the fecha of this InlineResponse20032MessageLiquidez.

        Última fecha en custodia  # noqa: E501

        :param fecha: The fecha of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: date
        """

        self._fecha = fecha

    @property
    def cantidad_outstanding(self):
        """Gets the cantidad_outstanding of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Saldo custodia  # noqa: E501

        :return: The cantidad_outstanding of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: float
        """
        return self._cantidad_outstanding

    @cantidad_outstanding.setter
    def cantidad_outstanding(self, cantidad_outstanding):
        """Sets the cantidad_outstanding of this InlineResponse20032MessageLiquidez.

        Saldo custodia  # noqa: E501

        :param cantidad_outstanding: The cantidad_outstanding of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: float
        """

        self._cantidad_outstanding = cantidad_outstanding

    @property
    def monto_outstanding_clp(self):
        """Gets the monto_outstanding_clp of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Monto outstanding en pesos  # noqa: E501

        :return: The monto_outstanding_clp of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: float
        """
        return self._monto_outstanding_clp

    @monto_outstanding_clp.setter
    def monto_outstanding_clp(self, monto_outstanding_clp):
        """Sets the monto_outstanding_clp of this InlineResponse20032MessageLiquidez.

        Monto outstanding en pesos  # noqa: E501

        :param monto_outstanding_clp: The monto_outstanding_clp of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: float
        """

        self._monto_outstanding_clp = monto_outstanding_clp

    @property
    def cantidad_trans_mes(self):
        """Gets the cantidad_trans_mes of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Cantidad transada último mes  # noqa: E501

        :return: The cantidad_trans_mes of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: float
        """
        return self._cantidad_trans_mes

    @cantidad_trans_mes.setter
    def cantidad_trans_mes(self, cantidad_trans_mes):
        """Sets the cantidad_trans_mes of this InlineResponse20032MessageLiquidez.

        Cantidad transada último mes  # noqa: E501

        :param cantidad_trans_mes: The cantidad_trans_mes of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: float
        """

        self._cantidad_trans_mes = cantidad_trans_mes

    @property
    def rotacion_mes(self):
        """Gets the rotacion_mes of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Rotación último mes  # noqa: E501

        :return: The rotacion_mes of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: float
        """
        return self._rotacion_mes

    @rotacion_mes.setter
    def rotacion_mes(self, rotacion_mes):
        """Sets the rotacion_mes of this InlineResponse20032MessageLiquidez.

        Rotación último mes  # noqa: E501

        :param rotacion_mes: The rotacion_mes of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: float
        """

        self._rotacion_mes = rotacion_mes

    @property
    def cantidad_trans_trimestre(self):
        """Gets the cantidad_trans_trimestre of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Cantidad transada últimos 3 meses  # noqa: E501

        :return: The cantidad_trans_trimestre of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: float
        """
        return self._cantidad_trans_trimestre

    @cantidad_trans_trimestre.setter
    def cantidad_trans_trimestre(self, cantidad_trans_trimestre):
        """Sets the cantidad_trans_trimestre of this InlineResponse20032MessageLiquidez.

        Cantidad transada últimos 3 meses  # noqa: E501

        :param cantidad_trans_trimestre: The cantidad_trans_trimestre of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: float
        """

        self._cantidad_trans_trimestre = cantidad_trans_trimestre

    @property
    def rotacion_trimestre(self):
        """Gets the rotacion_trimestre of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Rotación últimos 3 meses  # noqa: E501

        :return: The rotacion_trimestre of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: float
        """
        return self._rotacion_trimestre

    @rotacion_trimestre.setter
    def rotacion_trimestre(self, rotacion_trimestre):
        """Sets the rotacion_trimestre of this InlineResponse20032MessageLiquidez.

        Rotación últimos 3 meses  # noqa: E501

        :param rotacion_trimestre: The rotacion_trimestre of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: float
        """

        self._rotacion_trimestre = rotacion_trimestre

    @property
    def cantidad_trans_anual(self):
        """Gets the cantidad_trans_anual of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Cantidad transada último año  # noqa: E501

        :return: The cantidad_trans_anual of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: float
        """
        return self._cantidad_trans_anual

    @cantidad_trans_anual.setter
    def cantidad_trans_anual(self, cantidad_trans_anual):
        """Sets the cantidad_trans_anual of this InlineResponse20032MessageLiquidez.

        Cantidad transada último año  # noqa: E501

        :param cantidad_trans_anual: The cantidad_trans_anual of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: float
        """

        self._cantidad_trans_anual = cantidad_trans_anual

    @property
    def rotacion_anual(self):
        """Gets the rotacion_anual of this InlineResponse20032MessageLiquidez.  # noqa: E501
        Rotación último año  # noqa: E501

        :return: The rotacion_anual of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :rtype: float
        """
        return self._rotacion_anual

    @rotacion_anual.setter
    def rotacion_anual(self, rotacion_anual):
        """Sets the rotacion_anual of this InlineResponse20032MessageLiquidez.

        Rotación último año  # noqa: E501

        :param rotacion_anual: The rotacion_anual of this InlineResponse20032MessageLiquidez.  # noqa: E501
        :type: float
        """

        self._rotacion_anual = rotacion_anual

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
        if issubclass(InlineResponse20032MessageLiquidez, dict):
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
        if not isinstance(other, InlineResponse20032MessageLiquidez):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
