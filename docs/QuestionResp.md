# QuestionResp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | 
**answer** | **str** |  | 
**created_at** | **int** |  | 
**type** | [**InteractionType**](InteractionType.md) |  | 
**source_info** | **List[object]** |  | 
**search_entire_doc** | **bool** |  | 
**detailed_citation** | **bool** |  | 
**id** | **int** |  | 
**model_type** | [**APIAIModelEnum**](APIAIModelEnum.md) |  | 

## Example

```python
from chatdoc.models.question_resp import QuestionResp

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionResp from a JSON string
question_resp_instance = QuestionResp.from_json(json)
# print the JSON string representation of the object
print
QuestionResp.to_json()

# convert the object into a dict
question_resp_dict = question_resp_instance.to_dict()
# create an instance of QuestionResp from a dict
question_resp_form_dict = question_resp.from_dict(question_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


