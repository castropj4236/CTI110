"""
Broadcast Station Planner
A beginner-friendly GUI application for managing radio/TV programs,
daily schedules, and favorite shows.

Uses only Python's standard library: tkinter, json, os, and datetime.
"""

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

APP_TITLE = "Broadcast Station Planner"
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEDULE_FILE = os.path.join(DATA_DIR, "broadcast_schedule.json")
FAVORITES_FILE = os.path.join(DATA_DIR, "broadcast_favorites.json")

SAMPLE_PROGRAMS = [
    {"program_name": "Morning News", "category": "News"},
    {"program_name": "The Radio Mix", "category": "Music"},
    {"program_name": "Sports Central", "category": "Sports"},
    {"program_name": "Evening Talk", "category": "Talk Show"},
    {"program_name": "Movie Night", "category": "Entertainment"},
    {"program_name": "Weather Update", "category": "News"},
    {"program_name": "Classic Hits", "category": "Music"},
]


def load_json(filename, default_value):
    """Load JSON data; return a safe default if the file is missing or invalid."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return default_value
    except (json.JSONDecodeError, OSError):
        return default_value


def save_json(filename, data):
    """Save data to a JSON file and report whether saving succeeded."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError as error:
        messagebox.showerror("Save Error", f"Could not save data:\n{error}")
        return False


class BroadcastPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1000x680")
        self.root.minsize(820, 560)

        # Program information is built in; schedule and favorites persist in JSON.
        self.programs = [item.copy() for item in SAMPLE_PROGRAMS]
        loaded_schedule = load_json(SCHEDULE_FILE, [])
        loaded_favorites = load_json(FAVORITES_FILE, [])

        self.schedule = loaded_schedule if isinstance(loaded_schedule, list) else []
        self.favorites = loaded_favorites if isinstance(loaded_favorites, list) else []

        self.search_var = tk.StringVar()
        self.program_choice_var = tk.StringVar()
        self.start_time_var = tk.StringVar(value="09:00")
        self.duration_var = tk.StringVar(value="30")
        self.status_var = tk.StringVar(value="Ready — choose an option to get started.")

        self.setup_style()
        self.build_interface()
        self.refresh_all()

    def setup_style(self):
        """Set a simple, readable visual style for the application."""
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"))
        style.configure("Subtitle.TLabel", font=("Segoe UI", 10))
        style.configure("Section.TLabel", font=("Segoe UI", 12, "bold"))
        style.configure("Treeview", rowheight=27, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"))

    def build_interface(self):
        """Create the main window, tabs, tables, and controls."""
        header = ttk.Frame(self.root, padding=(18, 14))
        header.pack(fill="x")

        ttk.Label(header, text="📻 BROADCAST STATION PLANNER",
                  style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            header,
            text="Plan programs • Organize airtime • Keep your favorite shows",
            style="Subtitle.TLabel"
        ).pack(anchor="w", pady=(3, 0))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=16, pady=(0, 10))

        self.dashboard_tab = ttk.Frame(self.notebook, padding=16)
        self.programs_tab = ttk.Frame(self.notebook, padding=16)
        self.schedule_tab = ttk.Frame(self.notebook, padding=16)
        self.favorites_tab = ttk.Frame(self.notebook, padding=16)

        self.notebook.add(self.dashboard_tab, text="Dashboard")
        self.notebook.add(self.programs_tab, text="Programs & Search")
        self.notebook.add(self.schedule_tab, text="Broadcast Schedule")
        self.notebook.add(self.favorites_tab, text="Favorites")

        self.build_dashboard_tab()
        self.build_programs_tab()
        self.build_schedule_tab()
        self.build_favorites_tab()

        footer = ttk.Label(self.root, textvariable=self.status_var, anchor="w",
                           relief="sunken", padding=(10, 5))
        footer.pack(fill="x", side="bottom")

    def build_dashboard_tab(self):
        ttk.Label(self.dashboard_tab, text="Station Dashboard",
                  style="Title.TLabel").pack(anchor="w", pady=(0, 12))

        summary = ttk.Frame(self.dashboard_tab)
        summary.pack(fill="x", pady=(0, 18))

        self.program_count_label = self.make_stat_card(summary, "Available Programs")
        self.schedule_count_label = self.make_stat_card(summary, "Scheduled Shows")
        self.favorite_count_label = self.make_stat_card(summary, "Favorite Shows")

        ttk.Label(self.dashboard_tab, text="Quick actions",
                  style="Section.TLabel").pack(anchor="w", pady=(4, 8))

        actions = ttk.Frame(self.dashboard_tab)
        actions.pack(anchor="w", fill="x")
        ttk.Button(actions, text="Search Programs",
                   command=lambda: self.notebook.select(self.programs_tab)).pack(
                       side="left", padx=(0, 8), pady=4)
        ttk.Button(actions, text="Manage Schedule",
                   command=lambda: self.notebook.select(self.schedule_tab)).pack(
                       side="left", padx=8, pady=4)
        ttk.Button(actions, text="View Favorites",
                   command=lambda: self.notebook.select(self.favorites_tab)).pack(
                       side="left", padx=8, pady=4)

        ttk.Label(
            self.dashboard_tab,
            text=("Getting started\n\n"
                  "1. Open Programs & Search to browse the sample program catalog.\n"
                  "2. Open Broadcast Schedule to choose a show, start time, and duration.\n"
                  "3. Add programs to Favorites to keep a personal list.\n"
                  "4. Your schedule and favorites are saved automatically in JSON files."),
            justify="left"
        ).pack(anchor="w", pady=(22, 0))

    def make_stat_card(self, parent, label_text):
        card = ttk.LabelFrame(parent, text=label_text, padding=14)
        card.pack(side="left", fill="both", expand=True, padx=(0, 10))
        value_label = ttk.Label(card, text="0", font=("Segoe UI", 22, "bold"))
        value_label.pack(anchor="w")
        return value_label

    def build_programs_tab(self):
        ttk.Label(self.programs_tab, text="Program Catalog",
                  style="Title.TLabel").pack(anchor="w", pady=(0, 10))

        search_row = ttk.Frame(self.programs_tab)
        search_row.pack(fill="x", pady=(0, 10))
        ttk.Label(search_row, text="Search by name or category:").pack(side="left")
        search_entry = ttk.Entry(search_row, textvariable=self.search_var, width=32)
        search_entry.pack(side="left", padx=8)
        search_entry.bind("<KeyRelease>", lambda _event: self.refresh_programs())
        ttk.Button(search_row, text="Clear",
                   command=self.clear_search).pack(side="left", padx=(0, 8))
        ttk.Button(search_row, text="Add Selected to Favorites",
                   command=self.add_selected_program_to_favorites).pack(side="left")

        self.program_tree = ttk.Treeview(
            self.programs_tab, columns=("name", "category"), show="headings",
            selectmode="browse"
        )
        self.program_tree.heading("name", text="Program Name")
        self.program_tree.heading("category", text="Category")
        self.program_tree.column("name", width=430)
        self.program_tree.column("category", width=220)
        self.program_tree.pack(fill="both", expand=True)

        ttk.Label(self.programs_tab,
                  text="Tip: Search is not case-sensitive. Select a show before adding it to favorites.",
                  style="Subtitle.TLabel").pack(anchor="w", pady=(8, 0))

    def build_schedule_tab(self):
        ttk.Label(self.schedule_tab, text="Daily Broadcast Schedule",
                  style="Title.TLabel").pack(anchor="w", pady=(0, 10))

        form = ttk.LabelFrame(self.schedule_tab, text="Schedule a Program", padding=10)
        form.pack(fill="x", pady=(0, 12))

        ttk.Label(form, text="Program:").grid(row=0, column=0, sticky="w", padx=(0, 5))
        self.program_combo = ttk.Combobox(
            form, textvariable=self.program_choice_var, state="readonly", width=25
        )
        self.program_combo.grid(row=0, column=1, sticky="w", padx=(0, 14))

        ttk.Label(form, text="Start time (HH:MM):").grid(
            row=0, column=2, sticky="w", padx=(0, 5))
        ttk.Entry(form, textvariable=self.start_time_var, width=10).grid(
            row=0, column=3, sticky="w", padx=(0, 14))

        ttk.Label(form, text="Duration (minutes):").grid(
            row=0, column=4, sticky="w", padx=(0, 5))
        ttk.Entry(form, textvariable=self.duration_var, width=8).grid(
            row=0, column=5, sticky="w", padx=(0, 14))

        ttk.Button(form, text="Add to Schedule", style="Accent.TButton",
                   command=self.add_to_schedule).grid(
                       row=0, column=6, sticky="w", padx=(4, 0))

        self.schedule_tree = ttk.Treeview(
            self.schedule_tab,
            columns=("time", "name", "category", "duration", "end"),
            show="headings", selectmode="browse"
        )
        headings = [
            ("time", "Start Time", 100),
            ("name", "Program Name", 280),
            ("category", "Category", 160),
            ("duration", "Duration (min)", 120),
            ("end", "End Time", 100),
        ]
        for column, heading, width in headings:
            self.schedule_tree.heading(column, text=heading)
            self.schedule_tree.column(column, width=width, anchor="w")
        self.schedule_tree.pack(fill="both", expand=True)

        controls = ttk.Frame(self.schedule_tab)
        controls.pack(fill="x", pady=(8, 0))
        ttk.Button(controls, text="Remove Selected Schedule Entry",
                   command=self.remove_schedule_entry).pack(side="left")
        ttk.Button(controls, text="Save Now",
                   command=self.save_all_data).pack(side="left", padx=8)

    def build_favorites_tab(self):
        ttk.Label(self.favorites_tab, text="Favorite Programs",
                  style="Title.TLabel").pack(anchor="w", pady=(0, 10))
        ttk.Label(self.favorites_tab,
                  text="Your favorite programs stay saved when you close the app.",
                  style="Subtitle.TLabel").pack(anchor="w", pady=(0, 10))

        self.favorites_tree = ttk.Treeview(
            self.favorites_tab, columns=("name", "category"),
            show="headings", selectmode="browse"
        )
        self.favorites_tree.heading("name", text="Program Name")
        self.favorites_tree.heading("category", text="Category")
        self.favorites_tree.column("name", width=430)
        self.favorites_tree.column("category", width=220)
        self.favorites_tree.pack(fill="both", expand=True)

        ttk.Button(self.favorites_tab, text="Remove Selected Favorite",
                   command=self.remove_selected_favorite).pack(anchor="w", pady=(10, 0))

    def clear_search(self):
        self.search_var.set("")
        self.refresh_programs()

    def refresh_all(self):
        self.refresh_programs()
        self.refresh_schedule()
        self.refresh_favorites()
        self.refresh_dashboard()
        self.program_combo["values"] = [p["program_name"] for p in self.programs]
        if self.programs and not self.program_choice_var.get():
            self.program_choice_var.set(self.programs[0]["program_name"])

    def refresh_dashboard(self):
        self.program_count_label.config(text=str(len(self.programs)))
        self.schedule_count_label.config(text=str(len(self.schedule)))
        self.favorite_count_label.config(text=str(len(self.favorites)))

    def refresh_programs(self):
        if not hasattr(self, "program_tree"):
            return
        for row in self.program_tree.get_children():
            self.program_tree.delete(row)
        query = self.search_var.get().strip().casefold()
        for program in self.programs:
            name = str(program.get("program_name", ""))
            category = str(program.get("category", ""))
            if query and query not in name.casefold() and query not in category.casefold():
                continue
            self.program_tree.insert("", "end", iid=name, values=(name, category))

    def refresh_schedule(self):
        if not hasattr(self, "schedule_tree"):
            return
        for row in self.schedule_tree.get_children():
            self.schedule_tree.delete(row)

        valid_entries = []
        for entry in self.schedule:
            try:
                start = datetime.strptime(entry["start_time"], "%H:%M")
                duration = int(entry["duration"])
                if duration > 0 and 0 <= start.hour < 24:
                    valid_entries.append(entry)
            except (KeyError, TypeError, ValueError):
                continue

        valid_entries.sort(key=lambda item: item["start_time"])
        for index, entry in enumerate(valid_entries):
            start_minutes = self.time_to_minutes(entry["start_time"])
            end_minutes = start_minutes + int(entry["duration"])
            end_display = self.minutes_to_time(end_minutes)
            program = self.find_program(entry.get("program_name", ""))
            category = program.get("category", "Unknown") if program else "Unknown"
            iid = f"schedule_{index}"
            self.schedule_tree.insert(
                "", "end", iid=iid,
                values=(entry["start_time"], entry["program_name"], category,
                        entry["duration"], end_display)
            )

    def refresh_favorites(self):
        if not hasattr(self, "favorites_tree"):
            return
        for row in self.favorites_tree.get_children():
            self.favorites_tree.delete(row)
        for index, name in enumerate(self.favorites):
            program = self.find_program(name)
            category = program.get("category", "Unknown") if program else "Unknown"
            self.favorites_tree.insert("", "end", iid=f"favorite_{index}",
                                       values=(name, category))

    def find_program(self, name):
        for program in self.programs:
            if program["program_name"].casefold() == str(name).casefold():
                return program
        return None

    @staticmethod
    def time_to_minutes(time_text):
        parsed = datetime.strptime(time_text, "%H:%M")
        return parsed.hour * 60 + parsed.minute

    @staticmethod
    def minutes_to_time(total_minutes):
        # A schedule may run past midnight; display the clock time on the next day.
        total_minutes %= 24 * 60
        return f"{total_minutes // 60:02d}:{total_minutes % 60:02d}"

    def add_selected_program_to_favorites(self):
        selected = self.program_tree.selection()
        if not selected:
            messagebox.showinfo("Select a Program", "Select a program in the list first.")
            return
        self.add_favorite(selected[0])

    def add_favorite(self, program_name):
        if not self.find_program(program_name):
            messagebox.showerror("Program Not Found", "That program is not in the catalog.")
            return
        if program_name in self.favorites:
            messagebox.showinfo("Already a Favorite", f"{program_name} is already a favorite.")
            return
        self.favorites.append(program_name)
        self.save_all_data()
        self.refresh_all()
        self.status_var.set(f"Added {program_name} to favorites.")

    def remove_selected_favorite(self):
        selected = self.favorites_tree.selection()
        if not selected:
            messagebox.showinfo("Select a Favorite", "Select a favorite to remove.")
            return
        index = int(selected[0].split("_")[1])
        if 0 <= index < len(self.favorites):
            removed = self.favorites.pop(index)
            self.save_all_data()
            self.refresh_all()
            self.status_var.set(f"Removed {removed} from favorites.")

    def add_to_schedule(self):
        program_name = self.program_choice_var.get().strip()
        start_time = self.start_time_var.get().strip()
        duration_text = self.duration_var.get().strip()

        if not program_name or not self.find_program(program_name):
            messagebox.showerror("Missing Program", "Choose a program from the list.")
            return

        try:
            parsed_time = datetime.strptime(start_time, "%H:%M")
            # strptime can accept some non-zero-padded times; enforce HH:MM format.
            if parsed_time.strftime("%H:%M") != start_time:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid Time", "Enter the start time in 24-hour HH:MM format, such as 09:30."
            )
            return

        try:
            duration = int(duration_text)
            if duration <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Duration", "Duration must be a whole number greater than zero.")
            return

        start_minutes = self.time_to_minutes(start_time)
        end_minutes = start_minutes + duration
        if end_minutes > 24 * 60:
            messagebox.showerror(
                "Invalid Duration",
                "This beginner planner schedules one day at a time. Choose a duration that ends by midnight."
            )
            return

        conflicts = []
        for entry in self.schedule:
            try:
                existing_start = self.time_to_minutes(entry["start_time"])
                existing_end = existing_start + int(entry["duration"])
            except (KeyError, TypeError, ValueError):
                continue
            if start_minutes < existing_end and end_minutes > existing_start:
                conflicts.append(entry)

        if conflicts:
            conflict_names = "\n".join(
                f"• {entry['program_name']} ({entry['start_time']}–"
                f"{self.minutes_to_time(self.time_to_minutes(entry['start_time']) + int(entry['duration']))})"
                for entry in conflicts
            )
            proceed = messagebox.askyesno(
                "Schedule Conflict",
                f"This time overlaps with:\n{conflict_names}\n\nAdd the program anyway?"
            )
            if not proceed:
                self.status_var.set("Schedule entry cancelled because of a conflict.")
                return

        self.schedule.append({
            "program_name": program_name,
            "start_time": start_time,
            "duration": duration
        })
        self.save_all_data()
        self.refresh_all()
        self.status_var.set(f"Scheduled {program_name} at {start_time}.")
        messagebox.showinfo("Program Scheduled", f"{program_name} was added to the schedule.")

    def remove_schedule_entry(self):
        selected = self.schedule_tree.selection()
        if not selected:
            messagebox.showinfo("Select a Program", "Select a schedule entry to remove.")
            return

        # The visible rows are sorted; use the displayed values to identify the entry.
        values = self.schedule_tree.item(selected[0], "values")
        if not values:
            return
        start_time, program_name, _category, duration, _end = values
        for index, entry in enumerate(self.schedule):
            if (entry.get("start_time") == start_time
                    and entry.get("program_name") == program_name
                    and str(entry.get("duration")) == str(duration)):
                del self.schedule[index]
                break

        self.save_all_data()
        self.refresh_all()
        self.status_var.set(f"Removed {program_name} from the schedule.")

    def save_all_data(self):
        schedule_saved = save_json(SCHEDULE_FILE, self.schedule)
        favorites_saved = save_json(FAVORITES_FILE, self.favorites)
        if schedule_saved and favorites_saved:
            self.status_var.set("Schedule and favorites saved.")

    def on_close(self):
        self.save_all_data()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = BroadcastPlannerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()


if __name__ == "__main__":
    main()
