"""Temporary CLI demo for the PawPal+ logic layer."""

from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    """Create sample pets and print today's schedule."""
    owner = Owner(name="Jordan")

    mochi = Pet(name="Mochi", species="dog", age=4)
    luna = Pet(name="Luna", species="cat", age=2)

    mochi.add_task(Task(description="Morning walk", time="08:00", frequency="daily"))
    mochi.add_task(Task(description="Dinner feeding", time="18:00", frequency="daily"))
    luna.add_task(Task(description="Give medication", time="09:30", frequency="daily"))

    owner.add_pet(mochi)
    owner.add_pet(luna)

    scheduler = Scheduler(owner)
    print(scheduler.format_schedule())


if __name__ == "__main__":
    main()
