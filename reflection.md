# PawPal+ Project Reflection

## 1. System Design

The three core actions a PawPal+ user should be able to perform are:

- Enter basic owner and pet information so the app knows who the plan is for and what pet care needs to consider.
- Add and edit pet care tasks, including details like duration and priority, so walks, feeding, medication, enrichment, and grooming can be planned.
- Generate and view a daily care plan that fits the available time, respects priorities, and explains why certain tasks were scheduled.

**a. Initial design**

My initial UML design uses four main classes: `Owner`, `Pet`, `CareTask`, and `DailyPlanner`. `Owner` stores the pet owner's name, available care time, preferences, and pets. `Pet` stores the pet's name, species, care notes, and task list. `CareTask` represents one care activity, including its title, duration, priority, and preferred time. `DailyPlanner` is responsible for taking an owner, a pet, and the pet's tasks, then generating a daily care plan that can be explained to the user.

**b. Design changes**

After reviewing the class skeleton, I refined the design by making the relationships visible as attributes: `Owner` now has a `pets` list, and `Pet` now has a `tasks` list. This makes the "owner has pets" and "pet has tasks" relationships easier to represent in code instead of relying only on methods like `add_pet()` and `add_task()`.

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
