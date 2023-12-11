# openapi_client.QuestionsApi

All URIs are relative to *https://api.chatdoc.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ask_question_questions_post**](QuestionsApi.md#ask_question_questions_post) | **POST** /questions | Ask Question
[**ask_question_with_multiple_documents_questions_multi_documents_post**](QuestionsApi.md#ask_question_with_multiple_documents_questions_multi_documents_post) | **POST** /questions/multi-documents | Ask Question With Multiple Documents
[**get_question_questions_question_id_get**](QuestionsApi.md#get_question_questions_question_id_get) | **GET** /questions/{question_id} | Get Question
[**get_suggested_questions_questions_suggested_get**](QuestionsApi.md#get_suggested_questions_questions_suggested_get) | **GET** /questions/suggested | Get Suggested Questions


# **ask_question_questions_post**
> object ask_question_questions_post(question_req)

Ask Question

Chat with the document, response in [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) mode by default, you can change it through `stream` parameter.  Consume one question quota whether it's upon single document or collection.  **Response**:  if document is pdf/doc/docx format, structure is as follows:  ```json {     \"data\": {         \"answer\": \"answer to the question\",         \"id\": question_id,         \"source_info\": [             {                 # key: page number                 # value: rects                 '0': [[38.1063, 557.8058, 553.9003, 584.0043]]             },             {'1': [[38.0, 152.3994, 523.6151, 178.6392]], 'upload_id': 'xxxx'},             {'0': [[38.0, 758.0623, 537.0082, 784.0]], 'upload_id': 'xxxx'},             ...         ]     } } ```  if document is md/epub/txt/website format, structure is as follows:  ```json {     \"data\": {         \"answer\": \"answer to the question\",         \"id\": question_id,         \"source_info\": [             {             # key: element data-index             # value: element xpath             198: [{xpath: \"/html/body/div/div[199]\"}]             },             {             \"material\": \"\", # selected text with HTML tags             \"indexes\": [                 3,                 4,                 5,                 6             ],             \"focusNode\": \"div[1]/p[5]/text()[1]\",             \"upload_id\": \"903d971d-8250-47cc-a649-4b6ca35032dc\",             \"anchorNode\": \"div[1]/p[2]/text()[1]\",             \"focusOffset\": \"225\",             \"anchorOffset\": \"2\"         }             ...         ]     } } ```  * `answer`: chunks of answer, may be Markdown format to support rich text, for example: [Tables](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables). For `detailed_citation` answer, the span tag chunk may be as follows:      ```     autobiography captured the pre-Nazi Europe[<span data-index=\"0\">1</span>]     ```      The tag attr `data-index` is the index of the source in `source_info` array, which is used to highlight the source of the previous answer sentences in your PDF viewer. The highlighting method is same as `source_info`, and just use slice of `source_info` array as parameter.  * `id`: id of the question, you can use it to `GET /questions/{question_id}` later.  **Please note**: you should store `id` in your database, because we don't have a `GET /questions/list` API to list all questions for now.  * `source_info`: only responses in the last chunk of server-sent events mode, may be an empty list. So if the last chunk doesn't contain `source_info` attr, it means error occurred. Page number may not be ordered, you can use this information to highlight the source of specific `upload_id` document of the answer in your PDF viewer, by     calling [`drawSources`](/#section/ChatDOC-Document-Viewer/Methods) method of our DOCViewerSDK, and converting `source_info` to [`Source`](/#section/ChatDOC-Document-Viewer/Source) parameter.

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
from chatdoc.models.question_req import QuestionReq
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
    api_instance = chatdoc.QuestionsApi(api_client)
    question_req = chatdoc.QuestionReq()  # QuestionReq | 

    try:
        # Ask Question
        api_response = api_instance.ask_question_questions_post(question_req)
        print("The response of QuestionsApi->ask_question_questions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsApi->ask_question_questions_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_req** | [**QuestionReq**](QuestionReq.md)|  | 

### Return type

**object**

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

# **ask_question_with_multiple_documents_questions_multi_documents_post**
> object ask_question_with_multiple_documents_questions_multi_documents_post(question_req_with_upload_ids)

Ask Question With Multiple Documents

Chat with multiple documents, similar with `POST /questions`.  Consume one question quota no matter how many documents you ask upon.  **Response**:  Same as `POST /questions`.

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
from chatdoc.models.question_req_with_upload_ids import QuestionReqWithUploadIds
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
    api_instance = chatdoc.QuestionsApi(api_client)
    question_req_with_upload_ids = chatdoc.QuestionReqWithUploadIds()  # QuestionReqWithUploadIds | 

    try:
        # Ask Question With Multiple Documents
        api_response = api_instance.ask_question_with_multiple_documents_questions_multi_documents_post(
            question_req_with_upload_ids)
        print("The response of QuestionsApi->ask_question_with_multiple_documents_questions_multi_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling QuestionsApi->ask_question_with_multiple_documents_questions_multi_documents_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_req_with_upload_ids** | [**QuestionReqWithUploadIds**](QuestionReqWithUploadIds.md)|  | 

### Return type

**object**

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

# **get_question_questions_question_id_get**
> QuestionResp get_question_questions_question_id_get(question_id)

Get Question

Get a question detail  **Response**:  * `answer`: full content of answer, including content of Markdown format  * `type`: question type, refer [4 Ways to Make Queries](https://chatdoc.notion.site/4-Ways-to-Make-Queries-3d8d6d36060b4c7eb1d69e6a32405dd7):     * doc: Ask About Full Text     * select: Ask About Selected Text  * `source_info`: source information of answer, same with `POST /questions`

### Example

* Bearer Authentication (HTTPBearer):

```python
import time
import os
import chatdoc
from chatdoc.models.question_resp import QuestionResp
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
    api_instance = chatdoc.QuestionsApi(api_client)
    question_id = 56  # int | 

    try:
        # Get Question
        api_response = api_instance.get_question_questions_question_id_get(question_id)
        print("The response of QuestionsApi->get_question_questions_question_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsApi->get_question_questions_question_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**|  | 

### Return type

[**QuestionResp**](QuestionResp.md)

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

# **get_suggested_questions_questions_suggested_get**
> List[str] get_suggested_questions_questions_suggested_get(upload_id)

Get Suggested Questions

Suggested questions for a document, defaults to 5 questions.  Response example: ```json [     \"What is the name of the author?\",     \"What is the name of the book?\",     \"When was the book published?\",     \"What is the name of the publisher?\",     \"Where is the book published?\" ] ```  Only when analysis of the document has succeeded(status=300), can questions be generated.

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
    api_instance = chatdoc.QuestionsApi(api_client)
    upload_id = 'upload_id_example'  # str | document id or collection id, created by `POST /documents/upload` or `POST /collections` APIs accordingly.

    try:
        # Get Suggested Questions
        api_response = api_instance.get_suggested_questions_questions_suggested_get(upload_id)
        print("The response of QuestionsApi->get_suggested_questions_questions_suggested_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsApi->get_suggested_questions_questions_suggested_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| document id or collection id, created by &#x60;POST /documents/upload&#x60; or &#x60;POST /collections&#x60; APIs accordingly. | 

### Return type

**List[str]**

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

