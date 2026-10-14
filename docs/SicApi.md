# riam_api_client.SicApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sic_ajuste_tipo_i_download_file**](SicApi.md#sic_ajuste_tipo_i_download_file) | **POST** /Outputs/Generic/SIC/AjusteTipoI/downloadFile | Descarga la cartera ajustada Descarga la cartera ajustada
[**sic_ajuste_tipo_i_get_parametros**](SicApi.md#sic_ajuste_tipo_i_get_parametros) | **POST** /Outputs/Generic/SIC/AjusteTipoI/getParametros | Obtiene el listado de los parámetros posibles a ser usados en un ajuste.
[**sic_ajuste_tipo_i_get_resultado**](SicApi.md#sic_ajuste_tipo_i_get_resultado) | **POST** /Outputs/Generic/SIC/AjusteTipoI/getResultado | Genera y muestra la cartera ajustada.
[**sic_detalle_cartera_get_table**](SicApi.md#sic_detalle_cartera_get_table) | **POST** /Outputs/Generic/SIC/DetalleCartera/getTable | Obtiene la informacion de detalle de cartera para un fondo y un tipo de activo
[**sic_general_get_ejercicios**](SicApi.md#sic_general_get_ejercicios) | **POST** /Outputs/Generic/SIC/General/getEjercicios | Obtiene el listado de los ejercicios vigentes
[**sic_general_get_fondos**](SicApi.md#sic_general_get_fondos) | **POST** /Outputs/Generic/SIC/General/getFondos | Obtiene el listado de los fondos existentes.
[**sic_performance_get_orden**](SicApi.md#sic_performance_get_orden) | **POST** /Outputs/Generic/SIC/Performance/getOrden | Obtiene el listado de los idOrden por tipo de Activo
[**sic_performance_get_resumen**](SicApi.md#sic_performance_get_resumen) | **POST** /Outputs/Generic/SIC/Performance/getResumen | Obtiene el resumen del performance para un horizonte y idEjercicio dado
[**sic_performance_get_table**](SicApi.md#sic_performance_get_table) | **POST** /Outputs/Generic/SIC/Performance/getTable | Obtiene la tabla del performance para un tipo de analisis, para un tipo de activo, para un horizonte, un idEjercicio
[**sic_upload_upload**](SicApi.md#sic_upload_upload) | **POST** /Outputs/Generic/SIC/Upload/upload | Carga un archivo al módulo de Sistema Integrado de Carteras (SIC).

# **sic_ajuste_tipo_i_download_file**
> SicAjusteTipoIDownloadFileResponse sic_ajuste_tipo_i_download_file(id_parametro, id_ajuste_file_type)

Descarga la cartera ajustada Descarga la cartera ajustada

Descarga la cartera ajustada Descarga la cartera ajustada

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))
id_parametro = 56 # int | Identificador del set de parámetros a usar ( Se obtiene del método Generic/SIC/AjusteTipoI/getParametros
id_ajuste_file_type = 56 # int | Identificador del tipo de salida a generar ( 1=XML_RF, 2=XML_DERIVADOS, 4=XML_CONSOLIDADO)

try:
    # Descarga la cartera ajustada Descarga la cartera ajustada
    api_response = api_instance.sic_ajuste_tipo_i_download_file(id_parametro, id_ajuste_file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_ajuste_tipo_i_download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_parametro** | **int**| Identificador del set de parámetros a usar ( Se obtiene del método Generic/SIC/AjusteTipoI/getParametros | 
 **id_ajuste_file_type** | **int**| Identificador del tipo de salida a generar ( 1&#x3D;XML_RF, 2&#x3D;XML_DERIVADOS, 4&#x3D;XML_CONSOLIDADO) | 

### Return type

[**SicAjusteTipoIDownloadFileResponse**](SicAjusteTipoIDownloadFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_ajuste_tipo_i_get_parametros**
> SicAjusteTipoIGetParametrosResponse sic_ajuste_tipo_i_get_parametros()

Obtiene el listado de los parámetros posibles a ser usados en un ajuste.

Obtiene el listado de los parámetros posibles a ser usados en un ajuste. Nuevos parámetros pueden ser creados en el sitio web apps.riskamerica.com.

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene el listado de los parámetros posibles a ser usados en un ajuste.
    api_response = api_instance.sic_ajuste_tipo_i_get_parametros()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_ajuste_tipo_i_get_parametros: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SicAjusteTipoIGetParametrosResponse**](SicAjusteTipoIGetParametrosResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_ajuste_tipo_i_get_resultado**
> SicAjusteTipoIGetResultadoResponse sic_ajuste_tipo_i_get_resultado(id_fondo, id_parametro, fecha)

Genera y muestra la cartera ajustada.

Genera y muestra la cartera ajustada.

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))
id_fondo = 56 # int | Identificador del fondo al cual realizar el ajuste ( Se obtiene del método Generic/SIC/General/getFondos )
id_parametro = 56 # int | Identificador del set de parámetros a usar ( Se obtiene del método Generic/SIC/AjusteTipoI/getParametros )
fecha = '2013-10-20' # date | Fecha de la cartera a la cual realizarle el ajuste

try:
    # Genera y muestra la cartera ajustada.
    api_response = api_instance.sic_ajuste_tipo_i_get_resultado(id_fondo, id_parametro, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_ajuste_tipo_i_get_resultado: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_fondo** | **int**| Identificador del fondo al cual realizar el ajuste ( Se obtiene del método Generic/SIC/General/getFondos ) | 
 **id_parametro** | **int**| Identificador del set de parámetros a usar ( Se obtiene del método Generic/SIC/AjusteTipoI/getParametros ) | 
 **fecha** | **date**| Fecha de la cartera a la cual realizarle el ajuste | 

### Return type

[**SicAjusteTipoIGetResultadoResponse**](SicAjusteTipoIGetResultadoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_detalle_cartera_get_table**
> SicDetalleCarteraGetTableResponse sic_detalle_cartera_get_table(fecha, id_fondo, tipo_activo)

Obtiene la informacion de detalle de cartera para un fondo y un tipo de activo

Obtiene la informacion de detalle de cartera para un fondo y un tipo de activo

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
id_fondo = 56 # int | idFondo a consutal
tipo_activo = 'tipo_activo_example' # str | tipo de activo. RFN, RFI, RVN, RVI, DERIVADOS

try:
    # Obtiene la informacion de detalle de cartera para un fondo y un tipo de activo
    api_response = api_instance.sic_detalle_cartera_get_table(fecha, id_fondo, tipo_activo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_detalle_cartera_get_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **id_fondo** | **int**| idFondo a consutal | 
 **tipo_activo** | **str**| tipo de activo. RFN, RFI, RVN, RVI, DERIVADOS | 

### Return type

[**SicDetalleCarteraGetTableResponse**](SicDetalleCarteraGetTableResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_general_get_ejercicios**
> SicGeneralGetEjerciciosResponse sic_general_get_ejercicios(id_fondo)

Obtiene el listado de los ejercicios vigentes

Obtiene el listado de los fondos existentes para el idFondo

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))
id_fondo = 56 # int | Identificador del fondo para el cual obtener los ejercicios

try:
    # Obtiene el listado de los ejercicios vigentes
    api_response = api_instance.sic_general_get_ejercicios(id_fondo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_general_get_ejercicios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_fondo** | **int**| Identificador del fondo para el cual obtener los ejercicios | 

### Return type

[**SicGeneralGetEjerciciosResponse**](SicGeneralGetEjerciciosResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_general_get_fondos**
> SicGeneralGetFondosResponse sic_general_get_fondos()

Obtiene el listado de los fondos existentes.

Obtiene el listado de los fondos existentes para la API KEY suministrada

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene el listado de los fondos existentes.
    api_response = api_instance.sic_general_get_fondos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_general_get_fondos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SicGeneralGetFondosResponse**](SicGeneralGetFondosResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_performance_get_orden**
> SicPerformanceGetOrdenResponse sic_performance_get_orden(id_ejercicio, tipo_activo)

Obtiene el listado de los idOrden por tipo de Activo

Obtiene el listado de los idOrden por tipo de Activo

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))
id_ejercicio = 56 # int | idEjercicio a Consultar
tipo_activo = 'tipo_activo_example' # str | tipo de activo. RFN, RFI, RVN, RVI, DERIVADOS

try:
    # Obtiene el listado de los idOrden por tipo de Activo
    api_response = api_instance.sic_performance_get_orden(id_ejercicio, tipo_activo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_performance_get_orden: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_ejercicio** | **int**| idEjercicio a Consultar | 
 **tipo_activo** | **str**| tipo de activo. RFN, RFI, RVN, RVI, DERIVADOS | 

### Return type

[**SicPerformanceGetOrdenResponse**](SicPerformanceGetOrdenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_performance_get_resumen**
> SicPerformanceGetResumenResponse sic_performance_get_resumen(fecha, horizonte, id_ejercicio)

Obtiene el resumen del performance para un horizonte y idEjercicio dado

Obtiene el resumen del performance para un horizonte y idEjercicio dado

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
horizonte = 'horizonte_example' # str | Horizonte a consultar. YTD, MTD o Diario
id_ejercicio = 56 # int | idEjercicio a Consultar

try:
    # Obtiene el resumen del performance para un horizonte y idEjercicio dado
    api_response = api_instance.sic_performance_get_resumen(fecha, horizonte, id_ejercicio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_performance_get_resumen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **horizonte** | **str**| Horizonte a consultar. YTD, MTD o Diario | 
 **id_ejercicio** | **int**| idEjercicio a Consultar | 

### Return type

[**SicPerformanceGetResumenResponse**](SicPerformanceGetResumenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_performance_get_table**
> SicPerformanceGetTableResponse sic_performance_get_table(fecha, tipo_activo, tabla_analisis, horizonte, id_ejercicio, tipo_portafolio, id_orden, tipo_performance=tipo_performance)

Obtiene la tabla del performance para un tipo de analisis, para un tipo de activo, para un horizonte, un idEjercicio

Obtiene la tabla del performance para un tipo de analisis, para un tipo de activo, para un horizonte, un idEjercicio

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
tipo_activo = 'tipo_activo_example' # str | tipo de activo. RFN, RFI, RVN, RVI, DERIVADOS
tabla_analisis = 'tabla_analisis_example' # str | tabla del analisis a obtener. Pesos, Pesos_Contra_Total (%Fondo), Montos (MM$), Retornos, ContribRetornos, Performance
horizonte = 'horizonte_example' # str | Horizonte a consultar. YTD, MTD o Diario
id_ejercicio = 56 # int | idEjercicio a Consultar
tipo_portafolio = 'tipo_portafolio_example' # str | tipo de Portafolio. Fondo, Benchmark, Diferencia
id_orden = 56 # int | idOrden obtenido de getidOrden
tipo_performance = 'tipo_performance_example' # str | tipo de Performance. Solo se utiliza cuando la tablaAnalisis es igual a \"Performance\" (optional)

try:
    # Obtiene la tabla del performance para un tipo de analisis, para un tipo de activo, para un horizonte, un idEjercicio
    api_response = api_instance.sic_performance_get_table(fecha, tipo_activo, tabla_analisis, horizonte, id_ejercicio, tipo_portafolio, id_orden, tipo_performance=tipo_performance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_performance_get_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **tipo_activo** | **str**| tipo de activo. RFN, RFI, RVN, RVI, DERIVADOS | 
 **tabla_analisis** | **str**| tabla del analisis a obtener. Pesos, Pesos_Contra_Total (%Fondo), Montos (MM$), Retornos, ContribRetornos, Performance | 
 **horizonte** | **str**| Horizonte a consultar. YTD, MTD o Diario | 
 **id_ejercicio** | **int**| idEjercicio a Consultar | 
 **tipo_portafolio** | **str**| tipo de Portafolio. Fondo, Benchmark, Diferencia | 
 **id_orden** | **int**| idOrden obtenido de getidOrden | 
 **tipo_performance** | **str**| tipo de Performance. Solo se utiliza cuando la tablaAnalisis es igual a \&quot;Performance\&quot; | [optional] 

### Return type

[**SicPerformanceGetTableResponse**](SicPerformanceGetTableResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sic_upload_upload**
> SicUploadUploadResponse sic_upload_upload(file, id_file_type)

Carga un archivo al módulo de Sistema Integrado de Carteras (SIC).

Carga un archivo al módulo de Sistema Integrado de Carteras (SIC).<br> En caso de que existan problemas serios con la carga se devolvera un error de tipo SIC_FILE_INVALID_FORMAT.<br> En caso de que existan problemas con algunos registros del archivo cargado se devolverá el status WARNING y dentro de los issue se especificarán los problemas encontrados. Una carga exitosa sin problemas es identificada por status OK.

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
api_instance = riam_api_client.SicApi(riam_api_client.ApiClient(configuration))
file = 'file_example' # str | 
id_file_type = 'id_file_type_example' # str | Tipo de Archivo a cargar (1: CSV, 2: XLS, 3: XML)

try:
    # Carga un archivo al módulo de Sistema Integrado de Carteras (SIC).
    api_response = api_instance.sic_upload_upload(file, id_file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_upload_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **id_file_type** | **str**| Tipo de Archivo a cargar (1: CSV, 2: XLS, 3: XML) | 

### Return type

[**SicUploadUploadResponse**](SicUploadUploadResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

