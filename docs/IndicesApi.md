# riam_api_client.IndicesApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**indices_informacion_get_dias_con_retorno**](IndicesApi.md#indices_informacion_get_dias_con_retorno) | **POST** /Outputs/Generic/Indices/Informacion/getDiasConRetorno | Obtiene los posibles dias con retorno de los índices.
[**indices_informacion_get_grupos**](IndicesApi.md#indices_informacion_get_grupos) | **POST** /Outputs/Generic/Indices/Informacion/getGrupos | Obtiene el listado de grupos sobre los cuales se clasifican los índices.
[**indices_informacion_get_indices**](IndicesApi.md#indices_informacion_get_indices) | **POST** /Outputs/Generic/Indices/Informacion/getIndices | Obtiene el listado de índices disponibles para consultar.
[**indices_ponderacion_get**](IndicesApi.md#indices_ponderacion_get) | **POST** /Outputs/Generic/Indices/Ponderacion/get | Obtiene las ponderaciones de los instrumentos que componen un Índice.
[**indices_retorno_get_fecha**](IndicesApi.md#indices_retorno_get_fecha) | **POST** /Outputs/Generic/Indices/Retorno/getFecha | Obtiene el valor de los retornos de un Índice para una fecha.
[**indices_retorno_get_interval**](IndicesApi.md#indices_retorno_get_interval) | **POST** /Outputs/Generic/Indices/Retorno/getInterval | Obtiene el valor de los retornos de un Índice para un intervalo de fechas.

# **indices_informacion_get_dias_con_retorno**
> InlineResponse2008 indices_informacion_get_dias_con_retorno()

Obtiene los posibles dias con retorno de los índices.

Obtiene el listado de todos los posibles días con retornos y su identificador.

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
api_instance = riam_api_client.IndicesApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene los posibles dias con retorno de los índices.
    api_response = api_instance.indices_informacion_get_dias_con_retorno()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicesApi->indices_informacion_get_dias_con_retorno: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indices_informacion_get_grupos**
> InlineResponse2007 indices_informacion_get_grupos()

Obtiene el listado de grupos sobre los cuales se clasifican los índices.

Obtiene el listado de grupos sobre los cuales se clasifican los índices.

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
api_instance = riam_api_client.IndicesApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene el listado de grupos sobre los cuales se clasifican los índices.
    api_response = api_instance.indices_informacion_get_grupos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicesApi->indices_informacion_get_grupos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indices_informacion_get_indices**
> InlineResponse2006 indices_informacion_get_indices()

Obtiene el listado de índices disponibles para consultar.

Obtiene el listado de índices disponibles para consultar.

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
api_instance = riam_api_client.IndicesApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene el listado de índices disponibles para consultar.
    api_response = api_instance.indices_informacion_get_indices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicesApi->indices_informacion_get_indices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indices_ponderacion_get**
> InlineResponse2009 indices_ponderacion_get(id_indice, fecha)

Obtiene las ponderaciones de los instrumentos que componen un Índice.

Obtiene las ponderaciones de los instrumentos que componen un Índice.

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
api_instance = riam_api_client.IndicesApi(riam_api_client.ApiClient(configuration))
id_indice = 56 # int | Id del Índice a consultar
fecha = '2013-10-20' # date | Fecha a consultar

try:
    # Obtiene las ponderaciones de los instrumentos que componen un Índice.
    api_response = api_instance.indices_ponderacion_get(id_indice, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicesApi->indices_ponderacion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_indice** | **int**| Id del Índice a consultar | 
 **fecha** | **date**| Fecha a consultar | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indices_retorno_get_fecha**
> InlineResponse20010 indices_retorno_get_fecha(fecha, id_indice)

Obtiene el valor de los retornos de un Índice para una fecha.

Obtiene el valor de los retornos de un Índice para una fecha.

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
api_instance = riam_api_client.IndicesApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Límite inferior del intervalo de fechas a consultar
id_indice = 'id_indice_example' # str | ID del índice a consultar. Se pueden especificar varios separando por 'pipes' (ASCII 124). IE: 5

try:
    # Obtiene el valor de los retornos de un Índice para una fecha.
    api_response = api_instance.indices_retorno_get_fecha(fecha, id_indice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicesApi->indices_retorno_get_fecha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Límite inferior del intervalo de fechas a consultar | 
 **id_indice** | **str**| ID del índice a consultar. Se pueden especificar varios separando por &#x27;pipes&#x27; (ASCII 124). IE: 5 | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indices_retorno_get_interval**
> InlineResponse20010 indices_retorno_get_interval(fecha_min, fecha_max, id_indice)

Obtiene el valor de los retornos de un Índice para un intervalo de fechas.

Obtiene el valor de los retornos de un Índice para un intervalo de fechas.

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
api_instance = riam_api_client.IndicesApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Límite inferior del intervalo de fechas a consultar
fecha_max = '2013-10-20' # date | Límite superior del intervalo de fechas a consultar
id_indice = 56 # int | Id del Índice a consultar.

try:
    # Obtiene el valor de los retornos de un Índice para un intervalo de fechas.
    api_response = api_instance.indices_retorno_get_interval(fecha_min, fecha_max, id_indice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicesApi->indices_retorno_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Límite inferior del intervalo de fechas a consultar | 
 **fecha_max** | **date**| Límite superior del intervalo de fechas a consultar | 
 **id_indice** | **int**| Id del Índice a consultar. | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

