# riam_api_client.MonedasEIndicadoresApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monedase_indicadores_monedas_get_tipo_cambio**](MonedasEIndicadoresApi.md#monedase_indicadores_monedas_get_tipo_cambio) | **POST** /Outputs/Generic/Indicadores/Monedas/getTipoCambio | Obtiene el tipo cambio para una fecha específica.
[**monedase_indicadores_monedas_get_tipo_cambio_interval**](MonedasEIndicadoresApi.md#monedase_indicadores_monedas_get_tipo_cambio_interval) | **POST** /Outputs/Generic/Indicadores/Monedas/getTipoCambioInterval | Obtiene el tipo cambio para una fecha específica.

# **monedase_indicadores_monedas_get_tipo_cambio**
> InlineResponse20035 monedase_indicadores_monedas_get_tipo_cambio(fecha, moneda, base)

Obtiene el tipo cambio para una fecha específica.

Obtiene el tipo cambio para una fecha específica entregando el valor de la moneda pedida con respecto a la base dada. Por ejemplo si uno pide moneda USD para la base CLP este entega el valor de la moneda USD en unidades de CLP.<br> Las fechas de esta consulta siguen el estandar del Banco Central de Chile en donde el tipo cambio promedio del día T se guarda con fecha T+1. Por ejemplo el dolar observado del día 2017-04-04 queda guardado con fecha 2017-04-05 y debe ser consultado de la misma manera.

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
api_instance = riam_api_client.MonedasEIndicadoresApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a Consultar
moneda = 'moneda_example' # str | Moneda a consultar
base = 'base_example' # str | Moneda en la cual se expresa el tipo cambio obtenido

try:
    # Obtiene el tipo cambio para una fecha específica.
    api_response = api_instance.monedase_indicadores_monedas_get_tipo_cambio(fecha, moneda, base)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonedasEIndicadoresApi->monedase_indicadores_monedas_get_tipo_cambio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a Consultar | 
 **moneda** | **str**| Moneda a consultar | 
 **base** | **str**| Moneda en la cual se expresa el tipo cambio obtenido | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monedase_indicadores_monedas_get_tipo_cambio_interval**
> InlineResponse20036 monedase_indicadores_monedas_get_tipo_cambio_interval(fecha_min, fecha_max, moneda, base)

Obtiene el tipo cambio para una fecha específica.

Obtiene el tipo cambio para una fecha específica entregando el valor de la moneda pedida con respecto a la base dada. Por ejemplo si uno pide moneda USD para la base CLP este entega el valor de la moneda USD en unidades de CLP.<br> Las fechas de esta consulta siguen el estandar del Banco Central de Chile en donde el tipo cambio promedio del día T se guarda con fecha T+1. Por ejemplo el dolar observado del día 2017-04-04 queda guardado con fecha 2017-04-05 y debe ser consultado de la misma manera.<br> El intervalo de fechas debe ser menor o igual a 365 días.

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
api_instance = riam_api_client.MonedasEIndicadoresApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Intervalo Inferior de Fecha
fecha_max = '2013-10-20' # date | Intervalo Superior de Fecha
moneda = 'moneda_example' # str | Moneda a consultar
base = 'base_example' # str | Moneda en la cual se expresa el tipo cambio obtenido

try:
    # Obtiene el tipo cambio para una fecha específica.
    api_response = api_instance.monedase_indicadores_monedas_get_tipo_cambio_interval(fecha_min, fecha_max, moneda, base)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonedasEIndicadoresApi->monedase_indicadores_monedas_get_tipo_cambio_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Intervalo Inferior de Fecha | 
 **fecha_max** | **date**| Intervalo Superior de Fecha | 
 **moneda** | **str**| Moneda a consultar | 
 **base** | **str**| Moneda en la cual se expresa el tipo cambio obtenido | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

