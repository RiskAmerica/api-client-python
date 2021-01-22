# riam_api_client.RFNInformacionApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_informacion_informacion_get**](RFNInformacionApi.md#r_fn_informacion_informacion_get) | **POST** /Outputs/Generic/InformacionRF/Informacion/get | Obtiene la información del Instrumento.
[**r_fn_informacion_informacion_get_interval_tasa_prepago**](RFNInformacionApi.md#r_fn_informacion_informacion_get_interval_tasa_prepago) | **POST** /Outputs/Generic/InformacionRF/Informacion/getIntervalTasaPrepago | Obtiene las tasas de prepago de un instrumento, en un invervalo de tiempo.
[**r_fn_informacion_informacion_get_prepagos_historicos**](RFNInformacionApi.md#r_fn_informacion_informacion_get_prepagos_historicos) | **POST** /Outputs/Generic/InformacionRF/Informacion/getPrepagosHistoricos | Obtiene los prepagos realizados.
[**r_fn_informacion_informacion_get_tasa_prepago**](RFNInformacionApi.md#r_fn_informacion_informacion_get_tasa_prepago) | **POST** /Outputs/Generic/InformacionRF/Informacion/getTasaPrepago | Obtiene las tasas de prepago.
[**r_fn_informacion_liquidez_get**](RFNInformacionApi.md#r_fn_informacion_liquidez_get) | **POST** /Outputs/Generic/InformacionRF/Liquidez/get | Obtiene información de liquidez de un instrumento.
[**r_fn_informacion_liquidez_get_interval_ncg**](RFNInformacionApi.md#r_fn_informacion_liquidez_get_interval_ncg) | **POST** /Outputs/Generic/InformacionRF/Liquidez/getIntervalNCG | Obtiene información histórica del monto transado promedio definido por la Norma de Caracter General N°376.
[**r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto**](RFNInformacionApi.md#r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto) | **POST** /Outputs/Generic/InformacionRF/Liquidez/getIntervalSaldoCustodiaInsoluto | Obtiene información histórica del saldo insoluto.
[**r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal**](RFNInformacionApi.md#r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal) | **POST** /Outputs/Generic/InformacionRF/Liquidez/getIntervalSaldoCustodiaNominal | Obtiene información histórica del saldo de custodia nominal.
[**r_fn_informacion_riesgo_get**](RFNInformacionApi.md#r_fn_informacion_riesgo_get) | **POST** /Outputs/Generic/InformacionRF/Riesgo/get | Obtiene los cambios de clasificación de riesgo de un instrumento.
[**r_fn_informacion_tabla_desarrollo_get_cupones_futuros**](RFNInformacionApi.md#r_fn_informacion_tabla_desarrollo_get_cupones_futuros) | **POST** /Outputs/Generic/InformacionRF/TablaDesarrollo/getCuponesFuturos | Obtiene la tabla de desarrollo residual para un instrumento particular.

# **r_fn_informacion_informacion_get**
> InlineResponse20024 r_fn_informacion_informacion_get(nemo)

Obtiene la información del Instrumento.

Obtiene la información del Instrumento a la fecha de hoy.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene la información del Instrumento.
    api_response = api_instance.r_fn_informacion_informacion_get(nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_informacion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_interval_tasa_prepago**
> InlineResponse20026 r_fn_informacion_informacion_get_interval_tasa_prepago(nemo, fecha_min, fecha_max)

Obtiene las tasas de prepago de un instrumento, en un invervalo de tiempo.

Obtiene las tasas de prepago de un instrumento, en un invervalo de tiempo.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
fecha_min = '2013-10-20' # date | Límite inferior del intervalo de consulta
fecha_max = '2013-10-20' # date | Límite superior del intervalo de consulta

try:
    # Obtiene las tasas de prepago de un instrumento, en un invervalo de tiempo.
    api_response = api_instance.r_fn_informacion_informacion_get_interval_tasa_prepago(nemo, fecha_min, fecha_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_informacion_get_interval_tasa_prepago: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **fecha_min** | **date**| Límite inferior del intervalo de consulta | 
 **fecha_max** | **date**| Límite superior del intervalo de consulta | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_prepagos_historicos**
> InlineResponse20027 r_fn_informacion_informacion_get_prepagos_historicos(nemo)

Obtiene los prepagos realizados.

Obtiene una lista con la historia de los prepagos realizados.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene los prepagos realizados.
    api_response = api_instance.r_fn_informacion_informacion_get_prepagos_historicos(nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_informacion_get_prepagos_historicos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_tasa_prepago**
> InlineResponse20025 r_fn_informacion_informacion_get_tasa_prepago(nemo, fecha)

Obtiene las tasas de prepago.

Obtiene las tasas de prepago para una fecha determinada.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
fecha = '2013-10-20' # date | Fecha de consulta

try:
    # Obtiene las tasas de prepago.
    api_response = api_instance.r_fn_informacion_informacion_get_tasa_prepago(nemo, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_informacion_get_tasa_prepago: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **fecha** | **date**| Fecha de consulta | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_liquidez_get**
> InlineResponse20029 r_fn_informacion_liquidez_get(nemo, fecha)

Obtiene información de liquidez de un instrumento.

Obtiene información de liquidez de un instrumento para una fecha determinada.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
fecha = '2013-10-20' # date | Fecha de consulta

try:
    # Obtiene información de liquidez de un instrumento.
    api_response = api_instance.r_fn_informacion_liquidez_get(nemo, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_liquidez_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **fecha** | **date**| Fecha de consulta | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_liquidez_get_interval_ncg**
> InlineResponse20032 r_fn_informacion_liquidez_get_interval_ncg(nemo, fecha_min, fecha_max)

Obtiene información histórica del monto transado promedio definido por la Norma de Caracter General N°376.

Obtiene información histórica del monto transado promedio definido por la Norma de Caracter General N°376.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
fecha_min = '2013-10-20' # date | Límite inferior del intervalo a consultar
fecha_max = '2013-10-20' # date | Límite superior del intervalo a consultar

try:
    # Obtiene información histórica del monto transado promedio definido por la Norma de Caracter General N°376.
    api_response = api_instance.r_fn_informacion_liquidez_get_interval_ncg(nemo, fecha_min, fecha_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_liquidez_get_interval_ncg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **fecha_min** | **date**| Límite inferior del intervalo a consultar | 
 **fecha_max** | **date**| Límite superior del intervalo a consultar | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto**
> InlineResponse20031 r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto(nemo, fecha_min, fecha_max)

Obtiene información histórica del saldo insoluto.

Obtiene información histórica del saldo insoluto.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
fecha_min = '2013-10-20' # date | Límite inferior del intervalo a consultar
fecha_max = '2013-10-20' # date | Límite superior del intervalo a consultar

try:
    # Obtiene información histórica del saldo insoluto.
    api_response = api_instance.r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto(nemo, fecha_min, fecha_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **fecha_min** | **date**| Límite inferior del intervalo a consultar | 
 **fecha_max** | **date**| Límite superior del intervalo a consultar | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal**
> InlineResponse20030 r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal(nemo, fecha_min, fecha_max)

Obtiene información histórica del saldo de custodia nominal.

Obtiene información histórica del saldo de custodia nominal.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar
fecha_min = '2013-10-20' # date | Límite inferior del intervalo a consultar
fecha_max = '2013-10-20' # date | Límite superior del intervalo a consultar

try:
    # Obtiene información histórica del saldo de custodia nominal.
    api_response = api_instance.r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal(nemo, fecha_min, fecha_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 
 **fecha_min** | **date**| Límite inferior del intervalo a consultar | 
 **fecha_max** | **date**| Límite superior del intervalo a consultar | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_riesgo_get**
> InlineResponse20028 r_fn_informacion_riesgo_get(nemo)

Obtiene los cambios de clasificación de riesgo de un instrumento.

Obtiene los cambios de clasificación de riesgo asignadas a un instrumento.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar

try:
    # Obtiene los cambios de clasificación de riesgo de un instrumento.
    api_response = api_instance.r_fn_informacion_riesgo_get(nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_riesgo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_tabla_desarrollo_get_cupones_futuros**
> InlineResponse20033 r_fn_informacion_tabla_desarrollo_get_cupones_futuros(nemo, fecha)

Obtiene la tabla de desarrollo residual para un instrumento particular.

Obtiene la tabla de desarrollo residual para un instrumento particular.

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
api_instance = riam_api_client.RFNInformacionApi(riam_api_client.ApiClient(configuration))
nemo = '2013-10-20' # date | Nemotecnico a consultar
fecha = '2013-10-20' # date | Fecha a consultar

try:
    # Obtiene la tabla de desarrollo residual para un instrumento particular.
    api_response = api_instance.r_fn_informacion_tabla_desarrollo_get_cupones_futuros(nemo, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_tabla_desarrollo_get_cupones_futuros: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **date**| Nemotecnico a consultar | 
 **fecha** | **date**| Fecha a consultar | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

