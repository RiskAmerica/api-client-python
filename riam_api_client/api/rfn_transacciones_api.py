# coding: utf-8

"""
    APIs RISKAMERICA

    A continuación les presentamos la documentación las **APIs** **de** **RiskAmerica**, el cual es un servicio pagado ofrecido por RiskAmerica que se contrata por separado a nuestras otras ofertas de software.  Algunas consideraciones que debe tener al momento de usar las APIs: - El APIKEY o Token lo puede conseguir solicitándolo al equipo comercial de RiskAmerica - El request necesita ser enviado con el header **Accept:** **application/json** para que responda en formato **JSON** (de no ser enviado con esto se responderá en formato **XML**) - Todos los Servicios son **REST** y sus parametros pueden ser enviados tanto en **POST** como **GET** - El uso de las APIs puede llevar un cobro asociado según se pacte en el acuerdo comercial, por lo que le recomendamos ser cuidadosos en el uso de éstas para evitar sobre-cargos innecesarios. - RiskAmerica funciona con un mecanismo de **WhiteList** **de** **IPs** para las consultas de las API. Para habilitar o modificar la lista de IPs permitidas debe contactarse al mail **contacto@riskamerica.com**.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
# Model imports
from . import InlineResponse20016
from . import InlineResponse20017
from . import InlineResponse20018
from . import InlineResponse20018
# Importing for doctring purposes
# Api Client
from riam_api_client.api_client import ApiClient


class RFNTransaccionesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def r_fn_transacciones_transaccion_otc_get(self, fecha, **kwargs):  # noqa: E501
        """Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.  # noqa: E501

        Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_transacciones_transaccion_otc_get(fecha, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Intervalo Inferior de Fecha (required)
        :param str nemo: Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha.
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20016 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.r_fn_transacciones_transaccion_otc_get_with_http_info(fecha, **kwargs)  # noqa: E501
        else:
            (data) = self.r_fn_transacciones_transaccion_otc_get_with_http_info(fecha, **kwargs)  # noqa: E501
            return data

    def r_fn_transacciones_transaccion_otc_get_with_http_info(self, fecha, **kwargs):  # noqa: E501
        """Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.  # noqa: E501

        Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_transacciones_transaccion_otc_get_with_http_info(fecha, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Intervalo Inferior de Fecha (required)
        :param str nemo: Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha.
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20016 | multiprocessing.pool.ApplyResult
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
                    " to method r_fn_transacciones_transaccion_otc_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `r_fn_transacciones_transaccion_otc_get`")  # noqa: E501

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
            '/Outputs/Generic/TransaccionRF/TransaccionOTC/get', 'POST',
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

    def r_fn_transacciones_transaccion_otc_get_interval(self, nemo, fecha_min, fecha_max, **kwargs):  # noqa: E501
        """Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.  # noqa: E501

        Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_transacciones_transaccion_otc_get_interval(nemo, fecha_min, fecha_max, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str nemo: Nemotécnico del instrumento a consultar (required)
        :param date fecha_min: Intervalo Inferior de Fecha (required)
        :param date fecha_max: Intervalo Superior de Fecha (required)
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20017 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.r_fn_transacciones_transaccion_otc_get_interval_with_http_info(nemo, fecha_min, fecha_max, **kwargs)  # noqa: E501
        else:
            (data) = self.r_fn_transacciones_transaccion_otc_get_interval_with_http_info(nemo, fecha_min, fecha_max, **kwargs)  # noqa: E501
            return data

    def r_fn_transacciones_transaccion_otc_get_interval_with_http_info(self, nemo, fecha_min, fecha_max, **kwargs):  # noqa: E501
        """Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.  # noqa: E501

        Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_transacciones_transaccion_otc_get_interval_with_http_info(nemo, fecha_min, fecha_max, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str nemo: Nemotécnico del instrumento a consultar (required)
        :param date fecha_min: Intervalo Inferior de Fecha (required)
        :param date fecha_max: Intervalo Superior de Fecha (required)
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20017 | multiprocessing.pool.ApplyResult
        """

        all_params = ['nemo', 'fecha_min', 'fecha_max']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method r_fn_transacciones_transaccion_otc_get_interval" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'nemo' is set
        if ('nemo' not in params or
                params['nemo'] is None):
            raise ValueError("Missing the required parameter `nemo` when calling `r_fn_transacciones_transaccion_otc_get_interval`")  # noqa: E501
        # verify the required parameter 'fecha_min' is set
        if ('fecha_min' not in params or
                params['fecha_min'] is None):
            raise ValueError("Missing the required parameter `fecha_min` when calling `r_fn_transacciones_transaccion_otc_get_interval`")  # noqa: E501
        # verify the required parameter 'fecha_max' is set
        if ('fecha_max' not in params or
                params['fecha_max'] is None):
            raise ValueError("Missing the required parameter `fecha_max` when calling `r_fn_transacciones_transaccion_otc_get_interval`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nemo' in params:
            query_params.append(('nemo', params['nemo']))  # noqa: E501
        if 'fecha_min' in params:
            query_params.append(('fechaMin', params['fecha_min']))  # noqa: E501
        if 'fecha_max' in params:
            query_params.append(('fechaMax', params['fecha_max']))  # noqa: E501

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
            '/Outputs/Generic/TransaccionRF/TransaccionOTC/getInterval', 'POST',
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

    def r_fn_transacciones_transaccion_promedio_get(self, fecha, **kwargs):  # noqa: E501
        """Obtiene la transacción promedio de un Instrumento para una fecha.  # noqa: E501

        Obtiene la transacción promedio de un Instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_transacciones_transaccion_promedio_get(fecha, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Intervalo Inferior de Fecha (required)
        :param str nemo: Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha.
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20018 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.r_fn_transacciones_transaccion_promedio_get_with_http_info(fecha, **kwargs)  # noqa: E501
        else:
            (data) = self.r_fn_transacciones_transaccion_promedio_get_with_http_info(fecha, **kwargs)  # noqa: E501
            return data

    def r_fn_transacciones_transaccion_promedio_get_with_http_info(self, fecha, **kwargs):  # noqa: E501
        """Obtiene la transacción promedio de un Instrumento para una fecha.  # noqa: E501

        Obtiene la transacción promedio de un Instrumento para una fecha.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_transacciones_transaccion_promedio_get_with_http_info(fecha, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date fecha: Intervalo Inferior de Fecha (required)
        :param str nemo: Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha.
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20018 | multiprocessing.pool.ApplyResult
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
                    " to method r_fn_transacciones_transaccion_promedio_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fecha' is set
        if ('fecha' not in params or
                params['fecha'] is None):
            raise ValueError("Missing the required parameter `fecha` when calling `r_fn_transacciones_transaccion_promedio_get`")  # noqa: E501

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
            '/Outputs/Generic/TransaccionRF/TransaccionPromedio/get', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def r_fn_transacciones_transaccion_promedio_get_interval(self, nemo, fecha_min, fecha_max, **kwargs):  # noqa: E501
        """Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.  # noqa: E501

        Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_transacciones_transaccion_promedio_get_interval(nemo, fecha_min, fecha_max, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str nemo: Nemotécnico del instrumento a consultar (required)
        :param date fecha_min: Intervalo Inferior de Fecha (required)
        :param date fecha_max: Intervalo Superior de Fecha (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20018 | multiprocessing.pool.ApplyResult
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.r_fn_transacciones_transaccion_promedio_get_interval_with_http_info(nemo, fecha_min, fecha_max, **kwargs)  # noqa: E501
        else:
            (data) = self.r_fn_transacciones_transaccion_promedio_get_interval_with_http_info(nemo, fecha_min, fecha_max, **kwargs)  # noqa: E501
            return data

    def r_fn_transacciones_transaccion_promedio_get_interval_with_http_info(self, nemo, fecha_min, fecha_max, **kwargs):  # noqa: E501
        """Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.  # noqa: E501

        Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.r_fn_transacciones_transaccion_promedio_get_interval_with_http_info(nemo, fecha_min, fecha_max, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str nemo: Nemotécnico del instrumento a consultar (required)
        :param date fecha_min: Intervalo Inferior de Fecha (required)
        :param date fecha_max: Intervalo Superior de Fecha (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse20018 | multiprocessing.pool.ApplyResult
        """

        all_params = ['nemo', 'fecha_min', 'fecha_max']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method r_fn_transacciones_transaccion_promedio_get_interval" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'nemo' is set
        if ('nemo' not in params or
                params['nemo'] is None):
            raise ValueError("Missing the required parameter `nemo` when calling `r_fn_transacciones_transaccion_promedio_get_interval`")  # noqa: E501
        # verify the required parameter 'fecha_min' is set
        if ('fecha_min' not in params or
                params['fecha_min'] is None):
            raise ValueError("Missing the required parameter `fecha_min` when calling `r_fn_transacciones_transaccion_promedio_get_interval`")  # noqa: E501
        # verify the required parameter 'fecha_max' is set
        if ('fecha_max' not in params or
                params['fecha_max'] is None):
            raise ValueError("Missing the required parameter `fecha_max` when calling `r_fn_transacciones_transaccion_promedio_get_interval`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nemo' in params:
            query_params.append(('nemo', params['nemo']))  # noqa: E501
        if 'fecha_min' in params:
            query_params.append(('fechaMin', params['fecha_min']))  # noqa: E501
        if 'fecha_max' in params:
            query_params.append(('fechaMax', params['fecha_max']))  # noqa: E501

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
            '/Outputs/Generic/TransaccionRF/TransaccionPromedio/getInterval', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
