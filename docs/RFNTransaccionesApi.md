# riam_api_client.RFNTransaccionesApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_transacciones_transaccion_otc_get**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_otc_get) | **POST** /Outputs/Generic/TransaccionRF/TransaccionOTC/get | Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.
[**r_fn_transacciones_transaccion_otc_get_interval**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_otc_get_interval) | **POST** /Outputs/Generic/TransaccionRF/TransaccionOTC/getInterval | Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.
[**r_fn_transacciones_transaccion_promedio_get**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_promedio_get) | **POST** /Outputs/Generic/TransaccionRF/TransaccionPromedio/get | Obtiene la transacción promedio de un Instrumento para una fecha.
[**r_fn_transacciones_transaccion_promedio_get_interval**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_promedio_get_interval) | **POST** /Outputs/Generic/TransaccionRF/TransaccionPromedio/getInterval | Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.

# **r_fn_transacciones_transaccion_otc_get**
> InlineResponse20016 r_fn_transacciones_transaccion_otc_get(fecha, nemo=nemo)

Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.

Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.

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
api_instance = riam_api_client.RFNTransaccionesApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Intervalo Inferior de Fecha
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha. (optional)

try:
    # Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.
    api_response = api_instance.r_fn_transacciones_transaccion_otc_get(fecha, nemo=nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNTransaccionesApi->r_fn_transacciones_transaccion_otc_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Intervalo Inferior de Fecha | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_otc_get_interval**
> InlineResponse20017 r_fn_transacciones_transaccion_otc_get_interval(nemo, fecha_min, fecha_max)

Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.

Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.

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
api_instance = riam_api_client.RFNTransaccionesApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
fecha_min = '2013-10-20' # date | Intervalo Inferior de Fecha
fecha_max = '2013-10-20' # date | Intervalo Superior de Fecha

try:
    # Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.
    api_response = api_instance.r_fn_transacciones_transaccion_otc_get_interval(nemo, fecha_min, fecha_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNTransaccionesApi->r_fn_transacciones_transaccion_otc_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **fecha_min** | **date**| Intervalo Inferior de Fecha | 
 **fecha_max** | **date**| Intervalo Superior de Fecha | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_promedio_get**
> InlineResponse20018 r_fn_transacciones_transaccion_promedio_get(fecha, nemo=nemo)

Obtiene la transacción promedio de un Instrumento para una fecha.

Obtiene la transacción promedio de un Instrumento para una fecha.

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
api_instance = riam_api_client.RFNTransaccionesApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Intervalo Inferior de Fecha
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha. (optional)

try:
    # Obtiene la transacción promedio de un Instrumento para una fecha.
    api_response = api_instance.r_fn_transacciones_transaccion_promedio_get(fecha, nemo=nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNTransaccionesApi->r_fn_transacciones_transaccion_promedio_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Intervalo Inferior de Fecha | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_promedio_get_interval**
> InlineResponse20018 r_fn_transacciones_transaccion_promedio_get_interval(nemo, fecha_min, fecha_max)

Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.

Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.

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
api_instance = riam_api_client.RFNTransaccionesApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
fecha_min = '2013-10-20' # date | Intervalo Inferior de Fecha
fecha_max = '2013-10-20' # date | Intervalo Superior de Fecha

try:
    # Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.
    api_response = api_instance.r_fn_transacciones_transaccion_promedio_get_interval(nemo, fecha_min, fecha_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNTransaccionesApi->r_fn_transacciones_transaccion_promedio_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **fecha_min** | **date**| Intervalo Inferior de Fecha | 
 **fecha_max** | **date**| Intervalo Superior de Fecha | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

