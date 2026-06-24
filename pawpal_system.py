"""Core PawPal+ classes.

This module is the backend logic layer for the PawPal+ Streamlit app.
The classes are skeletons based on the draft UML and will be filled in
during the scheduling implementation phase.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class CareTask:
    """A single pet care task that may be included in a daily plan."""

    title: str
    duration_minutes: int
    priority: str
    preferred_time: str = ""

    def update_details(
        self, title: str, duration_minutes: int, priority: str, preferred_time: str = ""
    ) -> None:
        """Update the task's editable details."""
        raise NotImplementedError

    def priority_score(self) -> int:
        """Convert the priority label into a sortable score."""
        raise NotImplementedError


@dataclass
class Pet:
    """A pet with basic profile details and care tasks."""

    name: str
    species: str
    care_notes: str = ""
    tasks: list[CareTask] = field(default_factory=list)

    def add_task(self, task: CareTask) -> None:
        """Add a care task for this pet."""
        raise NotImplementedError

    def get_tasks(self) -> list[CareTask]:
        """Return this pet's care tasks."""
        raise NotImplementedError


@dataclass
class Owner:
    """A pet owner with availability, preferences, and pets."""

    name: str
    available_minutes: int
    preferences: str = ""
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's profile."""
        raise NotImplementedError

    def update_availability(self, minutes: int) -> None:
        """Update how many minutes the owner has available for pet care today."""
        raise NotImplementedError


@dataclass
class DailyPlanner:
    """Builds and explains a daily pet care plan."""

    plan_date: date
    scheduled_tasks: list[CareTask] = field(default_factory=list)

    def generate_plan(self, owner: Owner, pet: Pet) -> list[CareTask]:
        """Generate a daily schedule using owner constraints and pet tasks."""
        raise NotImplementedError

    def sort_tasks_by_priority(self, tasks: list[CareTask]) -> list[CareTask]:
        """Sort tasks so more important care appears earlier in the plan."""
        raise NotImplementedError

    def explain_plan(self) -> str:
        """Explain why the current daily plan was selected."""
        raise NotImplementedError
