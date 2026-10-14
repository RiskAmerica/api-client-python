# riam_api_client.SvcApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**svc_handler_download_input_file**](SvcApi.md#svc_handler_download_input_file) | **POST** /Outputs/Generic/SVC/Handler/downloadInputFile | Descarga el archivo cargado
[**svc_handler_download_output_file**](SvcApi.md#svc_handler_download_output_file) | **POST** /Outputs/Generic/SVC/Handler/downloadOutputFile | Descarga el archivo salida
[**svc_handler_get_file_tasks**](SvcApi.md#svc_handler_get_file_tasks) | **POST** /Outputs/Generic/SVC/Handler/getFileTasks | Obtiene los FileTask disponibles
[**svc_handler_get_input_formats**](SvcApi.md#svc_handler_get_input_formats) | **POST** /Outputs/Generic/SVC/Handler/getInputFormats | Obtiene los formatos de carga
[**svc_handler_get_output_formats**](SvcApi.md#svc_handler_get_output_formats) | **POST** /Outputs/Generic/SVC/Handler/getOutputFormats | Obtiene los formatos de descarga
[**svc_handler_get_status**](SvcApi.md#svc_handler_get_status) | **POST** /Outputs/Generic/SVC/Handler/getStatus | Revisa el estado de un FileTask
[**svc_handler_get_tipo_valorizaciones**](SvcApi.md#svc_handler_get_tipo_valorizaciones) | **POST** /Outputs/Generic/SVC/Handler/getTipoValorizaciones | Obtiene los tipos de valorizaciones
[**svc_handler_upload_file**](SvcApi.md#svc_handler_upload_file) | **POST** /Outputs/Generic/SVC/Handler/uploadFile | Envía un archivo al SVC

# **svc_handler_download_input_file**
> str svc_handler_download_input_file(id_file_task, fecha)

Descarga el archivo cargado

Descarga el archivo de INPUT el cual se subió para el FileTask pedido

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
api_instance = riam_api_client.SvcApi(riam_api_client.ApiClient(configuration))
id_file_task = 56 # int | Id FileTask para el cual se consulta (Obtenido del método getFileTasks)
fecha = '2013-10-20' # date | Fecha para la cual se esta descargando

try:
    # Descarga el archivo cargado
    api_response = api_instance.svc_handler_download_input_file(id_file_task, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SvcApi->svc_handler_download_input_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_file_task** | **int**| Id FileTask para el cual se consulta (Obtenido del método getFileTasks) | 
 **fecha** | **date**| Fecha para la cual se esta descargando | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svc_handler_download_output_file**
> str svc_handler_download_output_file(id_file_task, id_file_type, fecha)

Descarga el archivo salida

Descarga el archivo de OUTPUT solicitado para el FileTask pedido

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
api_instance = riam_api_client.SvcApi(riam_api_client.ApiClient(configuration))
id_file_task = 56 # int | Id FileTask para el cual se consulta (Obtenido del método getFileTasks)
id_file_type = 56 # int | Id del formato de descarga el cual se solicita (Obtenido del método getOutputFormats)
fecha = '2013-10-20' # date | Fecha para la cual se esta descargando

try:
    # Descarga el archivo salida
    api_response = api_instance.svc_handler_download_output_file(id_file_task, id_file_type, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SvcApi->svc_handler_download_output_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_file_task** | **int**| Id FileTask para el cual se consulta (Obtenido del método getFileTasks) | 
 **id_file_type** | **int**| Id del formato de descarga el cual se solicita (Obtenido del método getOutputFormats) | 
 **fecha** | **date**| Fecha para la cual se esta descargando | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svc_handler_get_file_tasks**
> SvcHandlerGetFileTasksResponse svc_handler_get_file_tasks(id_tipo_valorizacion)

Obtiene los FileTask disponibles

Obtiene los FileTask disponibles para ser usados por la API KEY suministrada

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
api_instance = riam_api_client.SvcApi(riam_api_client.ApiClient(configuration))
id_tipo_valorizacion = 'id_tipo_valorizacion_example' # str | Tipo de Valorizacion a consultar (Obtenido de getTipoValorizaciones)

try:
    # Obtiene los FileTask disponibles
    api_response = api_instance.svc_handler_get_file_tasks(id_tipo_valorizacion)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SvcApi->svc_handler_get_file_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_tipo_valorizacion** | **str**| Tipo de Valorizacion a consultar (Obtenido de getTipoValorizaciones) | 

### Return type

[**SvcHandlerGetFileTasksResponse**](SvcHandlerGetFileTasksResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svc_handler_get_input_formats**
> SvcHandlerGetInputFormatsResponse svc_handler_get_input_formats(id_file_task)

Obtiene los formatos de carga

Obtiene los formatos de carga posibles para el FileTask provisto

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
api_instance = riam_api_client.SvcApi(riam_api_client.ApiClient(configuration))
id_file_task = 56 # int | Id FileTask para el cual se consulta (Obtenido de getFileTasks)

try:
    # Obtiene los formatos de carga
    api_response = api_instance.svc_handler_get_input_formats(id_file_task)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SvcApi->svc_handler_get_input_formats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_file_task** | **int**| Id FileTask para el cual se consulta (Obtenido de getFileTasks) | 

### Return type

[**SvcHandlerGetInputFormatsResponse**](SvcHandlerGetInputFormatsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svc_handler_get_output_formats**
> SvcHandlerGetOutputFormatsResponse svc_handler_get_output_formats(id_file_task)

Obtiene los formatos de descarga

Obtiene los formatos de descarga posibles para el FileTask provisto

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
api_instance = riam_api_client.SvcApi(riam_api_client.ApiClient(configuration))
id_file_task = 56 # int | Id FileTask para el cual se consulta (Obtenido de getFileTasks)

try:
    # Obtiene los formatos de descarga
    api_response = api_instance.svc_handler_get_output_formats(id_file_task)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SvcApi->svc_handler_get_output_formats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_file_task** | **int**| Id FileTask para el cual se consulta (Obtenido de getFileTasks) | 

### Return type

[**SvcHandlerGetOutputFormatsResponse**](SvcHandlerGetOutputFormatsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svc_handler_get_status**
> SvcHandlerGetStatusResponse svc_handler_get_status(id_file_task, fecha)

Revisa el estado de un FileTask

Revisa el estado de un FileTask<br /> <br /> STATE_AWAITING_INPUT: El FileTask no ha sido cargado para la fecha consultada<br /> STATE_AWAITING_PROCESSING: El Filetask esta encolado para ser procesado, debería estar listo prontamente (aprox 1 minuto)<br /> STATE_AWAITING_PRICES: RiskAmerica aún no ha publicado los precios para el día solicitado<br /> STATE_AWAITING_DOWNLOAD: El archivo esta listo para ser descargado<br /> STATE_DOWNLOADED: El archivo ya ha sido descargado al menos una vez (y puede ser descargado nuevamente)

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
api_instance = riam_api_client.SvcApi(riam_api_client.ApiClient(configuration))
id_file_task = 56 # int | Id FileTask para el cual se consulta (Obtenido de getFileTasks)
fecha = '2013-10-20' # date | Fecha para la cual se esta cargando

try:
    # Revisa el estado de un FileTask
    api_response = api_instance.svc_handler_get_status(id_file_task, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SvcApi->svc_handler_get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_file_task** | **int**| Id FileTask para el cual se consulta (Obtenido de getFileTasks) | 
 **fecha** | **date**| Fecha para la cual se esta cargando | 

### Return type

[**SvcHandlerGetStatusResponse**](SvcHandlerGetStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svc_handler_get_tipo_valorizaciones**
> SvcHandlerGetTipoValorizacionesResponse svc_handler_get_tipo_valorizaciones()

Obtiene los tipos de valorizaciones

Obtiene los tipos de valorizaciones disponibles para la API KEY suministrada

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
api_instance = riam_api_client.SvcApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene los tipos de valorizaciones
    api_response = api_instance.svc_handler_get_tipo_valorizaciones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SvcApi->svc_handler_get_tipo_valorizaciones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SvcHandlerGetTipoValorizacionesResponse**](SvcHandlerGetTipoValorizacionesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **svc_handler_upload_file**
> SvcHandlerUploadFileResponse svc_handler_upload_file(file, id_file_task, id_file_type, fecha)

Envía un archivo al SVC

Envía un archivo de carga al Servicio de Valorización de Carteras. Para entender los estados que devuelve el sistema refierase a leer la documentación del metodo getStatus.

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
api_instance = riam_api_client.SvcApi(riam_api_client.ApiClient(configuration))
file = 'file_example' # str | 
id_file_task = 56 # int | Id FileTask para el cual se consulta (Obtenido de getFileTasks)
id_file_type = 56 # int | Id del formato de carga el cual se envía (Obtenido de getInputFormats)
fecha = '2013-10-20' # date | Fecha para la cual se esta cargando

try:
    # Envía un archivo al SVC
    api_response = api_instance.svc_handler_upload_file(file, id_file_task, id_file_type, fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SvcApi->svc_handler_upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **id_file_task** | **int**| Id FileTask para el cual se consulta (Obtenido de getFileTasks) | 
 **id_file_type** | **int**| Id del formato de carga el cual se envía (Obtenido de getInputFormats) | 
 **fecha** | **date**| Fecha para la cual se esta cargando | 

### Return type

[**SvcHandlerUploadFileResponse**](SvcHandlerUploadFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

