aria_attributes_list = """
Attribute	Applies to	Description
aria-activedescendant	Any descendant of an element with role="combobox", role="grid", role="listbox", role="menu", role="radiogroup", role="tablist", or role="tree".	- Identifies the currently active element when focus is on the parent.
aria-atomic	Any element. Typically used with live regions.	- Indicates whether assistive technologies will present all or only parts of the changed region based on the change notifications defined by the aria-relevant attribute.
aria-autocomplete	Elements with role="combobox" and role="searchbox".	- Indicates the availability and type of predictive text that appears when a user enters information in a form field.
aria-busy	Any element.	- Indicates that an element and its descendants are currently being modified and that assistive technologies MAY want to wait until the modifications are complete before exposing them to the user.
aria-checked	Elements with role="checkbox", role="menuitemcheckbox", and role="radio".	- Indicates the current "checked" state of checkboxes, radio buttons, and menu item checkboxes.
aria-colcount	Elements with role="grid" or role="table".	- Defines the total number of columns in a grid or table.
aria-colindex	Elements within a structure with role="gridcell", role="columnheader", or role="row".	- Defines an element's column index or position with respect to the total number of columns within a grid, table, or treegrid.
aria-colspan	Elements with role="gridcell" or role="columnheader".	- Defines the number of columns spanned by a grid cell or column header.
aria-controls	Any element.	- Identifies the element(s) whose content or presence is controlled by the current element.
aria-current	Any element.	- Indicates the element that represents the current item within a container or set of related elements.
aria-describedby	Any element.	- Identifies the element(s) that describe the object.
aria-details	Any element.	- Identifies the element that provides a detailed, extended description for the object.
aria-disabled	Any element.	- Indicates that the element is perceivable but disabled, so it is not editable or otherwise operable.
aria-dropeffect	Any element.	- Indicates what types of operations can be performed on a dragged object(s) that is released on this drop target.
aria-errormessage	Elements with role="alertdialog", role="dialog", or elements that are owned by or control content that is marked by aria-invalid="true".	- Identifies the element that provides an error message for the object.
aria-expanded	Elements with role="button", role="group", role="listitem", role="menuitem", role="row", role="tab", role="treeitem".	- Indicates whether the element, or another element it controls, is currently expanded or collapsed.
aria-flowto	Any element.	- Identifies the next element(s) in an alternate reading order of content which, at the user's discretion, allows assistive technology to override the general default reading order.
aria-grabbed	Any element that is draggable.	- Indicates an element's "grabbed" state in a drag-and-drop operation.
aria-haspopup	Elements with role="button", role="combobox", role="listbox", role="menu", role="textbox", or role="tree".	- Indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered by an element.
aria-hidden	Any element.	- Indicates whether the element is exposed to an accessibility API.
aria-invalid	Elements with role="textbox", role="searchbox", role="combobox", and any other element that supports user input.	- Indicates the entered value does not conform to the format expected by the application.
aria-keyshortcuts	Any element.	- Indicates keyboard shortcuts that an author has implemented to activate or give focus to an element.
aria-label	Any element.	- Defines a string value that labels the current element.
aria-labelledby	Any element.	- Identifies the element(s) that label the current element.
aria-level	Elements with role="heading", role="listitem", or role="treeitem".	- Defines the hierarchical level of an element within a structure.
aria-live	Any element.	- Indicates that an element will be updated, and describes the types of updates the user agents, assistive technologies, and user can expect from the element.
aria-modal	Elements with role="dialog".	- Indicates that an element is modal when displayed.
aria-multiline	Elements with role="textbox".	- Indicates whether a text box accepts multiple lines of input or only a single line.
aria-multiselectable	Elements with role="grid" or role="listbox".	- Indicates that the user may select more than one item from the current selectable descendants.
aria-orientation	Elements with role="progressbar", role="slider", role="scrollbar", or role="tablist".	- Indicates whether the orientation of the element is horizontal or vertical.
aria-owns	Any element.	- Identifies an element (or elements) whose presence and/or content is controlled by the current element.
aria-placeholder	Elements with role="textbox" or role="searchbox".	- Defines a short hint (a word or short phrase) intended to aid the user with data entry when the control has no value.
aria-posinset	Elements within a set (e.g., elements with role="listitem" within a role="listbox" or role="menuitem" within a role="menu").	- Defines an element's number or position in the current set of listitems or treeitems. Not required if all elements in the set are present in the DOM.
aria-pressed	Elements with role="button", role="checkbox", or role="radio".	- Indicates the current "pressed" state of toggle buttons.
aria-readonly	Elements with role="textbox", role="searchbox", role="combobox", role="gridcell", and other input types.	- Indicates that the element is not editable, but is otherwise operable.
aria-relevant	Elements with aria-live="assertive" or aria-live="polite".	- Indicates what notifications the user agent will trigger when the accessibility tree within a live region is modified.
aria-required	Elements with role="textbox", role="searchbox", role="combobox", and other form-related roles.	- Indicates that user input is required on the element before a form may be submitted.
aria-roledescription	Any element.	- Defines a human-readable, author-localized description for the role of an element.
aria-rowcount	Elements with role="grid" or role="table".	- Defines the total number of rows in a grid or table.
aria-rowindex	Elements within a structure with role="row", role="gridcell", or role="rowheader".	- Defines an element's row index or position with respect to the total number of rows within a grid, table, or treegrid.
aria-rowspan	Elements with role="gridcell" or role="rowheader".	- Defines the number of rows spanned by a grid cell or row header.
aria-selected	Elements within a selectable container like role="listbox", role="menu", role="radiogroup", role="tablist", or role="tree".	- Indicates the current "selected" state of various widgets.
aria-setsize	Elements within a set (e.g., elements with role="listitem" within a role="listbox" or role="menuitem" within a role="menu").	- Defines the number of items in the current set of listitems or treeitems. Not required if all elements in the set are present in the DOM.
aria-sort	Elements with role="columnheader".	- Indicates if items in a table or grid are sorted and, if so, the sort order.
aria-valuemax	Elements with role="progressbar", role="slider", or role="spinbutton".	- Defines the maximum allowed value for a range widget.
aria-valuemin	Elements with role="progressbar", role="slider", or role="spinbutton".	- Defines the minimum allowed value for a range widget.
aria-valuenow	Elements with role="progressbar", role="slider", or role="spinbutton".	- Defines the current value for a range widget.
aria-valuetext	Elements with role="progressbar", role="slider", or role="spinbutton".	- Defines the human-readable text alternative of aria-valuenow for a range widget.
"""
