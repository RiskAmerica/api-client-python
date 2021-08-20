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




class InlineResponse20026MessageInstrumento(object):
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
        'nemotecnico': 'str',
        'familia': 'str',
        'tipo': 'str',
        'tipo_svs': 'str',
        'emisor': 'str',
        'sector': 'str',
        'riesgo': 'str',
        'moneda': 'str',
        'fecha_emision': 'date',
        'fecha_vencimiento': 'date',
        'fecha_primera_transaccion': 'date',
        'fecha_prepagable': 'date',
        'periodicidad': 'str',
        'numero_cupones': 'str',
        'tasa_emision': 'float',
        'condicion_prepago': 'str',
        'tera': 'float',
        'base_tasa': 'str',
        'monto_emitido': 'int',
        'nominal_outstanding': 'float',
        'corte_maximo': 'int',
        'corte_minimo': 'int',
        'spread_colocacion': 'float'
    }

    attribute_map = {
        'nemotecnico': 'nemotecnico',
        'familia': 'familia',
        'tipo': 'tipo',
        'tipo_svs': 'tipoSVS',
        'emisor': 'emisor',
        'sector': 'sector',
        'riesgo': 'riesgo',
        'moneda': 'moneda',
        'fecha_emision': 'fechaEmision',
        'fecha_vencimiento': 'fechaVencimiento',
        'fecha_primera_transaccion': 'fechaPrimeraTransaccion',
        'fecha_prepagable': 'fechaPrepagable',
        'periodicidad': 'periodicidad',
        'numero_cupones': 'numeroCupones',
        'tasa_emision': 'tasaEmision',
        'condicion_prepago': 'condicionPrepago',
        'tera': 'tera',
        'base_tasa': 'baseTasa',
        'monto_emitido': 'montoEmitido',
        'nominal_outstanding': 'nominalOutstanding',
        'corte_maximo': 'corteMaximo',
        'corte_minimo': 'corteMinimo',
        'spread_colocacion': 'spreadColocacion'
    }

    def __init__(self, nemotecnico=None, familia=None, tipo=None, tipo_svs=None, emisor=None, sector=None, riesgo=None, moneda=None, fecha_emision=None, fecha_vencimiento=None, fecha_primera_transaccion=None, fecha_prepagable=None, periodicidad=None, numero_cupones=None, tasa_emision=None, condicion_prepago=None, tera=None, base_tasa=None, monto_emitido=None, nominal_outstanding=None, corte_maximo=None, corte_minimo=None, spread_colocacion=None):  # noqa: E501
        """InlineResponse20026MessageInstrumento - a model defined in Swagger"""  # noqa: E501
        self._nemotecnico = None
        self._familia = None
        self._tipo = None
        self._tipo_svs = None
        self._emisor = None
        self._sector = None
        self._riesgo = None
        self._moneda = None
        self._fecha_emision = None
        self._fecha_vencimiento = None
        self._fecha_primera_transaccion = None
        self._fecha_prepagable = None
        self._periodicidad = None
        self._numero_cupones = None
        self._tasa_emision = None
        self._condicion_prepago = None
        self._tera = None
        self._base_tasa = None
        self._monto_emitido = None
        self._nominal_outstanding = None
        self._corte_maximo = None
        self._corte_minimo = None
        self._spread_colocacion = None
        self.discriminator = None
        if nemotecnico is not None:
            self.nemotecnico = nemotecnico
        if familia is not None:
            self.familia = familia
        if tipo is not None:
            self.tipo = tipo
        if tipo_svs is not None:
            self.tipo_svs = tipo_svs
        if emisor is not None:
            self.emisor = emisor
        if sector is not None:
            self.sector = sector
        if riesgo is not None:
            self.riesgo = riesgo
        if moneda is not None:
            self.moneda = moneda
        if fecha_emision is not None:
            self.fecha_emision = fecha_emision
        if fecha_vencimiento is not None:
            self.fecha_vencimiento = fecha_vencimiento
        if fecha_primera_transaccion is not None:
            self.fecha_primera_transaccion = fecha_primera_transaccion
        if fecha_prepagable is not None:
            self.fecha_prepagable = fecha_prepagable
        if periodicidad is not None:
            self.periodicidad = periodicidad
        if numero_cupones is not None:
            self.numero_cupones = numero_cupones
        if tasa_emision is not None:
            self.tasa_emision = tasa_emision
        if condicion_prepago is not None:
            self.condicion_prepago = condicion_prepago
        if tera is not None:
            self.tera = tera
        if base_tasa is not None:
            self.base_tasa = base_tasa
        if monto_emitido is not None:
            self.monto_emitido = monto_emitido
        if nominal_outstanding is not None:
            self.nominal_outstanding = nominal_outstanding
        if corte_maximo is not None:
            self.corte_maximo = corte_maximo
        if corte_minimo is not None:
            self.corte_minimo = corte_minimo
        if spread_colocacion is not None:
            self.spread_colocacion = spread_colocacion

    @property
    def nemotecnico(self):
        """Gets the nemotecnico of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Nemotécnico del instrumento  # noqa: E501

        :return: The nemotecnico of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._nemotecnico

    @nemotecnico.setter
    def nemotecnico(self, nemotecnico):
        """Sets the nemotecnico of this InlineResponse20026MessageInstrumento.

        Nemotécnico del instrumento  # noqa: E501

        :param nemotecnico: The nemotecnico of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._nemotecnico = nemotecnico

    @property
    def familia(self):
        """Gets the familia of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Familia del instrumento  # noqa: E501

        :return: The familia of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._familia

    @familia.setter
    def familia(self, familia):
        """Sets the familia of this InlineResponse20026MessageInstrumento.

        Familia del instrumento  # noqa: E501

        :param familia: The familia of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._familia = familia

    @property
    def tipo(self):
        """Gets the tipo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Tipo del instrumento según notación RiskAmerica  # noqa: E501

        :return: The tipo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        """Sets the tipo of this InlineResponse20026MessageInstrumento.

        Tipo del instrumento según notación RiskAmerica  # noqa: E501

        :param tipo: The tipo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._tipo = tipo

    @property
    def tipo_svs(self):
        """Gets the tipo_svs of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Tipo del instrumento según notación SVS  # noqa: E501

        :return: The tipo_svs of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._tipo_svs

    @tipo_svs.setter
    def tipo_svs(self, tipo_svs):
        """Sets the tipo_svs of this InlineResponse20026MessageInstrumento.

        Tipo del instrumento según notación SVS  # noqa: E501

        :param tipo_svs: The tipo_svs of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._tipo_svs = tipo_svs

    @property
    def emisor(self):
        """Gets the emisor of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Emisor del instrumento  # noqa: E501

        :return: The emisor of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._emisor

    @emisor.setter
    def emisor(self, emisor):
        """Sets the emisor of this InlineResponse20026MessageInstrumento.

        Emisor del instrumento  # noqa: E501

        :param emisor: The emisor of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._emisor = emisor

    @property
    def sector(self):
        """Gets the sector of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Sector del instrumento  # noqa: E501

        :return: The sector of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._sector

    @sector.setter
    def sector(self, sector):
        """Sets the sector of this InlineResponse20026MessageInstrumento.

        Sector del instrumento  # noqa: E501

        :param sector: The sector of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._sector = sector

    @property
    def riesgo(self):
        """Gets the riesgo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Clasificación de riesgo mínima del instrumento  # noqa: E501

        :return: The riesgo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._riesgo

    @riesgo.setter
    def riesgo(self, riesgo):
        """Sets the riesgo of this InlineResponse20026MessageInstrumento.

        Clasificación de riesgo mínima del instrumento  # noqa: E501

        :param riesgo: The riesgo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._riesgo = riesgo

    @property
    def moneda(self):
        """Gets the moneda of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Moneda de Reajuste  # noqa: E501

        :return: The moneda of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._moneda

    @moneda.setter
    def moneda(self, moneda):
        """Sets the moneda of this InlineResponse20026MessageInstrumento.

        Moneda de Reajuste  # noqa: E501

        :param moneda: The moneda of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._moneda = moneda

    @property
    def fecha_emision(self):
        """Gets the fecha_emision of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Fecha de emisión  # noqa: E501

        :return: The fecha_emision of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: date
        """
        return self._fecha_emision

    @fecha_emision.setter
    def fecha_emision(self, fecha_emision):
        """Sets the fecha_emision of this InlineResponse20026MessageInstrumento.

        Fecha de emisión  # noqa: E501

        :param fecha_emision: The fecha_emision of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: date
        """

        self._fecha_emision = fecha_emision

    @property
    def fecha_vencimiento(self):
        """Gets the fecha_vencimiento of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Fecha de vencimiento  # noqa: E501

        :return: The fecha_vencimiento of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: date
        """
        return self._fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha_vencimiento):
        """Sets the fecha_vencimiento of this InlineResponse20026MessageInstrumento.

        Fecha de vencimiento  # noqa: E501

        :param fecha_vencimiento: The fecha_vencimiento of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: date
        """

        self._fecha_vencimiento = fecha_vencimiento

    @property
    def fecha_primera_transaccion(self):
        """Gets the fecha_primera_transaccion of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Fecha de primera transacción  # noqa: E501

        :return: The fecha_primera_transaccion of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: date
        """
        return self._fecha_primera_transaccion

    @fecha_primera_transaccion.setter
    def fecha_primera_transaccion(self, fecha_primera_transaccion):
        """Sets the fecha_primera_transaccion of this InlineResponse20026MessageInstrumento.

        Fecha de primera transacción  # noqa: E501

        :param fecha_primera_transaccion: The fecha_primera_transaccion of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: date
        """

        self._fecha_primera_transaccion = fecha_primera_transaccion

    @property
    def fecha_prepagable(self):
        """Gets the fecha_prepagable of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Fecha a partir de la que se puede prepagar el instrumento  # noqa: E501

        :return: The fecha_prepagable of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: date
        """
        return self._fecha_prepagable

    @fecha_prepagable.setter
    def fecha_prepagable(self, fecha_prepagable):
        """Sets the fecha_prepagable of this InlineResponse20026MessageInstrumento.

        Fecha a partir de la que se puede prepagar el instrumento  # noqa: E501

        :param fecha_prepagable: The fecha_prepagable of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: date
        """

        self._fecha_prepagable = fecha_prepagable

    @property
    def periodicidad(self):
        """Gets the periodicidad of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Periodicidad de pago de cupones  # noqa: E501

        :return: The periodicidad of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._periodicidad

    @periodicidad.setter
    def periodicidad(self, periodicidad):
        """Sets the periodicidad of this InlineResponse20026MessageInstrumento.

        Periodicidad de pago de cupones  # noqa: E501

        :param periodicidad: The periodicidad of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._periodicidad = periodicidad

    @property
    def numero_cupones(self):
        """Gets the numero_cupones of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Número de cupones  # noqa: E501

        :return: The numero_cupones of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._numero_cupones

    @numero_cupones.setter
    def numero_cupones(self, numero_cupones):
        """Sets the numero_cupones of this InlineResponse20026MessageInstrumento.

        Número de cupones  # noqa: E501

        :param numero_cupones: The numero_cupones of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._numero_cupones = numero_cupones

    @property
    def tasa_emision(self):
        """Gets the tasa_emision of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Tasa de emisión  # noqa: E501

        :return: The tasa_emision of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: float
        """
        return self._tasa_emision

    @tasa_emision.setter
    def tasa_emision(self, tasa_emision):
        """Sets the tasa_emision of this InlineResponse20026MessageInstrumento.

        Tasa de emisión  # noqa: E501

        :param tasa_emision: The tasa_emision of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: float
        """

        self._tasa_emision = tasa_emision

    @property
    def condicion_prepago(self):
        """Gets the condicion_prepago of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Condición de prepago  # noqa: E501

        :return: The condicion_prepago of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._condicion_prepago

    @condicion_prepago.setter
    def condicion_prepago(self, condicion_prepago):
        """Sets the condicion_prepago of this InlineResponse20026MessageInstrumento.

        Condición de prepago  # noqa: E501

        :param condicion_prepago: The condicion_prepago of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._condicion_prepago = condicion_prepago

    @property
    def tera(self):
        """Gets the tera of this InlineResponse20026MessageInstrumento.  # noqa: E501
        TERA  # noqa: E501

        :return: The tera of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: float
        """
        return self._tera

    @tera.setter
    def tera(self, tera):
        """Sets the tera of this InlineResponse20026MessageInstrumento.

        TERA  # noqa: E501

        :param tera: The tera of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: float
        """

        self._tera = tera

    @property
    def base_tasa(self):
        """Gets the base_tasa of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Base de las tasas  # noqa: E501

        :return: The base_tasa of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: str
        """
        return self._base_tasa

    @base_tasa.setter
    def base_tasa(self, base_tasa):
        """Sets the base_tasa of this InlineResponse20026MessageInstrumento.

        Base de las tasas  # noqa: E501

        :param base_tasa: The base_tasa of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: str
        """

        self._base_tasa = base_tasa

    @property
    def monto_emitido(self):
        """Gets the monto_emitido of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Monto de Emisión  # noqa: E501

        :return: The monto_emitido of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: int
        """
        return self._monto_emitido

    @monto_emitido.setter
    def monto_emitido(self, monto_emitido):
        """Sets the monto_emitido of this InlineResponse20026MessageInstrumento.

        Monto de Emisión  # noqa: E501

        :param monto_emitido: The monto_emitido of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: int
        """

        self._monto_emitido = monto_emitido

    @property
    def nominal_outstanding(self):
        """Gets the nominal_outstanding of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Monto Outstanding  # noqa: E501

        :return: The nominal_outstanding of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: float
        """
        return self._nominal_outstanding

    @nominal_outstanding.setter
    def nominal_outstanding(self, nominal_outstanding):
        """Sets the nominal_outstanding of this InlineResponse20026MessageInstrumento.

        Monto Outstanding  # noqa: E501

        :param nominal_outstanding: The nominal_outstanding of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: float
        """

        self._nominal_outstanding = nominal_outstanding

    @property
    def corte_maximo(self):
        """Gets the corte_maximo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Corte Máximo  # noqa: E501

        :return: The corte_maximo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: int
        """
        return self._corte_maximo

    @corte_maximo.setter
    def corte_maximo(self, corte_maximo):
        """Sets the corte_maximo of this InlineResponse20026MessageInstrumento.

        Corte Máximo  # noqa: E501

        :param corte_maximo: The corte_maximo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: int
        """

        self._corte_maximo = corte_maximo

    @property
    def corte_minimo(self):
        """Gets the corte_minimo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Corte Mínimo  # noqa: E501

        :return: The corte_minimo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: int
        """
        return self._corte_minimo

    @corte_minimo.setter
    def corte_minimo(self, corte_minimo):
        """Sets the corte_minimo of this InlineResponse20026MessageInstrumento.

        Corte Mínimo  # noqa: E501

        :param corte_minimo: The corte_minimo of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: int
        """

        self._corte_minimo = corte_minimo

    @property
    def spread_colocacion(self):
        """Gets the spread_colocacion of this InlineResponse20026MessageInstrumento.  # noqa: E501
        Spread de colocación  # noqa: E501

        :return: The spread_colocacion of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :rtype: float
        """
        return self._spread_colocacion

    @spread_colocacion.setter
    def spread_colocacion(self, spread_colocacion):
        """Sets the spread_colocacion of this InlineResponse20026MessageInstrumento.

        Spread de colocación  # noqa: E501

        :param spread_colocacion: The spread_colocacion of this InlineResponse20026MessageInstrumento.  # noqa: E501
        :type: float
        """

        self._spread_colocacion = spread_colocacion

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
        if issubclass(InlineResponse20026MessageInstrumento, dict):
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
        if not isinstance(other, InlineResponse20026MessageInstrumento):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other