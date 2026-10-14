# riam_api_client.EmisoresApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emisores_informacion_get**](EmisoresApi.md#emisores_informacion_get) | **POST** /Outputs/Generic/Emisores/Informacion/get | Obtiene la información del Emisor.
[**emisores_informacion_get_vigentes**](EmisoresApi.md#emisores_informacion_get_vigentes) | **POST** /Outputs/Generic/Emisores/Informacion/getVigentes | Obtiene la lista de emisores vigentes para una fecha.

# **emisores_informacion_get**
> EmisoresInformacionGetResponse emisores_informacion_get(emisor)

Obtiene la información del Emisor.

Obtiene la información del Emisor a la fecha de hoy.

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
api_instance = riam_api_client.EmisoresApi(riam_api_client.ApiClient(configuration))
emisor = 'emisor_example' # str | Emisor a consultar

try:
    # Obtiene la información del Emisor.
    api_response = api_instance.emisores_informacion_get(emisor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmisoresApi->emisores_informacion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emisor** | **str**| Emisor a consultar | 

### Return type

[**EmisoresInformacionGetResponse**](EmisoresInformacionGetResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emisores_informacion_get_vigentes**
> EmisoresInformacionGetVigentesResponse emisores_informacion_get_vigentes(fecha)

Obtiene la lista de emisores vigentes para una fecha.

Obtiene la lista de emisores vigentes para una fecha.

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
api_instance = riam_api_client.EmisoresApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha de consulta

try:
    # Obtiene la lista de emisores vigentes para una fecha.
    api_response = api_instance.emisores_informacion_get_vigentes(fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmisoresApi->emisores_informacion_get_vigentes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha de consulta | 

### Return type

[**EmisoresInformacionGetVigentesResponse**](EmisoresInformacionGetVigentesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

