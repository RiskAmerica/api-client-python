# riam_api_client.RFNValorizacionesSinDesfaseApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get**](RFNValorizacionesSinDesfaseApi.md#r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get) | **POST** /Outputs/Generic/ValorizacionRF/ValorizacionSinDesfase/get | Obtiene una valorización sin desfase.
[**r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get_interval**](RFNValorizacionesSinDesfaseApi.md#r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get_interval) | **POST** /Outputs/Generic/ValorizacionRF/ValorizacionSinDesfase/getInterval | Obtiene las valorizaciones para un intervalo de fechas, sin desfase.

# **r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get**
> InlineResponse20019 r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get(fecha, nemo)

Obtiene una valorización sin desfase.

Obtiene una valorización sin desfase.

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
api_instance = riam_api_client.RFNValorizacionesSinDesfaseApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene una valorización sin desfase.
    api_response = api_instance.r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get(fecha, nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesSinDesfaseApi->r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get_interval**
> InlineResponse20023 r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get_interval(fecha_min, fecha_max, nemo)

Obtiene las valorizaciones para un intervalo de fechas, sin desfase.

Obtiene las valorizaciones para un intervalo de fechas, sin desfase.

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
api_instance = riam_api_client.RFNValorizacionesSinDesfaseApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Intervalo Inferior de Fecha
fecha_max = '2013-10-20' # date | Intervalo Superior de Fecha
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene las valorizaciones para un intervalo de fechas, sin desfase.
    api_response = api_instance.r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get_interval(fecha_min, fecha_max, nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesSinDesfaseApi->r_fn_valorizaciones_sin_desfase_valorizacion_sin_desfase_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Intervalo Inferior de Fecha | 
 **fecha_max** | **date**| Intervalo Superior de Fecha | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

