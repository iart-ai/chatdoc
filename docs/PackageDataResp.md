# PackageDataResp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_count** | **int** | Max count of not expired package | 
**used_count** | **int** | Used count of not expired package | 

## Example

```python
from chatdoc.models.package_data_resp import PackageDataResp

# TODO update the JSON string below
json = "{}"
# create an instance of PackageDataResp from a JSON string
package_data_resp_instance = PackageDataResp.from_json(json)
# print the JSON string representation of the object
print
PackageDataResp.to_json()

# convert the object into a dict
package_data_resp_dict = package_data_resp_instance.to_dict()
# create an instance of PackageDataResp from a dict
package_data_resp_form_dict = package_data_resp.from_dict(package_data_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


