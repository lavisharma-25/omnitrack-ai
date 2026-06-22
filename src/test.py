from langchain_core.messages import HumanMessage

from src.tools.tracker_tools.create_tracker import create_tracker
from src.tools.tracker_tools.list_trackers import list_trackers
from src.tools.tracker_tools.edit_tracker import edit_tracker
from src.tools.tracker_tools.delete_tracker import delete_tracker
from src.tools.tracker_tools.remove_records import remove_records
from src.agents.supervisor_agent import supervisor_agent

# def run_test1():

#     print("\n🚀 CREATE TRACKER TEST")
#     result = create_tracker(
#         name="expenses",
#         columns=[
#             {"name": "amount", "type": "float"},
#             {"name": "category", "type": "string"},
#             {"name": "date", "type": "date"}
#         ]
#     )
#     print(result)

#     print("\n📋 LIST TRACKERS")
#     print(list_trackers())

    # print("\n✏️ EDIT TRACKER (ADD COLUMN)")
    # print(
    #     edit_tracker(
    #         name="expenses",
    #         action="add_column",
    #         payload={
    #             "column": {"name": "notes", "type": "string"}
    #         }
    #     )
    # )

    # print("\n🧾 REMOVE RECORDS (CLEAR ALL)")
    # print(remove_records(name="expenses"))

    # print("\n🗑️ DELETE TRACKER")
    # print(delete_tracker(name="expenses", password="admin123"))

    # print("\n📋 FINAL TRACKER LIST")
    # print(list_trackers())

def run_test2():
    print("\n==============================")
    print("🚀 TrackFlow AI - End to End Test")
    print("==============================\n")

    # 1. Create Tracker
    # print("\n🟢 USER: Create a tracker called expenses with amount, category, date\n")

    # response1 = supervisor_agent.invoke({
    #     "messages": [
    #         HumanMessage(content="""Create a tracker named expenses with columns: amount (float), category (string), date (date)""")
    #         # HumanMessage(content="""Create a tracker named habits with columns: habit_name (string), occurance (number), status (bool)""")
    #     ]
    # })

    # print("🤖 RESPONSE:\n", response1["messages"][-1].content)

    # 2. List Trackers
    # print("\n🟢 USER: List all trackers\n")

    # response2 = supervisor_agent.invoke({
    #     "messages": [HumanMessage(content="List all trackers")]
    # })

    # print("🤖 RESPONSE:\n", response2["messages"][-1].content)

    # 3. Edit Tracker
    print("\n🟢 USER: Add notes column in expenses tracker\n")

    response3 = supervisor_agent.invoke({
        "messages": [HumanMessage("Add a column 'notes' of type string in expenses tracker")]
    })

    print("🤖 RESPONSE:\n", response3["messages"][-1].content)

    # # 4. Remove Records
    # print("\n🟢 USER: Clear all records from expenses tracker\n")

    # response4 = supervisor_agent.invoke({
    #     "input": "Remove all records from expenses tracker"
    # })

    # print("🤖 RESPONSE:\n", response4)


if __name__ == "__main__":
    run_test2()