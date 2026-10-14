# riam_api_client.FondosCarterasApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fondos_carteras_carteras_get_fecha**](FondosCarterasApi.md#fondos_carteras_carteras_get_fecha) | **POST** /Outputs/Generic/Fondos/Carteras/getFecha | Obtiene la composición de cartera mensual para los fondos de un tipo en el mes de la fecha consultada.
[**fondos_carteras_carteras_get_fondo**](FondosCarterasApi.md#fondos_carteras_carteras_get_fondo) | **POST** /Outputs/Generic/Fondos/Carteras/getFondo | Obtiene la composición de cartera mensual de un fondo específico en el mes de la fecha consultada.
[**fondos_carteras_carteras_get_ultima_fecha**](FondosCarterasApi.md#fondos_carteras_carteras_get_ultima_fecha) | **POST** /Outputs/Generic/Fondos/Carteras/getUltimaFecha | Obtiene la última fecha de cartera disponible para un tipo de fondo.

# **fondos_carteras_carteras_get_fecha**
> FondosCarterasCarterasGetFechaResponse fondos_carteras_carteras_get_fecha(fecha, tipo_fondo, categoria_aafm=categoria_aafm, rut_desde=rut_desde, page_size=page_size)

Obtiene la composición de cartera mensual para los fondos de un tipo en el mes de la fecha consultada.

La respuesta está paginada por fondo (keyset sobre el rut) para acotar el volumen: cada llamada devuelve a lo más {pageSize} fondos, ordenados por rut ascendente. Para recorrer todo el universo, el cliente repite la llamada pasando en {rutDesde} el mayor rut recibido en la página anterior, y se detiene cuando una página vuelve vacía. La cartera de un fondo nunca se parte entre páginas.

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
api_instance = riam_api_client.FondosCarterasApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar (se usa el mes y año)
tipo_fondo = 'tipo_fondo_example' # str | Tipo de fondo: CFM o CFI
categoria_aafm = 'categoria_aafm_example' # str | Nombre de la categoría AAFM para filtrar (solo aplica a CFM). Si se omite, se retornan todos los fondos del tipo. (optional)
rut_desde = 56 # int | Paginación: rut del último fondo recibido en la página anterior. Se devuelven los fondos con rut mayor. Omitir (o 0) para la primera página. (optional)
page_size = 56 # int | Cantidad de fondos por página (default 50, máximo 100). (optional)

try:
    # Obtiene la composición de cartera mensual para los fondos de un tipo en el mes de la fecha consultada.
    api_response = api_instance.fondos_carteras_carteras_get_fecha(fecha, tipo_fondo, categoria_aafm=categoria_aafm, rut_desde=rut_desde, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosCarterasApi->fondos_carteras_carteras_get_fecha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar (se usa el mes y año) | 
 **tipo_fondo** | **str**| Tipo de fondo: CFM o CFI | 
 **categoria_aafm** | **str**| Nombre de la categoría AAFM para filtrar (solo aplica a CFM). Si se omite, se retornan todos los fondos del tipo. | [optional] 
 **rut_desde** | **int**| Paginación: rut del último fondo recibido en la página anterior. Se devuelven los fondos con rut mayor. Omitir (o 0) para la primera página. | [optional] 
 **page_size** | **int**| Cantidad de fondos por página (default 50, máximo 100). | [optional] 

### Return type

[**FondosCarterasCarterasGetFechaResponse**](FondosCarterasCarterasGetFechaResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_carteras_carteras_get_fondo**
> FondosCarterasCarterasGetFondoResponse fondos_carteras_carteras_get_fondo(fecha, rut)

Obtiene la composición de cartera mensual de un fondo específico en el mes de la fecha consultada.

Obtiene la composición de cartera mensual de un fondo específico en el mes de la fecha consultada.

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
api_instance = riam_api_client.FondosCarterasApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar (se usa el mes y año)
rut = 56 # int | Rut del Fondo (sin dígito verificador)

try:
    # Obtiene la composición de cartera mensual de un fondo específico en el mes de la fecha consultada.
    api_response = api_instance.fondos_carteras_carteras_get_fondo(fecha, rut)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosCarterasApi->fondos_carteras_carteras_get_fondo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar (se usa el mes y año) | 
 **rut** | **int**| Rut del Fondo (sin dígito verificador) | 

### Return type

[**FondosCarterasCarterasGetFondoResponse**](FondosCarterasCarterasGetFondoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_carteras_carteras_get_ultima_fecha**
> FondosCarterasCarterasGetUltimaFechaResponse fondos_carteras_carteras_get_ultima_fecha(tipo_fondo)

Obtiene la última fecha de cartera disponible para un tipo de fondo.

Obtiene la última fecha de cartera disponible para un tipo de fondo.

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
api_instance = riam_api_client.FondosCarterasApi(riam_api_client.ApiClient(configuration))
tipo_fondo = 'tipo_fondo_example' # str | Tipo de fondo: CFM o CFI

try:
    # Obtiene la última fecha de cartera disponible para un tipo de fondo.
    api_response = api_instance.fondos_carteras_carteras_get_ultima_fecha(tipo_fondo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosCarterasApi->fondos_carteras_carteras_get_ultima_fecha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tipo_fondo** | **str**| Tipo de fondo: CFM o CFI | 

### Return type

[**FondosCarterasCarterasGetUltimaFechaResponse**](FondosCarterasCarterasGetUltimaFechaResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

