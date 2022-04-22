# swagger_client.AvailabilityApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availability_get**](AvailabilityApi.md#availability_get) | **GET** /availability/ | Cars available according to the given pick up and drop off date


# **availability_get**
> CarList availability_get(pickup_date, dropoff_date, office_id)

Cars available according to the given pick up and drop off date

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AvailabilityApi()
pickup_date = '2013-10-20' # date | date user want to pick-up the car. It should be written in that format \"yyyy-mm-dd\"
dropoff_date = '2013-10-20' # date | date user want to drop-off the car. It should be written in that format \"yyyy-mm-dd\"
office_id = 56 # int | 

try:
    # Cars available according to the given pick up and drop off date
    api_response = api_instance.availability_get(pickup_date, dropoff_date, office_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvailabilityApi->availability_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pickup_date** | **date**| date user want to pick-up the car. It should be written in that format \&quot;yyyy-mm-dd\&quot; | 
 **dropoff_date** | **date**| date user want to drop-off the car. It should be written in that format \&quot;yyyy-mm-dd\&quot; | 
 **office_id** | **int**|  | 

### Return type

[**CarList**](CarList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

