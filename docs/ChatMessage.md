# ChatMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**ChatRoleEnum**](ChatRoleEnum.md) |  | 
**content** | **str** |  | 

## Example

```python
from chatdoc.models.chat_message import ChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessage from a JSON string
chat_message_instance = ChatMessage.from_json(json)
# print the JSON string representation of the object
print
ChatMessage.to_json()

# convert the object into a dict
chat_message_dict = chat_message_instance.to_dict()
# create an instance of ChatMessage from a dict
chat_message_form_dict = chat_message.from_dict(chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


