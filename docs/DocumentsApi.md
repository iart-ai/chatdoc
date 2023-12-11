# openapi_client.DocumentsApi

All URIs are relative to *https://api.chatdoc.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_documents_upload_id_delete**](DocumentsApi.md#delete_document_documents_upload_id_delete) | **DELETE** /documents/{upload_id} | Delete Document
[**download_document_documents_upload_id_download_get**](DocumentsApi.md#download_document_documents_upload_id_download_get) | **GET** /documents/{upload_id}/download | Download Document
[**get_document_documents_upload_id_get**](DocumentsApi.md#get_document_documents_upload_id_get) | **GET** /documents/{upload_id} | Get Document
[**upload_document_documents_upload_post**](DocumentsApi.md#upload_document_documents_upload_post) | **POST** /documents/upload | Upload Document
[**upload_document_documents_website_post**](DocumentsApi.md#upload_document_documents_website_post) | **POST** /documents/website | Upload Document


# **delete_document_documents_upload_id_delete**
> object delete_document_documents_upload_id_delete(upload_id)

Delete Document

Delete a document

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
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
    api_instance = chatdoc.DocumentsApi(api_client)
    upload_id = 'upload_id_example'  # str | 

    try:
        # Delete Document
        api_response = api_instance.delete_document_documents_upload_id_delete(upload_id)
        print("The response of DocumentsApi->delete_document_documents_upload_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_document_documents_upload_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document_documents_upload_id_download_get**
> object download_document_documents_upload_id_download_get(upload_id)

Download Document

Download content of the document, support CORS and range request.  * If the document is of doc/docx format, then it's converted to pdf version, and the original version can't be downloaded. * If the document is of pdf format, it's recommended to use your local file to avoid unnecessary network traffic. * If the document is of md/epub/txt/website format, then it's converted to html version, and the original version can't be downloaded.

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
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
    api_instance = chatdoc.DocumentsApi(api_client)
    upload_id = 'upload_id_example'  # str | 

    try:
        # Download Document
        api_response = api_instance.download_document_documents_upload_id_download_get(upload_id)
        print("The response of DocumentsApi->download_document_documents_upload_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->download_document_documents_upload_id_download_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_documents_upload_id_get**
> APICollectionOrUploadResp get_document_documents_upload_id_get(upload_id)

Get Document

Get a document  **Response**:  Similar with `POST /documents/upload`, and pay attention to the following fields:  * `type`:     * collection: document collection     * single_doc: standalone document     * doc_of_collection: sub document of collection  * `documents`: sub document list of collection, which only returns for collection

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
from chatdoc.models.api_collection_or_upload_resp import APICollectionOrUploadResp
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
    api_instance = chatdoc.DocumentsApi(api_client)
    upload_id = 'upload_id_example'  # str | 

    try:
        # Get Document
        api_response = api_instance.get_document_documents_upload_id_get(upload_id)
        print("The response of DocumentsApi->get_document_documents_upload_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_documents_upload_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**|  | 

### Return type

[**APICollectionOrUploadResp**](APICollectionOrUploadResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_documents_upload_post**
> APIUploadResp upload_document_documents_upload_post(file, package_type=package_type, collection_id=collection_id, ocr=ocr)

Upload Document

Upload a document  **Response**:  * `id`: document id, also called `upload_id`, you can use it to get the document by `GET /documents/{upload_id}`. It's of uuid format.  **Please note**: you should store `id` in your database, because we don't have a `GET /documents/list` API to list all documents for now.  * `status`: Once uploaded, the status is `UN_PARSED`, after a series of processing, the status would change by time, and finally to be one of the following two cases:  ``` UN_PARSED = 1              file uploaded or collection has no document # final statuses ELEMENT_PARSED = 300       analysis of the document has succeeded ERROR_STATUSES (< 0)       error occurred during analysis ```  So before the document status finalized, you can poll the status by `GET /documents/{upload_id}` at interval of 10s , generally it takes 1-2 minutes to finish depending on content length of the document. If error occurred, it doesn't consume your quota.  **Please note**:  * Uploading files consumes your pages quota, and uploading same files again will still consume quota. * We'll keep your uploaded file for one year. If you do not make another payment for the API after one year, the file will be permanently deleted. * Usage instructions for the OCR field:     > OCR Pages Package must be used in conjunction with PDF Pages Package; both packages are deducted equally.     > Three parameters are available: defaults to disable, with optional values auto or force.     > When OCR is set to force, it allows OCR Pages Package usage for Word documents. However, for other document types like ePub and Markdown, it won't take effect.  For reference, other statuses are as follows:  ``` UN_PARSED = 1                      file uploaded or collection has no document LINK_UN_PARSED = 10                file link submitted PARSING = 12                       parsing, mainly used for collection LINK_DOWNLOADING = 15              file link downloading PDF_CONVERTING = 20                docx to pdf converting PDF_CONVERTED = 30                 docx to pdf success TEXT_PARSING = 40                  text embedding（when element parse timeout 2min） ELEMENT_PARSING = 50               element embedding INSIGHT_CALLBACK = 70              element parse success TEXT_PARSED = 210                  text embedding success ELEMENT_PARSED = 300               element embedding success TEXT_PARSE_ERROR = -1              text embedding failed ELEMENT_PARED_ERROR = -2           element embedding failed PDF_CONVERT_ERROR = -3             docx to pdf failed LINK_DOWNLOAD_ERROR = -4           file link download failed EXCEED_SIZE_ERROR = -5             file size exceed limit EXCEED_TOKENS_ERROR = -6           exceed tokens limit PAGE_PACKAGE_NOT_ENOUGH_ERROR = -9 page package not enough PAGE_LIMIT_ERROR = -10             page limit error TITLE_COMPLETE_ERROR = -11         complete title failed READ_TMP_FILE_ERROR = -12          read tmp file error OCR_PAGE_LIMIT_ERROR = -13         ocr page limit error CONTENT_POLICY_ERROR = -14         content security check did not pass CONTENT_DECODE_ERROR = -15         file content decode error HTML_CONVERT_ERROR = -16           html convert error HTML_EMPTY_BODY_ERROR = -17        content is empty HTML_PARSE_ERROR = -18             html parse error HTML_DOWNLOAD_ERROR = -19          html download error from website PACKAGE_NOT_ENOUGH_ERROR = -25     package not enough ```

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
from chatdoc.models.api_upload_resp import APIUploadResp
from chatdoc.models.package_type import PackageType
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
    api_instance = chatdoc.DocumentsApi(api_client)
    file = None  # bytearray | 
    package_type = chatdoc.PackageType()  # PackageType |  (optional)
    collection_id = 'collection_id_example'  # str | if provided, add document to the collection, collection can be created by `POST /collections` (optional)
    ocr = chatdoc.UploadOcrType()  # UploadOcrType |  (optional)

    try:
        # Upload Document
        api_response = api_instance.upload_document_documents_upload_post(file, package_type=package_type,
                                                                          collection_id=collection_id, ocr=ocr)
        print("The response of DocumentsApi->upload_document_documents_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->upload_document_documents_upload_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **package_type** | [**PackageType**](PackageType.md)|  | [optional] 
 **collection_id** | **str**| if provided, add document to the collection, collection can be created by &#x60;POST /collections&#x60; | [optional] 
 **ocr** | [**UploadOcrType**](UploadOcrType.md)|  | [optional] 

### Return type

[**APIUploadResp**](APIUploadResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_documents_website_post**
> APIUploadResp upload_document_documents_website_post(website_req)

Upload Document

Upload a document by website  **Response**:  * `id`: document id, also called `upload_id`, you can use it to get the document by `GET /documents/{upload_id}`. It's of uuid format.  **Please note**: you should store `id` in your database, because we don't have a `GET /documents/list` API to list all documents for now.  * `status`: Once uploaded, the status is `UN_PARSED`, after a series of processing, the status would change by time, and finally to be one of the following two cases:  ``` UN_PARSED = 1              file uploaded or collection has no document # final statuses ELEMENT_PARSED = 300       analysis of the document has succeeded ERROR_STATUSES (< 0)       error occurred during analysis ```  So before the document status finalized, you can poll the status by `GET /documents/{upload_id}` at interval of 10s , generally it takes 1-2 minutes to finish depending on content length of the document. If error occurred, it doesn't consume your quota.  **Please note**:  * Uploading files consumes your pages quota, and uploading same files again will still consume quota. * We'll keep your uploaded file for one year. If you do not make another payment for the API after one year, the file will be permanently deleted.  For reference, other statuses are as follows:  ``` UN_PARSED = 1                      file uploaded or collection has no document LINK_UN_PARSED = 10                file link submitted PARSING = 12                       parsing, mainly used for collection LINK_DOWNLOADING = 15              file link downloading PDF_CONVERTING = 20                docx to pdf converting PDF_CONVERTED = 30                 docx to pdf success TEXT_PARSING = 40                  text embedding（when element parse timeout 2min） ELEMENT_PARSING = 50               element embedding INSIGHT_CALLBACK = 70              element parse success TEXT_PARSED = 210                  text embedding success ELEMENT_PARSED = 300               element embedding success TEXT_PARSE_ERROR = -1              text embedding failed ELEMENT_PARED_ERROR = -2           element embedding failed PDF_CONVERT_ERROR = -3             docx to pdf failed LINK_DOWNLOAD_ERROR = -4           file link download failed EXCEED_SIZE_ERROR = -5             file size exceed limit EXCEED_TOKENS_ERROR = -6           exceed tokens limit PAGE_PACKAGE_NOT_ENOUGH_ERROR = -9 page package not enough PAGE_LIMIT_ERROR = -10             page limit error TITLE_COMPLETE_ERROR = -11         complete title failed READ_TMP_FILE_ERROR = -12          read tmp file error OCR_PAGE_LIMIT_ERROR = -13         ocr page limit error CONTENT_POLICY_ERROR = -14         content security check did not pass CONTENT_DECODE_ERROR = -15         file content decode error HTML_CONVERT_ERROR = -16           html convert error HTML_EMPTY_BODY_ERROR = -17        content is empty HTML_PARSE_ERROR = -18             html parse error HTML_DOWNLOAD_ERROR = -19          html download error from website PACKAGE_NOT_ENOUGH_ERROR = -25     package not enough ```

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
from chatdoc.models.api_upload_resp import APIUploadResp
from chatdoc.models.website_req import WebsiteReq
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
    api_instance = chatdoc.DocumentsApi(api_client)
    website_req = chatdoc.WebsiteReq()  # WebsiteReq | 

    try:
        # Upload Document
        api_response = api_instance.upload_document_documents_website_post(website_req)
        print("The response of DocumentsApi->upload_document_documents_website_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->upload_document_documents_website_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_req** | [**WebsiteReq**](WebsiteReq.md)|  | 

### Return type

[**APIUploadResp**](APIUploadResp.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

