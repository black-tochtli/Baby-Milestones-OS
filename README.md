# 👶 Baby Milestone OS

> An AI agent that helps parents manage child routines, suggests age-appropriate activities, and sends smart alerts when things need attention.

---

## The Problem

Parents juggle nap schedules, meal times, screen limits, and activity ideas — all while trying to be present. This agent handles the logistics so parents can focus on the moments.

## How It Works

1. **Profile setup** — Input child's age, interests, dietary needs, and daily schedule
2. **Routine management** — Agent tracks naps, meals, and activities through the day
3. **Activity suggestions** — Claude generates age-appropriate activity ideas based on time available, weather, and energy level
4. **Parent alerts** — Proactive nudges ("Nap window in 20 min", "Last meal was 3hrs ago")

## Demo

```
$ python src/agent.py

> Child's name and age? Mia, 3 years old
> Current time? 2:15 PM
> Last nap ended? 11:30 AM

Status check for Mia:
  ⏰ Nap window approaching (target: 3:00 PM)
  🍎 Snack recommended — 2.75hrs since lunch
  🎨 Suggested activity: Finger painting (15-20 min quiet activity before nap)

Next alert: 2:45 PM — Start nap wind-down routine
```

---

## Tech Stack

- **AI:** Claude API (`claude-sonnet-4-6`) with tool use
- **Language:** Python 3.11+
- **Notifications:** SMS via Twilio (optional)

---

## Quick Start

```bash
git clone https://github.com/black-tochtli/digital-babysitter
cd digital-babysitter
cp .env.example .env        # add your ANTHROPIC_API_KEY
pip install -r requirements.txt
python src/agent.py
```

---

## Project Structure

```
digital-babysitter/
├── src/
│   ├── agent.py       # Main agent loop + Claude API calls
│   ├── prompts.py     # System prompts and child profile templates
│   ├── tools.py       # Claude tool_use definitions
│   └── config.py      # Settings and constants
├── tests/
│   └── test_agent.py
├── docs/
│   └── architecture.md
├── .env.example
├── requirements.txt
└── README.md
```

---

## Roadmap

- [x] Child profile and routine setup
- [ ] Activity suggestion engine
- [ ] Proactive parent alerts
- [ ] Multi-child household support
- [ ] Integration with smart home devices

---

## Status

🚧 **v0.1 in progress** — profile setup and activity suggestions working
