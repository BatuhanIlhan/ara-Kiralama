# swagger_client.ReservationApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservation_post**](ReservationApi.md#reservation_post) | **POST** /reservation/ | Make reservation


# **reservation_post**
> str reservation_post(reservation_request=reservation_request)

Make reservation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReservationApi()
reservation_request = swagger_client.MakeReservationRequest() # MakeReservationRequest |  (optional)

try:
    # Make reservation
    api_response = api_instance.reservation_post(reservation_request=reservation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReservationApi->reservation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_request** | [**MakeReservationRequest**](MakeReservationRequest.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

