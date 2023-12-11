# WebsiteReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website** | **str** | upload document by website url | 
**collection_id** | **str** | if provided, add document to the collection, collection can be created by &#x60;POST /collections&#x60; | [optional] 

## Example

```python
from chatdoc.models.website_req import WebsiteReq

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteReq from a JSON string
website_req_instance = WebsiteReq.from_json(json)
# print the JSON string representation of the object
print
WebsiteReq.to_json()

# convert the object into a dict
website_req_dict = website_req_instance.to_dict()
# create an instance of WebsiteReq from a dict
website_req_form_dict = website_req.from_dict(website_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


