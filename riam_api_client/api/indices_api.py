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
from . import InlineResponse20010
from . import InlineResponse2009
from . import InlineResponse2008
from . import InlineResponse20011
from . import InlineResponse20012
from . import InlineResponse20012
# Importing for doctring purposes
# Api Client
from riam_api_client.api_client import ApiClient


class IndicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def indices_informacion_get_dias_con_retorno(self, **kwargs):  # noqa: E501
        """Obtiene los posibles dias con retorno de los índices.  # noqa: E501

        Obtiene el listado de todos los posibles días con retornos y su identificador.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_informacion_get_dias_con_retorno(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20010 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.indices_informacion_get_dias_con_retorno_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.indices_informacion_get_dias_con_retorno_with_http_info(**kwargs)  # noqa: E501
            return data

    def indices_informacion_get_dias_con_retorno_with_http_info(self, **kwargs):  # noqa: E501
        """Obtiene los posibles dias con retorno de los índices.  # noqa: E501

        Obtiene el listado de todos los posibles días con retornos y su identificador.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_informacion_get_dias_con_retorno_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20010 | multiprocessing.pool.ApplyResult
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method indices_informacion_get_dias_con_retorno" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/Outputs/Generic/Indices/Informacion/getDiasConRetorno', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20010',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def indices_informacion_get_grupos(self, **kwargs):  # noqa: E501
        """Obtiene el listado de grupos sobre los cuales se clasifican los índices.  # noqa: E501

        Obtiene el listado de grupos sobre los cuales se clasifican los índices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_informacion_get_grupos(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2009 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.indices_informacion_get_grupos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.indices_informacion_get_grupos_with_http_info(**kwargs)  # noqa: E501
            return data

    def indices_informacion_get_grupos_with_http_info(self, **kwargs):  # noqa: E501
        """Obtiene el listado de grupos sobre los cuales se clasifican los índices.  # noqa: E501

        Obtiene el listado de grupos sobre los cuales se clasifican los índices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_informacion_get_grupos_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2009 | multiprocessing.pool.ApplyResult
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method indices_informacion_get_grupos" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/Outputs/Generic/Indices/Informacion/getGrupos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def indices_informacion_get_indices(self, **kwargs):  # noqa: E501
        """Obtiene el listado de índices disponibles para consultar.  # noqa: E501

        Obtiene el listado de índices disponibles para consultar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_informacion_get_indices(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2008 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.indices_informacion_get_indices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.indices_informacion_get_indices_with_http_info(**kwargs)  # noqa: E501
            return data

    def indices_informacion_get_indices_with_http_info(self, **kwargs):  # noqa: E501
        """Obtiene el listado de índices disponibles para consultar.  # noqa: E501

        Obtiene el listado de índices disponibles para consultar.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_informacion_get_indices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2008 | multiprocessing.pool.ApplyResult
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method indices_informacion_get_indices" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/Outputs/Generic/Indices/Informacion/getIndices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def indices_ponderacion_get(self, id_indice, fecha, **kwargs):  # noqa: E501
        """Obtiene las ponderaciones de los instrumentos que componen un Índice.  # noqa: E501

        Obtiene las ponderaciones de los instrumentos que componen un Índice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_ponderacion_get(id_indice, fecha, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id_indice: Id del Índice a consultar (required)
        :param date fecha: Fecha a consultar (required)
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20011 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.indices_ponderacion_get_with_http_info(id_indice, fecha, **kwargs)  # noqa: E501
        else:
            (data) = self.indices_ponderacion_get_with_http_info(id_indice, fecha, **kwargs)  # noqa: E501
            return data

    def indices_ponderacion_get_with_http_info(self, id_indice, fecha, **kwargs):  # noqa: E501
        """Obtiene las ponderaciones de los instrumentos que componen un Índice.  # noqa: E501

        Obtiene las ponderaciones de los instrumentos que componen un Índice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_ponderacion_get_with_http_info(id_indice, fecha, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id_indice: Id del Índice a consultar (required)
        :param date fecha: Fecha a consultar (required)
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20011 | multiprocessing.pool.ApplyResult
        """

        all_params = ['id_indice', 'fecha']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method indices_ponderacion_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_indice' is set
        if ('id_indice' not in params or
                params['id_indice'] is None):
            raise ValueError("Missing the required parameter `id_indice` when calling `indices_ponderacion_get`")  # noqa: E501
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `indices_ponderacion_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id_indice' in params:
            query_params.append(('idIndice', params['id_indice']))  # noqa: E501
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501

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
            '/Outputs/Generic/Indices/Ponderacion/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def indices_retorno_get_fecha(self, fecha, id_indice, **kwargs):  # noqa: E501
        """Obtiene el valor de los retornos de un Índice para una fecha.  # noqa: E501

        Obtiene el valor de los retornos de un Índice para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_retorno_get_fecha(fecha, id_indice, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Límite inferior del intervalo de fechas a consultar (required)
        :param str id_indice: ID del índice a consultar. Se pueden especificar varios separando por 'pipes' (ASCII 124). IE: 5 (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20012 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.indices_retorno_get_fecha_with_http_info(fecha, id_indice, **kwargs)  # noqa: E501
        else:
            (data) = self.indices_retorno_get_fecha_with_http_info(fecha, id_indice, **kwargs)  # noqa: E501
            return data

    def indices_retorno_get_fecha_with_http_info(self, fecha, id_indice, **kwargs):  # noqa: E501
        """Obtiene el valor de los retornos de un Índice para una fecha.  # noqa: E501

        Obtiene el valor de los retornos de un Índice para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_retorno_get_fecha_with_http_info(fecha, id_indice, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Límite inferior del intervalo de fechas a consultar (required)
        :param str id_indice: ID del índice a consultar. Se pueden especificar varios separando por 'pipes' (ASCII 124). IE: 5 (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20012 | multiprocessing.pool.ApplyResult
        """

        all_params = ['fecha', 'id_indice']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method indices_retorno_get_fecha" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `indices_retorno_get_fecha`")  # noqa: E501
        # verify the required parameter 'id_indice' is set
        if ('id_indice' not in params or
                params['id_indice'] is None):
            raise ValueError("Missing the required parameter `id_indice` when calling `indices_retorno_get_fecha`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501
        if 'id_indice' in params:
            query_params.append(('idIndice', params['id_indice']))  # noqa: E501

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
            '/Outputs/Generic/Indices/Retorno/getFecha', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def indices_retorno_get_interval(self, fecha_min, fecha_max, id_indice, **kwargs):  # noqa: E501
        """Obtiene el valor de los retornos de un Índice para un intervalo de fechas.  # noqa: E501

        Obtiene el valor de los retornos de un Índice para un intervalo de fechas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_retorno_get_interval(fecha_min, fecha_max, id_indice, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha_min: Límite inferior del intervalo de fechas a consultar (required)
        :param date fecha_max: Límite superior del intervalo de fechas a consultar (required)
        :param int id_indice: Id del Índice a consultar. (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20012 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.indices_retorno_get_interval_with_http_info(fecha_min, fecha_max, id_indice, **kwargs)  # noqa: E501
        else:
            (data) = self.indices_retorno_get_interval_with_http_info(fecha_min, fecha_max, id_indice, **kwargs)  # noqa: E501
            return data

    def indices_retorno_get_interval_with_http_info(self, fecha_min, fecha_max, id_indice, **kwargs):  # noqa: E501
        """Obtiene el valor de los retornos de un Índice para un intervalo de fechas.  # noqa: E501

        Obtiene el valor de los retornos de un Índice para un intervalo de fechas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.indices_retorno_get_interval_with_http_info(fecha_min, fecha_max, id_indice, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha_min: Límite inferior del intervalo de fechas a consultar (required)
        :param date fecha_max: Límite superior del intervalo de fechas a consultar (required)
        :param int id_indice: Id del Índice a consultar. (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20012 | multiprocessing.pool.ApplyResult
        """

        all_params = ['fecha_min', 'fecha_max', 'id_indice']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method indices_retorno_get_interval" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha_min' is set
        if ('fecha_min' not in params or
                params['fecha_min'] is None):
            raise ValueError("Missing the required parameter `fecha_min` when calling `indices_retorno_get_interval`")  # noqa: E501
        # verify the required parameter 'fecha_max' is set
        if ('fecha_max' not in params or
                params['fecha_max'] is None):
            raise ValueError("Missing the required parameter `fecha_max` when calling `indices_retorno_get_interval`")  # noqa: E501
        # verify the required parameter 'id_indice' is set
        if ('id_indice' not in params or
                params['id_indice'] is None):
            raise ValueError("Missing the required parameter `id_indice` when calling `indices_retorno_get_interval`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha_min' in params:
            query_params.append(('fechaMin', params['fecha_min']))  # noqa: E501
        if 'fecha_max' in params:
            query_params.append(('fechaMax', params['fecha_max']))  # noqa: E501
        if 'id_indice' in params:
            query_params.append(('idIndice', params['id_indice']))  # noqa: E501

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
            '/Outputs/Generic/Indices/Retorno/getInterval', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
