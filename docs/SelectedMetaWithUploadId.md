# SelectedMetaWithUploadId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**material** | **str** |  | 
**upload_id** | **str** |  | 
**rects** | [**List[PDFViewerRect]**](PDFViewerRect.md) |  | 

## Example

```python
from chatdoc.models.selected_meta_with_upload_id import SelectedMetaWithUploadId

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedMetaWithUploadId from a JSON string
selected_meta_with_upload_id_instance = SelectedMetaWithUploadId.from_json(json)
# print the JSON string representation of the object
print
SelectedMetaWithUploadId.to_json()

# convert the object into a dict
selected_meta_with_upload_id_dict = selected_meta_with_upload_id_instance.to_dict()
# create an instance of SelectedMetaWithUploadId from a dict
selected_meta_with_upload_id_form_dict = selected_meta_with_upload_id.from_dict(selected_meta_with_upload_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


