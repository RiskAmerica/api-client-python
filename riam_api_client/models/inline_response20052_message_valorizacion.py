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




class InlineResponse20052MessageValorizacion(object):
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
        'hora_transaccion': 'str',
        'remate': 'str',
        'tir': 'float',
        'monto_transado_clp': 'float',
        'cantidad': 'float',
        'precio_porcentaje_valor_par': 'float',
        'plazo_residual': 'int',
        'duracion_macaulay': 'float',
        'nemo': 'str'
    }

    attribute_map = {
        'fecha': 'fecha',
        'hora_transaccion': 'horaTransaccion',
        'remate': 'remate',
        'tir': 'tir',
        'monto_transado_clp': 'montoTransadoCLP',
        'cantidad': 'cantidad',
        'precio_porcentaje_valor_par': 'precioPorcentajeValorPar',
        'plazo_residual': 'plazoResidual',
        'duracion_macaulay': 'duracionMacaulay',
        'nemo': 'nemo'
    }

    def __init__(self, fecha=None, hora_transaccion=None, remate=None, tir=None, monto_transado_clp=None, cantidad=None, precio_porcentaje_valor_par=None, plazo_residual=None, duracion_macaulay=None, nemo=None):  # noqa: E501
        """InlineResponse20052MessageValorizacion - a model defined in Swagger"""  # noqa: E501
        self._fecha = None
        self._hora_transaccion = None
        self._remate = None
        self._tir = None
        self._monto_transado_clp = None
        self._cantidad = None
        self._precio_porcentaje_valor_par = None
        self._plazo_residual = None
        self._duracion_macaulay = None
        self._nemo = None
        self.discriminator = None
        if fecha is not None:
            self.fecha = fecha
        if hora_transaccion is not None:
            self.hora_transaccion = hora_transaccion
        if remate is not None:
            self.remate = remate
        if tir is not None:
            self.tir = tir
        if monto_transado_clp is not None:
            self.monto_transado_clp = monto_transado_clp
        if cantidad is not None:
            self.cantidad = cantidad
        if precio_porcentaje_valor_par is not None:
            self.precio_porcentaje_valor_par = precio_porcentaje_valor_par
        if plazo_residual is not None:
            self.plazo_residual = plazo_residual
        if duracion_macaulay is not None:
            self.duracion_macaulay = duracion_macaulay
        if nemo is not None:
            self.nemo = nemo

    @property
    def fecha(self):
        """Gets the fecha of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Fecha de la Valorización  # noqa: E501

        :return: The fecha of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: date
        """
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        """Sets the fecha of this InlineResponse20052MessageValorizacion.

        Fecha de la Valorización  # noqa: E501

        :param fecha: The fecha of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: date
        """

        self._fecha = fecha

    @property
    def hora_transaccion(self):
        """Gets the hora_transaccion of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Hora de la transaccion  # noqa: E501

        :return: The hora_transaccion of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: str
        """
        return self._hora_transaccion

    @hora_transaccion.setter
    def hora_transaccion(self, hora_transaccion):
        """Sets the hora_transaccion of this InlineResponse20052MessageValorizacion.

        Hora de la transaccion  # noqa: E501

        :param hora_transaccion: The hora_transaccion of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: str
        """

        self._hora_transaccion = hora_transaccion

    @property
    def remate(self):
        """Gets the remate of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Remate  # noqa: E501

        :return: The remate of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: str
        """
        return self._remate

    @remate.setter
    def remate(self, remate):
        """Sets the remate of this InlineResponse20052MessageValorizacion.

        Remate  # noqa: E501

        :param remate: The remate of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: str
        """

        self._remate = remate

    @property
    def tir(self):
        """Gets the tir of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Tir de la transacción  # noqa: E501

        :return: The tir of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._tir

    @tir.setter
    def tir(self, tir):
        """Sets the tir of this InlineResponse20052MessageValorizacion.

        Tir de la transacción  # noqa: E501

        :param tir: The tir of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._tir = tir

    @property
    def monto_transado_clp(self):
        """Gets the monto_transado_clp of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Monto Transado en Pesos  # noqa: E501

        :return: The monto_transado_clp of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._monto_transado_clp

    @monto_transado_clp.setter
    def monto_transado_clp(self, monto_transado_clp):
        """Sets the monto_transado_clp of this InlineResponse20052MessageValorizacion.

        Monto Transado en Pesos  # noqa: E501

        :param monto_transado_clp: The monto_transado_clp of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._monto_transado_clp = monto_transado_clp

    @property
    def cantidad(self):
        """Gets the cantidad of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Cantidad Transada  # noqa: E501

        :return: The cantidad of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        """Sets the cantidad of this InlineResponse20052MessageValorizacion.

        Cantidad Transada  # noqa: E501

        :param cantidad: The cantidad of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._cantidad = cantidad

    @property
    def precio_porcentaje_valor_par(self):
        """Gets the precio_porcentaje_valor_par of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Precio Porcentaje Valor Par  # noqa: E501

        :return: The precio_porcentaje_valor_par of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._precio_porcentaje_valor_par

    @precio_porcentaje_valor_par.setter
    def precio_porcentaje_valor_par(self, precio_porcentaje_valor_par):
        """Sets the precio_porcentaje_valor_par of this InlineResponse20052MessageValorizacion.

        Precio Porcentaje Valor Par  # noqa: E501

        :param precio_porcentaje_valor_par: The precio_porcentaje_valor_par of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._precio_porcentaje_valor_par = precio_porcentaje_valor_par

    @property
    def plazo_residual(self):
        """Gets the plazo_residual of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Días al vencimiento  # noqa: E501

        :return: The plazo_residual of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: int
        """
        return self._plazo_residual

    @plazo_residual.setter
    def plazo_residual(self, plazo_residual):
        """Sets the plazo_residual of this InlineResponse20052MessageValorizacion.

        Días al vencimiento  # noqa: E501

        :param plazo_residual: The plazo_residual of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: int
        """

        self._plazo_residual = plazo_residual

    @property
    def duracion_macaulay(self):
        """Gets the duracion_macaulay of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Duración de Macaulay  # noqa: E501

        :return: The duracion_macaulay of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._duracion_macaulay

    @duracion_macaulay.setter
    def duracion_macaulay(self, duracion_macaulay):
        """Sets the duracion_macaulay of this InlineResponse20052MessageValorizacion.

        Duración de Macaulay  # noqa: E501

        :param duracion_macaulay: The duracion_macaulay of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._duracion_macaulay = duracion_macaulay

    @property
    def nemo(self):
        """Gets the nemo of this InlineResponse20052MessageValorizacion.  # noqa: E501
        Nemotécnico del instrumento  # noqa: E501

        :return: The nemo of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :rtype: str
        """
        return self._nemo

    @nemo.setter
    def nemo(self, nemo):
        """Sets the nemo of this InlineResponse20052MessageValorizacion.

        Nemotécnico del instrumento  # noqa: E501

        :param nemo: The nemo of this InlineResponse20052MessageValorizacion.  # noqa: E501
        :type: str
        """

        self._nemo = nemo

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
        if issubclass(InlineResponse20052MessageValorizacion, dict):
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
        if not isinstance(other, InlineResponse20052MessageValorizacion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other