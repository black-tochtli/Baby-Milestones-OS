"""Claude tool_use definitions for Digital Babysitter."""

TOOLS = [
    {
        "name": "log_routine_event",
        "description": "Log a routine event (nap, meal, activity) with timestamp.",
        "input_schema": {
            "type": "object",
            "properties": {
                "child_name": {"type": "string"},
                "event_type": {
                    "type": "string",
                    "enum": ["nap_start", "nap_end", "meal", "snack", "activity_start", "activity_end"]
                },
                "timestamp": {"type": "string", "description": "Time in HH:MM format"},
                "notes": {"type": "string"}
            },
            "required": ["child_name", "event_type", "timestamp"]
        }
    },
    {
        "name": "send_parent_alert",
        "description": "Send a proactive alert to the parent about something that needs attention.",
        "input_schema": {
            "type": "object",
            "properties": {
                "alert_type": {
                    "type": "string",
                    "enum": ["nap_due", "meal_due", "activity_suggestion", "general"]
                },
                "message": {"type": "string", "description": "The alert message for the parent"},
                "urgency": {
                    "type": "string",
                    "enum": ["info", "soon", "now"]
                }
            },
            "required": ["alert_type", "message", "urgency"]
        }
    }
]


def handle_tool_call(tool_name: str, tool_input: dict) -> str:
    if tool_name == "log_routine_event":
        print(f"\n[Logged] {tool_input['child_name']} — "
              f"{tool_input['event_type']} at {tool_input['timestamp']}")
        return "Event logged."

    elif tool_name == "send_parent_alert":
        urgency_icons = {"info": "ℹ️", "soon": "⏰", "now": "🔔"}
        icon = urgency_icons.get(tool_input["urgency"], "📢")
        print(f"\n{icon} ALERT [{tool_input['alert_type']}]: {tool_input['message']}")
        return "Alert sent."

    return f"Unknown tool: {tool_name}"
