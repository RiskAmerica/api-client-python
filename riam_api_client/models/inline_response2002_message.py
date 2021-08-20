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




class InlineResponse2002Message(object):
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
        'moneda': 'str',
        'fecha': 'date',
        'valor_cuota': 'float',
        'cuotas_aportadas': 'float',
        'cuotas_rescatadas': 'float',
        'cuotas_en_circulacion': 'float',
        'patrimonio_neto': 'float',
        'numero_participes': 'int',
        'numero_participes_institucionales': 'int',
        'gastos_afectos': 'float',
        'gastos_no_afectos': 'float',
        'remuneracion_fija': 'float',
        'remuneracion_variable': 'float',
        'factor_ajuste': 'float',
        'factor_reparto': 'float',
        'activo_total': 'float'
    }

    attribute_map = {
        'rut': 'rut',
        'serie': 'serie',
        'moneda': 'moneda',
        'fecha': 'fecha',
        'valor_cuota': 'valorCuota',
        'cuotas_aportadas': 'cuotasAportadas',
        'cuotas_rescatadas': 'cuotasRescatadas',
        'cuotas_en_circulacion': 'cuotasEnCirculacion',
        'patrimonio_neto': 'patrimonioNeto',
        'numero_participes': 'numeroParticipes',
        'numero_participes_institucionales': 'numeroParticipesInstitucionales',
        'gastos_afectos': 'gastosAfectos',
        'gastos_no_afectos': 'gastosNoAfectos',
        'remuneracion_fija': 'remuneracionFija',
        'remuneracion_variable': 'remuneracionVariable',
        'factor_ajuste': 'factorAjuste',
        'factor_reparto': 'factorReparto',
        'activo_total': 'activoTotal'
    }

    def __init__(self, rut=None, serie=None, moneda=None, fecha=None, valor_cuota=None, cuotas_aportadas=None, cuotas_rescatadas=None, cuotas_en_circulacion=None, patrimonio_neto=None, numero_participes=None, numero_participes_institucionales=None, gastos_afectos=None, gastos_no_afectos=None, remuneracion_fija=None, remuneracion_variable=None, factor_ajuste=None, factor_reparto=None, activo_total=None):  # noqa: E501
        """InlineResponse2002Message - a model defined in Swagger"""  # noqa: E501
        self._rut = None
        self._serie = None
        self._moneda = None
        self._fecha = None
        self._valor_cuota = None
        self._cuotas_aportadas = None
        self._cuotas_rescatadas = None
        self._cuotas_en_circulacion = None
        self._patrimonio_neto = None
        self._numero_participes = None
        self._numero_participes_institucionales = None
        self._gastos_afectos = None
        self._gastos_no_afectos = None
        self._remuneracion_fija = None
        self._remuneracion_variable = None
        self._factor_ajuste = None
        self._factor_reparto = None
        self._activo_total = None
        self.discriminator = None
        if rut is not None:
            self.rut = rut
        if serie is not None:
            self.serie = serie
        if moneda is not None:
            self.moneda = moneda
        if fecha is not None:
            self.fecha = fecha
        if valor_cuota is not None:
            self.valor_cuota = valor_cuota
        if cuotas_aportadas is not None:
            self.cuotas_aportadas = cuotas_aportadas
        if cuotas_rescatadas is not None:
            self.cuotas_rescatadas = cuotas_rescatadas
        if cuotas_en_circulacion is not None:
            self.cuotas_en_circulacion = cuotas_en_circulacion
        if patrimonio_neto is not None:
            self.patrimonio_neto = patrimonio_neto
        if numero_participes is not None:
            self.numero_participes = numero_participes
        if numero_participes_institucionales is not None:
            self.numero_participes_institucionales = numero_participes_institucionales
        if gastos_afectos is not None:
            self.gastos_afectos = gastos_afectos
        if gastos_no_afectos is not None:
            self.gastos_no_afectos = gastos_no_afectos
        if remuneracion_fija is not None:
            self.remuneracion_fija = remuneracion_fija
        if remuneracion_variable is not None:
            self.remuneracion_variable = remuneracion_variable
        if factor_ajuste is not None:
            self.factor_ajuste = factor_ajuste
        if factor_reparto is not None:
            self.factor_reparto = factor_reparto
        if activo_total is not None:
            self.activo_total = activo_total

    @property
    def rut(self):
        """Gets the rut of this InlineResponse2002Message.  # noqa: E501
        Rut del Fondo  # noqa: E501

        :return: The rut of this InlineResponse2002Message.  # noqa: E501
        :rtype: int
        """
        return self._rut

    @rut.setter
    def rut(self, rut):
        """Sets the rut of this InlineResponse2002Message.

        Rut del Fondo  # noqa: E501

        :param rut: The rut of this InlineResponse2002Message.  # noqa: E501
        :type: int
        """

        self._rut = rut

    @property
    def serie(self):
        """Gets the serie of this InlineResponse2002Message.  # noqa: E501
        Código de la serie  # noqa: E501

        :return: The serie of this InlineResponse2002Message.  # noqa: E501
        :rtype: str
        """
        return self._serie

    @serie.setter
    def serie(self, serie):
        """Sets the serie of this InlineResponse2002Message.

        Código de la serie  # noqa: E501

        :param serie: The serie of this InlineResponse2002Message.  # noqa: E501
        :type: str
        """

        self._serie = serie

    @property
    def moneda(self):
        """Gets the moneda of this InlineResponse2002Message.  # noqa: E501
        Moneda en la cual se reportan los valores  # noqa: E501

        :return: The moneda of this InlineResponse2002Message.  # noqa: E501
        :rtype: str
        """
        return self._moneda

    @moneda.setter
    def moneda(self, moneda):
        """Sets the moneda of this InlineResponse2002Message.

        Moneda en la cual se reportan los valores  # noqa: E501

        :param moneda: The moneda of this InlineResponse2002Message.  # noqa: E501
        :type: str
        """

        self._moneda = moneda

    @property
    def fecha(self):
        """Gets the fecha of this InlineResponse2002Message.  # noqa: E501
        Fecha de los valores entregados  # noqa: E501

        :return: The fecha of this InlineResponse2002Message.  # noqa: E501
        :rtype: date
        """
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        """Sets the fecha of this InlineResponse2002Message.

        Fecha de los valores entregados  # noqa: E501

        :param fecha: The fecha of this InlineResponse2002Message.  # noqa: E501
        :type: date
        """

        self._fecha = fecha

    @property
    def valor_cuota(self):
        """Gets the valor_cuota of this InlineResponse2002Message.  # noqa: E501
        Valor cuota  # noqa: E501

        :return: The valor_cuota of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._valor_cuota

    @valor_cuota.setter
    def valor_cuota(self, valor_cuota):
        """Sets the valor_cuota of this InlineResponse2002Message.

        Valor cuota  # noqa: E501

        :param valor_cuota: The valor_cuota of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._valor_cuota = valor_cuota

    @property
    def cuotas_aportadas(self):
        """Gets the cuotas_aportadas of this InlineResponse2002Message.  # noqa: E501
        Cuotas aportadas  # noqa: E501

        :return: The cuotas_aportadas of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._cuotas_aportadas

    @cuotas_aportadas.setter
    def cuotas_aportadas(self, cuotas_aportadas):
        """Sets the cuotas_aportadas of this InlineResponse2002Message.

        Cuotas aportadas  # noqa: E501

        :param cuotas_aportadas: The cuotas_aportadas of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._cuotas_aportadas = cuotas_aportadas

    @property
    def cuotas_rescatadas(self):
        """Gets the cuotas_rescatadas of this InlineResponse2002Message.  # noqa: E501
        Cuotas rescatadas  # noqa: E501

        :return: The cuotas_rescatadas of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._cuotas_rescatadas

    @cuotas_rescatadas.setter
    def cuotas_rescatadas(self, cuotas_rescatadas):
        """Sets the cuotas_rescatadas of this InlineResponse2002Message.

        Cuotas rescatadas  # noqa: E501

        :param cuotas_rescatadas: The cuotas_rescatadas of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._cuotas_rescatadas = cuotas_rescatadas

    @property
    def cuotas_en_circulacion(self):
        """Gets the cuotas_en_circulacion of this InlineResponse2002Message.  # noqa: E501
        Cuotas en circulación  # noqa: E501

        :return: The cuotas_en_circulacion of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._cuotas_en_circulacion

    @cuotas_en_circulacion.setter
    def cuotas_en_circulacion(self, cuotas_en_circulacion):
        """Sets the cuotas_en_circulacion of this InlineResponse2002Message.

        Cuotas en circulación  # noqa: E501

        :param cuotas_en_circulacion: The cuotas_en_circulacion of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._cuotas_en_circulacion = cuotas_en_circulacion

    @property
    def patrimonio_neto(self):
        """Gets the patrimonio_neto of this InlineResponse2002Message.  # noqa: E501
        Patrimonio neto  # noqa: E501

        :return: The patrimonio_neto of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._patrimonio_neto

    @patrimonio_neto.setter
    def patrimonio_neto(self, patrimonio_neto):
        """Sets the patrimonio_neto of this InlineResponse2002Message.

        Patrimonio neto  # noqa: E501

        :param patrimonio_neto: The patrimonio_neto of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._patrimonio_neto = patrimonio_neto

    @property
    def numero_participes(self):
        """Gets the numero_participes of this InlineResponse2002Message.  # noqa: E501
        Número de partícipes  # noqa: E501

        :return: The numero_participes of this InlineResponse2002Message.  # noqa: E501
        :rtype: int
        """
        return self._numero_participes

    @numero_participes.setter
    def numero_participes(self, numero_participes):
        """Sets the numero_participes of this InlineResponse2002Message.

        Número de partícipes  # noqa: E501

        :param numero_participes: The numero_participes of this InlineResponse2002Message.  # noqa: E501
        :type: int
        """

        self._numero_participes = numero_participes

    @property
    def numero_participes_institucionales(self):
        """Gets the numero_participes_institucionales of this InlineResponse2002Message.  # noqa: E501
        Número de partícipes institucionales  # noqa: E501

        :return: The numero_participes_institucionales of this InlineResponse2002Message.  # noqa: E501
        :rtype: int
        """
        return self._numero_participes_institucionales

    @numero_participes_institucionales.setter
    def numero_participes_institucionales(self, numero_participes_institucionales):
        """Sets the numero_participes_institucionales of this InlineResponse2002Message.

        Número de partícipes institucionales  # noqa: E501

        :param numero_participes_institucionales: The numero_participes_institucionales of this InlineResponse2002Message.  # noqa: E501
        :type: int
        """

        self._numero_participes_institucionales = numero_participes_institucionales

    @property
    def gastos_afectos(self):
        """Gets the gastos_afectos of this InlineResponse2002Message.  # noqa: E501
        Gastos afectos  # noqa: E501

        :return: The gastos_afectos of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._gastos_afectos

    @gastos_afectos.setter
    def gastos_afectos(self, gastos_afectos):
        """Sets the gastos_afectos of this InlineResponse2002Message.

        Gastos afectos  # noqa: E501

        :param gastos_afectos: The gastos_afectos of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._gastos_afectos = gastos_afectos

    @property
    def gastos_no_afectos(self):
        """Gets the gastos_no_afectos of this InlineResponse2002Message.  # noqa: E501
        Gastos no afectos  # noqa: E501

        :return: The gastos_no_afectos of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._gastos_no_afectos

    @gastos_no_afectos.setter
    def gastos_no_afectos(self, gastos_no_afectos):
        """Sets the gastos_no_afectos of this InlineResponse2002Message.

        Gastos no afectos  # noqa: E501

        :param gastos_no_afectos: The gastos_no_afectos of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._gastos_no_afectos = gastos_no_afectos

    @property
    def remuneracion_fija(self):
        """Gets the remuneracion_fija of this InlineResponse2002Message.  # noqa: E501
        Remuneración fija  # noqa: E501

        :return: The remuneracion_fija of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._remuneracion_fija

    @remuneracion_fija.setter
    def remuneracion_fija(self, remuneracion_fija):
        """Sets the remuneracion_fija of this InlineResponse2002Message.

        Remuneración fija  # noqa: E501

        :param remuneracion_fija: The remuneracion_fija of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._remuneracion_fija = remuneracion_fija

    @property
    def remuneracion_variable(self):
        """Gets the remuneracion_variable of this InlineResponse2002Message.  # noqa: E501
        Remuneración variable  # noqa: E501

        :return: The remuneracion_variable of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._remuneracion_variable

    @remuneracion_variable.setter
    def remuneracion_variable(self, remuneracion_variable):
        """Sets the remuneracion_variable of this InlineResponse2002Message.

        Remuneración variable  # noqa: E501

        :param remuneracion_variable: The remuneracion_variable of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._remuneracion_variable = remuneracion_variable

    @property
    def factor_ajuste(self):
        """Gets the factor_ajuste of this InlineResponse2002Message.  # noqa: E501
        factor de ajuste  # noqa: E501

        :return: The factor_ajuste of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._factor_ajuste

    @factor_ajuste.setter
    def factor_ajuste(self, factor_ajuste):
        """Sets the factor_ajuste of this InlineResponse2002Message.

        factor de ajuste  # noqa: E501

        :param factor_ajuste: The factor_ajuste of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._factor_ajuste = factor_ajuste

    @property
    def factor_reparto(self):
        """Gets the factor_reparto of this InlineResponse2002Message.  # noqa: E501
        factor de reparto  # noqa: E501

        :return: The factor_reparto of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._factor_reparto

    @factor_reparto.setter
    def factor_reparto(self, factor_reparto):
        """Sets the factor_reparto of this InlineResponse2002Message.

        factor de reparto  # noqa: E501

        :param factor_reparto: The factor_reparto of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._factor_reparto = factor_reparto

    @property
    def activo_total(self):
        """Gets the activo_total of this InlineResponse2002Message.  # noqa: E501
        Activo Total  # noqa: E501

        :return: The activo_total of this InlineResponse2002Message.  # noqa: E501
        :rtype: float
        """
        return self._activo_total

    @activo_total.setter
    def activo_total(self, activo_total):
        """Sets the activo_total of this InlineResponse2002Message.

        Activo Total  # noqa: E501

        :param activo_total: The activo_total of this InlineResponse2002Message.  # noqa: E501
        :type: float
        """

        self._activo_total = activo_total

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
        if issubclass(InlineResponse2002Message, dict):
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
        if not isinstance(other, InlineResponse2002Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
