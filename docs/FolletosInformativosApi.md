# riam_api_client.FolletosInformativosApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folletos_informativos_datos_cuota_upload_file**](FolletosInformativosApi.md#folletos_informativos_datos_cuota_upload_file) | **POST** /Outputs/Generic/FolletosInformativos/DatosCuota/uploadFile | Carga un archivo con datos cuota para Fondos de Inversión

# **folletos_informativos_datos_cuota_upload_file**
> FolletosInformativosDatosCuotaUploadFileResponse folletos_informativos_datos_cuota_upload_file(file)

Carga un archivo con datos cuota para Fondos de Inversión

Carga un archivo con datos cuota para Fondos de Inversión públicos. Datos cargados con anterioridad serán reemplazados en una nueva carga.

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
api_instance = riam_api_client.FolletosInformativosApi(riam_api_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # Carga un archivo con datos cuota para Fondos de Inversión
    api_response = api_instance.folletos_informativos_datos_cuota_upload_file(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolletosInformativosApi->folletos_informativos_datos_cuota_upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

[**FolletosInformativosDatosCuotaUploadFileResponse**](FolletosInformativosDatosCuotaUploadFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

