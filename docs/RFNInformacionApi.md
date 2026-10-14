# riam_api_client.RFNInformacionApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_informacion_informacion_get**](RFNInformacionApi.md#r_fn_informacion_informacion_get) | **POST** /Outputs/Generic/InformacionRF/Informacion/get | Obtiene la información del Instrumento.
[**r_fn_informacion_informacion_get_all**](RFNInformacionApi.md#r_fn_informacion_informacion_get_all) | **POST** /Outputs/Generic/InformacionRF/Informacion/getAll | Obtiene la información de Instrumentos vigentes para una familia.
[**r_fn_informacion_informacion_get_familias**](RFNInformacionApi.md#r_fn_informacion_informacion_get_familias) | **POST** /Outputs/Generic/InformacionRF/Informacion/getFamilias | Obtiene las familias de instrumentos disponibles.
[**r_fn_informacion_informacion_get_interval_tasa_prepago**](RFNInformacionApi.md#r_fn_informacion_informacion_get_interval_tasa_prepago) | **POST** /Outputs/Generic/InformacionRF/Informacion/getIntervalTasaPrepago | Obtiene las tasas de prepago de un instrumento, en un invervalo de tiempo.
[**r_fn_informacion_informacion_get_prepagos_historicos**](RFNInformacionApi.md#r_fn_informacion_informacion_get_prepagos_historicos) | **POST** /Outputs/Generic/InformacionRF/Informacion/getPrepagosHistoricos | Obtiene los prepagos realizados.
[**r_fn_informacion_informacion_get_tasa_prepago**](RFNInformacionApi.md#r_fn_informacion_informacion_get_tasa_prepago) | **POST** /Outputs/Generic/InformacionRF/Informacion/getTasaPrepago | Obtiene las tasas de prepago.
[**r_fn_informacion_informacion_get_vigentes**](RFNInformacionApi.md#r_fn_informacion_informacion_get_vigentes) | **POST** /Outputs/Generic/InformacionRF/Informacion/getVigentes | Obtiene la lista de instrumentos vigentes para una fecha.
[**r_fn_informacion_liquidez_get**](RFNInformacionApi.md#r_fn_informacion_liquidez_get) | **POST** /Outputs/Generic/InformacionRF/Liquidez/get | Obtiene información de liquidez de un instrumento.
[**r_fn_informacion_liquidez_get_interval_ncg**](RFNInformacionApi.md#r_fn_informacion_liquidez_get_interval_ncg) | **POST** /Outputs/Generic/InformacionRF/Liquidez/getIntervalNCG | Obtiene información histórica del monto transado promedio definido por la Norma de Caracter General N°376.
[**r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto**](RFNInformacionApi.md#r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto) | **POST** /Outputs/Generic/InformacionRF/Liquidez/getIntervalSaldoCustodiaInsoluto | Obtiene información histórica del saldo insoluto.
[**r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal**](RFNInformacionApi.md#r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal) | **POST** /Outputs/Generic/InformacionRF/Liquidez/getIntervalSaldoCustodiaNominal | Obtiene información histórica del saldo de custodia nominal.
[**r_fn_informacion_riesgo_get**](RFNInformacionApi.md#r_fn_informacion_riesgo_get) | **POST** /Outputs/Generic/InformacionRF/Riesgo/get | Obtiene los cambios de clasificación de riesgo de uno o más instrumentos.
[**r_fn_informacion_riesgo_get_clasificadora**](RFNInformacionApi.md#r_fn_informacion_riesgo_get_clasificadora) | **POST** /Outputs/Generic/InformacionRF/Riesgo/getClasificadora | Obtiene la clasificación vigente de cada clasificadora para uno o más instrumentos, para la fecha de hoy.
[**r_fn_informacion_tabla_desarrollo_get_cambios_tabla_desarrollo**](RFNInformacionApi.md#r_fn_informacion_tabla_desarrollo_get_cambios_tabla_desarrollo) | **POST** /Outputs/Generic/InformacionRF/TablaDesarrollo/getCambiosTablaDesarrollo | Obtiene la lista de cambios de tablas de desarrollo de los últimos 90 días.
[**r_fn_informacion_tabla_desarrollo_get_cupones_futuros**](RFNInformacionApi.md#r_fn_informacion_tabla_desarrollo_get_cupones_futuros) | **POST** /Outputs/Generic/InformacionRF/TablaDesarrollo/getCuponesFuturos | Obtiene la tabla de desarrollo residual para un instrumento particular.

# **r_fn_informacion_informacion_get**
> RFNInformacionInformacionGetResponse r_fn_informacion_informacion_get(nemo)

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

[**RFNInformacionInformacionGetResponse**](RFNInformacionInformacionGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_all**
> RFNInformacionInformacionGetAllResponse r_fn_informacion_informacion_get_all(familia, nemo_desde=nemo_desde, page_size=page_size)

Obtiene la información de Instrumentos vigentes para una familia.

Obtiene la información de Instrumentos vigentes a la fecha de hoy para una familia.  La respuesta está paginada por instrumento (keyset sobre el nemo) para acotar el volumen: cada llamada devuelve a lo más {pageSize} instrumentos, ordenados por nemo ascendente. Para recorrer toda la familia, el cliente repite la llamada pasando en {nemoDesde} el mayor nemo recibido en la página anterior, y se detiene cuando una página vuelve vacía.

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
familia = 'familia_example' # str | familia a consultar. Ejemplo: BE, BB, BS, BCU, etc
nemo_desde = 'nemo_desde_example' # str | Paginación: nemo del último instrumento recibido en la página anterior. Se devuelven los instrumentos con nemo \"mayor\". Omitir para la primera página. (optional)
page_size = 56 # int | Cantidad de instrumentos por página (default 900, máximo 1000). (optional)

try:
    # Obtiene la información de Instrumentos vigentes para una familia.
    api_response = api_instance.r_fn_informacion_informacion_get_all(familia, nemo_desde=nemo_desde, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_informacion_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **familia** | **str**| familia a consultar. Ejemplo: BE, BB, BS, BCU, etc | 
 **nemo_desde** | **str**| Paginación: nemo del último instrumento recibido en la página anterior. Se devuelven los instrumentos con nemo \&quot;mayor\&quot;. Omitir para la primera página. | [optional] 
 **page_size** | **int**| Cantidad de instrumentos por página (default 900, máximo 1000). | [optional] 

### Return type

[**RFNInformacionInformacionGetAllResponse**](RFNInformacionInformacionGetAllResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_familias**
> RFNInformacionInformacionGetFamiliasResponse r_fn_informacion_informacion_get_familias()

Obtiene las familias de instrumentos disponibles.

Obtiene las familias de instrumentos disponibles.

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

try:
    # Obtiene las familias de instrumentos disponibles.
    api_response = api_instance.r_fn_informacion_informacion_get_familias()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_informacion_get_familias: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RFNInformacionInformacionGetFamiliasResponse**](RFNInformacionInformacionGetFamiliasResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_interval_tasa_prepago**
> RFNInformacionInformacionGetIntervalTasaPrepagoResponse r_fn_informacion_informacion_get_interval_tasa_prepago(nemo, fecha_min, fecha_max)

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

[**RFNInformacionInformacionGetIntervalTasaPrepagoResponse**](RFNInformacionInformacionGetIntervalTasaPrepagoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_prepagos_historicos**
> RFNInformacionInformacionGetPrepagosHistoricosResponse r_fn_informacion_informacion_get_prepagos_historicos(nemo)

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

[**RFNInformacionInformacionGetPrepagosHistoricosResponse**](RFNInformacionInformacionGetPrepagosHistoricosResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_tasa_prepago**
> RFNInformacionInformacionGetTasaPrepagoResponse r_fn_informacion_informacion_get_tasa_prepago(nemo, fecha)

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

[**RFNInformacionInformacionGetTasaPrepagoResponse**](RFNInformacionInformacionGetTasaPrepagoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_informacion_get_vigentes**
> RFNInformacionInformacionGetVigentesResponse r_fn_informacion_informacion_get_vigentes(fecha)

Obtiene la lista de instrumentos vigentes para una fecha.

Obtiene la lista de instrumentos vigentes para una fecha excluyendo depósitos y efectos de comercio ya que esos siempre se encuentran vigentes cuando tienen una fecha de vencimiento mayor a la fecha de consulta.

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
fecha = '2013-10-20' # date | Fecha de consulta

try:
    # Obtiene la lista de instrumentos vigentes para una fecha.
    api_response = api_instance.r_fn_informacion_informacion_get_vigentes(fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_informacion_get_vigentes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha de consulta | 

### Return type

[**RFNInformacionInformacionGetVigentesResponse**](RFNInformacionInformacionGetVigentesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_liquidez_get**
> RFNInformacionLiquidezGetResponse r_fn_informacion_liquidez_get(nemo, fecha)

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

[**RFNInformacionLiquidezGetResponse**](RFNInformacionLiquidezGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_liquidez_get_interval_ncg**
> RFNInformacionLiquidezGetIntervalNCGResponse r_fn_informacion_liquidez_get_interval_ncg(nemo, fecha_min, fecha_max)

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

[**RFNInformacionLiquidezGetIntervalNCGResponse**](RFNInformacionLiquidezGetIntervalNCGResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto**
> RFNInformacionLiquidezGetIntervalSaldoCustodiaInsolutoResponse r_fn_informacion_liquidez_get_interval_saldo_custodia_insoluto(nemo, fecha_min, fecha_max)

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

[**RFNInformacionLiquidezGetIntervalSaldoCustodiaInsolutoResponse**](RFNInformacionLiquidezGetIntervalSaldoCustodiaInsolutoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal**
> RFNInformacionLiquidezGetIntervalSaldoCustodiaNominalResponse r_fn_informacion_liquidez_get_interval_saldo_custodia_nominal(nemo, fecha_min, fecha_max)

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

[**RFNInformacionLiquidezGetIntervalSaldoCustodiaNominalResponse**](RFNInformacionLiquidezGetIntervalSaldoCustodiaNominalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_riesgo_get**
> RFNInformacionRiesgoGetResponse r_fn_informacion_riesgo_get(nemo)

Obtiene los cambios de clasificación de riesgo de uno o más instrumentos.

Obtiene los cambios de clasificación de riesgo asignadas a uno o más instrumentos.

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
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar. Se pueden especificar varios separando por 'pipes' (ASCII 124), máximo 20. IE: \"BACEN-A1

try:
    # Obtiene los cambios de clasificación de riesgo de uno o más instrumentos.
    api_response = api_instance.r_fn_informacion_riesgo_get(nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_riesgo_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar. Se pueden especificar varios separando por &#x27;pipes&#x27; (ASCII 124), máximo 20. IE: \&quot;BACEN-A1 | 

### Return type

[**RFNInformacionRiesgoGetResponse**](RFNInformacionRiesgoGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_riesgo_get_clasificadora**
> RFNInformacionRiesgoGetClasificadoraResponse r_fn_informacion_riesgo_get_clasificadora(nemo)

Obtiene la clasificación vigente de cada clasificadora para uno o más instrumentos, para la fecha de hoy.

Obtiene la clasificación vigente de cada clasificadora para uno o más instrumentos, para la fecha de hoy.

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
nemo = 'nemo_example' # str | Nemotécnico del instrumento a consultar. Se pueden especificar varios separando por 'pipes' (ASCII 124), máximo 20. IE: \"BACEN-A1

try:
    # Obtiene la clasificación vigente de cada clasificadora para uno o más instrumentos, para la fecha de hoy.
    api_response = api_instance.r_fn_informacion_riesgo_get_clasificadora(nemo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_riesgo_get_clasificadora: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotécnico del instrumento a consultar. Se pueden especificar varios separando por &#x27;pipes&#x27; (ASCII 124), máximo 20. IE: \&quot;BACEN-A1 | 

### Return type

[**RFNInformacionRiesgoGetClasificadoraResponse**](RFNInformacionRiesgoGetClasificadoraResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_tabla_desarrollo_get_cambios_tabla_desarrollo**
> RFNInformacionTablaDesarrolloGetCambiosTablaDesarrolloResponse r_fn_informacion_tabla_desarrollo_get_cambios_tabla_desarrollo(fecha)

Obtiene la lista de cambios de tablas de desarrollo de los últimos 90 días.

Obtiene la lista de cambios de tablas de desarrollo de los últimos 90 días.

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
fecha = '2013-10-20' # date | Fecha de consulta

try:
    # Obtiene la lista de cambios de tablas de desarrollo de los últimos 90 días.
    api_response = api_instance.r_fn_informacion_tabla_desarrollo_get_cambios_tabla_desarrollo(fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNInformacionApi->r_fn_informacion_tabla_desarrollo_get_cambios_tabla_desarrollo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha de consulta | 

### Return type

[**RFNInformacionTablaDesarrolloGetCambiosTablaDesarrolloResponse**](RFNInformacionTablaDesarrolloGetCambiosTablaDesarrolloResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_informacion_tabla_desarrollo_get_cupones_futuros**
> RFNInformacionTablaDesarrolloGetCuponesFuturosResponse r_fn_informacion_tabla_desarrollo_get_cupones_futuros(nemo, fecha)

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

[**RFNInformacionTablaDesarrolloGetCuponesFuturosResponse**](RFNInformacionTablaDesarrolloGetCuponesFuturosResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

