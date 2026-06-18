EXAMPLES = """
EXAMPLES

User: Create a tracker named Tasks with columns Title, Status, Priority

Assistant:
Use create_tracker tool.

--------------------------------------------------

User: Show all trackers

Assistant:
Use list_trackers tool.

--------------------------------------------------

User: Add a record to Tasks:
Title = Learn LangGraph
Status = In Progress
Priority = High

Assistant:
Use add_record tool.

--------------------------------------------------

User: Show all records from Tasks

Assistant:
Use list_records tool.

--------------------------------------------------

User: Delete record 123 from Tasks

Assistant:
Use delete_record tool.
"""