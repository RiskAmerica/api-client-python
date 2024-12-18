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
from . import InlineResponse20013
from . import InlineResponse20014
from . import InlineResponse20016
from . import InlineResponse20015
from . import InlineResponse20017
from . import InlineResponse20017
from . import InlineResponse20017
# Importing for doctring purposes
# Api Client
from riam_api_client.api_client import ApiClient


class CurvasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def curvas_informacion_get_curvas(self, **kwargs):  # noqa: E501
        """Obtiene el listado de curvas disponibles para consultar.  # noqa: E501

        Obtiene el listado de curvas disponibles para consultar. Es importante destacar que esto incluye tanto curvas públicas como otras curvas personalizadas a las que el usuario tenga acceso.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_informacion_get_curvas(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20013 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.curvas_informacion_get_curvas_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.curvas_informacion_get_curvas_with_http_info(**kwargs)  # noqa: E501
            return data

    def curvas_informacion_get_curvas_with_http_info(self, **kwargs):  # noqa: E501
        """Obtiene el listado de curvas disponibles para consultar.  # noqa: E501

        Obtiene el listado de curvas disponibles para consultar. Es importante destacar que esto incluye tanto curvas públicas como otras curvas personalizadas a las que el usuario tenga acceso.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_informacion_get_curvas_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20013 | multiprocessing.pool.ApplyResult
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
                    " to method curvas_informacion_get_curvas" % key
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
            '/Outputs/Generic/Curvas/Informacion/getCurvas', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def curvas_informacion_get_familias(self, **kwargs):  # noqa: E501
        """Obtiene el listado de familias sobre los cuales se clasifican las curvas.  # noqa: E501

        Obtiene el listado de familias sobre los cuales se clasifican las curvas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_informacion_get_familias(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20014 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.curvas_informacion_get_familias_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.curvas_informacion_get_familias_with_http_info(**kwargs)  # noqa: E501
            return data

    def curvas_informacion_get_familias_with_http_info(self, **kwargs):  # noqa: E501
        """Obtiene el listado de familias sobre los cuales se clasifican las curvas.  # noqa: E501

        Obtiene el listado de familias sobre los cuales se clasifican las curvas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_informacion_get_familias_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20014 | multiprocessing.pool.ApplyResult
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
                    " to method curvas_informacion_get_familias" % key
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
            '/Outputs/Generic/Curvas/Informacion/getFamilias', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def curvas_informacion_get_intradays(self, **kwargs):  # noqa: E501
        """Obtiene el listado de Intradays disponibles.  # noqa: E501

        Obtiene el listado de Intradays disponibles. Cabe destacar que el Intraday 10 es el que se usa para la valorización oficial de RiskAmerica.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_informacion_get_intradays(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20016 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.curvas_informacion_get_intradays_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.curvas_informacion_get_intradays_with_http_info(**kwargs)  # noqa: E501
            return data

    def curvas_informacion_get_intradays_with_http_info(self, **kwargs):  # noqa: E501
        """Obtiene el listado de Intradays disponibles.  # noqa: E501

        Obtiene el listado de Intradays disponibles. Cabe destacar que el Intraday 10 es el que se usa para la valorización oficial de RiskAmerica.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_informacion_get_intradays_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20016 | multiprocessing.pool.ApplyResult
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
                    " to method curvas_informacion_get_intradays" % key
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
            '/Outputs/Generic/Curvas/Informacion/getIntradays', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20016',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def curvas_informacion_get_unidad_tiempo(self, **kwargs):  # noqa: E501
        """Obtiene el listado de unidades de tiempo que se usan para consultar las curvas.  # noqa: E501

        Obtiene el listado de unidades de tiempo que se usan para consultar las curvas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_informacion_get_unidad_tiempo(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20015
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20015 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.curvas_informacion_get_unidad_tiempo_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.curvas_informacion_get_unidad_tiempo_with_http_info(**kwargs)  # noqa: E501
            return data

    def curvas_informacion_get_unidad_tiempo_with_http_info(self, **kwargs):  # noqa: E501
        """Obtiene el listado de unidades de tiempo que se usan para consultar las curvas.  # noqa: E501

        Obtiene el listado de unidades de tiempo que se usan para consultar las curvas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_informacion_get_unidad_tiempo_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20015
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20015 | multiprocessing.pool.ApplyResult
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
                    " to method curvas_informacion_get_unidad_tiempo" % key
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
            '/Outputs/Generic/Curvas/Informacion/getUnidadTiempo', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20015',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def curvas_valores_get(self, body, fecha, id_curva, id_intraday, **kwargs):  # noqa: E501
        """Obtiene los valores de una curva para los plazos solicitados.  # noqa: E501

        Obtiene los valores de una curva para los plazos solicitados.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_valores_get(body, fecha, id_curva, id_intraday, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValoresGetBody body: (required)
        :param date fecha: Fecha para la cual se consulta (required)
        :param str id_curva: Identificador de la Curva (required)
        :param int id_intraday: Identificador del Intraday para el cual se consulta (required)
        :param str id_unidad: Unidad en la que estan los plazos provistos, las opciones posibles son DIA, MES, ANIO
        :param str id_base_tasa: Tasa Base en la que se consultan los valores
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20017 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.curvas_valores_get_with_http_info(body, fecha, id_curva, id_intraday, **kwargs)  # noqa: E501
        else:
            (data) = self.curvas_valores_get_with_http_info(body, fecha, id_curva, id_intraday, **kwargs)  # noqa: E501
            return data

    def curvas_valores_get_with_http_info(self, body, fecha, id_curva, id_intraday, **kwargs):  # noqa: E501
        """Obtiene los valores de una curva para los plazos solicitados.  # noqa: E501

        Obtiene los valores de una curva para los plazos solicitados.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_valores_get_with_http_info(body, fecha, id_curva, id_intraday, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValoresGetBody body: (required)
        :param date fecha: Fecha para la cual se consulta (required)
        :param str id_curva: Identificador de la Curva (required)
        :param int id_intraday: Identificador del Intraday para el cual se consulta (required)
        :param str id_unidad: Unidad en la que estan los plazos provistos, las opciones posibles son DIA, MES, ANIO
        :param str id_base_tasa: Tasa Base en la que se consultan los valores
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20017 | multiprocessing.pool.ApplyResult
        """

        all_params = ['body', 'fecha', 'id_curva', 'id_intraday', 'id_unidad', 'id_base_tasa']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method curvas_valores_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `curvas_valores_get`")  # noqa: E501
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `curvas_valores_get`")  # noqa: E501
        # verify the required parameter 'id_curva' is set
        if ('id_curva' not in params or
                params['id_curva'] is None):
            raise ValueError("Missing the required parameter `id_curva` when calling `curvas_valores_get`")  # noqa: E501
        # verify the required parameter 'id_intraday' is set
        if ('id_intraday' not in params or
                params['id_intraday'] is None):
            raise ValueError("Missing the required parameter `id_intraday` when calling `curvas_valores_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501
        if 'id_curva' in params:
            query_params.append(('idCurva', params['id_curva']))  # noqa: E501
        if 'id_unidad' in params:
            query_params.append(('idUnidad', params['id_unidad']))  # noqa: E501
        if 'id_base_tasa' in params:
            query_params.append(('idBaseTasa', params['id_base_tasa']))  # noqa: E501
        if 'id_intraday' in params:
            query_params.append(('idIntraday', params['id_intraday']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/Outputs/Generic/Curvas/Valores/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def curvas_valores_get_all(self, fecha, id_curva, plazo_inicial, plazo_final, id_intraday, **kwargs):  # noqa: E501
        """Obtiene todos los valores de una curva para todos los plazos comprendidos entre el plazo minimo y el maximo.  # noqa: E501

        Obtiene todos los valores de una curva para todos los plazos comprendidos entre el plazo minimo y el maximo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_valores_get_all(fecha, id_curva, plazo_inicial, plazo_final, id_intraday, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha para la cual se consulta (required)
        :param str id_curva: Identificador de la Curva (required)
        :param float plazo_inicial: Plazo inicial a consultar en la base consultada (required)
        :param float plazo_final: Plazo final a consultar en la base consultada (required)
        :param int id_intraday: Identificador del Intraday para el cual se consulta (required)
        :param str id_unidad: Unidad en la que estan los plazos provistos, las opciones posibles son DIA, MES, ANIO
        :param str id_base_tasa: Tasa Base en la que se consultan los valores
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20017 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.curvas_valores_get_all_with_http_info(fecha, id_curva, plazo_inicial, plazo_final, id_intraday, **kwargs)  # noqa: E501
        else:
            (data) = self.curvas_valores_get_all_with_http_info(fecha, id_curva, plazo_inicial, plazo_final, id_intraday, **kwargs)  # noqa: E501
            return data

    def curvas_valores_get_all_with_http_info(self, fecha, id_curva, plazo_inicial, plazo_final, id_intraday, **kwargs):  # noqa: E501
        """Obtiene todos los valores de una curva para todos los plazos comprendidos entre el plazo minimo y el maximo.  # noqa: E501

        Obtiene todos los valores de una curva para todos los plazos comprendidos entre el plazo minimo y el maximo.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_valores_get_all_with_http_info(fecha, id_curva, plazo_inicial, plazo_final, id_intraday, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Fecha para la cual se consulta (required)
        :param str id_curva: Identificador de la Curva (required)
        :param float plazo_inicial: Plazo inicial a consultar en la base consultada (required)
        :param float plazo_final: Plazo final a consultar en la base consultada (required)
        :param int id_intraday: Identificador del Intraday para el cual se consulta (required)
        :param str id_unidad: Unidad en la que estan los plazos provistos, las opciones posibles son DIA, MES, ANIO
        :param str id_base_tasa: Tasa Base en la que se consultan los valores
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20017 | multiprocessing.pool.ApplyResult
        """

        all_params = ['fecha', 'id_curva', 'plazo_inicial', 'plazo_final', 'id_intraday', 'id_unidad', 'id_base_tasa']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method curvas_valores_get_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `curvas_valores_get_all`")  # noqa: E501
        # verify the required parameter 'id_curva' is set
        if ('id_curva' not in params or
                params['id_curva'] is None):
            raise ValueError("Missing the required parameter `id_curva` when calling `curvas_valores_get_all`")  # noqa: E501
        # verify the required parameter 'plazo_inicial' is set
        if ('plazo_inicial' not in params or
                params['plazo_inicial'] is None):
            raise ValueError("Missing the required parameter `plazo_inicial` when calling `curvas_valores_get_all`")  # noqa: E501
        # verify the required parameter 'plazo_final' is set
        if ('plazo_final' not in params or
                params['plazo_final'] is None):
            raise ValueError("Missing the required parameter `plazo_final` when calling `curvas_valores_get_all`")  # noqa: E501
        # verify the required parameter 'id_intraday' is set
        if ('id_intraday' not in params or
                params['id_intraday'] is None):
            raise ValueError("Missing the required parameter `id_intraday` when calling `curvas_valores_get_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha' in params:
            query_params.append(('fecha', params['fecha']))  # noqa: E501
        if 'id_curva' in params:
            query_params.append(('idCurva', params['id_curva']))  # noqa: E501
        if 'plazo_inicial' in params:
            query_params.append(('plazoInicial', params['plazo_inicial']))  # noqa: E501
        if 'plazo_final' in params:
            query_params.append(('plazoFinal', params['plazo_final']))  # noqa: E501
        if 'id_unidad' in params:
            query_params.append(('idUnidad', params['id_unidad']))  # noqa: E501
        if 'id_base_tasa' in params:
            query_params.append(('idBaseTasa', params['id_base_tasa']))  # noqa: E501
        if 'id_intraday' in params:
            query_params.append(('idIntraday', params['id_intraday']))  # noqa: E501

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
            '/Outputs/Generic/Curvas/Valores/getAll', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def curvas_valores_get_interval(self, fecha_min, fecha_max, id_curva, plazo, id_unidad, id_base_tasa, id_intraday, **kwargs):  # noqa: E501
        """Obtiene los valores de una curva para las fechas solicitadas a un plazo fijo.  # noqa: E501

        Obtiene los valores de una curva para las fechas solicitadas a un plazo fijo, RESTRICCIÓN: El intervalo de fechas debe ser menor a 365 días.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_valores_get_interval(fecha_min, fecha_max, id_curva, plazo, id_unidad, id_base_tasa, id_intraday, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha_min: Intervalo inferior de fecha para la que se consulta (required)
        :param date fecha_max: Intervalo superior de fecha para la que se consulta (required)
        :param str id_curva: Identificador de la Curva (required)
        :param float plazo: Plazos a consultar (required)
        :param str id_unidad: Unidad en la que estan los plazos provistos (required)
        :param str id_base_tasa: Tasa Base en la que se consultan los valores (required)
        :param int id_intraday: Identificador del Intraday para el cual se consulta (required)
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20017 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.curvas_valores_get_interval_with_http_info(fecha_min, fecha_max, id_curva, plazo, id_unidad, id_base_tasa, id_intraday, **kwargs)  # noqa: E501
        else:
            (data) = self.curvas_valores_get_interval_with_http_info(fecha_min, fecha_max, id_curva, plazo, id_unidad, id_base_tasa, id_intraday, **kwargs)  # noqa: E501
            return data

    def curvas_valores_get_interval_with_http_info(self, fecha_min, fecha_max, id_curva, plazo, id_unidad, id_base_tasa, id_intraday, **kwargs):  # noqa: E501
        """Obtiene los valores de una curva para las fechas solicitadas a un plazo fijo.  # noqa: E501

        Obtiene los valores de una curva para las fechas solicitadas a un plazo fijo, RESTRICCIÓN: El intervalo de fechas debe ser menor a 365 días.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.curvas_valores_get_interval_with_http_info(fecha_min, fecha_max, id_curva, plazo, id_unidad, id_base_tasa, id_intraday, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha_min: Intervalo inferior de fecha para la que se consulta (required)
        :param date fecha_max: Intervalo superior de fecha para la que se consulta (required)
        :param str id_curva: Identificador de la Curva (required)
        :param float plazo: Plazos a consultar (required)
        :param str id_unidad: Unidad en la que estan los plazos provistos (required)
        :param str id_base_tasa: Tasa Base en la que se consultan los valores (required)
        :param int id_intraday: Identificador del Intraday para el cual se consulta (required)
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20017 | multiprocessing.pool.ApplyResult
        """

        all_params = ['fecha_min', 'fecha_max', 'id_curva', 'plazo', 'id_unidad', 'id_base_tasa', 'id_intraday']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method curvas_valores_get_interval" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha_min' is set
        if ('fecha_min' not in params or
                params['fecha_min'] is None):
            raise ValueError("Missing the required parameter `fecha_min` when calling `curvas_valores_get_interval`")  # noqa: E501
        # verify the required parameter 'fecha_max' is set
        if ('fecha_max' not in params or
                params['fecha_max'] is None):
            raise ValueError("Missing the required parameter `fecha_max` when calling `curvas_valores_get_interval`")  # noqa: E501
        # verify the required parameter 'id_curva' is set
        if ('id_curva' not in params or
                params['id_curva'] is None):
            raise ValueError("Missing the required parameter `id_curva` when calling `curvas_valores_get_interval`")  # noqa: E501
        # verify the required parameter 'plazo' is set
        if ('plazo' not in params or
                params['plazo'] is None):
            raise ValueError("Missing the required parameter `plazo` when calling `curvas_valores_get_interval`")  # noqa: E501
        # verify the required parameter 'id_unidad' is set
        if ('id_unidad' not in params or
                params['id_unidad'] is None):
            raise ValueError("Missing the required parameter `id_unidad` when calling `curvas_valores_get_interval`")  # noqa: E501
        # verify the required parameter 'id_base_tasa' is set
        if ('id_base_tasa' not in params or
                params['id_base_tasa'] is None):
            raise ValueError("Missing the required parameter `id_base_tasa` when calling `curvas_valores_get_interval`")  # noqa: E501
        # verify the required parameter 'id_intraday' is set
        if ('id_intraday' not in params or
                params['id_intraday'] is None):
            raise ValueError("Missing the required parameter `id_intraday` when calling `curvas_valores_get_interval`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fecha_min' in params:
            query_params.append(('fechaMin', params['fecha_min']))  # noqa: E501
        if 'fecha_max' in params:
            query_params.append(('fechaMax', params['fecha_max']))  # noqa: E501
        if 'id_curva' in params:
            query_params.append(('idCurva', params['id_curva']))  # noqa: E501
        if 'plazo' in params:
            query_params.append(('plazo', params['plazo']))  # noqa: E501
        if 'id_unidad' in params:
            query_params.append(('idUnidad', params['id_unidad']))  # noqa: E501
        if 'id_base_tasa' in params:
            query_params.append(('idBaseTasa', params['id_base_tasa']))  # noqa: E501
        if 'id_intraday' in params:
            query_params.append(('idIntraday', params['id_intraday']))  # noqa: E501

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
            '/Outputs/Generic/Curvas/Valores/getInterval', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
