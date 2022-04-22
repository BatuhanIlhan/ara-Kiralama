# swagger_client.OfficeApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offices_delete**](OfficeApi.md#offices_delete) | **DELETE** /offices/ | Delete office with specsified id
[**offices_get**](OfficeApi.md#offices_get) | **GET** /offices/ | Get the office with specified id
[**offices_post**](OfficeApi.md#offices_post) | **POST** /offices/ | create or edit office


# **offices_delete**
> object offices_delete(id=id)

Delete office with specsified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OfficeApi()
id = swagger_client.Id() # Id |  (optional)

try:
    # Delete office with specsified id
    api_response = api_instance.offices_delete(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficeApi->offices_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offices_get**
> Office offices_get(id)

Get the office with specified id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OfficeApi()
id = 56 # int | 

try:
    # Get the office with specified id
    api_response = api_instance.offices_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficeApi->offices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Office**](Office.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offices_post**
> object offices_post(office_request_body=office_request_body)

create or edit office

if id exists in the parameters then it edits that office. Otherwise, creates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OfficeApi()
office_request_body = swagger_client.OfficeRequest() # OfficeRequest |  (optional)

try:
    # create or edit office
    api_response = api_instance.offices_post(office_request_body=office_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfficeApi->offices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_request_body** | [**OfficeRequest**](OfficeRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

