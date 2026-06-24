"""Core logic classes for the PawPal+ pet care planner."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Task:
    """Represents one pet care activity."""

    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark this task as not completed."""
        self.completed = False

    def display_status(self) -> str:
        """Return a readable completion status."""
        if self.completed:
            return "complete"
        return "pending"


@dataclass
class Pet:
    """Stores pet details and that pet's care tasks."""

    name: str
    species: str
    age: int | None = None
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> list[Task]:
        """Return all tasks assigned to this pet."""
        return self.tasks


@dataclass
class Owner:
    """Manages pets and provides access to their tasks."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_pets(self) -> list[Pet]:
        """Return all pets managed by this owner."""
        return self.pets

    def get_all_tasks(self) -> list[tuple[Pet, Task]]:
        """Return every task grouped with the pet it belongs to."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet, task))
        return all_tasks


@dataclass
class Scheduler:
    """Retrieves, organizes, and formats tasks across an owner's pets."""

    owner: Owner

    def get_todays_tasks(self) -> list[tuple[Pet, Task]]:
        """Return all tasks scheduled for today."""
        return self.owner.get_all_tasks()

    def sort_tasks_by_time(self, tasks: list[tuple[Pet, Task]]) -> list[tuple[Pet, Task]]:
        """Sort task entries by their time value."""
        return sorted(tasks, key=lambda entry: entry[1].time)

    def build_schedule(self) -> list[tuple[Pet, Task]]:
        """Build today's schedule in chronological order."""
        return self.sort_tasks_by_time(self.get_todays_tasks())

    def format_schedule(self) -> str:
        """Format today's schedule for terminal output."""
        schedule = self.build_schedule()
        lines = ["Today's Schedule", "----------------"]

        if not schedule:
            lines.append("No tasks scheduled.")
            return "\n".join(lines)

        for pet, task in schedule:
            lines.append(
                f"{task.time} | {pet.name} ({pet.species}) | "
                f"{task.description} [{task.frequency}, {task.display_status()}]"
            )

        return "\n".join(lines)
