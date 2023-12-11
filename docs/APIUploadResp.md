# APIUploadResp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**DocumentStatus**](DocumentStatus.md) |  | 
**name** | **str** |  | 
**created_at** | **int** |  | 
**type** | [**UploadType**](UploadType.md) |  | 

## Example

```python
from chatdoc.models.api_upload_resp import APIUploadResp

# TODO update the JSON string below
json = "{}"
# create an instance of APIUploadResp from a JSON string
api_upload_resp_instance = APIUploadResp.from_json(json)
# print the JSON string representation of the object
print
APIUploadResp.to_json()

# convert the object into a dict
api_upload_resp_dict = api_upload_resp_instance.to_dict()
# create an instance of APIUploadResp from a dict
api_upload_resp_form_dict = api_upload_resp.from_dict(api_upload_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


