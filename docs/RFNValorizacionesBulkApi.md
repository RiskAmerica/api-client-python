# riam_api_client.RFNValorizacionesBulkApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_valorizaciones_bulk_valorizacion_bulk_get_all**](RFNValorizacionesBulkApi.md#r_fn_valorizaciones_bulk_valorizacion_bulk_get_all) | **POST** /Outputs/Generic/ValorizacionRF/ValorizacionBulk/getAll | Obtiene valorizaciones para una familia de nemos.
[**r_fn_valorizaciones_bulk_valorizacion_bulk_get_familias**](RFNValorizacionesBulkApi.md#r_fn_valorizaciones_bulk_valorizacion_bulk_get_familias) | **POST** /Outputs/Generic/ValorizacionRF/ValorizacionBulk/getFamilias | Obtiene las familias de instrumentos disponibles.

# **r_fn_valorizaciones_bulk_valorizacion_bulk_get_all**
> RFNValorizacionesBulkValorizacionBulkGetAllResponse r_fn_valorizaciones_bulk_valorizacion_bulk_get_all(fecha, familia)

Obtiene valorizaciones para una familia de nemos.

Obtiene valorizaciones para una familia de nemos hasta la fecha hábil anterior a la fecha de consulta. WARNING: El cobro es por nemo consultado.

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
api_instance = riam_api_client.RFNValorizacionesBulkApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a consultar
familia = 'familia_example' # str | familia a consultar. Ejemplo: BE, BB, BS, BCU, etc.

try:
    # Obtiene valorizaciones para una familia de nemos.
    api_response = api_instance.r_fn_valorizaciones_bulk_valorizacion_bulk_get_all(fecha, familia)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesBulkApi->r_fn_valorizaciones_bulk_valorizacion_bulk_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a consultar | 
 **familia** | **str**| familia a consultar. Ejemplo: BE, BB, BS, BCU, etc. | 

### Return type

[**RFNValorizacionesBulkValorizacionBulkGetAllResponse**](RFNValorizacionesBulkValorizacionBulkGetAllResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_valorizaciones_bulk_valorizacion_bulk_get_familias**
> RFNValorizacionesBulkValorizacionBulkGetFamiliasResponse r_fn_valorizaciones_bulk_valorizacion_bulk_get_familias()

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
api_instance = riam_api_client.RFNValorizacionesBulkApi(riam_api_client.ApiClient(configuration))

try:
    # Obtiene las familias de instrumentos disponibles.
    api_response = api_instance.r_fn_valorizaciones_bulk_valorizacion_bulk_get_familias()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNValorizacionesBulkApi->r_fn_valorizaciones_bulk_valorizacion_bulk_get_familias: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RFNValorizacionesBulkValorizacionBulkGetFamiliasResponse**](RFNValorizacionesBulkValorizacionBulkGetFamiliasResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

