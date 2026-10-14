# riam_api_client.RFNValorizacionesApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_valorizaciones_retornos_get**](RFNValorizacionesApi.md#r_fn_valorizaciones_retornos_get) | **POST** /Outputs/Generic/ValorizacionRF/Retornos/get | Obtiene los Retornos para una fecha.
[**r_fn_valorizaciones_retornos_get_interval**](RFNValorizacionesApi.md#r_fn_valorizaciones_retornos_get_interval) | **POST** /Outputs/Generic/ValorizacionRF/Retornos/getInterval | Obtiene los Retornos para un intervalo de fechas.
[**r_fn_valorizaciones_valorizacion_calculadora**](RFNValorizacionesApi.md#r_fn_valorizaciones_valorizacion_calculadora) | **POST** /Outputs/Generic/ValorizacionRF/Valorizacion/calculadora | Obtiene la valorización de un instrumento.
[**r_fn_valorizaciones_valorizacion_get**](RFNValorizacionesApi.md#r_fn_valorizaciones_valorizacion_get) | **POST** /Outputs/Generic/ValorizacionRF/Valorizacion/get | Obtiene una valorización.
[**r_fn_valorizaciones_valorizacion_get_interval**](RFNValorizacionesApi.md#r_fn_valorizaciones_valorizacion_get_interval) | **POST** /Outputs/Generic/ValorizacionRF/Valorizacion/getInterval | Obtiene las valorizaciones para un intervalo de fechas.

# **r_fn_valorizaciones_retornos_get**
> RFNValorizacionesRetornosGetResponse r_fn_valorizaciones_retornos_get(fecha, nemo)

Obtiene los Retornos para una fecha.

Obtiene los Retornos para una fecha, esto incluye el retorno de los días no hábiles anteriores.

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
api_instance = riam_api_client.RFNValorizacionesApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene los Retornos para una fecha.
    api_response = api_instance.r_fn_valorizaciones_retornos_get(fecha, nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesApi->r_fn_valorizaciones_retornos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**RFNValorizacionesRetornosGetResponse**](RFNValorizacionesRetornosGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_retornos_get_interval**
> RFNValorizacionesRetornosGetIntervalResponse r_fn_valorizaciones_retornos_get_interval(fecha_min, fecha_max, nemo)

Obtiene los Retornos para un intervalo de fechas.

Obtiene los Retornos para un intervalo de fechas, esto incluye el retorno de los días no hábiles anteriores.

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
api_instance = riam_api_client.RFNValorizacionesApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Intervalo Inferior de Fecha
fecha_max = '2013-10-20' # date | Intervalo Superior de Fecha
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene los Retornos para un intervalo de fechas.
    api_response = api_instance.r_fn_valorizaciones_retornos_get_interval(fecha_min, fecha_max, nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesApi->r_fn_valorizaciones_retornos_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Intervalo Inferior de Fecha | 
 **fecha_max** | **date**| Intervalo Superior de Fecha | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**RFNValorizacionesRetornosGetIntervalResponse**](RFNValorizacionesRetornosGetIntervalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_valorizacion_calculadora**
> RFNValorizacionesValorizacionCalculadoraResponse r_fn_valorizaciones_valorizacion_calculadora(nemo, fecha, nominal=nominal, condicion_pago=condicion_pago)

Obtiene la valorización de un instrumento.

Obtiene la valorización de un instrumento.

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
api_instance = riam_api_client.RFNValorizacionesApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotecnico del instrumento a valorizar
fecha = '2013-10-20' # date | Fecha para la cual se efectua la valorización
nominal = 1.2 # float | Nominal a valorizar. Si no se carga se asume 1000 (optional)
condicion_pago = 'condicion_pago_example' # str | Condicion de Pago. Las opciones posibles son: PH, PM, CN. (optional)

try:
    # Obtiene la valorización de un instrumento.
    api_response = api_instance.r_fn_valorizaciones_valorizacion_calculadora(nemo, fecha, nominal=nominal, condicion_pago=condicion_pago)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesApi->r_fn_valorizaciones_valorizacion_calculadora: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotecnico del instrumento a valorizar | 
 **fecha** | **date**| Fecha para la cual se efectua la valorización | 
 **nominal** | **float**| Nominal a valorizar. Si no se carga se asume 1000 | [optional] 
 **condicion_pago** | **str**| Condicion de Pago. Las opciones posibles son: PH, PM, CN. | [optional] 

### Return type

[**RFNValorizacionesValorizacionCalculadoraResponse**](RFNValorizacionesValorizacionCalculadoraResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_valorizacion_get**
> RFNValorizacionesValorizacionGetResponse r_fn_valorizaciones_valorizacion_get(fecha, nemo)

Obtiene una valorización.

Obtiene una valorización disponible hasta la fecha hábil anterior a la fecha de consulta.

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
api_instance = riam_api_client.RFNValorizacionesApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene una valorización.
    api_response = api_instance.r_fn_valorizaciones_valorizacion_get(fecha, nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesApi->r_fn_valorizaciones_valorizacion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**RFNValorizacionesValorizacionGetResponse**](RFNValorizacionesValorizacionGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_valorizacion_get_interval**
> RFNValorizacionesValorizacionGetIntervalResponse r_fn_valorizaciones_valorizacion_get_interval(fecha_min, fecha_max, nemo)

Obtiene las valorizaciones para un intervalo de fechas.

Obtiene las valorizaciones para un intervalo de fechas, la fecha máxima de consulta corresponde al día hábil inmediatamente anterior al día en que se realiza la consulta.

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
api_instance = riam_api_client.RFNValorizacionesApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Intervalo Inferior de Fecha
fecha_max = '2013-10-20' # date | Intervalo Superior de Fecha
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene las valorizaciones para un intervalo de fechas.
    api_response = api_instance.r_fn_valorizaciones_valorizacion_get_interval(fecha_min, fecha_max, nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesApi->r_fn_valorizaciones_valorizacion_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Intervalo Inferior de Fecha | 
 **fecha_max** | **date**| Intervalo Superior de Fecha | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**RFNValorizacionesValorizacionGetIntervalResponse**](RFNValorizacionesValorizacionGetIntervalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

