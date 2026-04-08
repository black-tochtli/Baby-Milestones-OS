"""Digital Babysitter — main agent loop."""

import anthropic
from config import ANTHROPIC_API_KEY, MODEL, MAX_TOKENS
from prompts import SYSTEM_PROMPT, build_status_prompt, build_activity_prompt
from tools import TOOLS, handle_tool_call

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def chat(messages: list[dict]) -> str:
    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = handle_tool_call(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })
            messages.append({"role": "user", "content": tool_results})
            continue

        for block in response.content:
            if hasattr(block, "text"):
                return block.text
        return ""


def main():
    print("\n=== Digital Babysitter ===\n")
    child_name = input("Child's name: ").strip()
    age = float(input("Age (e.g. 3 or 1.5): ").strip())
    current_time = input("Current time (HH:MM): ").strip()
    last_nap = input("Last nap ended at (HH:MM): ").strip()
    last_meal = input("Last meal at (HH:MM): ").strip()

    user_message = build_status_prompt(child_name, age, last_nap, last_meal, current_time)
    messages = [{"role": "user", "content": user_message}]

    print("\nChecking in...\n")
    response = chat(messages)
    print(response)

    print("\n---\nAsk anything or type 'quit'.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        messages.append({"role": "user", "content": user_input})
        reply = chat(messages)
        print(f"\nAssistant: {reply}\n")


if __name__ == "__main__":
    main()
