# riam_api_client.RVNValorizacionesApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_vn_valorizaciones_valorizacion_get**](RVNValorizacionesApi.md#r_vn_valorizaciones_valorizacion_get) | **POST** /Outputs/Generic/ValorizacionRVN/Valorizacion/get | Obtiene una valorización de renta variable nacional.
[**r_vn_valorizaciones_valorizacion_get_interval**](RVNValorizacionesApi.md#r_vn_valorizaciones_valorizacion_get_interval) | **POST** /Outputs/Generic/ValorizacionRVN/Valorizacion/getInterval | Obtiene las valorizaciones de renta variable nacional para un intervalo de fechas.
[**r_vn_valorizaciones_valorizacion_get_status**](RVNValorizacionesApi.md#r_vn_valorizaciones_valorizacion_get_status) | **POST** /Outputs/Generic/ValorizacionRVN/Valorizacion/getStatus | Revisa el status del servicio de valorizacion para la fecha seleccionada.

# **r_vn_valorizaciones_valorizacion_get**
> RVNValorizacionesValorizacionGetResponse r_vn_valorizaciones_valorizacion_get(fecha, nemo)

Obtiene una valorización de renta variable nacional.

Obtiene una valorización de renta variable nacional.

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
api_instance = riam_api_client.RVNValorizacionesApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene una valorización de renta variable nacional.
    api_response = api_instance.r_vn_valorizaciones_valorizacion_get(fecha, nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RVNValorizacionesApi->r_vn_valorizaciones_valorizacion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**RVNValorizacionesValorizacionGetResponse**](RVNValorizacionesValorizacionGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_vn_valorizaciones_valorizacion_get_interval**
> RVNValorizacionesValorizacionGetIntervalResponse r_vn_valorizaciones_valorizacion_get_interval(fecha_min, fecha_max, nemo)

Obtiene las valorizaciones de renta variable nacional para un intervalo de fechas.

Obtiene las valorizaciones de renta variable nacional para un intervalo de fechas.

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
api_instance = riam_api_client.RVNValorizacionesApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Fecha inicial a consulta
fecha_max = '2013-10-20' # date | Fecha final a consultar
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene las valorizaciones de renta variable nacional para un intervalo de fechas.
    api_response = api_instance.r_vn_valorizaciones_valorizacion_get_interval(fecha_min, fecha_max, nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RVNValorizacionesApi->r_vn_valorizaciones_valorizacion_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Fecha inicial a consulta | 
 **fecha_max** | **date**| Fecha final a consultar | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**RVNValorizacionesValorizacionGetIntervalResponse**](RVNValorizacionesValorizacionGetIntervalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_vn_valorizaciones_valorizacion_get_status**
> RVNValorizacionesValorizacionGetStatusResponse r_vn_valorizaciones_valorizacion_get_status(fecha)

Revisa el status del servicio de valorizacion para la fecha seleccionada.

Revisa el status del servicio de valorizacion para la fecha seleccionada.

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
api_instance = riam_api_client.RVNValorizacionesApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar

try:
    # Revisa el status del servicio de valorizacion para la fecha seleccionada.
    api_response = api_instance.r_vn_valorizaciones_valorizacion_get_status(fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RVNValorizacionesApi->r_vn_valorizaciones_valorizacion_get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 

### Return type

[**RVNValorizacionesValorizacionGetStatusResponse**](RVNValorizacionesValorizacionGetStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

