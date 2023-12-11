# APIPackageInfoResp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PackageDataResp**](PackageDataResp.md) |  | [optional] 
**question** | [**PackageDataResp**](PackageDataResp.md) |  | [optional] 
**lite_page** | [**PackageDataResp**](PackageDataResp.md) |  | [optional] 
**basic_page** | [**PackageDataResp**](PackageDataResp.md) |  | [optional] 
**elite_page** | [**PackageDataResp**](PackageDataResp.md) |  | [optional] 
**documents_tokens** | [**PackageDataResp**](PackageDataResp.md) |  | [optional] 
**gpt4_question** | [**PackageDataResp**](PackageDataResp.md) |  | [optional] 
**ocr_page** | [**PackageDataResp**](PackageDataResp.md) |  | [optional] 

## Example

```python
from chatdoc.models.api_package_info_resp import APIPackageInfoResp

# TODO update the JSON string below
json = "{}"
# create an instance of APIPackageInfoResp from a JSON string
api_package_info_resp_instance = APIPackageInfoResp.from_json(json)
# print the JSON string representation of the object
print
APIPackageInfoResp.to_json()

# convert the object into a dict
api_package_info_resp_dict = api_package_info_resp_instance.to_dict()
# create an instance of APIPackageInfoResp from a dict
api_package_info_resp_form_dict = api_package_info_resp.from_dict(api_package_info_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


