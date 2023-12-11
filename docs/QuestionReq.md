# QuestionReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | document id or collection id, created by &#x60;POST /documents/upload&#x60; or &#x60;POST /collections&#x60; APIs accordingly. | 
**question** | **str** | question to ask | 
**stream** | **bool** | If set, partial message deltas will be sent, like in ChatGPT of [OpenAI](https://platform.openai.com/docs/api-reference/chat/create#stream). Tokens will be sent as data-only server-sent events as they become available. | [optional] [default to True]
**selected_meta** | [**SelectedMeta**](SelectedMeta.md) |  | [optional] 
**history** | [**List[ChatMessage]**](ChatMessage.md) | chat history, used for [Threaded Chat](https://chatdoc.notion.site/2-Ways-to-Dive-Deeper-1f2e3a8705e744a6872da0d39254f182), this parameter simulates [OpenAI&#39; API](https://platform.openai.com/docs/guides/gpt/chat-completions-api). &#x60;history&#x60; is question and answer pairs, which is a list of &#x60;ChatMessage&#x60; objects. The max input tokens of &#x60;history&#x60;, &#x60;selected_meta.material&#x60; and &#x60;question&#x60; is 8000, which is a little less than OpenAI&#39;s limit of [Embedding models](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings). Sample parameter is as follows:          [           {\&quot;role\&quot;: \&quot;user\&quot;, \&quot;content\&quot;: \&quot;Who...\&quot;},           {\&quot;role\&quot;: \&quot;assistant\&quot;, \&quot;content\&quot;: \&quot;The...\&quot;},           {\&quot;role\&quot;: \&quot;user\&quot;, \&quot;content\&quot;: \&quot;Where...\&quot;}           {\&quot;role\&quot;: \&quot;assistant\&quot;, \&quot;content\&quot;: \&quot;The...\&quot;},         ]          | [optional] [default to []]
**search_entire_doc** | **bool** | if true: limit responses to current file&#39;s information, else: responses go freely with knowledge of our AI | [optional] [default to True]
**detailed_citation** | **bool** | Whether to show the source at the end of each sentence or not. Requires enabling the &#x60;search_entire_doc&#x60; setting. | [optional] [default to False]
**language** | **str** | preferred language of answer to the question, if not provided, we will try to detect the language automatically, which is flexible and also works well. You&#39;d better use [ISO language name](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes?useskin&#x3D;vector), such as English, Chinese. But we can&#39;t promise, when AI can&#39;t answer your question well, it generally answers in English. | [optional] 
**model_type** | [**APIAIModelEnum**](APIAIModelEnum.md) |  | [optional] 

## Example

```python
from chatdoc.models.question_req import QuestionReq

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionReq from a JSON string
question_req_instance = QuestionReq.from_json(json)
# print the JSON string representation of the object
print
QuestionReq.to_json()

# convert the object into a dict
question_req_dict = question_req_instance.to_dict()
# create an instance of QuestionReq from a dict
question_req_form_dict = question_req.from_dict(question_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


