from pawpal_system import Pet, Task


def test_task_completion_marks_task_complete():
    task = Task(description="Morning walk", time="08:00", frequency="daily")

    task.mark_complete()

    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    task = Task(description="Dinner feeding", time="18:00", frequency="daily")

    pet.add_task(task)

    assert len(pet.tasks) == 1
