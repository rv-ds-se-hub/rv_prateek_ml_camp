# Phase 1: The Infrastructure (The Skeleton)

**Objective**: Build a Python bot that responds to a specific command (/agenda) by retrieving and displaying the next 5 events from the user's Google Calendar.
> Status: Free (Google Cloud Free Tier & Telegram).

> AI Component: None (Pure logic and API handling).

## Part 1: The Telegram Handshake

**Goal**: Ensure communication with a Python script via Telegram.

- [ ] Create the Bot Identity
    - Open Telegram and message @BotFather.
    - Create a new bot and secure the HTTP API Token.

- [ ] Setup Python Environment
    - Create a project folder.
    - Install python-telegram-bot.

- [ ] The "Hello World" Script
    - Write a script that listens for messages.
    - Program a basic command (e.g., /start) where the bot replies "I am online."
    - Run the script locally on a laptop to confirm the loop works.

## Part 2: The Google Cloud Barrier

**Goal**: Authenticate with Google without using a browser login flow (Service Account method).

- [ ] Project Setup

    - Go to Google Cloud Console > Create New Project (e.g., "MyAgent").
    - Search for and Enable "Google Calendar API".

- [ ] Credentials Creation
    - Create a Service Account (acts as a "robot user").
    - Generate and download the JSON Key file. Store it in the project folder (add to .gitignore immediately).

- [ ] The Permission Bridge (Crucial Step)
    - Open your personal Google Calendar on the web.
    - Go to Settings > Sharing and Settings.
    - Share the calendar with the Service Account Email Address (found inside the JSON file).
    - Permission Level: Set to "Make changes to events" (needed for Phase 2, set it now).

## Part 3: The Data Reader (Standalone)

**Goal**: Fetch data using Python in the terminal before adding Bot complexity.

- [ ] Install Google Libraries

    - Install google-api-python-client and google-auth.

- [ ] Write test_calendar.py
    - Write a script that authenticates using the JSON file.
    - Create a function to fetch the next 10 upcoming events.
    - Print the raw data to the terminal console.

- [ ] Data Parsing
    - Refine the script to extract only specific fields: Event Name, Start Time, and End Time.

## Part 4: The Merger

**Goal**: Connect the Telegram command to the Google function.

- [ ] Import Logic
    - Import the calendar functions into the main Bot script.

- [ ] Create Command Handler
    - Create a listener for /agenda.

- [ ] Formatting
    - When /agenda is triggered:
    - Bot calls Google API.
    - Bot formats the list into a readable string (e.g., "📅 Math: 10:00 AM").
    - Bot sends the message back to the user.

## Common Gotchas (Blockers)


1. Timezones:

    Issue: Google returns time in UTC (Zulu time).

    Fix: Ensure the request body asks for the specific local timezone, or convert it in Python.

2. Service Account "Ghosting":

    Issue: The script runs without errors but returns [] (empty list) even though the calendar has events.

    Blocker: This happens if the user forgot to share their personal calendar with the Service Account email.

## The Testing Process

Run these tests before moving to Phase 2:

1. The "Empty" Test: Create a dummy calendar with zero events. Run /agenda.

    Pass: Bot replies "No upcoming events found."

    Fail: Bot crashes or says nothing.

2. The "Birthday" Test:

    Add an "All Day" event for tomorrow. Run /agenda.

    Pass: Bot displays the event with just the date, no time.

3. The "Disconnect" Test:

    Turn off Wi-Fi on the laptop. Run the bot.

    Pass: Script handles the error gracefully (prints "Connection Error" in terminal).

    Fail: Script terminates with a raw stack trace.