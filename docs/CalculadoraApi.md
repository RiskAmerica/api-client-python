# riam_api_client.CalculadoraApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculadora_calculadora_calcular_con_tir**](CalculadoraApi.md#calculadora_calculadora_calcular_con_tir) | **POST** /Outputs/Generic/Calculadora/Calculadora/calcularConTir | Obtiene la valorización de un instrumento para una tasa dada.

# **calculadora_calculadora_calcular_con_tir**
> InlineResponse20034 calculadora_calculadora_calcular_con_tir(nemo, fecha, tir, nominal)

Obtiene la valorización de un instrumento para una tasa dada.

Obtiene la valorización de un instrumento para una tasa dada.

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
api_instance = riam_api_client.CalculadoraApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotecnico del instrumento a valorizar
fecha = '2013-10-20' # date | Fecha para la cual se efectua la valorización
tir = 1.2 # float | Tasa usada para valorizar
nominal = 1000 # float | Nominal a valorizar (default to 1000)

try:
    # Obtiene la valorización de un instrumento para una tasa dada.
    api_response = api_instance.calculadora_calculadora_calcular_con_tir(nemo, fecha, tir, nominal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CalculadoraApi->calculadora_calculadora_calcular_con_tir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotecnico del instrumento a valorizar | 
 **fecha** | **date**| Fecha para la cual se efectua la valorización | 
 **tir** | **float**| Tasa usada para valorizar | 
 **nominal** | **float**| Nominal a valorizar | [default to 1000]

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

