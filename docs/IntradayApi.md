# riam_api_client.IntradayApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**intraday_puntas_get_puntas**](IntradayApi.md#intraday_puntas_get_puntas) | **POST** /Outputs/Generic/Intraday/Puntas/getPuntas | Obtiene las puntas de un Instrumento para una fecha.
[**intraday_transaccion_intraday_get**](IntradayApi.md#intraday_transaccion_intraday_get) | **POST** /Outputs/Generic/Intraday/TransaccionIntraday/get | Obtiene las transacciones Intraday de un instrumento para una fecha.
[**intraday_valorizacion_intraday_calculadora**](IntradayApi.md#intraday_valorizacion_intraday_calculadora) | **POST** /Outputs/Generic/Intraday/ValorizacionIntraday/calculadora | Obtiene la valorización de un instrumento.
[**intraday_valorizacion_intraday_familia_get**](IntradayApi.md#intraday_valorizacion_intraday_familia_get) | **POST** /Outputs/Generic/Intraday/ValorizacionIntradayFamilia/get | Obtiene las valorizaciones Intraday para una familia para una fecha.
[**intraday_valorizacion_intraday_get**](IntradayApi.md#intraday_valorizacion_intraday_get) | **POST** /Outputs/Generic/Intraday/ValorizacionIntraday/get | Obtiene las valorizaciones Intraday de un Instrumento para una fecha.

# **intraday_puntas_get_puntas**
> IntradayPuntasGetPuntasResponse intraday_puntas_get_puntas(fecha, nemo, tipo_punta=tipo_punta)

Obtiene las puntas de un Instrumento para una fecha.

Obtiene las puntas de un Instrumento para una fecha.

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
api_instance = riam_api_client.IntradayApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar.
tipo_punta = 'tipo_punta_example' # str | Tipo de punta (Compra - Venta). Si no se especifica se entregan ambos tipos. (optional)

try:
    # Obtiene las puntas de un Instrumento para una fecha.
    api_response = api_instance.intraday_puntas_get_puntas(fecha, nemo, tipo_punta=tipo_punta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntradayApi->intraday_puntas_get_puntas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar. | 
 **tipo_punta** | **str**| Tipo de punta (Compra - Venta). Si no se especifica se entregan ambos tipos. | [optional] 

### Return type

[**IntradayPuntasGetPuntasResponse**](IntradayPuntasGetPuntasResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intraday_transaccion_intraday_get**
> IntradayTransaccionIntradayGetResponse intraday_transaccion_intraday_get(fecha, nemo=nemo)

Obtiene las transacciones Intraday de un instrumento para una fecha.

Obtiene las transacciones Intraday de un instrumento para una fecha.

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
api_instance = riam_api_client.IntradayApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha. (optional)

try:
    # Obtiene las transacciones Intraday de un instrumento para una fecha.
    api_response = api_instance.intraday_transaccion_intraday_get(fecha, nemo=nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntradayApi->intraday_transaccion_intraday_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar. Si no se especifica se entregan todos los de la fecha. | [optional] 

### Return type

[**IntradayTransaccionIntradayGetResponse**](IntradayTransaccionIntradayGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intraday_valorizacion_intraday_calculadora**
> IntradayValorizacionIntradayCalculadoraResponse intraday_valorizacion_intraday_calculadora(nemo, fecha, nominal=nominal, condicion_pago=condicion_pago)

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
api_instance = riam_api_client.IntradayApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotecnico del instrumento a valorizar
fecha = '2013-10-20' # date | Fecha para la cual se efectua la valorización
nominal = 1.2 # float | Nominal a valorizar. Si no se carga se asume 1000 (optional)
condicion_pago = 'condicion_pago_example' # str | Condicion de Pago. Las opciones posibles son: PH, PM, CN. (optional)

try:
    # Obtiene la valorización de un instrumento.
    api_response = api_instance.intraday_valorizacion_intraday_calculadora(nemo, fecha, nominal=nominal, condicion_pago=condicion_pago)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntradayApi->intraday_valorizacion_intraday_calculadora: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotecnico del instrumento a valorizar | 
 **fecha** | **date**| Fecha para la cual se efectua la valorización | 
 **nominal** | **float**| Nominal a valorizar. Si no se carga se asume 1000 | [optional] 
 **condicion_pago** | **str**| Condicion de Pago. Las opciones posibles son: PH, PM, CN. | [optional] 

### Return type

[**IntradayValorizacionIntradayCalculadoraResponse**](IntradayValorizacionIntradayCalculadoraResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intraday_valorizacion_intraday_familia_get**
> IntradayValorizacionIntradayFamiliaGetResponse intraday_valorizacion_intraday_familia_get(fecha, familia, ultimo_remate=ultimo_remate)

Obtiene las valorizaciones Intraday para una familia para una fecha.

Obtiene las valorizaciones Intraday para una familia  para una fecha.

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
api_instance = riam_api_client.IntradayApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
familia = 'familia_example' # str | familia a consultar. Ejemplo: BE, BB, BS, BCU, etc
ultimo_remate = true # bool | Si es 1, entrega solo la valorizacion del ultimo remate disponible de cada instrumento en vez de todos los remates del dia (optional)

try:
    # Obtiene las valorizaciones Intraday para una familia para una fecha.
    api_response = api_instance.intraday_valorizacion_intraday_familia_get(fecha, familia, ultimo_remate=ultimo_remate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntradayApi->intraday_valorizacion_intraday_familia_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **familia** | **str**| familia a consultar. Ejemplo: BE, BB, BS, BCU, etc | 
 **ultimo_remate** | **bool**| Si es 1, entrega solo la valorizacion del ultimo remate disponible de cada instrumento en vez de todos los remates del dia | [optional] 

### Return type

[**IntradayValorizacionIntradayFamiliaGetResponse**](IntradayValorizacionIntradayFamiliaGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intraday_valorizacion_intraday_get**
> IntradayValorizacionIntradayGetResponse intraday_valorizacion_intraday_get(fecha, nemo, ultimo_remate=ultimo_remate)

Obtiene las valorizaciones Intraday de un Instrumento para una fecha.

Obtiene las valorizaciones Intraday de un Instrumento para una fecha.

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
api_instance = riam_api_client.IntradayApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
ultimo_remate = true # bool | Si es 1, entrega solo la valorizacion del ultimo remate disponible en vez de todos los remates del dia (optional)

try:
    # Obtiene las valorizaciones Intraday de un Instrumento para una fecha.
    api_response = api_instance.intraday_valorizacion_intraday_get(fecha, nemo, ultimo_remate=ultimo_remate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntradayApi->intraday_valorizacion_intraday_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **ultimo_remate** | **bool**| Si es 1, entrega solo la valorizacion del ultimo remate disponible en vez de todos los remates del dia | [optional] 

### Return type

[**IntradayValorizacionIntradayGetResponse**](IntradayValorizacionIntradayGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

