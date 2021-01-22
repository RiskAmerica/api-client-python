# riam_api_client.FondosApi

All URIs are relative to *https://webservices.riskamerica.com/webservice/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fondos_datos_cuota_get_fecha**](FondosApi.md#fondos_datos_cuota_get_fecha) | **POST** /Outputs/Generic/Fondos/DatosCuota/getFecha | Obtiene los registros de datos cuota para todos los fondos para la fecha consultada.
[**fondos_datos_cuota_get_serie**](FondosApi.md#fondos_datos_cuota_get_serie) | **POST** /Outputs/Generic/Fondos/DatosCuota/getSerie | Obtiene los registros de datos cuota para todos los fondos para la serie consultada.
[**fondos_informacion_get**](FondosApi.md#fondos_informacion_get) | **POST** /Outputs/Generic/Fondos/Informacion/get | Obtiene la información de un fondo y sus series.
[**fondos_reprocesos_get_periodo**](FondosApi.md#fondos_reprocesos_get_periodo) | **POST** /Outputs/Generic/Fondos/Reprocesos/getPeriodo | Obtiene los reprocesos de los datos cuota que han ocurrido en un periodo de tiempo.
[**fondos_reprocesos_get_serie**](FondosApi.md#fondos_reprocesos_get_serie) | **POST** /Outputs/Generic/Fondos/Reprocesos/getSerie | Obtiene los reprocesos de los datos cuota para una serie particular.
[**fondos_retornos_ajustados_get_fecha**](FondosApi.md#fondos_retornos_ajustados_get_fecha) | **POST** /Outputs/Generic/Fondos/RetornosAjustados/getFecha | Obtiene los registros de retornos del valor cuota ajustados por remuneración para todos los fondos para la fecha consultada.
[**fondos_retornos_ajustados_get_serie**](FondosApi.md#fondos_retornos_ajustados_get_serie) | **POST** /Outputs/Generic/Fondos/RetornosAjustados/getSerie | Obtiene los registros de retornos del valor cuota ajustados por remuneración para la serie consultada para la fecha consultada.
[**fondos_retornos_get_fecha**](FondosApi.md#fondos_retornos_get_fecha) | **POST** /Outputs/Generic/Fondos/Retornos/getFecha | Obtiene los registros de retornos del valor cuota para todos los fondos en la fecha consultada.
[**fondos_retornos_get_serie**](FondosApi.md#fondos_retornos_get_serie) | **POST** /Outputs/Generic/Fondos/Retornos/getSerie | Obtiene los registros de retornos del valor cuota para la serie consultada.

# **fondos_datos_cuota_get_fecha**
> InlineResponse2001 fondos_datos_cuota_get_fecha(fecha, moneda=moneda)

Obtiene los registros de datos cuota para todos los fondos para la fecha consultada.

Obtiene los registros de datos cuota para todos los fondos para la fecha consultada.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a Consultar
moneda = 'moneda_example' # str | Moneda en la cual se despliegan los valores. Si se omite este valor se despliegan en la moneda contable del fondo. (optional)

try:
    # Obtiene los registros de datos cuota para todos los fondos para la fecha consultada.
    api_response = api_instance.fondos_datos_cuota_get_fecha(fecha, moneda=moneda)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_datos_cuota_get_fecha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a Consultar | 
 **moneda** | **str**| Moneda en la cual se despliegan los valores. Si se omite este valor se despliegan en la moneda contable del fondo. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_datos_cuota_get_serie**
> InlineResponse2002 fondos_datos_cuota_get_serie(fecha_min, fecha_max, rut, serie, moneda=moneda)

Obtiene los registros de datos cuota para todos los fondos para la serie consultada.

Obtiene los registros de datos cuota para todos los fondos para la serie consultada entre un rango de fechas.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Fecha mínima a consultar
fecha_max = '2013-10-20' # date | Fecha máxima a consultar
rut = 56 # int | Rut del Fondo (sin dígito verificador)
serie = 'serie_example' # str | Código de la serie
moneda = 'moneda_example' # str | Moneda en la cual se despliegan los valores. Si se omite este valor se despliegan en la moneda contable del fondo. (optional)

try:
    # Obtiene los registros de datos cuota para todos los fondos para la serie consultada.
    api_response = api_instance.fondos_datos_cuota_get_serie(fecha_min, fecha_max, rut, serie, moneda=moneda)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_datos_cuota_get_serie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Fecha mínima a consultar | 
 **fecha_max** | **date**| Fecha máxima a consultar | 
 **rut** | **int**| Rut del Fondo (sin dígito verificador) | 
 **serie** | **str**| Código de la serie | 
 **moneda** | **str**| Moneda en la cual se despliegan los valores. Si se omite este valor se despliegan en la moneda contable del fondo. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_informacion_get**
> InlineResponse200 fondos_informacion_get(rut, serie=serie)

Obtiene la información de un fondo y sus series.

Obtiene la información de un fondo y sus series.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
rut = 56 # int | Rut del Fondo (sin dígito verificador)
serie = 'serie_example' # str | Código de la serie. Si no se especifica se muestran todas las series. (optional)

try:
    # Obtiene la información de un fondo y sus series.
    api_response = api_instance.fondos_informacion_get(rut, serie=serie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_informacion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rut** | **int**| Rut del Fondo (sin dígito verificador) | 
 **serie** | **str**| Código de la serie. Si no se especifica se muestran todas las series. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_reprocesos_get_periodo**
> InlineResponse2005 fondos_reprocesos_get_periodo(fecha_min, fecha_max)

Obtiene los reprocesos de los datos cuota que han ocurrido en un periodo de tiempo.

Obtiene los reprocesos de los datos cuota que han ocurrido en un periodo de tiempo. Este servicio solo tiene disponible reprocesos a partir del 2017-10-01.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Fecha mínima a consultar
fecha_max = '2013-10-20' # date | Fecha máxima a consultar (No inclusive)

try:
    # Obtiene los reprocesos de los datos cuota que han ocurrido en un periodo de tiempo.
    api_response = api_instance.fondos_reprocesos_get_periodo(fecha_min, fecha_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_reprocesos_get_periodo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Fecha mínima a consultar | 
 **fecha_max** | **date**| Fecha máxima a consultar (No inclusive) | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_reprocesos_get_serie**
> InlineResponse2005 fondos_reprocesos_get_serie(rut, serie)

Obtiene los reprocesos de los datos cuota para una serie particular.

Obtiene los reprocesos de los datos cuota para una serie particular. Este servicio solo tiene disponible reprocesos a partir del 2017-10-01.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
rut = 56 # int | Rut del Fondo (sin dígito verificador)
serie = 'serie_example' # str | Código de la serie

try:
    # Obtiene los reprocesos de los datos cuota para una serie particular.
    api_response = api_instance.fondos_reprocesos_get_serie(rut, serie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_reprocesos_get_serie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rut** | **int**| Rut del Fondo (sin dígito verificador) | 
 **serie** | **str**| Código de la serie | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_retornos_ajustados_get_fecha**
> InlineResponse2004 fondos_retornos_ajustados_get_fecha(fecha)

Obtiene los registros de retornos del valor cuota ajustados por remuneración para todos los fondos para la fecha consultada.

Obtiene los registros de retornos del valor cuota ajustados por remuneración para todos los fondos para la fecha consultada.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a Consultar

try:
    # Obtiene los registros de retornos del valor cuota ajustados por remuneración para todos los fondos para la fecha consultada.
    api_response = api_instance.fondos_retornos_ajustados_get_fecha(fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_retornos_ajustados_get_fecha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a Consultar | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_retornos_ajustados_get_serie**
> InlineResponse2004 fondos_retornos_ajustados_get_serie(fecha_min, fecha_max, rut, serie)

Obtiene los registros de retornos del valor cuota ajustados por remuneración para la serie consultada para la fecha consultada.

Obtiene los registros de retornos del valor cuota ajustados por remuneración para la serie consultada entre un rango de fechas.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Fecha mínima a consultar
fecha_max = '2013-10-20' # date | Fecha máxima a consultar
rut = 56 # int | Rut del Fondo (sin dígito verificador)
serie = 'serie_example' # str | Código de la serie

try:
    # Obtiene los registros de retornos del valor cuota ajustados por remuneración para la serie consultada para la fecha consultada.
    api_response = api_instance.fondos_retornos_ajustados_get_serie(fecha_min, fecha_max, rut, serie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_retornos_ajustados_get_serie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Fecha mínima a consultar | 
 **fecha_max** | **date**| Fecha máxima a consultar | 
 **rut** | **int**| Rut del Fondo (sin dígito verificador) | 
 **serie** | **str**| Código de la serie | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_retornos_get_fecha**
> InlineResponse2003 fondos_retornos_get_fecha(fecha)

Obtiene los registros de retornos del valor cuota para todos los fondos en la fecha consultada.

Obtiene los registros de retornos del valor cuota para todos los fondos en la fecha consultada.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
fecha = '2013-10-20' # date | Fecha a Consultar

try:
    # Obtiene los registros de retornos del valor cuota para todos los fondos en la fecha consultada.
    api_response = api_instance.fondos_retornos_get_fecha(fecha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_retornos_get_fecha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha** | **date**| Fecha a Consultar | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fondos_retornos_get_serie**
> InlineResponse2003 fondos_retornos_get_serie(fecha_min, fecha_max, rut, serie)

Obtiene los registros de retornos del valor cuota para la serie consultada.

Obtiene los registros de retornos del valor cuota para la serie consultada entre un rango de fechas.

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
api_instance = riam_api_client.FondosApi(riam_api_client.ApiClient(configuration))
fecha_min = '2013-10-20' # date | Fecha mínima a consultar
fecha_max = '2013-10-20' # date | Fecha máxima a consultar
rut = 56 # int | Rut del Fondo (sin dígito verificador)
serie = 'serie_example' # str | Código de la serie

try:
    # Obtiene los registros de retornos del valor cuota para la serie consultada.
    api_response = api_instance.fondos_retornos_get_serie(fecha_min, fecha_max, rut, serie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FondosApi->fondos_retornos_get_serie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fecha_min** | **date**| Fecha mínima a consultar | 
 **fecha_max** | **date**| Fecha máxima a consultar | 
 **rut** | **int**| Rut del Fondo (sin dígito verificador) | 
 **serie** | **str**| Código de la serie | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

