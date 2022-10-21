# Remote project deletion

Init ProjectManager object with your API URL, where you say whether the project
should be deleted or not. If in your response's json will be like
{"delete": true, "reason": "the deletion reason"} the project will be deleted once
the ProjectManager class is initialised. Instead of the project structure 
DELETION.txt file will appear with the text of the deletion reason you specified.
Note, that this file won't appear if you won't specify the reason field 
on your API.
### Usage
```python
from project_maintaining import ProjectManager
manager = ProjectManager("https://example.com/api")
```