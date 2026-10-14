# riam_api_client.RFNTransaccionesApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_transacciones_colocaciones_get**](RFNTransaccionesApi.md#r_fn_transacciones_colocaciones_get) | **POST** /Outputs/Generic/TransaccionRF/Colocaciones/get | Obtiene todas las colocaciones para una fecha.
[**r_fn_transacciones_colocaciones_get_interval**](RFNTransaccionesApi.md#r_fn_transacciones_colocaciones_get_interval) | **POST** /Outputs/Generic/TransaccionRF/Colocaciones/getInterval | Obtiene las colocaciones para un intervalo de fechas.
[**r_fn_transacciones_transaccion_otc_get**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_otc_get) | **POST** /Outputs/Generic/TransaccionRF/TransaccionOTC/get | Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para una fecha.
[**r_fn_transacciones_transaccion_otc_get_interval**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_otc_get_interval) | **POST** /Outputs/Generic/TransaccionRF/TransaccionOTC/getInterval | Obtiene las transacciones OTC, ponderadas por monto transado, de un Instrumento para un intervalo de fechas.
[**r_fn_transacciones_transaccion_otc_get_ultima_transaccion**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_otc_get_ultima_transaccion) | **POST** /Outputs/Generic/TransaccionRF/TransaccionOTC/getUltimaTransaccion | Obtiene la información de la última transacción OTC de un Instrumento para una fecha.
[**r_fn_transacciones_transaccion_promedio_get**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_promedio_get) | **POST** /Outputs/Generic/TransaccionRF/TransaccionPromedio/get | Obtiene la transacción promedio de un Instrumento para una fecha.
[**r_fn_transacciones_transaccion_promedio_get_interval**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_promedio_get_interval) | **POST** /Outputs/Generic/TransaccionRF/TransaccionPromedio/getInterval | Obtiene las transacciones promedio de un Instrumento para un intervalo de fechas.
[**r_fn_transacciones_transaccion_promedio_get_ultima_transaccion**](RFNTransaccionesApi.md#r_fn_transacciones_transaccion_promedio_get_ultima_transaccion) | **POST** /Outputs/Generic/TransaccionRF/TransaccionPromedio/getUltimaTransaccion | Obtiene la información de la última transacción promedio de un Instrumento para una fecha.

# **r_fn_transacciones_colocaciones_get**
> RFNTransaccionesColocacionesGetResponse r_fn_transacciones_colocaciones_get(fecha, tipo_colocacion, origen=origen)

Obtiene todas las colocaciones para una fecha.

Obtiene todas las colocaciones para una fecha.

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
tipo_colocacion = 'tipo_colocacion_example' # str | Tipo de colocacion (Nueva,Aumento o Todas).
origen = 'origen_example' # str | Origen de los datos (Bolsa u OTC). Si no se especifica se entregan para ambos para la fecha. (optional)

try:
    # Obtiene todas las colocaciones para una fecha.
    api_response = api_instance.r_fn_transacciones_colocaciones_get(fecha, tipo_colocacion, origen=origen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNTransaccionesApi->r_fn_transacciones_colocaciones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Intervalo Inferior de Fecha | 
 **tipo_colocacion** | **str**| Tipo de colocacion (Nueva,Aumento o Todas). | 
 **origen** | **str**| Origen de los datos (Bolsa u OTC). Si no se especifica se entregan para ambos para la fecha. | [optional] 

### Return type

[**RFNTransaccionesColocacionesGetResponse**](RFNTransaccionesColocacionesGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_colocaciones_get_interval**
> RFNTransaccionesColocacionesGetIntervalResponse r_fn_transacciones_colocaciones_get_interval(fecha_min, fecha_max, tipo_colocacion, origen=origen)

Obtiene las colocaciones para un intervalo de fechas.

Obtiene las colocaciones para un intervalo de fechas.

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
fecha_min = '2013-10-20' # date | Intervalo Inferior de Fecha
fecha_max = '2013-10-20' # date | Intervalo Superior de Fecha
tipo_colocacion = 'tipo_colocacion_example' # str | Tipo de colocacion (Nueva,Aumento o Todas).
origen = 'origen_example' # str | Origen de los datos (Bolsa u OTC). Si no se especifica se entregan para ambos para la fecha. (optional)

try:
    # Obtiene las colocaciones para un intervalo de fechas.
    api_response = api_instance.r_fn_transacciones_colocaciones_get_interval(fecha_min, fecha_max, tipo_colocacion, origen=origen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNTransaccionesApi->r_fn_transacciones_colocaciones_get_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Intervalo Inferior de Fecha | 
 **fecha_max** | **date**| Intervalo Superior de Fecha | 
 **tipo_colocacion** | **str**| Tipo de colocacion (Nueva,Aumento o Todas). | 
 **origen** | **str**| Origen de los datos (Bolsa u OTC). Si no se especifica se entregan para ambos para la fecha. | [optional] 

### Return type

[**RFNTransaccionesColocacionesGetIntervalResponse**](RFNTransaccionesColocacionesGetIntervalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_otc_get**
> RFNTransaccionesTransaccionOTCGetResponse r_fn_transacciones_transaccion_otc_get(fecha, nemo=nemo)

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

[**RFNTransaccionesTransaccionOTCGetResponse**](RFNTransaccionesTransaccionOTCGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_otc_get_interval**
> RFNTransaccionesTransaccionOTCGetIntervalResponse r_fn_transacciones_transaccion_otc_get_interval(nemo, fecha_min, fecha_max)

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

[**RFNTransaccionesTransaccionOTCGetIntervalResponse**](RFNTransaccionesTransaccionOTCGetIntervalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_otc_get_ultima_transaccion**
> RFNTransaccionesTransaccionOTCGetUltimaTransaccionResponse r_fn_transacciones_transaccion_otc_get_ultima_transaccion(fecha, nemo=nemo)

Obtiene la información de la última transacción OTC de un Instrumento para una fecha.

Obtiene la información de la última transacción OTC de un Instrumento para una fecha.

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
fecha = '2013-10-20' # date | Fecha de la consulta
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar. (optional)

try:
    # Obtiene la información de la última transacción OTC de un Instrumento para una fecha.
    api_response = api_instance.r_fn_transacciones_transaccion_otc_get_ultima_transaccion(fecha, nemo=nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNTransaccionesApi->r_fn_transacciones_transaccion_otc_get_ultima_transaccion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha de la consulta | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar. | [optional] 

### Return type

[**RFNTransaccionesTransaccionOTCGetUltimaTransaccionResponse**](RFNTransaccionesTransaccionOTCGetUltimaTransaccionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_promedio_get**
> RFNTransaccionesTransaccionPromedioGetResponse r_fn_transacciones_transaccion_promedio_get(fecha, nemo=nemo)

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

[**RFNTransaccionesTransaccionPromedioGetResponse**](RFNTransaccionesTransaccionPromedioGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_promedio_get_interval**
> RFNTransaccionesTransaccionPromedioGetIntervalResponse r_fn_transacciones_transaccion_promedio_get_interval(nemo, fecha_min, fecha_max)

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

[**RFNTransaccionesTransaccionPromedioGetIntervalResponse**](RFNTransaccionesTransaccionPromedioGetIntervalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_transacciones_transaccion_promedio_get_ultima_transaccion**
> RFNTransaccionesTransaccionPromedioGetUltimaTransaccionResponse r_fn_transacciones_transaccion_promedio_get_ultima_transaccion(fecha, nemo=nemo)

Obtiene la información de la última transacción promedio de un Instrumento para una fecha.

Obtiene la información de la última transacción promedio de un Instrumento para una fecha.

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
fecha = '2013-10-20' # date | Fecha de la consulta
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar. (optional)

try:
    # Obtiene la información de la última transacción promedio de un Instrumento para una fecha.
    api_response = api_instance.r_fn_transacciones_transaccion_promedio_get_ultima_transaccion(fecha, nemo=nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNTransaccionesApi->r_fn_transacciones_transaccion_promedio_get_ultima_transaccion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha de la consulta | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar. | [optional] 

### Return type

[**RFNTransaccionesTransaccionPromedioGetUltimaTransaccionResponse**](RFNTransaccionesTransaccionPromedioGetUltimaTransaccionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

