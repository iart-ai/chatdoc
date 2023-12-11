# openapi_client.UsersApi

All URIs are relative to *https://api.chatdoc.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quota_users_quota_get**](UsersApi.md#get_quota_users_quota_get) | **GET** /users/quota | Get Quota


# **get_quota_users_quota_get**
> PackageQuotaResp get_quota_users_quota_get()

Get Quota

Get quota of not expired package  Response example: ```json {   \"data\": {     \"package\": { # may be null       \"basic_page\": { # may be null         \"max_count\": 3000,         \"used_count\": 1044       },       \"elite_page\": { # may be null         \"max_count\": 3000,         \"used_count\": 1045       },       \"lite_page\": { # may be null         \"max_count\": 3000,         \"used_count\": 1046       },       \"question\": { # may be null         \"max_count\": 3000,         \"used_count\": 11       },       \"documents_tokens\": { # may be null         \"max_count\": 3000,         \"used_count\": 11       },       \"ocr_page\": { # may be null         \"max_count\": 3000,         \"used_count\": 11       },       \"gpt4_question\": { # may be null         \"max_count\": 3000,         \"used_count\": 11       }     }   } } ```

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
from chatdoc.models.package_quota_resp import PackageQuotaResp
from chatdoc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.chatdoc.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = chatdoc.Configuration(
    host="https://api.chatdoc.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = chatdoc.Configuration(
    access_token=os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with chatdoc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = chatdoc.UsersApi(api_client)

    try:
        # Get Quota
        api_response = api_instance.get_quota_users_quota_get()
        print("The response of UsersApi->get_quota_users_quota_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_quota_users_quota_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PackageQuotaResp**](PackageQuotaResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

