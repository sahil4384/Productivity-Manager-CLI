import json

from datetime import date

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()




def main():
    while True:
        console.clear()
        data = load_data()

        console.print(Panel.fit("[bold cyan]📈 PRODUCTIVITY MANAGER[/bold cyan]\n[italic]Your Personal Productivity Toolkit[/italic]", padding=(1, 6), border_style="bright_cyan"))
        console.print()

        console.print("1️⃣  [bold]Tasks List[/bold]")
        console.print("2️⃣  [bold]Habit Tracker[/bold]")
        console.print("3️⃣  [bold red]Exit[/bold red]")
        console.rule("[bold blue]Menu[/bold blue]")

        console.print("[dim]Use numbers (1-3) to navigate.[/dim]\n")
        choice = console.input("[bold green]➡️ Choose an option:[/bold green] ")

        if choice == "1":
            handle_task(data)
        elif choice == "2":
            handle_habit(data)
        elif choice == "3":
            console.print("[bold yellow]👋 Goodbye![/bold yellow]\n")
            break
        else:
            console.print("[bold red]Invalid option. Try again.[/bold red]\n")








def load_data():
    try:
        with open("project_data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {
                "tasks": [],
                "habits": []
                }



def save_data(data, filename="project_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)




def handle_task(data):
    console.clear()
    while True:

        console.print(Panel.fit("[bold yellow]🗒️ TASKS LIST[/bold yellow]", border_style="yellow"))
        console.print("1️⃣  [bold]View Tasks[/bold]")
        console.print("2️⃣  [bold]Add a Task[/bold]")
        console.print("3️⃣  [bold]Remove a Completed Task[/bold]")
        console.print("4️⃣  [bold red]Back to Main Menu[/bold red]")
        console.rule("[bold blue]Task Options[/bold blue]")

        console.print("[dim]Use numbers (1-4) to navigate.[/dim]\n")
        option = console.input("[bold green]➡️ Choose an option:[/bold green] ")

        if option == "1":
            console.clear()
            if not data["tasks"]:
                console.print("[bold red]❌ No tasks available.[/bold red]")
            else:
                table = Table(title="📋 Your Tasks", header_style="bold magenta")
                table.add_column("No.", justify="center", style="cyan", no_wrap=True)
                table.add_column("Task", style="yellow", overflow="fold")

                for i, task in enumerate(data["tasks"], 1):
                    table.add_row(str(i), task)

                console.print(table)
                console.print(f"\n\n")


        elif option == "2":
            console.clear()
            task = console.input("\n[bold green]📝 Enter the new task:[/bold green] ")
            data["tasks"].append(task)
            save_data(data)
            console.print("\n[bold green]✅ Task added successfully![/bold green]")
            console.print(f'\n\n')

        elif option == "3":
            console.clear()
            for i, task in enumerate(data["tasks"]):
                console.print(f"[{i+1}] [yellow]{task}[/yellow]")
            try:
                index = int(console.input("\n[bold green]✅ Enter the index of completed task:[/bold green] "))
            except ValueError:
                continue
            index -= 1
            if 0 <= index < len(data["tasks"]):
                data["tasks"].pop(index)
                save_data(data)
                console.print("\n[bold green]🗑️ Task deleted successfully![/bold green]")
                console.print(f'\n\n')
            else:
                console.print("[bold red]⚠️ Invalid index![/bold red]")
                console.print(f'\n\n')

        elif option == "4":
            break

        else:
            console.clear()
            console.print("[bold red]⚠️ Invalid option. Try again.[/bold red]")








def handle_habit(data):
    console.clear()
    while True:
        console.print(Panel.fit("[bold magenta]🔥 HABIT TRACKER[/bold magenta]", border_style="magenta"))
        console.print("1️⃣  [bold]View Habits[/bold]")
        console.print("2️⃣  [bold]Add a Habit[/bold]")
        console.print("3️⃣  [bold]Log Today's Habit[/bold]")
        console.print("4️⃣  [bold]Remove a Habit[/bold]")
        console.print("5️⃣  [bold]View Habit Logs[/bold]")
        console.print("6️⃣  [bold red]Back to Main Menu[/bold red]")
        console.rule("[bold magenta]Habit Options[/bold magenta]")

        console.print("[dim]Use numbers (1-6) to navigate.[/dim]\n")
        choice = console.input("[bold green]➡️ Choose an option:[/bold green] ")

        if choice == "1":
            console.clear()
            if not data["habits"]:
                console.print("[bold red]❌ No habits added yet![/bold red]")

            else:
                table = Table(title="💪 Your Habits", header_style="bold magenta")
                table.add_column("No.", justify="center", style="cyan")
                table.add_column("Habit", style="yellow")
                table.add_column("Days Logged", justify="center", style="green")
                for i, habit in enumerate(data["habits"], 1):
                    table.add_row(str(i), habit["name"], str(len(habit["log"])))

                console.print(table)
                console.print(f"\n\n")

        elif choice == "2":
            console.clear()
            habit_name = console.input("\n[bold green]➕ Enter the new habit name:[/bold green] ")
            exists = False
            for habits in data["habits"]:
                if habits["name"].lower() == habit_name.lower():
                    exists = True
                    break
            if exists:
                console.print("\n[bold red]⚠️ Habit already exists![/bold red]")
                console.print(f'\n\n')
            else:
                habit = {"name": habit_name, "log": []}
                data["habits"].append(habit)
                save_data(data)
                console.print("\n[bold green]✅ Habit added successfully![/bold green]")
                console.print(f'\n\n')


        elif choice == "3":
            console.clear()
            today = str(date.today())
            if not data["habits"]:
                console.print("[bold red]❌ No habits to log! Add one first.[/bold red]")
                console.print(f'\n\n')
                continue

            table = Table(title="📅 Log Habit", header_style="bold magenta")
            table.add_column("No.", justify="center", style="cyan")
            table.add_column("Habit", style="yellow")
            for i, habit in enumerate(data["habits"], 1):
                table.add_row(str(i), habit["name"])
            console.print(table)
            console.print(f"\n\n")


            try:
                index = int(console.input("\n[bold green]📌 Which habit did you complete today: [/bold green]")) - 1
            except ValueError:
                continue
            if not 0 <= index < len(data["habits"]):
                console.print("[bold red]⚠️ Invalid index![/bold red]")
                console.print(f'\n\n')
                continue

            temp = data["habits"][index]
            if today in temp["log"]:
                console.print("[bold yellow]⚠️ Already logged today.[/bold yellow]")
                console.print(f'\n\n')
            else:
                temp["log"].append(today)
                save_data(data)
                console.print("[bold green]✅ Logged successfully for today![/bold green]")
                console.print(f'\n\n')


        elif choice == "4":
            console.clear()
            if not data["habits"]:
                console.print("[bold red]❌ No habits to remove![/bold red]")
                continue

            console.print("\n[bold underline cyan]🗑️ Choose a Habit to Remove:[/bold underline cyan]")
            for i, habit in enumerate(data["habits"], 1):
                console.print(f"[{i}] [green]{habit['name']}[/green]")

            try:
                index = int(console.input("\n[bold yellow]Select habit number to remove: [/bold yellow]")) - 1
                removed = data["habits"].pop(index)
                save_data(data)
                console.print(f"[bold green]✅ Removed habit:[/bold green] [yellow]{removed['name']}[/yellow]")
                console.print(f'\n\n')

            except (ValueError, IndexError):
                console.print("[bold red]⚠️ Invalid selection. No habit removed.[/bold red]")
                console.print(f'\n\n')



        elif choice == "5":
            console.clear()

            if not data["habits"]:
                console.print("[bold red]❌ No habits added yet![/bold red]")
                console.print(f'\n\n')
                continue

            console.print("\n[bold underline cyan]📋 Available Habits:[/bold underline cyan]")
            for i, habit in enumerate(data["habits"], 1):
                console.print(f"[{i}] [green]{habit['name']}[/green]")


            try:
                index = int(console.input("\n[bold yellow]📌 Select a habit by number: [/bold yellow]")) - 1
                temp = data["habits"][index]
            except (ValueError, IndexError):
                console.print("[bold red]⚠️ Invalid selection.[/bold red]")
                console.print(f'\n\n')
                continue

            option = console.input("[bold blue]📊 View by 'dates' or 'days'? [/bold blue]").strip().lower()

            if option.lower() == "days":
                console.print(f"\n[bold green]✅ Total days logged: {len(temp['log'])}[/bold green]")
            elif option.lower() == "dates":
                console.print(f"\n[bold cyan]📅 Logged Dates for [green]{temp['name']}[/green]:[/bold cyan]\n")
                if not temp["log"]:
                    console.print("[italic]No entries yet.[/italic]")
                else:
                    for log_date in temp["log"]:
                        console.print(f"• [yellow]{log_date}[/yellow]")
                    console.print(f'\n\n')

        elif choice == "6":
            break

        else:
            console.clear()
            console.print("[bold red]⚠️ Invalid option. Try again.[/bold red]")
            console.print(f'\n\n')



if __name__ == "__main__":
    main()
