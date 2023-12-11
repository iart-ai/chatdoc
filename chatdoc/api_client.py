# coding: utf-8

"""
    ChatDOC API

    # Introduction  Welcome to ChatDOC API, Version 0.2.0!  ChatDOC is a powerful SaaS AI product that enables you to engage with documents, instantly retrieving answers along with cited sources. Our API provides developers with the tools to interact with the ChatDOC system, allowing you to create immersive experiences for your users.  This reference serves as a comprehensive guide to the ChatDOC system and its Version 0.2.0 API. Here, you'll find detailed information on the objects and endpoints used in the API. We greatly value your feedback. If you notice any missing or inaccurate information, please don't hesitate to open an issue on [GitHub](https://github.com/chatdoc-com/chatdoc-com.github.io/issues) or submit a pull request to help improve our documentation.   > To leverage ChatDOC's API capabilities, you'll need an API key. API keys can be   created by subscribing to an appropriate membership plan or purchasing an API package on   [ChatDOC.com](https://chatdoc.com/).  ## Conventions  All API requests should be directed to the domain `api.chatdoc.com`. and secure HTTPS is mandatory for all interactions.  Our ChatDOC API adheres to RESTful conventions where applicable, utilizing standard HTTP methods such as GET, POST, PUT, and DELETE. Request and response payloads are encoded in JSON format.  HTTP status codes are used in accordance with industry standards. Successful requests return a 200 OK response, while failed requests produce 4xx or 5xx error codes.  Please note that this documentation pertains to ChatDOC API Version 0.2.0, which is not backward compatible with Version 0.1.0. While Version 0.1.0 remains functional, we strongly encourage users to migrate to Version 0.2.0 for the best experience.  If you have any questions or need further assistance, please don't hesitate to reach out to our support team.  This revised introduction reflects the transition to ChatDOC API Version 0.2.0 and highlights its features and benefits.  ## JSON conventions  * Response body of success requests is generally as follows:      ```json     {       \"status\": \"ok\",       \"data\": {         \"id\": 160,         \"name\": \"Bo\",         ...       }     }     ```      * `status` and `data` are common properties.     * Object properties are contained directly in `data`, there is no extra model objects. (e.g. \"document\", \"user\", etc.) * And failed response may be:      `400 Bad Request`      ```json     {         \"detail\": \"Error message\"     }     ```      * `detail` is the error message.     * `status` is not returned.      `404 Not Found`      ```json     {         \"data\": {},         \"detail\": \"This page has expired, please refresh the page and try again.\"     }     ```      * `detail` of `404` is unified as above message, no matter which kind of resources you get.  * Property names are in snake_case (not camelCase or kebab-case). * Time is stored as [Unix timestamps](https://www.unixtimestamp.com/) in seconds, and this point in time technically does not change no matter where you are located on the globe. You can convert it to datetime of your local timezone. * Optional properties are nullable, you can just ignore it sometimes.  ## Request limits  To ensure a consistent developer experience for all API users, the ChatDOC API is rate limited.  ## Authentication  Requests use the HTTP `Authorization` header to both authenticate and authorize operations. The ChatDOC API accepts bearer tokens in this header. Bearer keys can be managed in our web site.  ```curl curl 'https://api.chatdoc.com/api/v2/documents/upload'   -H 'Authorization: Bearer \"$API_KEY\"' ```  Different keys of the same user are interoperable of each others' resource, they share common permission of the user.  **Please note**: keep your API keys confidential, and do not put them in any client code, including browser html and mobile client, API interactions should be done on the server side.  # Quick Start To use the **ChatDOC API**, you have two options: - Directly call the [ChatDOC RESTful API](#section/ChatDOC-RESTful-API) from your own service and custom the UI by yourself. - Use the `@chatdocai/chatdoc-sdk` to display documents(.pdf, .epub, .txt, .md, .html) and retrieve data by calling the ChatDOC RESTful API.    > Before using the API, you need to obtain an API Key on [ChatDOC.com](https://chatdoc.com/).  You can download [ChatDOC-API-Demo](https://github.com/chatdoc-com/ChatDOC-API-Demo) to start your application. ```sh git clone https://github.com/chatdoc-com/ChatDOC-API-Demo ```     > The  server folder is an node server, which request the ChatDOC RESTful API.     > The  client folder is a vue web app, which use `@chatdocai/chatdoc-sdk` to show the document, and request the node server.  Here are the steps to start the demo: 1. run `pnpm install` 2. Set the env variable **API_KEY**.  > **API_KEY** is the API key that you obtained after purchasing the API package or membership plan.  3. run `pnpm start`  > When using a self-signed certificate in your local development environment, you may encounter a browser prompt saying: 'This site can't provide a secure connection'. Please be aware that this is a specific situation in the local development environment and will not affect the use of your genuine SSL certificate when deployed online. For online deployment, you can use your own SSL certificate to ensure a secure connection.  By following these steps, you will have a simple ChatDOC API application.  If you only want to know how to use the `@chatdocai/chatdoc-sdk`, you can refer to the [ChatDOC Document Viewer](#section/ChatDOC-Document-Viewer) section.  Here are some typical use cases of `@chatdocai/chatdoc-sdk` in the demo that you might be interested in:  1. When you select text on the document and click the chat icon, you can obtain the [`HTMLMaterialData`](#section/ChatDOC-Document-Viewer/HTMLMaterialData) or [`PDFMaterialData`](#section/ChatDOC-Document-Viewer/PDFMaterialData) from the callback handler of [EVENT_TYPES.CHAT_ICON_CLICKED](#section/ChatDOC-Document-Viewer/EVENT_TYPES) event. Then, you can post it to the [Ask Question API](#tag/Questions/operation/Ask_Question_questions_post).  2. The response from the [Ask Question API](#tag/Questions/operation/Ask_Question_questions_post) contains the `source_info` field. You can convert the `source_info` to the data type of [Source](#section/ChatDOC-Document-Viewer/Source) and   use the [drawSources](#section/ChatDOC-Document-Viewer/Methods) method of `@chatdocai/chatdoc-sdk` to navigate to the page of the sources and highlight them.  3. By using the [setFileUrl](#section/ChatDOC-Document-Viewer/Methods) method of @chatdocai/chatdoc-sdk, you can switch the displayed document.      # ChatDOC Document Viewer If you want to view the document in the browser, you can use the `@chatdocai/chatdoc-sdk` npm package.  The `@chatdocai/chatdoc-sdk` npm package is used to display documents(.pdf, .epub, .txt, .md, .html) and interact with them by selecting text and asking questions. Here are the steps to get started:  1. **Install `@chatdocai/chatdoc-sdk`**     ```bash    pnpm install @chatdocai/chatdoc-sdk    # npm install @chatdocai/chatdoc-sdk    # yarn add @chatdocai/chatdoc-sdk    ``` 2. **Init chatdoc-sdk**      Initialize the chatdoc-sdk by importing the **initSDK** function from `@chatdocai/chatdoc-sdk` and using it to create an instance of the [DOCViewerSDK](#section/ChatDOC-Document-Viewer/DOCViewerSDK).       Please provide the DOM element or CSS selector string where you want to mount the SDK. You can find detailed parameter information in the [Config](#section/ChatDOC-Document-Viewer/Config) section.      **Usage Example:**      ```js     import { initSDK } from '@chatdocai/chatdoc-sdk';      const sdk = initSDK({       el: '#doc-viewer',     })      ``` 3. **Open document**      Use the `open` method of `@chatdocai/chatdoc-sdk` to open the document.      **Usage Example:**      ```js     // Please replace the URL with your own file URL.     sdk.open({url: 'https://example.com/pdf-file.pdf', viewerType: 'pdf'})      // If you want to view other documents (such as .epub, .html, .txt, .md), you need to set the viewerType to `html`.     sdk.open({url: 'https://example.com/document.txt', viewerType: 'html'})     ```     4. **Add event listener**      Add event listeners to handle specific events. For example, you can listen to the **CHAT_ICON_CLICKED** event to get the selected text from the document when the chat icon is clicked.      The `@chatdocai/chatdoc-sdk` package also exports the EVENT_TYPES object, which types the [event name](#section/ChatDOC-Document-Viewer/EVENT_TYPES).      **Usage Example:**     ```js     import { EVENT_TYPES } from '@chatdocai/chatdoc-sdk';      // this event is dispatched after you clicked the chat icon in document     sdk.on(EVENT_TYPES.CHAT_ICON_CLICKED, (data) => {       // if your viewType is `pdf`, the data is `PDFMaterialData`       // if your viewType is `html`, the data is `HTMLMaterialData`       console.log(data)     });      ```  ## DOCViewerSDK The DOCViewerSDK class provides a document viewer SDK with various methods and properties for interacting with the document viewer. Here are some key details about the class:   ## Config  The configuration parameters for the SDK.   **Properties:**  - **el:** `string | HTMLElement` - the DOM element or CSS selector string used for mounting and rendering the SDK.  - **fileUrl:** `string` (optional) `Deprecated` - The URL of the document. (This field is no longer recommended for use in new code. Consider using the [open](#section/ChatDOC-Document-Viewer/Methods) method instead.)  - **getToken:** `() => Promise<string>` (optional) - An optional function that returns a Promise resolving to a string representing the [JWT](https://jwt.io/) token.The token is encoded using an API key, and the payload is `{\"upload_id\": \"xxx\"}`.     ```js     import jwt from 'jsonwebtoken';     // token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cGxvYWRfaWQiOiI2YjNmYzdlOS1kYzE3LTQwYjYtODI4Ny04MDM5N2JhMWU5MmEifQ.sXUbg6tGtF6KqFtCGALTcm7eG6H23dhrKW1wUAAAyus'     const token = jwt.sign({ upload_id: '6b3fc7e9-dc17-40b6-8287-80397ba1e92a' }, 'ak-ifypHN4we-v07xhp0pDKRG-znEb-5YQeFuhXgjt4byM', { noTimestamp: true} );     ```  **Usage Example:** ```javascript  // node server import jwt from 'jsonwebtoken'; async getDocumentToken(ctx) {   const { id: uploadId } = ctx.params   const token = jwt.sign({ upload_id: uploadId }, 'API_KEY', { noTimestamp: true} );   ctx.body = {     status: 'ok',     data: {token}   } }  // client const getToken = async () => {   const { token } = await getDocumentToken('uploadId');   return token; }; const config: Config = {   el: '#pdf-viewer',   getToken };   ``` ## ViewType   This type represents the available view types for a document. It is a union type that can have one of two values: `pdf` or `html`. This type is utilized to specify the desired view type when rendering or displaying a document.  - **pdf:** Set the view type to 'pdf' when you want to view files with the .pdf extension. - **html:** Set the view type to 'html' when you want to view files with .txt, .md, .epub, or .html extensions.  ## FileOptions  The `FileOptions` type represents the options for opening a document.  **Properties:**  - **url:** `string` - The URL of the document. - **viewerType:** [`ViewType`](#section/ChatDOC-Document-Viewer/ViewType) - The desired view type for rendering the document, which can be either `pdf` or `html`.  **Usage Example:**  ```javascript const options = {   url: 'https://example.com/document.pdf',   viewerType: 'pdf', }; ```  ## Source  The Source type represents a source in the SDK, which is the parameter of the [drawSources](#section/ChatDOC-Document-Viewer/Methods) method.  **Properties:**  - **pageNumber:** `number` - The page number of the source.  - **rects:** `number[][]` -  An array of rectangles represented by four numbers `[left, top, right, bottom]` indicating their positions within the source coordinates.  **Usage Example:** ``` const source: Source = {   pageNumber: 1,   rects: [[10, 10, 50, 50], [60, 60, 100, 100]], }; ```  ## HTMLMaterialData  The `HTMLMaterialData` type contains the material content and the document selection obtained from the callback handler of the EVENT_TYPES.CHAT_ICON_CLICKED event when the [FileOptions.viewType](#section/ChatDOC-Document-Viewer/ViewType) is set to `html`.  **Properties:**  - **material:** `string` - The selected text or HTML content.  - **indexes:** `number[]` - An array of indexes representing the selected text node index in the document.  - **focusNode**: `string` - A XPath string of the selection's focusNode in the document.  - **focusOffset**: `number` - The number of characters that the selection's focus is offset within the focusNode.  - **anchorNode**: `string` - A XPath string of the selection's anchorNode in the document.  - **anchorOffset**: `number` - The number of characters that the selection's anchor is offset within anchorNode.  **Usage Example:** ``` const material: HTMLMaterialData = {   material: 'content',   indexes: [1, 2, 3],   focusNode: 'div/div[4]/text()',   focusOffset: 2,   anchorNode: 'div/div[2]/text()',   anchorOffset: 3, }; ```  ## PDFMaterialData The `PDFMaterialData` type contains the selected text and the outlines in the document obtained from the callback handler of the EVENT_TYPES.CHAT_ICON_CLICKED event when the [FileOptions.viewType](#section/ChatDOC-Document-Viewer/ViewType) is set to `pdf`.  **Properties:**  - **material:** `string` - The selected text.  - **rects:** [`Rect[]`](#section/ChatDOC-Document-Viewer/Rect) (optional) - An array of rectangles representing the outlines.  **Usage Example:** ``` const material: PDFMaterialData = {   material: 'content',   rects: [     {       pageNumber: 1,       outline: [10, 10, 50, 50],     },     {       pageNumber: 2,       outline: [60, 60, 100, 100],     },   ], }; ```  ## Rect The Rect type represents a rectangle in the document, and it is a field in the [MaterialData](#section/ChatDOC-Document-Viewer/MaterialData) type.  **Properties:**  - **pageNumber:** `number` - The page number of the rectangle.  - **outline:** `number[]` - The outline array represents the rectangle's outline coordinates as four values: `left, top, right, and bottom`.  **Usage Example:** ``` const rect: Rect = {   pageNumber: 1,   outline: [10, 10, 50, 50], }; ``` ## Methods  ### setFileUrl(fileUrl: string): any `Deprecated`  This method is used to set the file URL for opening a document.  - **fileUrl:** `string` - The URL of the file to load.  **`Deprecated Note:`**  It is recommended to use the `open` method instead for opening a document. The `setFileUrl` method is deprecated.  ### drawSources(sources: Source[]): Promise<void>  Draws source rectangles on the document viewer.  - **sources:** [`Source[]`](#section/ChatDOC-Document-Viewer/Source) - The source rectangles to draw.  ### clearSources(): void  Clears source annotations.  ### destroy(): void  Destroys the document viewer SDK instance.  ### on(name: string, handler: Func): void  Adds an event listener for the specified event.  - **name:** `string` - The name of the event, you can get the event name from [EVENT_TYPES](#section/ChatDOC-Document-Viewer/EVENT_TYPES). - **handler:** `Func` - The event handler function.  ### off(name: string, handler: Func): void  Removes an event listener for the specified event.  - **name:** `string` - The name of the event. - **handler:** `Func` - The event handler function.  ### getCurrentPageNumber(): any  Gets the current page number.  - Returns: `any` - The current page number.  ### open(options: FileOptions): any This method is used to open a document using the provided options.  - **options:** [`FileOptions`](#section/ChatDOC-Document-Viewer/FileOptions) - An object that specifies the options for opening the document.  ## EVENT_TYPES  - **PAGE_RENDERED** - After each page is rendered, this event is dispatched, and you can obtain the current page number from the callback handler.  - **CHAT_ICON_CLICKED** - After you clicked the chat icon in document, and you can obtain the [`HTMLMaterialData`](#section/ChatDOC-Document-Viewer/HTMLMaterialData) or [`PDFMaterialData`](#section/ChatDOC-Document-Viewer/PDFMaterialData) from the callback handler.   # OBJECTS  ## Document  You can first upload documents to get started. Supported document formats including pdf, docx/doc, and more formats such as markdown, epub are upcoming.  ## Collection  Collection is just a special type of `document`, they have common properties like `name`, `status` etc. The difference is that as for questioning, a document can be standalone or grouped as a `collection`, each file collection is a customized database, and you can acquire knowledge effortlessly through conversation.  ChatDOC offers three distinct page package types: Elite, Basic, and Lite. When you use one of these page packages to upload a file, the same page package type is automatically applied when you clone that file into a collection.  ## Question  Namely message or chat, there can be [4 Ways to Make Queries](https://chatdoc.notion.site/4-Ways-to-Make-Queries-3d8d6d36060b4c7eb1d69e6a32405dd7):  * **Try our Suggested Queries** * **Ask About Full Text** * **Ask About Selected Text** * **Query across multi docs**  # ChatDOC RESTful API  Consuming quota APIs:  ### Document Pages  * POST /documents/upload * POST /documents/website * POST /collections/clone-documents  ### Questions  * POST /questions * POST /questions/multi-documents 

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import atexit
import datetime
from dateutil.parser import parse
import json
import mimetypes
import os
import re
import tempfile

from urllib.parse import quote
from typing import Tuple, Optional, List

from chatdoc.configuration import Configuration
from chatdoc.api_response import ApiResponse
import chatdoc.models
from chatdoc import rest
from chatdoc.exceptions import (
    ApiValueError,
    ApiException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ServiceException
)


class ApiClient:
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int, # TODO remove as only py3 is supported?
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }
    _pool = None

    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None
    ) -> None:
        # use default configuration if none is provided
        if configuration is None:
            configuration = Configuration.get_default()
        self.configuration = configuration

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'
        self.client_side_validation = configuration.client_side_validation

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value


    _default = None

    @classmethod
    def get_default(cls):
        """Return new instance of ApiClient.

        This method returns newly created, based on default constructor,
        object of ApiClient class or returns a copy of default
        ApiClient.

        :return: The ApiClient object.
        """
        if cls._default is None:
            cls._default = ApiClient()
        return cls._default

    @classmethod
    def set_default(cls, default):
        """Set default instance of ApiClient.

        It stores default ApiClient.

        :param default: object of ApiClient.
        """
        cls._default = default

    def param_serialize(
        self,
        method,
        resource_path,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None, auth_settings=None,
        collection_formats=None,
        _host=None,
        _request_auth=None
    ) -> Tuple:

        """Builds the HTTP request params needed by the request.
        :param method: Method to call.
        :param resource_path: Path to method endpoint.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :return: tuple of form (path, http_method, query_params, header_params,
            body, post_params, files)
        """

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params,collection_formats)
            )

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(
                path_params,
                collection_formats
            )
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(
                post_params,
                collection_formats
            )
            post_params.extend(self.files_parameters(files))

        # auth setting
        self.update_params_for_auth(
            header_params,
            query_params,
            auth_settings,
            resource_path,
            method,
            body,
            request_auth=_request_auth
        )

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        if _host is None:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(
                query_params,
                collection_formats
            )
            url += "?" + url_query

        return method, url, header_params, body, post_params


    def call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ) -> rest.RESTResponse:
        """Makes the HTTP request (synchronous)
        :param method: Method to call.
        :param url: Path to method endpoint.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param _request_timeout: timeout setting for this request.
        :return: RESTResponse
        """

        try:
            # perform request and return response
            response_data = self.rest_client.request(
                method, url,
                headers=header_params,
                body=body, post_params=post_params,
                _request_timeout=_request_timeout
            )

        except ApiException as e:
            if e.body:
                e.body = e.body.decode('utf-8')
            raise e

        return response_data

    def response_deserialize(
        self,
        response_data=None,
        response_types_map=None
    ) -> ApiResponse:
        """Deserializes response into an object.
        :param response_data: RESTResponse object to be deserialized.
        :param response_types_map: dict of response types.
        :return: ApiResponse
        """


        response_type = response_types_map.get(str(response_data.status), None)
        if not response_type and isinstance(response_data.status, int) and 100 <= response_data.status <= 599:
            # if not found, look for '1XX', '2XX', etc.
            response_type = response_types_map.get(str(response_data.status)[0] + "XX", None)

        if not 200 <= response_data.status <= 299:
            if response_data.status == 400:
                raise BadRequestException(http_resp=response_data)

            if response_data.status == 401:
                raise UnauthorizedException(http_resp=response_data)

            if response_data.status == 403:
                raise ForbiddenException(http_resp=response_data)

            if response_data.status == 404:
                raise NotFoundException(http_resp=response_data)

            if 500 <= response_data.status <= 599:
                raise ServiceException(http_resp=response_data)
            raise ApiException(http_resp=response_data)

        # deserialize response data

        if response_type == "bytearray":
            return_data = response_data.data
        elif response_type is None:
            return_data = None
        elif response_type == "file":
            return_data = self.__deserialize_file(response_data)
        else:
            match = None
            content_type = response_data.getheader('content-type')
            if content_type is not None:
                match = re.search(r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
            encoding = match.group(1) if match else "utf-8"
            response_text = response_data.data.decode(encoding)
            return_data = self.deserialize(response_text, response_type)

        return ApiResponse(
            status_code = response_data.status,
            data = return_data,
            headers = response_data.getheaders(),
            raw_data = response_data.data
        )

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            ]
        elif isinstance(obj, tuple):
            return tuple(
                self.sanitize_for_serialization(sub_obj) for sub_obj in obj
            )
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        elif isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `openapi_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = obj.to_dict()

        return {
            key: self.sanitize_for_serialization(val)
            for key, val in obj_dict.items()
        }

    def deserialize(self, response_text, response_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """

        # fetch data from response object
        try:
            data = json.loads(response_text)
            if 'data' in data:
                data = data['data']
        except ValueError:
            data = response_text

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith('List['):
                sub_kls = re.match(r'List\[(.*)]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('Dict['):
                sub_kls = re.match(r'Dict\[([^,]*), (.*)]', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in data.items()}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(chatdoc.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datetime(data)
        else:
            return self.__deserialize_model(data, klass)

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def parameters_to_url_query(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: URL query string (e.g. a=Hello%20World&b=123)
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, dict):
                v = json.dumps(v)

            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v))
                    )
            else:
                new_params.append((k, quote(str(v))))

        return "&".join(["=".join(item) for item in new_params])

    def files_parameters(self, files=None):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if files:
            for k, v in files.items():
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (
                            mimetypes.guess_type(filename)[0]
                            or 'application/octet-stream'
                        )
                        params.append(
                            tuple([k, tuple([filename, filedata, mimetype])])
                        )

        return params

    def select_header_accept(self, accepts: List[str]) -> Optional[str]:
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        for accept in accepts:
            if re.search('json', accept, re.IGNORECASE):
                return accept

        return accepts[0]

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        for content_type in content_types:
            if re.search('json', content_type, re.IGNORECASE):
                return content_type

        return content_types[0]

    def update_params_for_auth(
        self,
        headers,
        queries,
        auth_settings,
        resource_path,
        method,
        body,
        request_auth=None
    ) -> None:
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param request_auth: if set, the provided settings will
                             override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auth:
            self._apply_auth_params(
                headers,
                queries,
                resource_path,
                method,
                body,
                request_auth
            )
        else:
            for auth in auth_settings:
                auth_setting = self.configuration.auth_settings().get(auth)
                if auth_setting:
                    self._apply_auth_params(
                        headers,
                        queries,
                        resource_path,
                        method,
                        body,
                        auth_setting
                    )

    def _apply_auth_params(
        self,
        headers,
        queries,
        resource_path,
        method,
        body,
        auth_setting
    ) -> None:
        """Updates the request parameters based on a single auth_setting

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param auth_setting: auth settings for the endpoint
        """
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        handle file downloading
        save response body into a tmp file and return the instance

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(
                r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                content_disposition
            ).group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "wb") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        return klass.from_dict(data)
