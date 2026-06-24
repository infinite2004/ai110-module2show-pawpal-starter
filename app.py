import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task


def task_rows(owner: Owner) -> list[dict[str, str]]:
    """Build table rows for every task owned by every pet."""
    rows = []
    for pet, task in owner.get_all_tasks():
        rows.append(
            {
                "Time": task.time,
                "Pet": pet.name,
                "Species": pet.species,
                "Task": task.description,
                "Frequency": task.frequency,
                "Status": task.display_status(),
            }
        )
    return rows


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

owner = st.session_state.owner

st.title("🐾 PawPal+")

st.markdown(
    """
PawPal+ helps a pet owner keep track of care tasks and build a simple daily schedule.
"""
)

with st.expander("Scenario", expanded=False):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

st.divider()

st.subheader("Owner")
owner_name = st.text_input("Owner name", value=owner.name)
owner.name = owner_name.strip() or "Unnamed owner"

st.divider()

st.subheader("Pets")

with st.form("add_pet_form", clear_on_submit=True):
    pet_name = st.text_input("Pet name", placeholder="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Age", min_value=0, max_value=40, value=1)
    submitted_pet = st.form_submit_button("Add pet")

if submitted_pet:
    if pet_name.strip():
        owner.add_pet(Pet(name=pet_name.strip(), species=species, age=int(age)))
        st.success(f"Added {pet_name.strip()} to {owner.name}'s pets.")
    else:
        st.error("Enter a pet name before adding a pet.")

if owner.get_pets():
    st.write("Current pets:")
    st.table(
        [
            {"Name": pet.name, "Species": pet.species, "Age": pet.age}
            for pet in owner.get_pets()
        ]
    )
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Tasks")

if owner.get_pets():
    pet_options = {pet.name: pet for pet in owner.get_pets()}

    with st.form("add_task_form", clear_on_submit=True):
        selected_pet_name = st.selectbox("Pet", list(pet_options.keys()))
        description = st.text_input("Task description", placeholder="Morning walk")
        task_time = st.time_input("Time")
        frequency = st.selectbox("Frequency", ["daily", "weekly", "as needed"])
        submitted_task = st.form_submit_button("Add task")

    if submitted_task:
        if description.strip():
            selected_pet = pet_options[selected_pet_name]
            selected_pet.add_task(
                Task(
                    description=description.strip(),
                    time=task_time.strftime("%H:%M"),
                    frequency=frequency,
                )
            )
            st.success(f"Added task for {selected_pet.name}.")
        else:
            st.error("Enter a task description before adding a task.")

    rows = task_rows(owner)
    if rows:
        st.write("Current tasks:")
        st.table(rows)
    else:
        st.info("No tasks yet. Add one above.")
else:
    st.info("Add a pet before scheduling tasks.")

st.divider()

st.subheader("Today's Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner)
    schedule = scheduler.build_schedule()

    if schedule:
        for pet, task in schedule:
            st.write(
                f"**{task.time}** | {pet.name} ({pet.species}) | "
                f"{task.description} [{task.frequency}, {task.display_status()}]"
            )
    else:
        st.warning("No tasks are available to schedule yet.")
