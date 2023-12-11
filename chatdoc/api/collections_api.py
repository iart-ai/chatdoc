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

from typing import Any

from chatdoc.models.api_clone_req import APICloneReq
from chatdoc.models.api_upload_resp import APIUploadResp
from chatdoc.models.collection_req import CollectionReq

from chatdoc.api_client import ApiClient
from chatdoc.api_response import ApiResponse
from chatdoc.rest import RESTResponseType


class CollectionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def clone_document_to_collection_collections_clone_documents_post(
        self,
        api_clone_req: APICloneReq,
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
        """Clone Document To Collection

        Only parsed normal document (status=300) can be cloned to collection, max document count of collection is 30.  Cloned documents also consume your document page quota.

        :param api_clone_req: (required)
        :type api_clone_req: APICloneReq
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

        _param = self._clone_document_to_collection_collections_clone_documents_post_serialize(
            api_clone_req=api_clone_req,
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
    def clone_document_to_collection_collections_clone_documents_post_with_http_info(
        self,
        api_clone_req: APICloneReq,
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
        """Clone Document To Collection

        Only parsed normal document (status=300) can be cloned to collection, max document count of collection is 30.  Cloned documents also consume your document page quota.

        :param api_clone_req: (required)
        :type api_clone_req: APICloneReq
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

        _param = self._clone_document_to_collection_collections_clone_documents_post_serialize(
            api_clone_req=api_clone_req,
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
    def clone_document_to_collection_collections_clone_documents_post_without_preload_content(
        self,
        api_clone_req: APICloneReq,
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
        """Clone Document To Collection

        Only parsed normal document (status=300) can be cloned to collection, max document count of collection is 30.  Cloned documents also consume your document page quota.

        :param api_clone_req: (required)
        :type api_clone_req: APICloneReq
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

        _param = self._clone_document_to_collection_collections_clone_documents_post_serialize(
            api_clone_req=api_clone_req,
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


    def _clone_document_to_collection_collections_clone_documents_post_serialize(
        self,
        api_clone_req,
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
        if api_clone_req is not None:
            _body_params = api_clone_req


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
            resource_path='/collections/clone-documents',
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
    def create_collection_collections_post(
        self,
        collection_req: CollectionReq,
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
        """Create Collection

        Create an empty collection  **Response**:  Similar with `POST /documents/upload`, response `id` also called `upload_id`, which can be used for document related APIs:  * `GET /documents/{upload_id}` * `DELETE /documents/{upload_id}` * `POST /questions?upload_id={upload_id}`  Upon created you can add sub documents to the collection by:  * `POST /documents/upload` * `POST /collections/clone-documents`.

        :param collection_req: (required)
        :type collection_req: CollectionReq
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

        _param = self._create_collection_collections_post_serialize(
            collection_req=collection_req,
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
    def create_collection_collections_post_with_http_info(
        self,
        collection_req: CollectionReq,
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
        """Create Collection

        Create an empty collection  **Response**:  Similar with `POST /documents/upload`, response `id` also called `upload_id`, which can be used for document related APIs:  * `GET /documents/{upload_id}` * `DELETE /documents/{upload_id}` * `POST /questions?upload_id={upload_id}`  Upon created you can add sub documents to the collection by:  * `POST /documents/upload` * `POST /collections/clone-documents`.

        :param collection_req: (required)
        :type collection_req: CollectionReq
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

        _param = self._create_collection_collections_post_serialize(
            collection_req=collection_req,
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
    def create_collection_collections_post_without_preload_content(
        self,
        collection_req: CollectionReq,
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
        """Create Collection

        Create an empty collection  **Response**:  Similar with `POST /documents/upload`, response `id` also called `upload_id`, which can be used for document related APIs:  * `GET /documents/{upload_id}` * `DELETE /documents/{upload_id}` * `POST /questions?upload_id={upload_id}`  Upon created you can add sub documents to the collection by:  * `POST /documents/upload` * `POST /collections/clone-documents`.

        :param collection_req: (required)
        :type collection_req: CollectionReq
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

        _param = self._create_collection_collections_post_serialize(
            collection_req=collection_req,
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


    def _create_collection_collections_post_serialize(
        self,
        collection_req,
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
        if collection_req is not None:
            _body_params = collection_req


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
            resource_path='/collections',
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


