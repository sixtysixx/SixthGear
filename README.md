# Syx

**Syx** is a hybrid productivity application built on the [Frappe Framework](https://frappe.io/framework). It combines the **LifeOS** philosophy (Action/Execution) with the **Building a Second Brain** methodology (Knowledge Management) into a single, cohesive system.

## Core Philosophy

Syx operates on the principle that organizing by **actionability** is superior to organizing by topic. It uses **Projects** as the central hub where your actions (Tasks) meet your knowledge (Notes).

### Key Methodologies

1. **PARA Method:**
    * **Projects:** Short-term efforts with a deadline.
    * **Areas:** Long-term responsibilities with no deadline.
    * **Resources:** Topics of ongoing interest.
    * **Archives:** (Implicitly handled by Status fields).

2. **CODE Framework:**
    * **Capture:** Quick entry of thoughts via the Inbox (`Capture Item`).
    * **Organize:** Move items to Projects or Areas.
    * **Distill:** Summarize notes.
    * **Express:** Execute tasks.

3. **Timeblocking:**
    * The `Task` system is designed for calendar-based scheduling.

## Features

* **Project Hub:** A specialized dashboard for every Project that displays your **Action List** (Tasks) side-by-side with your **Knowledge Context** (Notes & Resources).
* **Inbox:** A dedicated `Capture Item` DocType for fleeting thoughts.
* **Home Base:** A customized Workspace with quick stats and shortcuts.
* **Review Wizard:** Integrated Morning/Evening review workflows that save directly to your Notes.
* **Habit Tracker:** Track daily and weekly habits.
* **Recurring Tasks:** Automate task generation for repetitive actions (Daily, Weekly, Monthly).
* **Goal Tracking:** High-level OKR/Goal management linked to Projects.
* **Mood Log:** Track mood and energy levels.
* **Focus Mode:** Distraction-free interface for deep work.
* **Readwise Import (Beta):** Basic integration to import highlights from Readwise.

## Roadmap

* **Voice Memos:** Mobile-friendly audio recording with auto-transcription (OpenAI Whisper).
* **Browser Extension:** Chrome/Firefox extension to clip URLs directly to Syx.
* **Email-to-Inbox:** Forward emails to creating Capture Items.
* **Offline Support:** Full PWA capabilities for offline access.

## Installation

### Using Docker (Recommended)

1. Clone this repository.
2. Navigate to the directory:

    ```bash
    cd syx
    ```

3. Run with Podman/Docker Compose:

    ```bash
    podman compose up -d --build
    # or
    docker-compose up -d --build
    ```

4. Access the site at `http://localhost:8000` (default Frappe port).

### Manual Installation

1. Ensure you have a running Bench instance.
2. Get the app:

    ```bash
    bench get-app https://github.com/yourusername/syx
    ```

3. Install into your site:

    ```bash
    bench --site [your-site-name] install-app syx
    ```

4. Migrate database:

    ```bash
    bench --site [your-site-name] migrate
    ```

## Troubleshooting

### Windows: Error during connect

If you encounter an error like `error during connect: Get ... open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified`, this usually indicates that Docker Desktop is not running or not accessible.

1. Ensure **Docker Desktop** is installed and running.
2. If it is running, try restarting it.
3. Ensure you are running the command in a terminal that has access to the Docker daemon.

## License

MIT