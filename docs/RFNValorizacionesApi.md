# riam_api_client.RFNValorizacionesApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_valorizaciones_retornos_get**](RFNValorizacionesApi.md#r_fn_valorizaciones_retornos_get) | **POST** /Outputs/Generic/ValorizacionRF/Retornos/get | Obtiene los Retornos para una fecha.
[**r_fn_valorizaciones_retornos_get_interval**](RFNValorizacionesApi.md#r_fn_valorizaciones_retornos_get_interval) | **POST** /Outputs/Generic/ValorizacionRF/Retornos/getInterval | Obtiene los Retornos para un intervalo de fechas.
[**r_fn_valorizaciones_valorizacion_get**](RFNValorizacionesApi.md#r_fn_valorizaciones_valorizacion_get) | **POST** /Outputs/Generic/ValorizacionRF/Valorizacion/get | Obtiene una valorización.
[**r_fn_valorizaciones_valorizacion_get_interval**](RFNValorizacionesApi.md#r_fn_valorizaciones_valorizacion_get_interval) | **POST** /Outputs/Generic/ValorizacionRF/Valorizacion/getInterval | Obtiene las valorizaciones para un intervalo de fechas.

# **r_fn_valorizaciones_retornos_get**
> InlineResponse20021 r_fn_valorizaciones_retornos_get(fecha, nemo)

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

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_retornos_get_interval**
> InlineResponse20022 r_fn_valorizaciones_retornos_get_interval(fecha_min, fecha_max, nemo)

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

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_valorizacion_get**
> InlineResponse20019 r_fn_valorizaciones_valorizacion_get(fecha, nemo)

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

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_valorizacion_get_interval**
> InlineResponse20020 r_fn_valorizaciones_valorizacion_get_interval(fecha_min, fecha_max, nemo)

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

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

