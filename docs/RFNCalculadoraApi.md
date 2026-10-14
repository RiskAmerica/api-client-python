# riam_api_client.RFNCalculadoraApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_fn_calculadora_calculadora_calcular_con_monto**](RFNCalculadoraApi.md#r_fn_calculadora_calculadora_calcular_con_monto) | **POST** /Outputs/Generic/Calculadora/Calculadora/calcularConMonto | Obtiene la tasa de un instrumento para un monto CLP dado.
[**r_fn_calculadora_calculadora_calcular_con_tir**](RFNCalculadoraApi.md#r_fn_calculadora_calculadora_calcular_con_tir) | **POST** /Outputs/Generic/Calculadora/Calculadora/calcularConTir | Obtiene la valorización de un instrumento para una tasa dada.

# **r_fn_calculadora_calculadora_calcular_con_monto**
> RFNCalculadoraCalculadoraCalcularConMontoResponse r_fn_calculadora_calculadora_calcular_con_monto(nemo, fecha, monto_clp, nominal, condicion_pago=condicion_pago)

Obtiene la tasa de un instrumento para un monto CLP dado.

Obtiene la tasa de un instrumento para un monto CLP dado.

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
api_instance = riam_api_client.RFNCalculadoraApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotecnico del instrumento a valorizar
fecha = '2013-10-20' # date | Fecha para la cual se efectua la valorización
monto_clp = 1.2 # float | Monto CLP utilizado para encontrar la TIR
nominal = 1.2 # float | Nominal a valorizar.
condicion_pago = 'condicion_pago_example' # str | Condicion de Pago. Las opciones posibles son: PH, PM, CN. (optional)

try:
    # Obtiene la tasa de un instrumento para un monto CLP dado.
    api_response = api_instance.r_fn_calculadora_calculadora_calcular_con_monto(nemo, fecha, monto_clp, nominal, condicion_pago=condicion_pago)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNCalculadoraApi->r_fn_calculadora_calculadora_calcular_con_monto: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotecnico del instrumento a valorizar | 
 **fecha** | **date**| Fecha para la cual se efectua la valorización | 
 **monto_clp** | **float**| Monto CLP utilizado para encontrar la TIR | 
 **nominal** | **float**| Nominal a valorizar. | 
 **condicion_pago** | **str**| Condicion de Pago. Las opciones posibles son: PH, PM, CN. | [optional] 

### Return type

[**RFNCalculadoraCalculadoraCalcularConMontoResponse**](RFNCalculadoraCalculadoraCalcularConMontoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **r_fn_calculadora_calculadora_calcular_con_tir**
> RFNCalculadoraCalculadoraCalcularConTirResponse r_fn_calculadora_calculadora_calcular_con_tir(nemo, fecha, tir, nominal=nominal, condicion_pago=condicion_pago)

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
api_instance = riam_api_client.RFNCalculadoraApi(riam_api_client.ApiClient(configuration))
nemo = 'nemo_example' # str | Nemotecnico del instrumento a valorizar
fecha = '2013-10-20' # date | Fecha para la cual se efectua la valorización
tir = 1.2 # float | Tasa usada para valorizar
nominal = 1.2 # float | Nominal a valorizar. Si no se carga se asume 1000 (optional)
condicion_pago = 'condicion_pago_example' # str | Condicion de Pago. Las opciones posibles son: PH, PM, CN. (optional)

try:
    # Obtiene la valorización de un instrumento para una tasa dada.
    api_response = api_instance.r_fn_calculadora_calculadora_calcular_con_tir(nemo, fecha, tir, nominal=nominal, condicion_pago=condicion_pago)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RFNCalculadoraApi->r_fn_calculadora_calculadora_calcular_con_tir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nemo** | **str**| Nemotecnico del instrumento a valorizar | 
 **fecha** | **date**| Fecha para la cual se efectua la valorización | 
 **tir** | **float**| Tasa usada para valorizar | 
 **nominal** | **float**| Nominal a valorizar. Si no se carga se asume 1000 | [optional] 
 **condicion_pago** | **str**| Condicion de Pago. Las opciones posibles son: PH, PM, CN. | [optional] 

### Return type

[**RFNCalculadoraCalculadoraCalcularConTirResponse**](RFNCalculadoraCalculadoraCalcularConTirResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

