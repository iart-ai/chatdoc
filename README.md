# ChatDOC API Usage

This document provides a brief overview of how to interact with the ChatDOC API using Python.

## Prerequisites

- Python 3.7+
- `chatdoc` Python package

## Installation

You can install the `chatdoc` package using pip:

```bash
pip install --upgrade git+https://github.com/iart-ai/chatdoc.git#egg=chatdoc
```

## Usage

First, import the necessary modules from the `chatdoc` package:

```python
from chatdoc.api import DocumentsApi, QuestionsApi, CollectionsApi
from chatdoc.models import WebsiteReq, QuestionReq, CollectionReq
import requests
```

### Uploading a Document

To upload a document, you can use the `upload_document_documents_upload_post` method from the `DocumentsApi` class. Here is an example of how to upload a PDF file:

```python
documents_api = DocumentsApi()
with open('test.pdf','wb') as f:
    f.write(requests.get('https://arxiv.org/pdf/2312.00752.pdf').content)
upload_response = documents_api.upload_document_documents_upload_post(file='test.pdf')
```

### Uploading a Website

To upload a website, you can use the `upload_document_documents_website_post` method from the `DocumentsApi` class. Here is an example of how to upload a website:

```python
website_request = WebsiteReq(website = 'https://api-reference.chatdoc.com/')
website_response = documents_api.upload_document_documents_website_post(website_request)
```

### Getting Document Information

To get information about a document, you can use the `get_document_documents_upload_id_get` method from the `DocumentsApi` class. Here is an example of how to get document information:

```python
documents_api.get_document_documents_upload_id_get(website_response.id)
```

### Asking a Question

To ask a question, you can use the `ask_question_questions_post` method from the `QuestionsApi` class. Here is an example of how to ask a question:

```python
question_request = QuestionReq(upload_id=upload_response.id, question='summary',stream=False)
question_response = questions_api.ask_question_questions_post(question_request)
questions_api.get_question_questions_question_id_get(question_response['id'])
```

### Downloading a Document

To download a document, you can use the `download_document_documents_upload_id_download_get` method from the `DocumentsApi` class. Here is an example of how to download a document:

```python
data = documents_api.download_document_documents_upload_id_download_get(website_response.id)
```

### Creating a Collection

To create a collection, you can use the `create_collection_collections_post` method from the `CollectionsApi` class. Here is an example of how to create a collection:

```python
collection_request = CollectionReq(name='test')
collection_response = collections_api.create_collection_collections_post(collection_request)
documents_api.get_document_documents_upload_id_get(collection_response.id)
```

Please note that you need to replace `'test.pdf'`, `'https://arxiv.org/pdf/2312.00752.pdf'`, `'https://api-reference.chatdoc.com/'`, and `'summary'` with your own file path, file URL, website URL, and question respectively.