# coding: utf-8

"""
    APIs RISKAMERICA

    A continuación les presentamos la documentación las **APIs** **de** **RiskAmerica**, el cual es un servicio pagado ofrecido por RiskAmerica que se contrata por separado a nuestras otras ofertas de software.  Algunas consideraciones que debe tener al momento de usar las APIs: - El APIKEY o Token lo puede conseguir solicitándolo al equipo comercial de RiskAmerica - El request necesita ser enviado con el header **Accept:** **application/json** para que responda en formato **JSON** (de no ser enviado con esto se responderá en formato **XML**) - Todos los Servicios son **REST** y sus parametros pueden ser enviados tanto en **POST** como **GET** - El uso de las APIs puede llevar un cobro asociado según se pacte en el acuerdo comercial, por lo que le recomendamos ser cuidadosos en el uso de éstas para evitar sobre-cargos innecesarios. - RiskAmerica funciona con un mecanismo de **WhiteList** **de** **IPs** para las consultas de las API. Para habilitar o modificar la lista de IPs permitidas debe contactarse al mail **contacto@riskamerica.com**. - En caso de usar **Python** como lenguaje de programación puede visitar nuestro SKD disponible en [https://github.com/RiskAmerica/api-client-python](https://github.com/RiskAmerica/api-client-python) .  - En caso de usar otros lenguajes de programación puede usar el proyecto [https://github.com/swagger-api/swagger-codegen/tree/3.0.0](https://github.com/swagger-api/swagger-codegen/tree/3.0.0) para generar su propio SDK a partir del archivo [openapi.json](https://ra-public-files.s3-sa-east-1.amazonaws.com/wide-public/riam-api/openapi.json) . - Todas las APIs funcionan exclusivamente bajo el protocolo HTTPS usando TLS 1.2 o 1.3   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
# Model imports
from . import InlineResponse20037
# Importing for doctring purposes
# Api Client
from riam_api_client.api_client import ApiClient


class RFNCalculadoraApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def r_fn_calculadora_calculadora_calcular_con_tir(self, nemo, fecha, tir, nominal, **kwargs):  # noqa: E501
        """Obtiene la valorización de un instrumento para una tasa dada.  # noqa: E501

        Obtiene la valorización de un instrumento para una tasa dada.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_calculadora_calculadora_calcular_con_tir(nemo, fecha, tir, nominal, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str nemo: Nemotecnico del instrumento a valorizar (required)
        :param date fecha: Fecha para la cual se efectua la valorización (required)
        :param float tir: Tasa usada para valorizar (required)
        :param float nominal: Nominal a valorizar (required)
        :return: InlineResponse20037
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20037 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.r_fn_calculadora_calculadora_calcular_con_tir_with_http_info(nemo, fecha, tir, nominal, **kwargs)  # noqa: E501
        else:
            (data) = self.r_fn_calculadora_calculadora_calcular_con_tir_with_http_info(nemo, fecha, tir, nominal, **kwargs)  # noqa: E501
            return data

    def r_fn_calculadora_calculadora_calcular_con_tir_with_http_info(self, nemo, fecha, tir, nominal, **kwargs):  # noqa: E501
        """Obtiene la valorización de un instrumento para una tasa dada.  # noqa: E501

        Obtiene la valorización de un instrumento para una tasa dada.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_calculadora_calculadora_calcular_con_tir_with_http_info(nemo, fecha, tir, nominal, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str nemo: Nemotecnico del instrumento a valorizar (required)
        :param date fecha: Fecha para la cual se efectua la valorización (required)
        :param float tir: Tasa usada para valorizar (required)
        :param float nominal: Nominal a valorizar (required)
        :return: InlineResponse20037
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20037 | multiprocessing.pool.ApplyResult
        """

        all_params = ['nemo', 'fecha', 'tir', 'nominal']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method r_fn_calculadora_calculadora_calcular_con_tir" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'nemo' is set
        if ('nemo' not in params or
                params['nemo'] is None):
            raise ValueError("Missing the required parameter `nemo` when calling `r_fn_calculadora_calculadora_calcular_con_tir`")  # noqa: E501
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `r_fn_calculadora_calculadora_calcular_con_tir`")  # noqa: E501
        # verify the required parameter 'tir' is set
        if ('tir' not in params or
                params['tir'] is None):
            raise ValueError("Missing the required parameter `tir` when calling `r_fn_calculadora_calculadora_calcular_con_tir`")  # noqa: E501
        # verify the required parameter 'nominal' is set
        if ('nominal' not in params or
                params['nominal'] is None):
            raise ValueError("Missing the required parameter `nominal` when calling `r_fn_calculadora_calculadora_calcular_con_tir`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nemo' in params:
            query_params.append(('nemo', params['nemo']))  # noqa: E501
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501
        if 'tir' in params:
            query_params.append(('tir', params['tir']))  # noqa: E501
        if 'nominal' in params:
            query_params.append(('nominal', params['nominal']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Outputs/Generic/Calculadora/Calculadora/calcularConTir', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20037',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)