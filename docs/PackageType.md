# PackageType

if provided, use this package(lite, basic, elite) to upload, this parameter is only effective for PDF file. if upload file type is (md,epub,txt), this parameter will be ignore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from chatdoc.models.package_type import PackageType

# TODO update the JSON string below
json = "{}"
# create an instance of PackageType from a JSON string
package_type_instance = PackageType.from_json(json)
# print the JSON string representation of the object
print
PackageType.to_json()

# convert the object into a dict
package_type_dict = package_type_instance.to_dict()
# create an instance of PackageType from a dict
package_type_form_dict = package_type.from_dict(package_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


