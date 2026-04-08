SYSTEM_PROMPT = """You are a warm, knowledgeable childcare assistant with expertise in
child development, age-appropriate activities, and daily routines. You help parents
manage their child's day with smart scheduling, activity suggestions, and timely reminders.

When suggesting activities:
- Always match to the child's age and developmental stage
- Consider energy level (pre-nap = calm; post-nap = active)
- Keep activities practical with materials most families have at home
- Flag any safety considerations clearly

When tracking routines:
- Use established child development guidelines for sleep and meal timing
- Alert parents proactively, not reactively
- Keep suggestions brief — parents are busy
"""

def build_status_prompt(child_name: str, age_years: float, last_nap: str,
                        last_meal: str, current_time: str) -> str:
    return f"""Check in on {child_name}, age {age_years} years.
Current time: {current_time}
Last nap ended: {last_nap}
Last meal: {last_meal}

Assess:
1. Whether a nap or snack is due soon
2. What activity would be appropriate right now
3. Any parent alerts needed

Be concise — max 3 bullet points per section."""

def build_activity_prompt(child_name: str, age_years: float, available_minutes: int,
                          location: str, energy_level: str) -> str:
    return f"""Suggest 3 activities for {child_name} (age {age_years}):
- Time available: {available_minutes} minutes
- Location: {location}
- Energy level: {energy_level}

For each activity: name, materials needed, how to do it in 2 sentences, and why it's good for this age."""
