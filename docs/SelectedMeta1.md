# SelectedMeta1

When use [**Ask About Selected Text**](https://chatdoc.notion.site/4-Ways-to-Make-Queries-3d8d6d36060b4c7eb1d69e6a32405dd7), this field is acquired from [EVENT_TYPES.CHAT_ICON_CLICKED](/#section/ChatDOC-Document-Viewer/EVENT_TYPES) of our DOCViewerSDK.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**material** | **str** | Select the html node text | 
**upload_id** | **str** | Upload id | 
**rects** | [**List[PDFViewerRect]**](PDFViewerRect.md) |  | 
**indexes** | **List[int]** | Select the collection of all data-index attributes of the html node | 
**focus_node** | **str** | The Node in which the selection ends. Can return null if selection never existed in the document (for example, in an iframe that was never clicked on) | 
**anchor_node** | **str** | The Node in which the selection begins. Can return null if selection never existed in the document (e.g., an iframe that was never clicked on) | 
**focus_offset** | **int** | Number representing the offset of the selection&#39;s anchor within the focusNode. If focusNode is a text node, this is the number of characters within focusNode preceding the focus. If focusNode is an element, this is the number of child nodes of the focusNode preceding the focus | 
**anchor_offset** | **int** | Number representing the offset of the selection&#39;s anchor within the anchorNode. If anchorNode is a text node, this is the number of characters within anchorNode preceding the anchor. If anchorNode is an element, this is the number of child nodes of the anchorNode preceding the anchor | 

## Example

```python
from chatdoc.models.selected_meta1 import SelectedMeta1

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedMeta1 from a JSON string
selected_meta1_instance = SelectedMeta1.from_json(json)
# print the JSON string representation of the object
print
SelectedMeta1.to_json()

# convert the object into a dict
selected_meta1_dict = selected_meta1_instance.to_dict()
# create an instance of SelectedMeta1 from a dict
selected_meta1_form_dict = selected_meta1.from_dict(selected_meta1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


