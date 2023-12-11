# APICloneReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**upload_ids** | **List[str]** | upload id list | 

## Example

```python
from chatdoc.models.api_clone_req import APICloneReq

# TODO update the JSON string below
json = "{}"
# create an instance of APICloneReq from a JSON string
api_clone_req_instance = APICloneReq.from_json(json)
# print the JSON string representation of the object
print
APICloneReq.to_json()

# convert the object into a dict
api_clone_req_dict = api_clone_req_instance.to_dict()
# create an instance of APICloneReq from a dict
api_clone_req_form_dict = api_clone_req.from_dict(api_clone_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


