# SicAjusteTipoIGetParametrosResponseMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificador del parámetro | [optional] 
**name** | **str** | Nombre | [optional] 
**fecha_creacion** | **date** | Fecha de creación | [optional] 
**trigger_clp** | **float** | maxima desviacion absoluta de instrumentos RF CLP | [optional] 
**trigger_otros** | **float** | maxima desviacion absoluta de instrumentos no RF CLP | [optional] 
**trigger_cartera** | **float** | maxima desviacion absoluta de cartera | [optional] 
**objetivo_clp** | **float** | desviacion buscada al ajustar por criterio CLP (triggerClp) 0&#x3D;mercado | [optional] 
**objetivo_otros** | **float** | desviacion buscada al ajustar por criterio Otros (triggerOtros) 0&#x3D;mercado | [optional] 
**objetivo_cartera** | **float** | desviacion de cartera buscada al ajustar por criterio de cartera(triggerCartera) 0&#x3D;mercado | [optional] 
**primer_criterio** | **str** | primer criterio de ordenamiento de instrumentos al ajustar por criterio de cartera (DESVIACION,IMPACTO,PESO CARTERA,DURACION,PLAZO,valido para objetivoCartera&gt;0) | [optional] 
**orden_primer_criterio** | **str** | order primer criterio (ASC,DESC) | [optional] 
**segundo_criterio** | **str** | segundo criterio de ordenamiento de instrumentos al ajustar por criterio de cartera (DESVIACION,IMPACTO,PESO CARTERA,DURACION,PLAZO,valido para objetivoCartera&gt;0) | [optional] 
**orden_segundo_criterio** | **str** | order segundo criterio (ASC,DESC) | [optional] 
**ultimo_ajuste** | **str** | desviacion buscada al ajustar el ultimo instrumento por criterio de cartera (valido para objetivoCartera&gt;0) | [optional] 
**ajuste_derivado** | **str** | criterio para ajustar derivados(PRIMER_RECURSO,ULTIMO_RECURSO,POR_CRITERIO) | [optional] 
**ajustar_siempre_derivado** | **int** | Detalla si siempre se ajustan los derivados a mercado (1 &#x3D; si, 0 &#x3D; no) | [optional] 
**condicion_pago** | **str** | Detalla si los instrumentos se realizan a Pago Hoy (PH) o Pago Mañana (PM) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

