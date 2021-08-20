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




class InlineResponse20037MessageValorizacion(object):
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
        'nemo': 'str',
        'fecha': 'date',
        'nominal': 'int',
        'tasa': 'float',
        'ppv_par': 'float',
        'valor_par': 'float',
        'duracion': 'float',
        'plazo_residual': 'float',
        'convexidad': 'float',
        'monto': 'float',
        'monto_clp': 'float'
    }

    attribute_map = {
        'nemo': 'nemo',
        'fecha': 'fecha',
        'nominal': 'nominal',
        'tasa': 'tasa',
        'ppv_par': 'PPVPar',
        'valor_par': 'valorPar',
        'duracion': 'duracion',
        'plazo_residual': 'plazoResidual',
        'convexidad': 'convexidad',
        'monto': 'monto',
        'monto_clp': 'montoCLP'
    }

    def __init__(self, nemo=None, fecha=None, nominal=None, tasa=None, ppv_par=None, valor_par=None, duracion=None, plazo_residual=None, convexidad=None, monto=None, monto_clp=None):  # noqa: E501
        """InlineResponse20037MessageValorizacion - a model defined in Swagger"""  # noqa: E501
        self._nemo = None
        self._fecha = None
        self._nominal = None
        self._tasa = None
        self._ppv_par = None
        self._valor_par = None
        self._duracion = None
        self._plazo_residual = None
        self._convexidad = None
        self._monto = None
        self._monto_clp = None
        self.discriminator = None
        if nemo is not None:
            self.nemo = nemo
        if fecha is not None:
            self.fecha = fecha
        if nominal is not None:
            self.nominal = nominal
        if tasa is not None:
            self.tasa = tasa
        if ppv_par is not None:
            self.ppv_par = ppv_par
        if valor_par is not None:
            self.valor_par = valor_par
        if duracion is not None:
            self.duracion = duracion
        if plazo_residual is not None:
            self.plazo_residual = plazo_residual
        if convexidad is not None:
            self.convexidad = convexidad
        if monto is not None:
            self.monto = monto
        if monto_clp is not None:
            self.monto_clp = monto_clp

    @property
    def nemo(self):
        """Gets the nemo of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Nemotecnico Valorizado  # noqa: E501

        :return: The nemo of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: str
        """
        return self._nemo

    @nemo.setter
    def nemo(self, nemo):
        """Sets the nemo of this InlineResponse20037MessageValorizacion.

        Nemotecnico Valorizado  # noqa: E501

        :param nemo: The nemo of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: str
        """

        self._nemo = nemo

    @property
    def fecha(self):
        """Gets the fecha of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Fecha para la cual se efectuó la valorización  # noqa: E501

        :return: The fecha of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: date
        """
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        """Sets the fecha of this InlineResponse20037MessageValorizacion.

        Fecha para la cual se efectuó la valorización  # noqa: E501

        :param fecha: The fecha of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: date
        """

        self._fecha = fecha

    @property
    def nominal(self):
        """Gets the nominal of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Nominal usado para la valorización  # noqa: E501

        :return: The nominal of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: int
        """
        return self._nominal

    @nominal.setter
    def nominal(self, nominal):
        """Sets the nominal of this InlineResponse20037MessageValorizacion.

        Nominal usado para la valorización  # noqa: E501

        :param nominal: The nominal of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: int
        """

        self._nominal = nominal

    @property
    def tasa(self):
        """Gets the tasa of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Tasa usada para la valorización  # noqa: E501

        :return: The tasa of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._tasa

    @tasa.setter
    def tasa(self, tasa):
        """Sets the tasa of this InlineResponse20037MessageValorizacion.

        Tasa usada para la valorización  # noqa: E501

        :param tasa: The tasa of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._tasa = tasa

    @property
    def ppv_par(self):
        """Gets the ppv_par of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Precio como porcentaje del Valor Par  # noqa: E501

        :return: The ppv_par of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._ppv_par

    @ppv_par.setter
    def ppv_par(self, ppv_par):
        """Sets the ppv_par of this InlineResponse20037MessageValorizacion.

        Precio como porcentaje del Valor Par  # noqa: E501

        :param ppv_par: The ppv_par of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._ppv_par = ppv_par

    @property
    def valor_par(self):
        """Gets the valor_par of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Valor Par  # noqa: E501

        :return: The valor_par of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._valor_par

    @valor_par.setter
    def valor_par(self, valor_par):
        """Sets the valor_par of this InlineResponse20037MessageValorizacion.

        Valor Par  # noqa: E501

        :param valor_par: The valor_par of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._valor_par = valor_par

    @property
    def duracion(self):
        """Gets the duracion of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Duración Macaulay del Instrumento  # noqa: E501

        :return: The duracion of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        """Sets the duracion of this InlineResponse20037MessageValorizacion.

        Duración Macaulay del Instrumento  # noqa: E501

        :param duracion: The duracion of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._duracion = duracion

    @property
    def plazo_residual(self):
        """Gets the plazo_residual of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Plazo al vencimiento en años del Instrumento  # noqa: E501

        :return: The plazo_residual of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._plazo_residual

    @plazo_residual.setter
    def plazo_residual(self, plazo_residual):
        """Sets the plazo_residual of this InlineResponse20037MessageValorizacion.

        Plazo al vencimiento en años del Instrumento  # noqa: E501

        :param plazo_residual: The plazo_residual of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._plazo_residual = plazo_residual

    @property
    def convexidad(self):
        """Gets the convexidad of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Convexidad del Instrumento  # noqa: E501

        :return: The convexidad of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._convexidad

    @convexidad.setter
    def convexidad(self, convexidad):
        """Sets the convexidad of this InlineResponse20037MessageValorizacion.

        Convexidad del Instrumento  # noqa: E501

        :param convexidad: The convexidad of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._convexidad = convexidad

    @property
    def monto(self):
        """Gets the monto of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Valorización en la moneda del Instrumento  # noqa: E501

        :return: The monto of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._monto

    @monto.setter
    def monto(self, monto):
        """Sets the monto of this InlineResponse20037MessageValorizacion.

        Valorización en la moneda del Instrumento  # noqa: E501

        :param monto: The monto of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._monto = monto

    @property
    def monto_clp(self):
        """Gets the monto_clp of this InlineResponse20037MessageValorizacion.  # noqa: E501
        Valorización en pesos del Instrumento  # noqa: E501

        :return: The monto_clp of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :rtype: float
        """
        return self._monto_clp

    @monto_clp.setter
    def monto_clp(self, monto_clp):
        """Sets the monto_clp of this InlineResponse20037MessageValorizacion.

        Valorización en pesos del Instrumento  # noqa: E501

        :param monto_clp: The monto_clp of this InlineResponse20037MessageValorizacion.  # noqa: E501
        :type: float
        """

        self._monto_clp = monto_clp

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
        if issubclass(InlineResponse20037MessageValorizacion, dict):
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
        if not isinstance(other, InlineResponse20037MessageValorizacion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
