# Sixth Gear

**Sixth Gear** is a hybrid productivity application built on the [Frappe Framework](https://frappe.io/framework). It combines the **LifeOS** philosophy (Action/Execution) with the **Building a Second Brain** methodology (Knowledge Management) into a single, cohesive system.

## Core Philosophy

Sixth Gear operates on the principle that organizing by **actionability** is superior to organizing by topic. It uses **Projects** as the central hub where your actions (Tasks) meet your knowledge (Notes).

### Key Methodologies

1.  **PARA Method:**
    *   **Projects:** Short-term efforts with a deadline (e.g., "Complete App Design").
    *   **Areas:** Long-term responsibilities with no deadline (e.g., "Health", "Finances").
    *   **Resources:** Topics of ongoing interest (e.g., "Python", "Gardening").
    *   **Archives:** (Implicitly handled by Status fields).

2.  **CODE Framework:**
    *   **Capture:** Quick entry of thoughts via the Inbox (`Capture Item`).
    *   **Organize:** Move items to Projects or Areas.
    *   **Distill:** Summarize notes using "Progressive Summarization".
    *   **Express:** Execute tasks and create output.

3.  **Timeblocking:**
    *   The `Task` system is designed for calendar-based scheduling.

## Features

*   **Project Hub:** A specialized dashboard for every Project that displays your **Action List** (Tasks) side-by-side with your **Knowledge Context** (Notes & Resources).
*   **Inbox:** A dedicated `Capture Item` DocType for fleeting thoughts.
*   **Home Base:** A customized Workspace with quick stats and shortcuts.
*   **Progressive Summarization:** Dedicated fields in Notes for raw content, summarization, and key takeaways.

## Installation

### Using Docker (Recommended)

1.  Clone this repository.
2.  Navigate to the directory:
    ```bash
    cd sixth_gear
    ```
3.  Run with Docker Compose:
    ```bash
    docker-compose up -d --build
    ```
4.  Access the site at `http://localhost:8000` (default Frappe port).

### Manual Installation

1.  Ensure you have a running Bench instance.
2.  Get the app:
    ```bash
    bench get-app https://github.com/yourusername/sixth_gear
    ```
3.  Install into your site:
    ```bash
    bench --site [your-site-name] install-app sixth_gear
    ```
4.  Migrate database:
    ```bash
    bench --site [your-site-name] migrate
    ```

## Usage Guide

1.  **Start at the Home Base:** Check your "Tasks Due Today".
2.  **Capture:** Use the "Quick Capture" shortcut to log ideas.
3.  **Clarify:** Go to your Inbox list. Convert `Capture Items` into `Tasks` (if actionable) or `Notes` (if reference).
4.  **Execute:** Open a `Project`. Review the "Action List" to see what needs doing. Read the "Knowledge Context" notes to refresh your memory.
5.  **Reflect:** Update your `Area` descriptions and review `Resource` notes periodically.

## License

MIT
