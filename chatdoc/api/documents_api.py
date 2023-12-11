# coding: utf-8

"""
    ChatDOC API

    # Introduction  Welcome to ChatDOC API, Version 0.2.0!  ChatDOC is a powerful SaaS AI product that enables you to engage with documents, instantly retrieving answers along with cited sources. Our API provides developers with the tools to interact with the ChatDOC system, allowing you to create immersive experiences for your users.  This reference serves as a comprehensive guide to the ChatDOC system and its Version 0.2.0 API. Here, you'll find detailed information on the objects and endpoints used in the API. We greatly value your feedback. If you notice any missing or inaccurate information, please don't hesitate to open an issue on [GitHub](https://github.com/chatdoc-com/chatdoc-com.github.io/issues) or submit a pull request to help improve our documentation.   > To leverage ChatDOC's API capabilities, you'll need an API key. API keys can be   created by subscribing to an appropriate membership plan or purchasing an API package on   [ChatDOC.com](https://chatdoc.com/).  ## Conventions  All API requests should be directed to the domain `api.chatdoc.com`. and secure HTTPS is mandatory for all interactions.  Our ChatDOC API adheres to RESTful conventions where applicable, utilizing standard HTTP methods such as GET, POST, PUT, and DELETE. Request and response payloads are encoded in JSON format.  HTTP status codes are used in accordance with industry standards. Successful requests return a 200 OK response, while failed requests produce 4xx or 5xx error codes.  Please note that this documentation pertains to ChatDOC API Version 0.2.0, which is not backward compatible with Version 0.1.0. While Version 0.1.0 remains functional, we strongly encourage users to migrate to Version 0.2.0 for the best experience.  If you have any questions or need further assistance, please don't hesitate to reach out to our support team.  This revised introduction reflects the transition to ChatDOC API Version 0.2.0 and highlights its features and benefits.  ## JSON conventions  * Response body of success requests is generally as follows:      ```json     {       \"status\": \"ok\",       \"data\": {         \"id\": 160,         \"name\": \"Bo\",         ...       }     }     ```      * `status` and `data` are common properties.     * Object properties are contained directly in `data`, there is no extra model objects. (e.g. \"document\", \"user\", etc.) * And failed response may be:      `400 Bad Request`      ```json     {         \"detail\": \"Error message\"     }     ```      * `detail` is the error message.     * `status` is not returned.      `404 Not Found`      ```json     {         \"data\": {},         \"detail\": \"This page has expired, please refresh the page and try again.\"     }     ```      * `detail` of `404` is unified as above message, no matter which kind of resources you get.  * Property names are in snake_case (not camelCase or kebab-case). * Time is stored as [Unix timestamps](https://www.unixtimestamp.com/) in seconds, and this point in time technically does not change no matter where you are located on the globe. You can convert it to datetime of your local timezone. * Optional properties are nullable, you can just ignore it sometimes.  ## Request limits  To ensure a consistent developer experience for all API users, the ChatDOC API is rate limited.  ## Authentication  Requests use the HTTP `Authorization` header to both authenticate and authorize operations. The ChatDOC API accepts bearer tokens in this header. Bearer keys can be managed in our web site.  ```curl curl 'https://api.chatdoc.com/api/v2/documents/upload'   -H 'Authorization: Bearer \"$API_KEY\"' ```  Different keys of the same user are interoperable of each others' resource, they share common permission of the user.  **Please note**: keep your API keys confidential, and do not put them in any client code, including browser html and mobile client, API interactions should be done on the server side.  # Quick Start To use the **ChatDOC API**, you have two options: - Directly call the [ChatDOC RESTful API](#section/ChatDOC-RESTful-API) from your own service and custom the UI by yourself. - Use the `@chatdocai/chatdoc-sdk` to display documents(.pdf, .epub, .txt, .md, .html) and retrieve data by calling the ChatDOC RESTful API.    > Before using the API, you need to obtain an API Key on [ChatDOC.com](https://chatdoc.com/).  You can download [ChatDOC-API-Demo](https://github.com/chatdoc-com/ChatDOC-API-Demo) to start your application. ```sh git clone https://github.com/chatdoc-com/ChatDOC-API-Demo ```     > The  server folder is an node server, which request the ChatDOC RESTful API.     > The  client folder is a vue web app, which use `@chatdocai/chatdoc-sdk` to show the document, and request the node server.  Here are the steps to start the demo: 1. run `pnpm install` 2. Set the env variable **API_KEY**.  > **API_KEY** is the API key that you obtained after purchasing the API package or membership plan.  3. run `pnpm start`  > When using a self-signed certificate in your local development environment, you may encounter a browser prompt saying: 'This site can't provide a secure connection'. Please be aware that this is a specific situation in the local development environment and will not affect the use of your genuine SSL certificate when deployed online. For online deployment, you can use your own SSL certificate to ensure a secure connection.  By following these steps, you will have a simple ChatDOC API application.  If you only want to know how to use the `@chatdocai/chatdoc-sdk`, you can refer to the [ChatDOC Document Viewer](#section/ChatDOC-Document-Viewer) section.  Here are some typical use cases of `@chatdocai/chatdoc-sdk` in the demo that you might be interested in:  1. When you select text on the document and click the chat icon, you can obtain the [`HTMLMaterialData`](#section/ChatDOC-Document-Viewer/HTMLMaterialData) or [`PDFMaterialData`](#section/ChatDOC-Document-Viewer/PDFMaterialData) from the callback handler of [EVENT_TYPES.CHAT_ICON_CLICKED](#section/ChatDOC-Document-Viewer/EVENT_TYPES) event. Then, you can post it to the [Ask Question API](#tag/Questions/operation/Ask_Question_questions_post).  2. The response from the [Ask Question API](#tag/Questions/operation/Ask_Question_questions_post) contains the `source_info` field. You can convert the `source_info` to the data type of [Source](#section/ChatDOC-Document-Viewer/Source) and   use the [drawSources](#section/ChatDOC-Document-Viewer/Methods) method of `@chatdocai/chatdoc-sdk` to navigate to the page of the sources and highlight them.  3. By using the [setFileUrl](#section/ChatDOC-Document-Viewer/Methods) method of @chatdocai/chatdoc-sdk, you can switch the displayed document.      # ChatDOC Document Viewer If you want to view the document in the browser, you can use the `@chatdocai/chatdoc-sdk` npm package.  The `@chatdocai/chatdoc-sdk` npm package is used to display documents(.pdf, .epub, .txt, .md, .html) and interact with them by selecting text and asking questions. Here are the steps to get started:  1. **Install `@chatdocai/chatdoc-sdk`**     ```bash    pnpm install @chatdocai/chatdoc-sdk    # npm install @chatdocai/chatdoc-sdk    # yarn add @chatdocai/chatdoc-sdk    ``` 2. **Init chatdoc-sdk**      Initialize the chatdoc-sdk by importing the **initSDK** function from `@chatdocai/chatdoc-sdk` and using it to create an instance of the [DOCViewerSDK](#section/ChatDOC-Document-Viewer/DOCViewerSDK).       Please provide the DOM element or CSS selector string where you want to mount the SDK. You can find detailed parameter information in the [Config](#section/ChatDOC-Document-Viewer/Config) section.      **Usage Example:**      ```js     import { initSDK } from '@chatdocai/chatdoc-sdk';      const sdk = initSDK({       el: '#doc-viewer',     })      ``` 3. **Open document**      Use the `open` method of `@chatdocai/chatdoc-sdk` to open the document.      **Usage Example:**      ```js     // Please replace the URL with your own file URL.     sdk.open({url: 'https://example.com/pdf-file.pdf', viewerType: 'pdf'})      // If you want to view other documents (such as .epub, .html, .txt, .md), you need to set the viewerType to `html`.     sdk.open({url: 'https://example.com/document.txt', viewerType: 'html'})     ```     4. **Add event listener**      Add event listeners to handle specific events. For example, you can listen to the **CHAT_ICON_CLICKED** event to get the selected text from the document when the chat icon is clicked.      The `@chatdocai/chatdoc-sdk` package also exports the EVENT_TYPES object, which types the [event name](#section/ChatDOC-Document-Viewer/EVENT_TYPES).      **Usage Example:**     ```js     import { EVENT_TYPES } from '@chatdocai/chatdoc-sdk';      // this event is dispatched after you clicked the chat icon in document     sdk.on(EVENT_TYPES.CHAT_ICON_CLICKED, (data) => {       // if your viewType is `pdf`, the data is `PDFMaterialData`       // if your viewType is `html`, the data is `HTMLMaterialData`       console.log(data)     });      ```  ## DOCViewerSDK The DOCViewerSDK class provides a document viewer SDK with various methods and properties for interacting with the document viewer. Here are some key details about the class:   ## Config  The configuration parameters for the SDK.   **Properties:**  - **el:** `string | HTMLElement` - the DOM element or CSS selector string used for mounting and rendering the SDK.  - **fileUrl:** `string` (optional) `Deprecated` - The URL of the document. (This field is no longer recommended for use in new code. Consider using the [open](#section/ChatDOC-Document-Viewer/Methods) method instead.)  - **getToken:** `() => Promise<string>` (optional) - An optional function that returns a Promise resolving to a string representing the [JWT](https://jwt.io/) token.The token is encoded using an API key, and the payload is `{\"upload_id\": \"xxx\"}`.     ```js     import jwt from 'jsonwebtoken';     // token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cGxvYWRfaWQiOiI2YjNmYzdlOS1kYzE3LTQwYjYtODI4Ny04MDM5N2JhMWU5MmEifQ.sXUbg6tGtF6KqFtCGALTcm7eG6H23dhrKW1wUAAAyus'     const token = jwt.sign({ upload_id: '6b3fc7e9-dc17-40b6-8287-80397ba1e92a' }, 'ak-ifypHN4we-v07xhp0pDKRG-znEb-5YQeFuhXgjt4byM', { noTimestamp: true} );     ```  **Usage Example:** ```javascript  // node server import jwt from 'jsonwebtoken'; async getDocumentToken(ctx) {   const { id: uploadId } = ctx.params   const token = jwt.sign({ upload_id: uploadId }, 'API_KEY', { noTimestamp: true} );   ctx.body = {     status: 'ok',     data: {token}   } }  // client const getToken = async () => {   const { token } = await getDocumentToken('uploadId');   return token; }; const config: Config = {   el: '#pdf-viewer',   getToken };   ``` ## ViewType   This type represents the available view types for a document. It is a union type that can have one of two values: `pdf` or `html`. This type is utilized to specify the desired view type when rendering or displaying a document.  - **pdf:** Set the view type to 'pdf' when you want to view files with the .pdf extension. - **html:** Set the view type to 'html' when you want to view files with .txt, .md, .epub, or .html extensions.  ## FileOptions  The `FileOptions` type represents the options for opening a document.  **Properties:**  - **url:** `string` - The URL of the document. - **viewerType:** [`ViewType`](#section/ChatDOC-Document-Viewer/ViewType) - The desired view type for rendering the document, which can be either `pdf` or `html`.  **Usage Example:**  ```javascript const options = {   url: 'https://example.com/document.pdf',   viewerType: 'pdf', }; ```  ## Source  The Source type represents a source in the SDK, which is the parameter of the [drawSources](#section/ChatDOC-Document-Viewer/Methods) method.  **Properties:**  - **pageNumber:** `number` - The page number of the source.  - **rects:** `number[][]` -  An array of rectangles represented by four numbers `[left, top, right, bottom]` indicating their positions within the source coordinates.  **Usage Example:** ``` const source: Source = {   pageNumber: 1,   rects: [[10, 10, 50, 50], [60, 60, 100, 100]], }; ```  ## HTMLMaterialData  The `HTMLMaterialData` type contains the material content and the document selection obtained from the callback handler of the EVENT_TYPES.CHAT_ICON_CLICKED event when the [FileOptions.viewType](#section/ChatDOC-Document-Viewer/ViewType) is set to `html`.  **Properties:**  - **material:** `string` - The selected text or HTML content.  - **indexes:** `number[]` - An array of indexes representing the selected text node index in the document.  - **focusNode**: `string` - A XPath string of the selection's focusNode in the document.  - **focusOffset**: `number` - The number of characters that the selection's focus is offset within the focusNode.  - **anchorNode**: `string` - A XPath string of the selection's anchorNode in the document.  - **anchorOffset**: `number` - The number of characters that the selection's anchor is offset within anchorNode.  **Usage Example:** ``` const material: HTMLMaterialData = {   material: 'content',   indexes: [1, 2, 3],   focusNode: 'div/div[4]/text()',   focusOffset: 2,   anchorNode: 'div/div[2]/text()',   anchorOffset: 3, }; ```  ## PDFMaterialData The `PDFMaterialData` type contains the selected text and the outlines in the document obtained from the callback handler of the EVENT_TYPES.CHAT_ICON_CLICKED event when the [FileOptions.viewType](#section/ChatDOC-Document-Viewer/ViewType) is set to `pdf`.  **Properties:**  - **material:** `string` - The selected text.  - **rects:** [`Rect[]`](#section/ChatDOC-Document-Viewer/Rect) (optional) - An array of rectangles representing the outlines.  **Usage Example:** ``` const material: PDFMaterialData = {   material: 'content',   rects: [     {       pageNumber: 1,       outline: [10, 10, 50, 50],     },     {       pageNumber: 2,       outline: [60, 60, 100, 100],     },   ], }; ```  ## Rect The Rect type represents a rectangle in the document, and it is a field in the [MaterialData](#section/ChatDOC-Document-Viewer/MaterialData) type.  **Properties:**  - **pageNumber:** `number` - The page number of the rectangle.  - **outline:** `number[]` - The outline array represents the rectangle's outline coordinates as four values: `left, top, right, and bottom`.  **Usage Example:** ``` const rect: Rect = {   pageNumber: 1,   outline: [10, 10, 50, 50], }; ``` ## Methods  ### setFileUrl(fileUrl: string): any `Deprecated`  This method is used to set the file URL for opening a document.  - **fileUrl:** `string` - The URL of the file to load.  **`Deprecated Note:`**  It is recommended to use the `open` method instead for opening a document. The `setFileUrl` method is deprecated.  ### drawSources(sources: Source[]): Promise<void>  Draws source rectangles on the document viewer.  - **sources:** [`Source[]`](#section/ChatDOC-Document-Viewer/Source) - The source rectangles to draw.  ### clearSources(): void  Clears source annotations.  ### destroy(): void  Destroys the document viewer SDK instance.  ### on(name: string, handler: Func): void  Adds an event listener for the specified event.  - **name:** `string` - The name of the event, you can get the event name from [EVENT_TYPES](#section/ChatDOC-Document-Viewer/EVENT_TYPES). - **handler:** `Func` - The event handler function.  ### off(name: string, handler: Func): void  Removes an event listener for the specified event.  - **name:** `string` - The name of the event. - **handler:** `Func` - The event handler function.  ### getCurrentPageNumber(): any  Gets the current page number.  - Returns: `any` - The current page number.  ### open(options: FileOptions): any This method is used to open a document using the provided options.  - **options:** [`FileOptions`](#section/ChatDOC-Document-Viewer/FileOptions) - An object that specifies the options for opening the document.  ## EVENT_TYPES  - **PAGE_RENDERED** - After each page is rendered, this event is dispatched, and you can obtain the current page number from the callback handler.  - **CHAT_ICON_CLICKED** - After you clicked the chat icon in document, and you can obtain the [`HTMLMaterialData`](#section/ChatDOC-Document-Viewer/HTMLMaterialData) or [`PDFMaterialData`](#section/ChatDOC-Document-Viewer/PDFMaterialData) from the callback handler.   # OBJECTS  ## Document  You can first upload documents to get started. Supported document formats including pdf, docx/doc, and more formats such as markdown, epub are upcoming.  ## Collection  Collection is just a special type of `document`, they have common properties like `name`, `status` etc. The difference is that as for questioning, a document can be standalone or grouped as a `collection`, each file collection is a customized database, and you can acquire knowledge effortlessly through conversation.  ChatDOC offers three distinct page package types: Elite, Basic, and Lite. When you use one of these page packages to upload a file, the same page package type is automatically applied when you clone that file into a collection.  ## Question  Namely message or chat, there can be [4 Ways to Make Queries](https://chatdoc.notion.site/4-Ways-to-Make-Queries-3d8d6d36060b4c7eb1d69e6a32405dd7):  * **Try our Suggested Queries** * **Ask About Full Text** * **Ask About Selected Text** * **Query across multi docs**  # ChatDOC RESTful API  Consuming quota APIs:  ### Document Pages  * POST /documents/upload * POST /documents/website * POST /collections/clone-documents  ### Questions  * POST /questions * POST /questions/multi-documents 

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBytes, StrictStr

from typing import Any, Optional, Union

from chatdoc.models.api_collection_or_upload_resp import APICollectionOrUploadResp
from chatdoc.models.api_upload_resp import APIUploadResp
from chatdoc.models.package_type import PackageType
from chatdoc.models.website_req import WebsiteReq

from chatdoc.api_client import ApiClient
from chatdoc.api_response import ApiResponse
from chatdoc.rest import RESTResponseType


class DocumentsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def delete_document_documents_upload_id_delete(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """Delete Document

        Delete a document

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_document_documents_upload_id_delete_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_document_documents_upload_id_delete_with_http_info(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """Delete Document

        Delete a document

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_document_documents_upload_id_delete_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_document_documents_upload_id_delete_without_preload_content(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete Document

        Delete a document

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_document_documents_upload_id_delete_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_document_documents_upload_id_delete_serialize(
        self,
        upload_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if upload_id is not None:
            _path_params['upload_id'] = upload_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'HTTPBearer'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/documents/{upload_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def download_document_documents_upload_id_download_get(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> object:
        """Download Document

        Download content of the document, support CORS and range request.  * If the document is of doc/docx format, then it's converted to pdf version, and the original version can't be downloaded. * If the document is of pdf format, it's recommended to use your local file to avoid unnecessary network traffic. * If the document is of md/epub/txt/website format, then it's converted to html version, and the original version can't be downloaded.

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._download_document_documents_upload_id_download_get_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def download_document_documents_upload_id_download_get_with_http_info(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[object]:
        """Download Document

        Download content of the document, support CORS and range request.  * If the document is of doc/docx format, then it's converted to pdf version, and the original version can't be downloaded. * If the document is of pdf format, it's recommended to use your local file to avoid unnecessary network traffic. * If the document is of md/epub/txt/website format, then it's converted to html version, and the original version can't be downloaded.

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._download_document_documents_upload_id_download_get_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def download_document_documents_upload_id_download_get_without_preload_content(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Download Document

        Download content of the document, support CORS and range request.  * If the document is of doc/docx format, then it's converted to pdf version, and the original version can't be downloaded. * If the document is of pdf format, it's recommended to use your local file to avoid unnecessary network traffic. * If the document is of md/epub/txt/website format, then it's converted to html version, and the original version can't be downloaded.

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._download_document_documents_upload_id_download_get_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "object",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _download_document_documents_upload_id_download_get_serialize(
        self,
        upload_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if upload_id is not None:
            _path_params['upload_id'] = upload_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'HTTPBearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/documents/{upload_id}/download',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_document_documents_upload_id_get(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> APICollectionOrUploadResp:
        """Get Document

        Get a document  **Response**:  Similar with `POST /documents/upload`, and pay attention to the following fields:  * `type`:     * collection: document collection     * single_doc: standalone document     * doc_of_collection: sub document of collection  * `documents`: sub document list of collection, which only returns for collection

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_document_documents_upload_id_get_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APICollectionOrUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_document_documents_upload_id_get_with_http_info(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[APICollectionOrUploadResp]:
        """Get Document

        Get a document  **Response**:  Similar with `POST /documents/upload`, and pay attention to the following fields:  * `type`:     * collection: document collection     * single_doc: standalone document     * doc_of_collection: sub document of collection  * `documents`: sub document list of collection, which only returns for collection

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_document_documents_upload_id_get_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APICollectionOrUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_document_documents_upload_id_get_without_preload_content(
        self,
        upload_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Document

        Get a document  **Response**:  Similar with `POST /documents/upload`, and pay attention to the following fields:  * `type`:     * collection: document collection     * single_doc: standalone document     * doc_of_collection: sub document of collection  * `documents`: sub document list of collection, which only returns for collection

        :param upload_id: (required)
        :type upload_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_document_documents_upload_id_get_serialize(
            upload_id=upload_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APICollectionOrUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_document_documents_upload_id_get_serialize(
        self,
        upload_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if upload_id is not None:
            _path_params['upload_id'] = upload_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'HTTPBearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/documents/{upload_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def upload_document_documents_upload_post(
        self,
        file: Union[StrictBytes, StrictStr],
        package_type: Optional[PackageType] = None,
        collection_id: Annotated[Optional[StrictStr], Field(description="if provided, add document to the collection, collection can be created by `POST /collections`")] = None,
        ocr: Optional[Any] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> APIUploadResp:
        """Upload Document

        Upload a document  **Response**:  * `id`: document id, also called `upload_id`, you can use it to get the document by `GET /documents/{upload_id}`. It's of uuid format.  **Please note**: you should store `id` in your database, because we don't have a `GET /documents/list` API to list all documents for now.  * `status`: Once uploaded, the status is `UN_PARSED`, after a series of processing, the status would change by time, and finally to be one of the following two cases:  ``` UN_PARSED = 1              file uploaded or collection has no document # final statuses ELEMENT_PARSED = 300       analysis of the document has succeeded ERROR_STATUSES (< 0)       error occurred during analysis ```  So before the document status finalized, you can poll the status by `GET /documents/{upload_id}` at interval of 10s , generally it takes 1-2 minutes to finish depending on content length of the document. If error occurred, it doesn't consume your quota.  **Please note**:  * Uploading files consumes your pages quota, and uploading same files again will still consume quota. * We'll keep your uploaded file for one year. If you do not make another payment for the API after one year, the file will be permanently deleted. * Usage instructions for the OCR field:     > OCR Pages Package must be used in conjunction with PDF Pages Package; both packages are deducted equally.     > Three parameters are available: defaults to disable, with optional values auto or force.     > When OCR is set to force, it allows OCR Pages Package usage for Word documents. However, for other document types like ePub and Markdown, it won't take effect.  For reference, other statuses are as follows:  ``` UN_PARSED = 1                      file uploaded or collection has no document LINK_UN_PARSED = 10                file link submitted PARSING = 12                       parsing, mainly used for collection LINK_DOWNLOADING = 15              file link downloading PDF_CONVERTING = 20                docx to pdf converting PDF_CONVERTED = 30                 docx to pdf success TEXT_PARSING = 40                  text embedding（when element parse timeout 2min） ELEMENT_PARSING = 50               element embedding INSIGHT_CALLBACK = 70              element parse success TEXT_PARSED = 210                  text embedding success ELEMENT_PARSED = 300               element embedding success TEXT_PARSE_ERROR = -1              text embedding failed ELEMENT_PARED_ERROR = -2           element embedding failed PDF_CONVERT_ERROR = -3             docx to pdf failed LINK_DOWNLOAD_ERROR = -4           file link download failed EXCEED_SIZE_ERROR = -5             file size exceed limit EXCEED_TOKENS_ERROR = -6           exceed tokens limit PAGE_PACKAGE_NOT_ENOUGH_ERROR = -9 page package not enough PAGE_LIMIT_ERROR = -10             page limit error TITLE_COMPLETE_ERROR = -11         complete title failed READ_TMP_FILE_ERROR = -12          read tmp file error OCR_PAGE_LIMIT_ERROR = -13         ocr page limit error CONTENT_POLICY_ERROR = -14         content security check did not pass CONTENT_DECODE_ERROR = -15         file content decode error HTML_CONVERT_ERROR = -16           html convert error HTML_EMPTY_BODY_ERROR = -17        content is empty HTML_PARSE_ERROR = -18             html parse error HTML_DOWNLOAD_ERROR = -19          html download error from website PACKAGE_NOT_ENOUGH_ERROR = -25     package not enough ```

        :param file: (required)
        :type file: bytearray
        :param package_type:
        :type package_type: PackageType
        :param collection_id: if provided, add document to the collection, collection can be created by `POST /collections`
        :type collection_id: str
        :param ocr:
        :type ocr: UploadOcrType
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_document_documents_upload_post_serialize(
            file=file,
            package_type=package_type,
            collection_id=collection_id,
            ocr=ocr,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APIUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def upload_document_documents_upload_post_with_http_info(
        self,
        file: Union[StrictBytes, StrictStr],
        package_type: Optional[PackageType] = None,
        collection_id: Annotated[Optional[StrictStr], Field(description="if provided, add document to the collection, collection can be created by `POST /collections`")] = None,
        ocr: Optional[Any] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[APIUploadResp]:
        """Upload Document

        Upload a document  **Response**:  * `id`: document id, also called `upload_id`, you can use it to get the document by `GET /documents/{upload_id}`. It's of uuid format.  **Please note**: you should store `id` in your database, because we don't have a `GET /documents/list` API to list all documents for now.  * `status`: Once uploaded, the status is `UN_PARSED`, after a series of processing, the status would change by time, and finally to be one of the following two cases:  ``` UN_PARSED = 1              file uploaded or collection has no document # final statuses ELEMENT_PARSED = 300       analysis of the document has succeeded ERROR_STATUSES (< 0)       error occurred during analysis ```  So before the document status finalized, you can poll the status by `GET /documents/{upload_id}` at interval of 10s , generally it takes 1-2 minutes to finish depending on content length of the document. If error occurred, it doesn't consume your quota.  **Please note**:  * Uploading files consumes your pages quota, and uploading same files again will still consume quota. * We'll keep your uploaded file for one year. If you do not make another payment for the API after one year, the file will be permanently deleted. * Usage instructions for the OCR field:     > OCR Pages Package must be used in conjunction with PDF Pages Package; both packages are deducted equally.     > Three parameters are available: defaults to disable, with optional values auto or force.     > When OCR is set to force, it allows OCR Pages Package usage for Word documents. However, for other document types like ePub and Markdown, it won't take effect.  For reference, other statuses are as follows:  ``` UN_PARSED = 1                      file uploaded or collection has no document LINK_UN_PARSED = 10                file link submitted PARSING = 12                       parsing, mainly used for collection LINK_DOWNLOADING = 15              file link downloading PDF_CONVERTING = 20                docx to pdf converting PDF_CONVERTED = 30                 docx to pdf success TEXT_PARSING = 40                  text embedding（when element parse timeout 2min） ELEMENT_PARSING = 50               element embedding INSIGHT_CALLBACK = 70              element parse success TEXT_PARSED = 210                  text embedding success ELEMENT_PARSED = 300               element embedding success TEXT_PARSE_ERROR = -1              text embedding failed ELEMENT_PARED_ERROR = -2           element embedding failed PDF_CONVERT_ERROR = -3             docx to pdf failed LINK_DOWNLOAD_ERROR = -4           file link download failed EXCEED_SIZE_ERROR = -5             file size exceed limit EXCEED_TOKENS_ERROR = -6           exceed tokens limit PAGE_PACKAGE_NOT_ENOUGH_ERROR = -9 page package not enough PAGE_LIMIT_ERROR = -10             page limit error TITLE_COMPLETE_ERROR = -11         complete title failed READ_TMP_FILE_ERROR = -12          read tmp file error OCR_PAGE_LIMIT_ERROR = -13         ocr page limit error CONTENT_POLICY_ERROR = -14         content security check did not pass CONTENT_DECODE_ERROR = -15         file content decode error HTML_CONVERT_ERROR = -16           html convert error HTML_EMPTY_BODY_ERROR = -17        content is empty HTML_PARSE_ERROR = -18             html parse error HTML_DOWNLOAD_ERROR = -19          html download error from website PACKAGE_NOT_ENOUGH_ERROR = -25     package not enough ```

        :param file: (required)
        :type file: bytearray
        :param package_type:
        :type package_type: PackageType
        :param collection_id: if provided, add document to the collection, collection can be created by `POST /collections`
        :type collection_id: str
        :param ocr:
        :type ocr: UploadOcrType
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_document_documents_upload_post_serialize(
            file=file,
            package_type=package_type,
            collection_id=collection_id,
            ocr=ocr,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APIUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def upload_document_documents_upload_post_without_preload_content(
        self,
        file: Union[StrictBytes, StrictStr],
        package_type: Optional[PackageType] = None,
        collection_id: Annotated[Optional[StrictStr], Field(description="if provided, add document to the collection, collection can be created by `POST /collections`")] = None,
        ocr: Optional[Any] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Upload Document

        Upload a document  **Response**:  * `id`: document id, also called `upload_id`, you can use it to get the document by `GET /documents/{upload_id}`. It's of uuid format.  **Please note**: you should store `id` in your database, because we don't have a `GET /documents/list` API to list all documents for now.  * `status`: Once uploaded, the status is `UN_PARSED`, after a series of processing, the status would change by time, and finally to be one of the following two cases:  ``` UN_PARSED = 1              file uploaded or collection has no document # final statuses ELEMENT_PARSED = 300       analysis of the document has succeeded ERROR_STATUSES (< 0)       error occurred during analysis ```  So before the document status finalized, you can poll the status by `GET /documents/{upload_id}` at interval of 10s , generally it takes 1-2 minutes to finish depending on content length of the document. If error occurred, it doesn't consume your quota.  **Please note**:  * Uploading files consumes your pages quota, and uploading same files again will still consume quota. * We'll keep your uploaded file for one year. If you do not make another payment for the API after one year, the file will be permanently deleted. * Usage instructions for the OCR field:     > OCR Pages Package must be used in conjunction with PDF Pages Package; both packages are deducted equally.     > Three parameters are available: defaults to disable, with optional values auto or force.     > When OCR is set to force, it allows OCR Pages Package usage for Word documents. However, for other document types like ePub and Markdown, it won't take effect.  For reference, other statuses are as follows:  ``` UN_PARSED = 1                      file uploaded or collection has no document LINK_UN_PARSED = 10                file link submitted PARSING = 12                       parsing, mainly used for collection LINK_DOWNLOADING = 15              file link downloading PDF_CONVERTING = 20                docx to pdf converting PDF_CONVERTED = 30                 docx to pdf success TEXT_PARSING = 40                  text embedding（when element parse timeout 2min） ELEMENT_PARSING = 50               element embedding INSIGHT_CALLBACK = 70              element parse success TEXT_PARSED = 210                  text embedding success ELEMENT_PARSED = 300               element embedding success TEXT_PARSE_ERROR = -1              text embedding failed ELEMENT_PARED_ERROR = -2           element embedding failed PDF_CONVERT_ERROR = -3             docx to pdf failed LINK_DOWNLOAD_ERROR = -4           file link download failed EXCEED_SIZE_ERROR = -5             file size exceed limit EXCEED_TOKENS_ERROR = -6           exceed tokens limit PAGE_PACKAGE_NOT_ENOUGH_ERROR = -9 page package not enough PAGE_LIMIT_ERROR = -10             page limit error TITLE_COMPLETE_ERROR = -11         complete title failed READ_TMP_FILE_ERROR = -12          read tmp file error OCR_PAGE_LIMIT_ERROR = -13         ocr page limit error CONTENT_POLICY_ERROR = -14         content security check did not pass CONTENT_DECODE_ERROR = -15         file content decode error HTML_CONVERT_ERROR = -16           html convert error HTML_EMPTY_BODY_ERROR = -17        content is empty HTML_PARSE_ERROR = -18             html parse error HTML_DOWNLOAD_ERROR = -19          html download error from website PACKAGE_NOT_ENOUGH_ERROR = -25     package not enough ```

        :param file: (required)
        :type file: bytearray
        :param package_type:
        :type package_type: PackageType
        :param collection_id: if provided, add document to the collection, collection can be created by `POST /collections`
        :type collection_id: str
        :param ocr:
        :type ocr: UploadOcrType
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_document_documents_upload_post_serialize(
            file=file,
            package_type=package_type,
            collection_id=collection_id,
            ocr=ocr,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APIUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _upload_document_documents_upload_post_serialize(
        self,
        file,
        package_type,
        collection_id,
        ocr,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if package_type is not None:
            _form_params.append(('package_type', package_type))
        if collection_id is not None:
            _form_params.append(('collection_id', collection_id))
        if ocr is not None:
            _form_params.append(('ocr', ocr))
        if file is not None:
            _files['file'] = file
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'HTTPBearer'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/documents/upload',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def upload_document_documents_website_post(
        self,
        website_req: WebsiteReq,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> APIUploadResp:
        """Upload Document

        Upload a document by website  **Response**:  * `id`: document id, also called `upload_id`, you can use it to get the document by `GET /documents/{upload_id}`. It's of uuid format.  **Please note**: you should store `id` in your database, because we don't have a `GET /documents/list` API to list all documents for now.  * `status`: Once uploaded, the status is `UN_PARSED`, after a series of processing, the status would change by time, and finally to be one of the following two cases:  ``` UN_PARSED = 1              file uploaded or collection has no document # final statuses ELEMENT_PARSED = 300       analysis of the document has succeeded ERROR_STATUSES (< 0)       error occurred during analysis ```  So before the document status finalized, you can poll the status by `GET /documents/{upload_id}` at interval of 10s , generally it takes 1-2 minutes to finish depending on content length of the document. If error occurred, it doesn't consume your quota.  **Please note**:  * Uploading files consumes your pages quota, and uploading same files again will still consume quota. * We'll keep your uploaded file for one year. If you do not make another payment for the API after one year, the file will be permanently deleted.  For reference, other statuses are as follows:  ``` UN_PARSED = 1                      file uploaded or collection has no document LINK_UN_PARSED = 10                file link submitted PARSING = 12                       parsing, mainly used for collection LINK_DOWNLOADING = 15              file link downloading PDF_CONVERTING = 20                docx to pdf converting PDF_CONVERTED = 30                 docx to pdf success TEXT_PARSING = 40                  text embedding（when element parse timeout 2min） ELEMENT_PARSING = 50               element embedding INSIGHT_CALLBACK = 70              element parse success TEXT_PARSED = 210                  text embedding success ELEMENT_PARSED = 300               element embedding success TEXT_PARSE_ERROR = -1              text embedding failed ELEMENT_PARED_ERROR = -2           element embedding failed PDF_CONVERT_ERROR = -3             docx to pdf failed LINK_DOWNLOAD_ERROR = -4           file link download failed EXCEED_SIZE_ERROR = -5             file size exceed limit EXCEED_TOKENS_ERROR = -6           exceed tokens limit PAGE_PACKAGE_NOT_ENOUGH_ERROR = -9 page package not enough PAGE_LIMIT_ERROR = -10             page limit error TITLE_COMPLETE_ERROR = -11         complete title failed READ_TMP_FILE_ERROR = -12          read tmp file error OCR_PAGE_LIMIT_ERROR = -13         ocr page limit error CONTENT_POLICY_ERROR = -14         content security check did not pass CONTENT_DECODE_ERROR = -15         file content decode error HTML_CONVERT_ERROR = -16           html convert error HTML_EMPTY_BODY_ERROR = -17        content is empty HTML_PARSE_ERROR = -18             html parse error HTML_DOWNLOAD_ERROR = -19          html download error from website PACKAGE_NOT_ENOUGH_ERROR = -25     package not enough ```

        :param website_req: (required)
        :type website_req: WebsiteReq
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_document_documents_website_post_serialize(
            website_req=website_req,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APIUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def upload_document_documents_website_post_with_http_info(
        self,
        website_req: WebsiteReq,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[APIUploadResp]:
        """Upload Document

        Upload a document by website  **Response**:  * `id`: document id, also called `upload_id`, you can use it to get the document by `GET /documents/{upload_id}`. It's of uuid format.  **Please note**: you should store `id` in your database, because we don't have a `GET /documents/list` API to list all documents for now.  * `status`: Once uploaded, the status is `UN_PARSED`, after a series of processing, the status would change by time, and finally to be one of the following two cases:  ``` UN_PARSED = 1              file uploaded or collection has no document # final statuses ELEMENT_PARSED = 300       analysis of the document has succeeded ERROR_STATUSES (< 0)       error occurred during analysis ```  So before the document status finalized, you can poll the status by `GET /documents/{upload_id}` at interval of 10s , generally it takes 1-2 minutes to finish depending on content length of the document. If error occurred, it doesn't consume your quota.  **Please note**:  * Uploading files consumes your pages quota, and uploading same files again will still consume quota. * We'll keep your uploaded file for one year. If you do not make another payment for the API after one year, the file will be permanently deleted.  For reference, other statuses are as follows:  ``` UN_PARSED = 1                      file uploaded or collection has no document LINK_UN_PARSED = 10                file link submitted PARSING = 12                       parsing, mainly used for collection LINK_DOWNLOADING = 15              file link downloading PDF_CONVERTING = 20                docx to pdf converting PDF_CONVERTED = 30                 docx to pdf success TEXT_PARSING = 40                  text embedding（when element parse timeout 2min） ELEMENT_PARSING = 50               element embedding INSIGHT_CALLBACK = 70              element parse success TEXT_PARSED = 210                  text embedding success ELEMENT_PARSED = 300               element embedding success TEXT_PARSE_ERROR = -1              text embedding failed ELEMENT_PARED_ERROR = -2           element embedding failed PDF_CONVERT_ERROR = -3             docx to pdf failed LINK_DOWNLOAD_ERROR = -4           file link download failed EXCEED_SIZE_ERROR = -5             file size exceed limit EXCEED_TOKENS_ERROR = -6           exceed tokens limit PAGE_PACKAGE_NOT_ENOUGH_ERROR = -9 page package not enough PAGE_LIMIT_ERROR = -10             page limit error TITLE_COMPLETE_ERROR = -11         complete title failed READ_TMP_FILE_ERROR = -12          read tmp file error OCR_PAGE_LIMIT_ERROR = -13         ocr page limit error CONTENT_POLICY_ERROR = -14         content security check did not pass CONTENT_DECODE_ERROR = -15         file content decode error HTML_CONVERT_ERROR = -16           html convert error HTML_EMPTY_BODY_ERROR = -17        content is empty HTML_PARSE_ERROR = -18             html parse error HTML_DOWNLOAD_ERROR = -19          html download error from website PACKAGE_NOT_ENOUGH_ERROR = -25     package not enough ```

        :param website_req: (required)
        :type website_req: WebsiteReq
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_document_documents_website_post_serialize(
            website_req=website_req,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APIUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def upload_document_documents_website_post_without_preload_content(
        self,
        website_req: WebsiteReq,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Upload Document

        Upload a document by website  **Response**:  * `id`: document id, also called `upload_id`, you can use it to get the document by `GET /documents/{upload_id}`. It's of uuid format.  **Please note**: you should store `id` in your database, because we don't have a `GET /documents/list` API to list all documents for now.  * `status`: Once uploaded, the status is `UN_PARSED`, after a series of processing, the status would change by time, and finally to be one of the following two cases:  ``` UN_PARSED = 1              file uploaded or collection has no document # final statuses ELEMENT_PARSED = 300       analysis of the document has succeeded ERROR_STATUSES (< 0)       error occurred during analysis ```  So before the document status finalized, you can poll the status by `GET /documents/{upload_id}` at interval of 10s , generally it takes 1-2 minutes to finish depending on content length of the document. If error occurred, it doesn't consume your quota.  **Please note**:  * Uploading files consumes your pages quota, and uploading same files again will still consume quota. * We'll keep your uploaded file for one year. If you do not make another payment for the API after one year, the file will be permanently deleted.  For reference, other statuses are as follows:  ``` UN_PARSED = 1                      file uploaded or collection has no document LINK_UN_PARSED = 10                file link submitted PARSING = 12                       parsing, mainly used for collection LINK_DOWNLOADING = 15              file link downloading PDF_CONVERTING = 20                docx to pdf converting PDF_CONVERTED = 30                 docx to pdf success TEXT_PARSING = 40                  text embedding（when element parse timeout 2min） ELEMENT_PARSING = 50               element embedding INSIGHT_CALLBACK = 70              element parse success TEXT_PARSED = 210                  text embedding success ELEMENT_PARSED = 300               element embedding success TEXT_PARSE_ERROR = -1              text embedding failed ELEMENT_PARED_ERROR = -2           element embedding failed PDF_CONVERT_ERROR = -3             docx to pdf failed LINK_DOWNLOAD_ERROR = -4           file link download failed EXCEED_SIZE_ERROR = -5             file size exceed limit EXCEED_TOKENS_ERROR = -6           exceed tokens limit PAGE_PACKAGE_NOT_ENOUGH_ERROR = -9 page package not enough PAGE_LIMIT_ERROR = -10             page limit error TITLE_COMPLETE_ERROR = -11         complete title failed READ_TMP_FILE_ERROR = -12          read tmp file error OCR_PAGE_LIMIT_ERROR = -13         ocr page limit error CONTENT_POLICY_ERROR = -14         content security check did not pass CONTENT_DECODE_ERROR = -15         file content decode error HTML_CONVERT_ERROR = -16           html convert error HTML_EMPTY_BODY_ERROR = -17        content is empty HTML_PARSE_ERROR = -18             html parse error HTML_DOWNLOAD_ERROR = -19          html download error from website PACKAGE_NOT_ENOUGH_ERROR = -25     package not enough ```

        :param website_req: (required)
        :type website_req: WebsiteReq
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._upload_document_documents_website_post_serialize(
            website_req=website_req,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "APIUploadResp",
            '422': "HTTPValidationError"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _upload_document_documents_website_post_serialize(
        self,
        website_req,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if website_req is not None:
            _body_params = website_req


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'HTTPBearer'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/documents/website',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


