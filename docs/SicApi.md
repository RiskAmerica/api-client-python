# riam_api_client.SicApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sic_upload_upload**](SicApi.md#sic_upload_upload) | **POST** /Outputs/Generic/SIC/Upload/upload | Carga un archivo al módulo de Sistema Integrado de Carteras (SIC).

# **sic_upload_upload**
> InlineResponse20037 sic_upload_upload(id_file_type, file=file)

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
id_file_type = 'id_file_type_example' # str | Tipo de Archivo a cargar (1: CSV, 2: XLS, 3: XML)
file = 'file_example' # str |  (optional)

try:
    # Carga un archivo al módulo de Sistema Integrado de Carteras (SIC).
    api_response = api_instance.sic_upload_upload(id_file_type, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SicApi->sic_upload_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_file_type** | **str**| Tipo de Archivo a cargar (1: CSV, 2: XLS, 3: XML) | 
 **file** | **str**|  | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

