# PackageQuotaResp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**APIPackageInfoResp**](APIPackageInfoResp.md) |  | [optional] 

## Example

```python
from chatdoc.models.package_quota_resp import PackageQuotaResp

# TODO update the JSON string below
json = "{}"
# create an instance of PackageQuotaResp from a JSON string
package_quota_resp_instance = PackageQuotaResp.from_json(json)
# print the JSON string representation of the object
print
PackageQuotaResp.to_json()

# convert the object into a dict
package_quota_resp_dict = package_quota_resp_instance.to_dict()
# create an instance of PackageQuotaResp from a dict
package_quota_resp_form_dict = package_quota_resp.from_dict(package_quota_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


