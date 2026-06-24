# PawPal+ Project Reflection

## 1. System Design

The three core actions a PawPal+ user should be able to perform are:

- Enter basic owner and pet information so the app knows who the plan is for and what pet care needs to consider.
- Add and edit pet care tasks, including details like duration and priority, so walks, feeding, medication, enrichment, and grooming can be planned.
- Generate and view a daily care plan that fits the available time, respects priorities, and explains why certain tasks were scheduled.

**a. Initial design**

My initial UML design uses four main classes: `Owner`, `Pet`, `Task`, and `Scheduler`. `Owner` stores the pet owner's name and pets. `Pet` stores the pet's name, species, age, and task list. `Task` represents one care activity, including its description, time, frequency, and completion status. `Scheduler` is responsible for retrieving tasks from the owner, sorting them by time, and formatting a readable daily schedule.

**b. Design changes**

After reviewing and implementing the class skeleton, I refined the design by renaming `CareTask` to `Task` and `DailyPlanner` to `Scheduler` so the class names better match the assignment language. I also made the relationships visible as attributes: `Owner` has a `pets` list, and `Pet` has a `tasks` list. The `Scheduler` retrieves tasks through `Owner.get_all_tasks()`, which keeps schedule-building separate from pet storage.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
