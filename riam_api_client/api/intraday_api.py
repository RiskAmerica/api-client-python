# coding: utf-8

"""
    APIs RISKAMERICA

    A continuación les presentamos la documentación las **APIs** **de** **RiskAmerica**, el cual es un servicio pagado ofrecido por RiskAmerica que se contrata por separado a nuestras otras ofertas de software.  Algunas consideraciones que debe tener al momento de usar las APIs: - El APIKEY o Token lo puede conseguir solicitándolo al equipo comercial de RiskAmerica - El request necesita ser enviado con el header **Accept:** **application/json** para que responda en formato **JSON** (de no ser enviado con esto se responderá en formato **XML**) - Todos los Servicios son **REST** y sus parametros pueden ser enviados tanto en **POST** como **GET** - El uso de las APIs puede llevar un cobro asociado según se pacte en el acuerdo comercial, por lo que le recomendamos ser cuidadosos en el uso de éstas para evitar sobre-cargos innecesarios. - RiskAmerica funciona con un mecanismo de **WhiteList** **de** **IPs** para las consultas de las API. Para habilitar o modificar la lista de IPs permitidas debe contactarse al mail **contacto@riskamerica.com**. - En caso de usar **Python** como lenguaje de programación puede visitar nuestro SDK disponible en [https://github.com/RiskAmerica/api-client-python](https://github.com/RiskAmerica/api-client-python) .  - En caso de usar otros lenguajes de programación puede usar el proyecto [https://github.com/swagger-api/swagger-codegen/tree/3.0.0](https://github.com/swagger-api/swagger-codegen/tree/3.0.0) para generar su propio SDK a partir del archivo [openapi.json](https://ra-public-files.s3-sa-east-1.amazonaws.com/wide-public/riam-api/openapi.json) . - Todas las APIs funcionan exclusivamente bajo el protocolo HTTPS usando TLS 1.2 o 1.3   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
# Model imports
from . import InlineResponse20051
from . import InlineResponse20052
from . import InlineResponse20054
from . import InlineResponse20053
# Importing for doctring purposes
# Api Client
from riam_api_client.api_client import ApiClient


class IntradayApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def intraday_puntas_get_puntas(self, fecha, nemo, **kwargs):  # noqa: E501
        """Obtiene las puntas de un Instrumento para una fecha.  # noqa: E501

        Obtiene las puntas de un Instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intraday_puntas_get_puntas(fecha, nemo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha (required)
        :param str nemo: Nemotécnico del instrumento a consultar. (required)
        :param str tipo_punta: Tipo de punta (Compra - Venta). Si no se especifica se entregan ambos tipos.
        :return: InlineResponse20051
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20051 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.intraday_puntas_get_puntas_with_http_info(fecha, nemo, **kwargs)  # noqa: E501
        else:
            (data) = self.intraday_puntas_get_puntas_with_http_info(fecha, nemo, **kwargs)  # noqa: E501
            return data

    def intraday_puntas_get_puntas_with_http_info(self, fecha, nemo, **kwargs):  # noqa: E501
        """Obtiene las puntas de un Instrumento para una fecha.  # noqa: E501

        Obtiene las puntas de un Instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intraday_puntas_get_puntas_with_http_info(fecha, nemo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha (required)
        :param str nemo: Nemotécnico del instrumento a consultar. (required)
        :param str tipo_punta: Tipo de punta (Compra - Venta). Si no se especifica se entregan ambos tipos.
        :return: InlineResponse20051
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20051 | multiprocessing.pool.ApplyResult
        """

        all_params = ['fecha', 'nemo', 'tipo_punta']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method intraday_puntas_get_puntas" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `intraday_puntas_get_puntas`")  # noqa: E501
        # verify the required parameter 'nemo' is set
        if ('nemo' not in params or
                params['nemo'] is None):
            raise ValueError("Missing the required parameter `nemo` when calling `intraday_puntas_get_puntas`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501
        if 'nemo' in params:
            query_params.append(('nemo', params['nemo']))  # noqa: E501
        if 'tipo_punta' in params:
            query_params.append(('tipoPunta', params['tipo_punta']))  # noqa: E501

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
            '/Outputs/Generic/Intraday/Puntas/getPuntas', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20051',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def intraday_transaccion_intraday_get(self, fecha, **kwargs):  # noqa: E501
        """Obtiene las transacciones Intraday de un instrumento para una fecha.  # noqa: E501

        Obtiene las transacciones Intraday de un instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intraday_transaccion_intraday_get(fecha, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha a consultar (required)
        :param str nemo: Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha.
        :return: InlineResponse20052
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20052 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.intraday_transaccion_intraday_get_with_http_info(fecha, **kwargs)  # noqa: E501
        else:
            (data) = self.intraday_transaccion_intraday_get_with_http_info(fecha, **kwargs)  # noqa: E501
            return data

    def intraday_transaccion_intraday_get_with_http_info(self, fecha, **kwargs):  # noqa: E501
        """Obtiene las transacciones Intraday de un instrumento para una fecha.  # noqa: E501

        Obtiene las transacciones Intraday de un instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intraday_transaccion_intraday_get_with_http_info(fecha, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha a consultar (required)
        :param str nemo: Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha.
        :return: InlineResponse20052
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20052 | multiprocessing.pool.ApplyResult
        """

        all_params = ['fecha', 'nemo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method intraday_transaccion_intraday_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `intraday_transaccion_intraday_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501
        if 'nemo' in params:
            query_params.append(('nemo', params['nemo']))  # noqa: E501

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
            '/Outputs/Generic/Intraday/TransaccionIntraday/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20052',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def intraday_valorizacion_intraday_familia_get(self, fecha, familia, **kwargs):  # noqa: E501
        """Obtiene las valorizaciones Intraday para una familia para una fecha.  # noqa: E501

        Obtiene las valorizaciones Intraday para una familia  para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intraday_valorizacion_intraday_familia_get(fecha, familia, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha a consultar (required)
        :param str familia: familia a consultar. Ejemplo: BE, BB, BS, BCU, etc (required)
        :return: InlineResponse20054
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20054 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.intraday_valorizacion_intraday_familia_get_with_http_info(fecha, familia, **kwargs)  # noqa: E501
        else:
            (data) = self.intraday_valorizacion_intraday_familia_get_with_http_info(fecha, familia, **kwargs)  # noqa: E501
            return data

    def intraday_valorizacion_intraday_familia_get_with_http_info(self, fecha, familia, **kwargs):  # noqa: E501
        """Obtiene las valorizaciones Intraday para una familia para una fecha.  # noqa: E501

        Obtiene las valorizaciones Intraday para una familia  para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intraday_valorizacion_intraday_familia_get_with_http_info(fecha, familia, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha a consultar (required)
        :param str familia: familia a consultar. Ejemplo: BE, BB, BS, BCU, etc (required)
        :return: InlineResponse20054
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20054 | multiprocessing.pool.ApplyResult
        """

        all_params = ['fecha', 'familia']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method intraday_valorizacion_intraday_familia_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `intraday_valorizacion_intraday_familia_get`")  # noqa: E501
        # verify the required parameter 'familia' is set
        if ('familia' not in params or
                params['familia'] is None):
            raise ValueError("Missing the required parameter `familia` when calling `intraday_valorizacion_intraday_familia_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501
        if 'familia' in params:
            query_params.append(('familia', params['familia']))  # noqa: E501

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
            '/Outputs/Generic/Intraday/ValorizacionIntradayFamilia/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20054',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def intraday_valorizacion_intraday_get(self, fecha, nemo, **kwargs):  # noqa: E501
        """Obtiene las valorizaciones Intraday de un Instrumento para una fecha.  # noqa: E501

        Obtiene las valorizaciones Intraday de un Instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intraday_valorizacion_intraday_get(fecha, nemo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha a consultar (required)
        :param str nemo: Nemotécnico del instrumento a consultar (required)
        :return: InlineResponse20053
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20053 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.intraday_valorizacion_intraday_get_with_http_info(fecha, nemo, **kwargs)  # noqa: E501
        else:
            (data) = self.intraday_valorizacion_intraday_get_with_http_info(fecha, nemo, **kwargs)  # noqa: E501
            return data

    def intraday_valorizacion_intraday_get_with_http_info(self, fecha, nemo, **kwargs):  # noqa: E501
        """Obtiene las valorizaciones Intraday de un Instrumento para una fecha.  # noqa: E501

        Obtiene las valorizaciones Intraday de un Instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.intraday_valorizacion_intraday_get_with_http_info(fecha, nemo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha a consultar (required)
        :param str nemo: Nemotécnico del instrumento a consultar (required)
        :return: InlineResponse20053
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20053 | multiprocessing.pool.ApplyResult
        """

        all_params = ['fecha', 'nemo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method intraday_valorizacion_intraday_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `intraday_valorizacion_intraday_get`")  # noqa: E501
        # verify the required parameter 'nemo' is set
        if ('nemo' not in params or
                params['nemo'] is None):
            raise ValueError("Missing the required parameter `nemo` when calling `intraday_valorizacion_intraday_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501
        if 'nemo' in params:
            query_params.append(('nemo', params['nemo']))  # noqa: E501

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
            '/Outputs/Generic/Intraday/ValorizacionIntraday/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20053',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
