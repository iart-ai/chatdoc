# DocumentErrorMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**error_msg** | **str** |  | [optional] 
**page_num** | **int** |  | [optional] 
**ocr_page_num** | **int** |  | [optional] 

## Example

```python
from chatdoc.models.document_error_message import DocumentErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentErrorMessage from a JSON string
document_error_message_instance = DocumentErrorMessage.from_json(json)
# print the JSON string representation of the object
print
DocumentErrorMessage.to_json()

# convert the object into a dict
document_error_message_dict = document_error_message_instance.to_dict()
# create an instance of DocumentErrorMessage from a dict
document_error_message_form_dict = document_error_message.from_dict(document_error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


