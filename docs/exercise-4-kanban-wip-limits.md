# Exercise 4: Kanban WIP Limits Analysis

## Task Overview
**Project Board:** https://github.com/orgs/iu-data-sci-swe/projects/1

Analyze how the "Limit WIP" (Work In Progress) rule is enforced in this Kanban-themed project board.

---

## What is WIP Limit?

**WIP (Work In Progress) Limit** is a core Kanban principle that restricts the number of items that can be in a particular state (column) at any given time.

### Purpose of WIP Limits:
1. **Prevent multitasking** - Focus on completing work, not starting work
2. **Identify bottlenecks** - Makes flow problems visible
3. **Improve throughput** - Finish items faster
4. **Reduce context switching** - Better focus and quality
5. **Encourage collaboration** - Team swarms on blockers

---

## Kanban WIP Limit Principles

### The Core Rule:
> **"Stop starting, start finishing"**

### How WIP Limits Work:

**Example Kanban Board with WIP Limits:**

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   To Do     │ In Progress │   Review    │    Done     │
│             │   (WIP: 3)  │  (WIP: 2)   │             │
├─────────────┼─────────────┼─────────────┼─────────────┤
│   Item A    │   Item B    │   Item E    │   Item G    │
│   Item C    │   Item D    │   Item F    │   Item H    │
│   Item I    │   Item J    │             │             │
│   Item K    │             │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

**Rules:**
- ✅ "In Progress" has 3 items (at limit)
- ✅ "Review" has 2 items (at limit)
- ❌ Cannot pull Item C into "In Progress" until Item B/D/J moves forward
- ❌ Cannot pull Item E into "Review" until Item F moves to Done

---

## How WIP Limits Are Enforced

### 1. **Visual Enforcement (Manual)**

**Column Headers Show Limits:**
```
In Progress (WIP: 3/5)
```
- Shows current count: 3 items
- Shows limit: maximum 5 items
- Team self-enforces the rule

**Indicators:**
- 🟢 **Green:** Below limit (can add more)
- 🟡 **Yellow:** At limit (no more items)
- 🔴 **Red:** Over limit (violation, remove items)

**Team Discipline:**
- Daily stand-up: Review WIP counts
- Before pulling work: Check if limit allows
- If at limit: Help finish existing work instead of starting new

---

### 2. **Automated Enforcement (Tool-Based)**

**GitHub Projects / Jira / Azure DevOps:**
- **Hard limits:** Tool prevents adding items beyond limit
- **Soft limits:** Warning shown but allows override
- **Notifications:** Alert when approaching limit

**Example Automated Rules:**
```yaml
Rule: "Limit In Progress to 3 items"
- When: User tries to move item to "In Progress"
- If: Column has 3 items already
- Then: Block the move with message "WIP limit reached"
```

---

### 3. **Policy-Based Enforcement**

**Team Agreement:**
- Written Kanban policy document
- Reviewed in retrospectives
- Updated based on team velocity

**Example Policy:**
```
WIP Limits Policy:
- Backlog: No limit (prioritized queue)
- In Progress: 1 item per team member (4 total for 4-person team)
- In Review: 2 items (encourages quick reviews)
- Done: No limit

Exceptions:
- Blockers can exceed WIP if dependencies external
- Urgent production issues bypass WIP limits
- Must be discussed in daily stand-up
```

---

## Analyzing GitHub Project Board WIP Enforcement

### Method 1: Visual Inspection

**Steps to Analyze:**
1. **Count items in each column**
   - How many items in "In Progress"?
   - How many items in "Review"?
   - How many items in "Testing"?

2. **Look for WIP indicators**
   - Are limits shown in column headers?
   - Example: "In Progress (3/5)" or "Review [2]"

3. **Check for violations**
   - Are any columns over-full?
   - Do some columns have zero items (starvation)?

4. **Observe bottlenecks**
   - Which column has the most items?
   - Where is work piling up?

---

### Method 2: Board Configuration

**GitHub Projects Automation:**
Check for automated workflows:
- **Automation rules** that enforce limits
- **Required fields** that affect WIP
- **Status transitions** that check capacity

**Example Automation:**
```
When: Item moves to "In Progress"
If: "In Progress" column has ≥5 items
Then: Auto-move oldest item back to "To Do"
And: Add comment "@team WIP limit exceeded"
```

---

### Method 3: Historical Analysis

**Metrics to Review:**
1. **Cycle Time:** Time from start to done
   - Higher WIP → Longer cycle time
   - Lower WIP → Shorter cycle time

2. **Throughput:** Items completed per week
   - Optimal WIP = Maximum throughput
   - Too high WIP = Lower throughput

3. **Flow Efficiency:** Active time / Total time
   - High WIP = Low efficiency (waiting time)
   - Low WIP = High efficiency (active work)

4. **Lead Time:** Time from request to delivery
   - WIP limits reduce lead time variability

---

## Common WIP Limit Strategies

### Strategy 1: Per-Person Limit
**Rule:** Each team member works on 1-2 items maximum

**Calculation:**
```
WIP Limit = Number of Team Members × 1.5
```
Example: 4 people → WIP limit of 6

**Pros:**
- ✅ Prevents individual overload
- ✅ Easy to understand

**Cons:**
- ❌ Doesn't account for item size
- ❌ Can underutilize team if items blocked

---

### Strategy 2: Per-Column Limit Based on Throughput
**Rule:** Limit = Average throughput × Average cycle time

**Calculation:**
```
Optimal WIP = Throughput × Cycle Time (Little's Law)
```
Example: 
- Throughput: 10 items/week
- Cycle time: 2 days in "In Progress"
- WIP Limit = 10 × (2/7) ≈ 3 items

**Pros:**
- ✅ Data-driven
- ✅ Optimizes flow

**Cons:**
- ❌ Requires historical data
- ❌ Needs regular adjustment

---

### Strategy 3: Pull-Based Constraints
**Rule:** Can only pull when downstream can accept

**Implementation:**
- ❌ Can't pull into "In Progress" if "Review" is full
- ✅ Encourages helping with reviews
- ✅ Creates pull system throughout

**Pros:**
- ✅ Prevents bottleneck overflow
- ✅ Encourages collaboration

**Cons:**
- ❌ Complex coordination
- ❌ Potential idle time if strict

---

## Practical Exercise: Analyzing the Board

### Questions to Ask:

1. **Are WIP limits visible?**
   - Look at column headers
   - Check board settings/automation
   - Review team documentation

2. **What are the current limits?**
   - Backlog: Unlimited?
   - Selected for Development: ?
   - In Progress: ?
   - In Review: ?
   - Done: Unlimited?

3. **Are limits being respected?**
   - Count items in each column
   - Compare to stated limits
   - Check for violations

4. **Where are bottlenecks?**
   - Which column has most items?
   - Where is flow slowest?
   - What's blocking progress?

5. **How is enforcement working?**
   - Manual (team discipline)?
   - Automated (tool enforces)?
   - Policy-based (documented rules)?

---

## Example Analysis Template

**Board:** https://github.com/orgs/iu-data-sci-swe/projects/1

### Column Analysis:

| Column | Item Count | WIP Limit | Status | Notes |
|--------|------------|-----------|--------|-------|
| Backlog | 15 | ∞ | ✅ OK | Prioritized list |
| Ready | 5 | 7 | ✅ OK | Below limit |
| In Progress | 8 | 5 | ❌ OVER | Bottleneck identified |
| In Review | 2 | 3 | ✅ OK | Flowing well |
| Done | 42 | ∞ | ✅ OK | Good throughput |

### Observations:
- **Bottleneck:** "In Progress" column over limit (8 items vs. 5 limit)
- **Root cause:** Team starting too much work
- **Impact:** Lower throughput, longer cycle times
- **Recommendation:** 
  - Stop pulling new work
  - Swarm to complete existing items
  - Pair programming to finish faster
  - Review if limit is too low (may need to increase to 6-7)

---

## WIP Limit Violations and Fixes

### Common Violations:

#### 1. **Starting Too Much Work**
**Problem:** Team pulls items without finishing existing ones

**Fix:**
- ✅ Enforce pull rule: "Finish before starting"
- ✅ Daily WIP count check in stand-up
- ✅ Pair programming to complete items faster

#### 2. **Blocked Items Count Toward WIP**
**Problem:** Blocked items fill up WIP limit

**Fix:**
- ✅ Create separate "Blocked" column (doesn't count toward WIP)
- ✅ Expedite unblocking in daily stand-up
- ✅ Track blocker resolution time

#### 3. **Uneven Distribution**
**Problem:** Some stages always at limit, others empty

**Fix:**
- ✅ Cross-train team members
- ✅ Adjust limits based on capacity
- ✅ Encourage helping upstream/downstream

#### 4. **External Dependencies**
**Problem:** Waiting for external teams

**Fix:**
- ✅ WIP sublimit for "Waiting" items
- ✅ Proactive dependency management
- ✅ Buffer column for dependencies

---

## Benefits of Proper WIP Limits

### 1. **Faster Delivery**
- Items move through system faster
- Less context switching
- Better focus

### 2. **Better Quality**
- More attention per item
- Proper testing and review
- Less rush and errors

### 3. **Predictability**
- Consistent throughput
- Reliable forecasts
- Better planning

### 4. **Team Collaboration**
- Swarm on bottlenecks
- Help each other
- Shared responsibility

### 5. **Continuous Improvement**
- Bottlenecks become visible
- Data-driven adjustments
- Regular retrospective topics

---

## Key Takeaways

### WIP Limits Core Principles:
1. **"Stop Starting, Start Finishing"** - Complete before beginning
2. **Make Work Visible** - Everyone sees the flow
3. **Manage Flow** - Remove bottlenecks
4. **Continuous Improvement** - Adjust limits based on data
5. **Team Ownership** - Self-organizing enforcement

### Enforcement Methods:
- 🔵 **Visual:** Team sees and respects limits
- 🔵 **Automated:** Tools prevent violations
- 🔵 **Policy-Based:** Written rules and team discipline

### Signs WIP Limits Are Working:
✅ Steady throughput  
✅ Predictable cycle times  
✅ Team helps each other  
✅ Bottlenecks identified and resolved  
✅ Less stress and overtime  

### Signs WIP Limits Need Adjustment:
⚠️ Frequent violations  
⚠️ Team idle time  
⚠️ Constant bottlenecks  
⚠️ Decreasing throughput  
⚠️ Team frustration  

**Remember:** WIP limits are not about restricting work, they're about **optimizing flow** and helping teams **finish what they start**.
