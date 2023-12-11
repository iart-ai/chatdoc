# coding: utf-8

"""
    ChatDOC API

    # Introduction  Welcome to ChatDOC API, Version 0.2.0!  ChatDOC is a powerful SaaS AI product that enables you to engage with documents, instantly retrieving answers along with cited sources. Our API provides developers with the tools to interact with the ChatDOC system, allowing you to create immersive experiences for your users.  This reference serves as a comprehensive guide to the ChatDOC system and its Version 0.2.0 API. Here, you'll find detailed information on the objects and endpoints used in the API. We greatly value your feedback. If you notice any missing or inaccurate information, please don't hesitate to open an issue on [GitHub](https://github.com/chatdoc-com/chatdoc-com.github.io/issues) or submit a pull request to help improve our documentation.   > To leverage ChatDOC's API capabilities, you'll need an API key. API keys can be   created by subscribing to an appropriate membership plan or purchasing an API package on   [ChatDOC.com](https://chatdoc.com/).  ## Conventions  All API requests should be directed to the domain `api.chatdoc.com`. and secure HTTPS is mandatory for all interactions.  Our ChatDOC API adheres to RESTful conventions where applicable, utilizing standard HTTP methods such as GET, POST, PUT, and DELETE. Request and response payloads are encoded in JSON format.  HTTP status codes are used in accordance with industry standards. Successful requests return a 200 OK response, while failed requests produce 4xx or 5xx error codes.  Please note that this documentation pertains to ChatDOC API Version 0.2.0, which is not backward compatible with Version 0.1.0. While Version 0.1.0 remains functional, we strongly encourage users to migrate to Version 0.2.0 for the best experience.  If you have any questions or need further assistance, please don't hesitate to reach out to our support team.  This revised introduction reflects the transition to ChatDOC API Version 0.2.0 and highlights its features and benefits.  ## JSON conventions  * Response body of success requests is generally as follows:      ```json     {       \"status\": \"ok\",       \"data\": {         \"id\": 160,         \"name\": \"Bo\",         ...       }     }     ```      * `status` and `data` are common properties.     * Object properties are contained directly in `data`, there is no extra model objects. (e.g. \"document\", \"user\", etc.) * And failed response may be:      `400 Bad Request`      ```json     {         \"detail\": \"Error message\"     }     ```      * `detail` is the error message.     * `status` is not returned.      `404 Not Found`      ```json     {         \"data\": {},         \"detail\": \"This page has expired, please refresh the page and try again.\"     }     ```      * `detail` of `404` is unified as above message, no matter which kind of resources you get.  * Property names are in snake_case (not camelCase or kebab-case). * Time is stored as [Unix timestamps](https://www.unixtimestamp.com/) in seconds, and this point in time technically does not change no matter where you are located on the globe. You can convert it to datetime of your local timezone. * Optional properties are nullable, you can just ignore it sometimes.  ## Request limits  To ensure a consistent developer experience for all API users, the ChatDOC API is rate limited.  ## Authentication  Requests use the HTTP `Authorization` header to both authenticate and authorize operations. The ChatDOC API accepts bearer tokens in this header. Bearer keys can be managed in our web site.  ```curl curl 'https://api.chatdoc.com/api/v2/documents/upload'   -H 'Authorization: Bearer \"$API_KEY\"' ```  Different keys of the same user are interoperable of each others' resource, they share common permission of the user.  **Please note**: keep your API keys confidential, and do not put them in any client code, including browser html and mobile client, API interactions should be done on the server side.  # Quick Start To use the **ChatDOC API**, you have two options: - Directly call the [ChatDOC RESTful API](#section/ChatDOC-RESTful-API) from your own service and custom the UI by yourself. - Use the `@chatdocai/chatdoc-sdk` to display documents(.pdf, .epub, .txt, .md, .html) and retrieve data by calling the ChatDOC RESTful API.    > Before using the API, you need to obtain an API Key on [ChatDOC.com](https://chatdoc.com/).  You can download [ChatDOC-API-Demo](https://github.com/chatdoc-com/ChatDOC-API-Demo) to start your application. ```sh git clone https://github.com/chatdoc-com/ChatDOC-API-Demo ```     > The  server folder is an node server, which request the ChatDOC RESTful API.     > The  client folder is a vue web app, which use `@chatdocai/chatdoc-sdk` to show the document, and request the node server.  Here are the steps to start the demo: 1. run `pnpm install` 2. Set the env variable **API_KEY**.  > **API_KEY** is the API key that you obtained after purchasing the API package or membership plan.  3. run `pnpm start`  > When using a self-signed certificate in your local development environment, you may encounter a browser prompt saying: 'This site can't provide a secure connection'. Please be aware that this is a specific situation in the local development environment and will not affect the use of your genuine SSL certificate when deployed online. For online deployment, you can use your own SSL certificate to ensure a secure connection.  By following these steps, you will have a simple ChatDOC API application.  If you only want to know how to use the `@chatdocai/chatdoc-sdk`, you can refer to the [ChatDOC Document Viewer](#section/ChatDOC-Document-Viewer) section.  Here are some typical use cases of `@chatdocai/chatdoc-sdk` in the demo that you might be interested in:  1. When you select text on the document and click the chat icon, you can obtain the [`HTMLMaterialData`](#section/ChatDOC-Document-Viewer/HTMLMaterialData) or [`PDFMaterialData`](#section/ChatDOC-Document-Viewer/PDFMaterialData) from the callback handler of [EVENT_TYPES.CHAT_ICON_CLICKED](#section/ChatDOC-Document-Viewer/EVENT_TYPES) event. Then, you can post it to the [Ask Question API](#tag/Questions/operation/Ask_Question_questions_post).  2. The response from the [Ask Question API](#tag/Questions/operation/Ask_Question_questions_post) contains the `source_info` field. You can convert the `source_info` to the data type of [Source](#section/ChatDOC-Document-Viewer/Source) and   use the [drawSources](#section/ChatDOC-Document-Viewer/Methods) method of `@chatdocai/chatdoc-sdk` to navigate to the page of the sources and highlight them.  3. By using the [setFileUrl](#section/ChatDOC-Document-Viewer/Methods) method of @chatdocai/chatdoc-sdk, you can switch the displayed document.      # ChatDOC Document Viewer If you want to view the document in the browser, you can use the `@chatdocai/chatdoc-sdk` npm package.  The `@chatdocai/chatdoc-sdk` npm package is used to display documents(.pdf, .epub, .txt, .md, .html) and interact with them by selecting text and asking questions. Here are the steps to get started:  1. **Install `@chatdocai/chatdoc-sdk`**     ```bash    pnpm install @chatdocai/chatdoc-sdk    # npm install @chatdocai/chatdoc-sdk    # yarn add @chatdocai/chatdoc-sdk    ``` 2. **Init chatdoc-sdk**      Initialize the chatdoc-sdk by importing the **initSDK** function from `@chatdocai/chatdoc-sdk` and using it to create an instance of the [DOCViewerSDK](#section/ChatDOC-Document-Viewer/DOCViewerSDK).       Please provide the DOM element or CSS selector string where you want to mount the SDK. You can find detailed parameter information in the [Config](#section/ChatDOC-Document-Viewer/Config) section.      **Usage Example:**      ```js     import { initSDK } from '@chatdocai/chatdoc-sdk';      const sdk = initSDK({       el: '#doc-viewer',     })      ``` 3. **Open document**      Use the `open` method of `@chatdocai/chatdoc-sdk` to open the document.      **Usage Example:**      ```js     // Please replace the URL with your own file URL.     sdk.open({url: 'https://example.com/pdf-file.pdf', viewerType: 'pdf'})      // If you want to view other documents (such as .epub, .html, .txt, .md), you need to set the viewerType to `html`.     sdk.open({url: 'https://example.com/document.txt', viewerType: 'html'})     ```     4. **Add event listener**      Add event listeners to handle specific events. For example, you can listen to the **CHAT_ICON_CLICKED** event to get the selected text from the document when the chat icon is clicked.      The `@chatdocai/chatdoc-sdk` package also exports the EVENT_TYPES object, which types the [event name](#section/ChatDOC-Document-Viewer/EVENT_TYPES).      **Usage Example:**     ```js     import { EVENT_TYPES } from '@chatdocai/chatdoc-sdk';      // this event is dispatched after you clicked the chat icon in document     sdk.on(EVENT_TYPES.CHAT_ICON_CLICKED, (data) => {       // if your viewType is `pdf`, the data is `PDFMaterialData`       // if your viewType is `html`, the data is `HTMLMaterialData`       console.log(data)     });      ```  ## DOCViewerSDK The DOCViewerSDK class provides a document viewer SDK with various methods and properties for interacting with the document viewer. Here are some key details about the class:   ## Config  The configuration parameters for the SDK.   **Properties:**  - **el:** `string | HTMLElement` - the DOM element or CSS selector string used for mounting and rendering the SDK.  - **fileUrl:** `string` (optional) `Deprecated` - The URL of the document. (This field is no longer recommended for use in new code. Consider using the [open](#section/ChatDOC-Document-Viewer/Methods) method instead.)  - **getToken:** `() => Promise<string>` (optional) - An optional function that returns a Promise resolving to a string representing the [JWT](https://jwt.io/) token.The token is encoded using an API key, and the payload is `{\"upload_id\": \"xxx\"}`.     ```js     import jwt from 'jsonwebtoken';     // token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cGxvYWRfaWQiOiI2YjNmYzdlOS1kYzE3LTQwYjYtODI4Ny04MDM5N2JhMWU5MmEifQ.sXUbg6tGtF6KqFtCGALTcm7eG6H23dhrKW1wUAAAyus'     const token = jwt.sign({ upload_id: '6b3fc7e9-dc17-40b6-8287-80397ba1e92a' }, 'ak-ifypHN4we-v07xhp0pDKRG-znEb-5YQeFuhXgjt4byM', { noTimestamp: true} );     ```  **Usage Example:** ```javascript  // node server import jwt from 'jsonwebtoken'; async getDocumentToken(ctx) {   const { id: uploadId } = ctx.params   const token = jwt.sign({ upload_id: uploadId }, 'API_KEY', { noTimestamp: true} );   ctx.body = {     status: 'ok',     data: {token}   } }  // client const getToken = async () => {   const { token } = await getDocumentToken('uploadId');   return token; }; const config: Config = {   el: '#pdf-viewer',   getToken };   ``` ## ViewType   This type represents the available view types for a document. It is a union type that can have one of two values: `pdf` or `html`. This type is utilized to specify the desired view type when rendering or displaying a document.  - **pdf:** Set the view type to 'pdf' when you want to view files with the .pdf extension. - **html:** Set the view type to 'html' when you want to view files with .txt, .md, .epub, or .html extensions.  ## FileOptions  The `FileOptions` type represents the options for opening a document.  **Properties:**  - **url:** `string` - The URL of the document. - **viewerType:** [`ViewType`](#section/ChatDOC-Document-Viewer/ViewType) - The desired view type for rendering the document, which can be either `pdf` or `html`.  **Usage Example:**  ```javascript const options = {   url: 'https://example.com/document.pdf',   viewerType: 'pdf', }; ```  ## Source  The Source type represents a source in the SDK, which is the parameter of the [drawSources](#section/ChatDOC-Document-Viewer/Methods) method.  **Properties:**  - **pageNumber:** `number` - The page number of the source.  - **rects:** `number[][]` -  An array of rectangles represented by four numbers `[left, top, right, bottom]` indicating their positions within the source coordinates.  **Usage Example:** ``` const source: Source = {   pageNumber: 1,   rects: [[10, 10, 50, 50], [60, 60, 100, 100]], }; ```  ## HTMLMaterialData  The `HTMLMaterialData` type contains the material content and the document selection obtained from the callback handler of the EVENT_TYPES.CHAT_ICON_CLICKED event when the [FileOptions.viewType](#section/ChatDOC-Document-Viewer/ViewType) is set to `html`.  **Properties:**  - **material:** `string` - The selected text or HTML content.  - **indexes:** `number[]` - An array of indexes representing the selected text node index in the document.  - **focusNode**: `string` - A XPath string of the selection's focusNode in the document.  - **focusOffset**: `number` - The number of characters that the selection's focus is offset within the focusNode.  - **anchorNode**: `string` - A XPath string of the selection's anchorNode in the document.  - **anchorOffset**: `number` - The number of characters that the selection's anchor is offset within anchorNode.  **Usage Example:** ``` const material: HTMLMaterialData = {   material: 'content',   indexes: [1, 2, 3],   focusNode: 'div/div[4]/text()',   focusOffset: 2,   anchorNode: 'div/div[2]/text()',   anchorOffset: 3, }; ```  ## PDFMaterialData The `PDFMaterialData` type contains the selected text and the outlines in the document obtained from the callback handler of the EVENT_TYPES.CHAT_ICON_CLICKED event when the [FileOptions.viewType](#section/ChatDOC-Document-Viewer/ViewType) is set to `pdf`.  **Properties:**  - **material:** `string` - The selected text.  - **rects:** [`Rect[]`](#section/ChatDOC-Document-Viewer/Rect) (optional) - An array of rectangles representing the outlines.  **Usage Example:** ``` const material: PDFMaterialData = {   material: 'content',   rects: [     {       pageNumber: 1,       outline: [10, 10, 50, 50],     },     {       pageNumber: 2,       outline: [60, 60, 100, 100],     },   ], }; ```  ## Rect The Rect type represents a rectangle in the document, and it is a field in the [MaterialData](#section/ChatDOC-Document-Viewer/MaterialData) type.  **Properties:**  - **pageNumber:** `number` - The page number of the rectangle.  - **outline:** `number[]` - The outline array represents the rectangle's outline coordinates as four values: `left, top, right, and bottom`.  **Usage Example:** ``` const rect: Rect = {   pageNumber: 1,   outline: [10, 10, 50, 50], }; ``` ## Methods  ### setFileUrl(fileUrl: string): any `Deprecated`  This method is used to set the file URL for opening a document.  - **fileUrl:** `string` - The URL of the file to load.  **`Deprecated Note:`**  It is recommended to use the `open` method instead for opening a document. The `setFileUrl` method is deprecated.  ### drawSources(sources: Source[]): Promise<void>  Draws source rectangles on the document viewer.  - **sources:** [`Source[]`](#section/ChatDOC-Document-Viewer/Source) - The source rectangles to draw.  ### clearSources(): void  Clears source annotations.  ### destroy(): void  Destroys the document viewer SDK instance.  ### on(name: string, handler: Func): void  Adds an event listener for the specified event.  - **name:** `string` - The name of the event, you can get the event name from [EVENT_TYPES](#section/ChatDOC-Document-Viewer/EVENT_TYPES). - **handler:** `Func` - The event handler function.  ### off(name: string, handler: Func): void  Removes an event listener for the specified event.  - **name:** `string` - The name of the event. - **handler:** `Func` - The event handler function.  ### getCurrentPageNumber(): any  Gets the current page number.  - Returns: `any` - The current page number.  ### open(options: FileOptions): any This method is used to open a document using the provided options.  - **options:** [`FileOptions`](#section/ChatDOC-Document-Viewer/FileOptions) - An object that specifies the options for opening the document.  ## EVENT_TYPES  - **PAGE_RENDERED** - After each page is rendered, this event is dispatched, and you can obtain the current page number from the callback handler.  - **CHAT_ICON_CLICKED** - After you clicked the chat icon in document, and you can obtain the [`HTMLMaterialData`](#section/ChatDOC-Document-Viewer/HTMLMaterialData) or [`PDFMaterialData`](#section/ChatDOC-Document-Viewer/PDFMaterialData) from the callback handler.   # OBJECTS  ## Document  You can first upload documents to get started. Supported document formats including pdf, docx/doc, and more formats such as markdown, epub are upcoming.  ## Collection  Collection is just a special type of `document`, they have common properties like `name`, `status` etc. The difference is that as for questioning, a document can be standalone or grouped as a `collection`, each file collection is a customized database, and you can acquire knowledge effortlessly through conversation.  ChatDOC offers three distinct page package types: Elite, Basic, and Lite. When you use one of these page packages to upload a file, the same page package type is automatically applied when you clone that file into a collection.  ## Question  Namely message or chat, there can be [4 Ways to Make Queries](https://chatdoc.notion.site/4-Ways-to-Make-Queries-3d8d6d36060b4c7eb1d69e6a32405dd7):  * **Try our Suggested Queries** * **Ask About Full Text** * **Ask About Selected Text** * **Query across multi docs**  # ChatDOC RESTful API  Consuming quota APIs:  ### Document Pages  * POST /documents/upload * POST /documents/website * POST /collections/clone-documents  ### Questions  * POST /questions * POST /questions/multi-documents 

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import copy
import logging
import os
import sys
import urllib3

import http.client as httplib

JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems'
}

class Configuration:
    """This class contains various settings of the API client.

    :param host: Base url.
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer).
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param access_token: Access token.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.

    :Example:
    """

    _default = None

    def __init__(self, host=None,
                 api_key=None, api_key_prefix=None,
                 username=None, password=None,
                 access_token=None,
                 server_index=None, server_variables=None,
                 server_operation_index=None, server_operation_variables=None,
                 ssl_ca_cert=None,
                 ) -> None:
        """Constructor
        """
        self._base_path = "https://api.chatdoc.com/api/v2" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.access_token = access_token if access_token else os.environ['CHATDOC_API_KEY']
        """Access token
        """
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("chatdoc")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """


        self.proxy = os.environ.get('HTTPS_PROXY')
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = default

    @classmethod
    def get_default_copy(cls):
        """Deprecated. Please use `get_default` instead.

        Deprecated. Please use `get_default` instead.

        :return: The configuration object.
        """
        return cls.get_default()

    @classmethod
    def get_default(cls):
        """Return the default configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.

        :return: The configuration object.
        """
        if cls._default is None:
            cls._default = Configuration()
        return cls._default

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, alias=None):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if self.access_token is not None:
            auth['HTTPBearer'] = {
                'type': 'bearer',
                'in': 'header',
                'key': 'Authorization',
                'value': 'Bearer ' + self.access_token
            }
        return auth

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 0.2.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://api.chatdoc.com/api/v2",
                'description': "No description provided",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self):
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value):
        """Fix base path."""
        self._base_path = value
        self.server_index = None
