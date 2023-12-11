# APICollectionOrUploadResp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**DocumentStatus**](DocumentStatus.md) |  | 
**name** | **str** |  | 
**created_at** | **int** |  | 
**type** | [**UploadType**](UploadType.md) |  | 
**documents** | [**List[APIUploadResp]**](APIUploadResp.md) |  | [optional] 
**error_msg** | [**DocumentErrorMessage**](DocumentErrorMessage.md) |  | [optional] 
**ocr_type** | [**UploadOcrType**](UploadOcrType.md) |  | [optional] 

## Example

```python
from chatdoc.models.api_collection_or_upload_resp import APICollectionOrUploadResp

# TODO update the JSON string below
json = "{}"
# create an instance of APICollectionOrUploadResp from a JSON string
api_collection_or_upload_resp_instance = APICollectionOrUploadResp.from_json(json)
# print the JSON string representation of the object
print
APICollectionOrUploadResp.to_json()

# convert the object into a dict
api_collection_or_upload_resp_dict = api_collection_or_upload_resp_instance.to_dict()
# create an instance of APICollectionOrUploadResp from a dict
api_collection_or_upload_resp_form_dict = api_collection_or_upload_resp.from_dict(api_collection_or_upload_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


