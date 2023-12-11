# HtmlSelectedMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**material** | **str** | Select the html node text | 
**indexes** | **List[int]** | Select the collection of all data-index attributes of the html node | 
**focus_node** | **str** | The Node in which the selection ends. Can return null if selection never existed in the document (for example, in an iframe that was never clicked on) | 
**upload_id** | **str** | Upload id | 
**anchor_node** | **str** | The Node in which the selection begins. Can return null if selection never existed in the document (e.g., an iframe that was never clicked on) | 
**focus_offset** | **int** | Number representing the offset of the selection&#39;s anchor within the focusNode. If focusNode is a text node, this is the number of characters within focusNode preceding the focus. If focusNode is an element, this is the number of child nodes of the focusNode preceding the focus | 
**anchor_offset** | **int** | Number representing the offset of the selection&#39;s anchor within the anchorNode. If anchorNode is a text node, this is the number of characters within anchorNode preceding the anchor. If anchorNode is an element, this is the number of child nodes of the anchorNode preceding the anchor | 

## Example

```python
from chatdoc.models.html_selected_meta import HtmlSelectedMeta

# TODO update the JSON string below
json = "{}"
# create an instance of HtmlSelectedMeta from a JSON string
html_selected_meta_instance = HtmlSelectedMeta.from_json(json)
# print the JSON string representation of the object
print
HtmlSelectedMeta.to_json()

# convert the object into a dict
html_selected_meta_dict = html_selected_meta_instance.to_dict()
# create an instance of HtmlSelectedMeta from a dict
html_selected_meta_form_dict = html_selected_meta.from_dict(html_selected_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


