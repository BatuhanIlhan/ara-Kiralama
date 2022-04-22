# swagger_client.CarApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cars_car_id_delete**](CarApi.md#cars_car_id_delete) | **DELETE** /cars/{car_id} | Delete the car with the specified id
[**cars_car_id_get**](CarApi.md#cars_car_id_get) | **GET** /cars/{car_id} | Get the car with the specified id
[**cars_car_id_post**](CarApi.md#cars_car_id_post) | **POST** /cars/{car_id} | Update the car with the specified id
[**cars_get**](CarApi.md#cars_get) | **GET** /cars/ | Get list of all cars
[**cars_post**](CarApi.md#cars_post) | **POST** /cars/ | Create a new car


# **cars_car_id_delete**
> str cars_car_id_delete(car_id)

Delete the car with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CarApi()
car_id = 56 # int | Car id

try:
    # Delete the car with the specified id
    api_response = api_instance.cars_car_id_delete(car_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarApi->cars_car_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| Car id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cars_car_id_get**
> Car cars_car_id_get(car_id)

Get the car with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CarApi()
car_id = 56 # int | Car id

try:
    # Get the car with the specified id
    api_response = api_instance.cars_car_id_get(car_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarApi->cars_car_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| Car id | 

### Return type

[**Car**](Car.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cars_car_id_post**
> str cars_car_id_post(car_id)

Update the car with the specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CarApi()
car_id = 56 # int | Car id

try:
    # Update the car with the specified id
    api_response = api_instance.cars_car_id_post(car_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarApi->cars_car_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**| Car id | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cars_get**
> CarList cars_get()

Get list of all cars

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CarApi()

try:
    # Get list of all cars
    api_response = api_instance.cars_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarApi->cars_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CarList**](CarList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cars_post**
> CreateCarMessage cars_post()

Create a new car

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CarApi()

try:
    # Create a new car
    api_response = api_instance.cars_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarApi->cars_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateCarMessage**](CreateCarMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

