# riam_api_client.CurvasApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**curvas_informacion_get_curvas**](CurvasApi.md#curvas_informacion_get_curvas) | **POST** /Outputs/Generic/Curvas/Informacion/getCurvas | Obtiene el listado de curvas disponibles para consultar.
[**curvas_informacion_get_familias**](CurvasApi.md#curvas_informacion_get_familias) | **POST** /Outputs/Generic/Curvas/Informacion/getFamilias | Obtiene el listado de familias sobre los cuales se clasifican las curvas.
[**curvas_informacion_get_intradays**](CurvasApi.md#curvas_informacion_get_intradays) | **POST** /Outputs/Generic/Curvas/Informacion/getIntradays | Obtiene el listado de Intradays disponibles.
[**curvas_informacion_get_unidad_tiempo**](CurvasApi.md#curvas_informacion_get_unidad_tiempo) | **POST** /Outputs/Generic/Curvas/Informacion/getUnidadTiempo | Obtiene el listado de unidades de tiempo que se usan para consultar las curvas.
[**curvas_valores_get**](CurvasApi.md#curvas_valores_get) | **POST** /Outputs/Generic/Curvas/Valores/get | Obtiene los valores de una curva para los plazos solicitados.
[**curvas_valores_get_all**](CurvasApi.md#curvas_valores_get_all) | **POST** /Outputs/Generic/Curvas/Valores/getAll | Obtiene todos los valores de una curva para todos los plazos comprendidos entre el plazo minimo y el maximo.
[**curvas_valores_get_interval**](CurvasApi.md#curvas_valores_get_interval) | **POST** /Outputs/Generic/Curvas/Valores/getInterval | Obtiene los valores de una curva para las fechas solicitadas a un plazo fijo.

# **curvas_informacion_get_curvas**
> InlineResponse20011 curvas_informacion_get_curvas()

Obtiene el listado de curvas disponibles para consultar.

Obtiene el listado de curvas disponibles para consultar. Es importante destacar que esto incluye tanto curvas públicas como otras curvas personalizadas a las que el usuario tenga acceso.

### Example
```python
from __future__ import print_function
import time
import riam_api_client
from riam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = riam_api_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = riam_api_client.CurvasApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene el listado de curvas disponibles para consultar.
    api_response = api_instance.curvas_informacion_get_curvas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurvasApi->curvas_informacion_get_curvas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curvas_informacion_get_familias**
> InlineResponse20012 curvas_informacion_get_familias()

Obtiene el listado de familias sobre los cuales se clasifican las curvas.

Obtiene el listado de familias sobre los cuales se clasifican las curvas.

### Example
```python
from __future__ import print_function
import time
import riam_api_client
from riam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = riam_api_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = riam_api_client.CurvasApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene el listado de familias sobre los cuales se clasifican las curvas.
    api_response = api_instance.curvas_informacion_get_familias()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurvasApi->curvas_informacion_get_familias: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curvas_informacion_get_intradays**
> InlineResponse20014 curvas_informacion_get_intradays()

Obtiene el listado de Intradays disponibles.

Obtiene el listado de Intradays disponibles. Cabe destacar que el Intraday 10 es el que se usa para la valorización oficial de RiskAmerica.

### Example
```python
from __future__ import print_function
import time
import riam_api_client
from riam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = riam_api_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = riam_api_client.CurvasApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene el listado de Intradays disponibles.
    api_response = api_instance.curvas_informacion_get_intradays()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurvasApi->curvas_informacion_get_intradays: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curvas_informacion_get_unidad_tiempo**
> InlineResponse20013 curvas_informacion_get_unidad_tiempo()

Obtiene el listado de unidades de tiempo que se usan para consultar las curvas.

Obtiene el listado de unidades de tiempo que se usan para consultar las curvas.

### Example
```python
from __future__ import print_function
import time
import riam_api_client
from riam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = riam_api_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = riam_api_client.CurvasApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene el listado de unidades de tiempo que se usan para consultar las curvas.
    api_response = api_instance.curvas_informacion_get_unidad_tiempo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurvasApi->curvas_informacion_get_unidad_tiempo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curvas_valores_get**
> InlineResponse20015 curvas_valores_get(fecha, id_curva, id_intraday, body=body, id_unidad=id_unidad, id_base_tasa=id_base_tasa)

Obtiene los valores de una curva para los plazos solicitados.

Obtiene los valores de una curva para los plazos solicitados.

### Example
```python
from __future__ import print_function
import time
import riam_api_client
from riam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = riam_api_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = riam_api_client.CurvasApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha para la cual se consulta
id_curva = 'id_curva_example' # str | Identificador de la Curva
id_intraday = 10 # int | Identificador del Intraday para el cual se consulta (default to 10)
body = riam_api_client.Body() # Body |  (optional)
id_unidad = 'id_unidad_example' # str | Unidad en la que estan los plazos provistos, las opciones posibles son DIA, MES, ANIO (optional)
id_base_tasa = 'id_base_tasa_example' # str | Tasa Base en la que se consultan los valores (optional)

try:
    # Obtiene los valores de una curva para los plazos solicitados.
    api_response = api_instance.curvas_valores_get(fecha, id_curva, id_intraday, body=body, id_unidad=id_unidad, id_base_tasa=id_base_tasa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurvasApi->curvas_valores_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha para la cual se consulta | 
 **id_curva** | **str**| Identificador de la Curva | 
 **id_intraday** | **int**| Identificador del Intraday para el cual se consulta | [default to 10]
 **body** | [**Body**](Body.md)|  | [optional] 
 **id_unidad** | **str**| Unidad en la que estan los plazos provistos, las opciones posibles son DIA, MES, ANIO | [optional] 
 **id_base_tasa** | **str**| Tasa Base en la que se consultan los valores | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curvas_valores_get_all**
> InlineResponse20015 curvas_valores_get_all(fecha, id_curva, plazo_inicial, plazo_final, id_intraday, id_unidad=id_unidad, id_base_tasa=id_base_tasa)

Obtiene todos los valores de una curva para todos los plazos comprendidos entre el plazo minimo y el maximo.

Obtiene todos los valores de una curva para todos los plazos comprendidos entre el plazo minimo y el maximo.

### Example
```python
from __future__ import print_function
import time
import riam_api_client
from riam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = riam_api_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = riam_api_client.CurvasApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha para la cual se consulta
id_curva = 'id_curva_example' # str | Identificador de la Curva
plazo_inicial = 1.2 # float | Plazo inicial a consultar en la base consultada
plazo_final = 1.2 # float | Plazo final a consultar en la base consultada
id_intraday = 10 # int | Identificador del Intraday para el cual se consulta (default to 10)
id_unidad = 'id_unidad_example' # str | Unidad en la que estan los plazos provistos, las opciones posibles son DIA, MES, ANIO (optional)
id_base_tasa = 'id_base_tasa_example' # str | Tasa Base en la que se consultan los valores (optional)

try:
    # Obtiene todos los valores de una curva para todos los plazos comprendidos entre el plazo minimo y el maximo.
    api_response = api_instance.curvas_valores_get_all(fecha, id_curva, plazo_inicial, plazo_final, id_intraday, id_unidad=id_unidad, id_base_tasa=id_base_tasa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurvasApi->curvas_valores_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha para la cual se consulta | 
 **id_curva** | **str**| Identificador de la Curva | 
 **plazo_inicial** | **float**| Plazo inicial a consultar en la base consultada | 
 **plazo_final** | **float**| Plazo final a consultar en la base consultada | 
 **id_intraday** | **int**| Identificador del Intraday para el cual se consulta | [default to 10]
 **id_unidad** | **str**| Unidad en la que estan los plazos provistos, las opciones posibles son DIA, MES, ANIO | [optional] 
 **id_base_tasa** | **str**| Tasa Base en la que se consultan los valores | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curvas_valores_get_interval**
> InlineResponse20015 curvas_valores_get_interval(fecha_min, fecha_max, id_curva, plazo, id_unidad, id_base_tasa, id_intraday)

Obtiene los valores de una curva para las fechas solicitadas a un plazo fijo.

Obtiene los valores de una curva para las fechas solicitadas a un plazo fijo, RESTRICCIÓN: El intervalo de fechas debe ser menor a 365 días.

### Example
```python
from __future__ import print_function
import time
import riam_api_client
from riam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = riam_api_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = riam_api_client.CurvasApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Intervalo inferior de fecha para la que se consulta
fecha_max = '2013-10-20' # date | Intervalo superior de fecha para la que se consulta
id_curva = 'id_curva_example' # str | Identificador de la Curva
plazo = 1.2 # float | Plazos a consultar
id_unidad = '<i>Unidad base de la Curva</i>' # str | Unidad en la que estan los plazos provistos (default to <i>Unidad base de la Curva</i>)
id_base_tasa = '<i>Unidad base de la Curva</i>' # str | Tasa Base en la que se consultan los valores (default to <i>Unidad base de la Curva</i>)
id_intraday = 10 # int | Identificador del Intraday para el cual se consulta (default to 10)

try:
    # Obtiene los valores de una curva para las fechas solicitadas a un plazo fijo.
    api_response = api_instance.curvas_valores_get_interval(fecha_min, fecha_max, id_curva, plazo, id_unidad, id_base_tasa, id_intraday)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurvasApi->curvas_valores_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Intervalo inferior de fecha para la que se consulta | 
 **fecha_max** | **date**| Intervalo superior de fecha para la que se consulta | 
 **id_curva** | **str**| Identificador de la Curva | 
 **plazo** | **float**| Plazos a consultar | 
 **id_unidad** | **str**| Unidad en la que estan los plazos provistos | [default to &lt;i&gt;Unidad base de la Curva&lt;/i&gt;]
 **id_base_tasa** | **str**| Tasa Base en la que se consultan los valores | [default to &lt;i&gt;Unidad base de la Curva&lt;/i&gt;]
 **id_intraday** | **int**| Identificador del Intraday para el cual se consulta | [default to 10]

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

