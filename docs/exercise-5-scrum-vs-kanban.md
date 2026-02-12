# Exercise 5: Scrum vs. Kanban - When to Use Which?

## Overview
Analyzing different project scenarios to determine whether Scrum or Kanban is the better fit.

---

## Scrum vs. Kanban Quick Comparison

| Aspect | Scrum | Kanban |
|--------|-------|--------|
| **Cadence** | Fixed sprints (1-4 weeks) | Continuous flow |
| **Roles** | Scrum Master, Product Owner, Dev Team | No prescribed roles |
| **Work Items** | User stories from sprint backlog | Cards from prioritized backlog |
| **Changes** | No changes during sprint | Changes anytime |
| **Commitment** | Team commits to sprint goal | No commitments |
| **Planning** | Sprint planning every sprint | Continuous planning |
| **Delivery** | End of sprint | Continuous delivery |
| **Metrics** | Velocity, burndown | Lead time, cycle time, throughput |
| **Meetings** | Sprint planning, daily stand-up, review, retro | Daily stand-up (optional others) |
| **WIP Limits** | Implicit (sprint backlog size) | Explicit (column limits) |
| **Priorities** | Fixed during sprint | Can change anytime |
| **Best For** | Product development, defined features | Support, maintenance, flow-based work |

---

## Scenario Analysis

### Scenario 1: Developing a New Mobile App with Regular Releases

#### ✅ **RECOMMENDATION: Scrum**

**Why Scrum Wins:**

1. **Clear Release Cadence:**
   - Scrum's time-boxed sprints align with release schedule
   - Sprint review = Release candidate
   - Predictable delivery to app stores
   - Marketing can plan around sprint schedule

2. **Feature-Based Work:**
   - Work is discrete features (login, profile, messaging, etc.)
   - Stories fit well into sprint backlog
   - Features can be demoed at sprint review
   - Product Owner can prioritize features

3. **Need for Planning:**
   - App development requires coordinated features
   - Design, frontend, backend must align
   - Sprint planning ensures team alignment
   - Dependencies managed within sprint

4. **Stakeholder Engagement:**
   - Regular demos (sprint reviews) to stakeholders
   - Feedback incorporated in next sprint
   - Product Owner represents customer needs
   - Clear sprint goals for business value

5. **Team Structure:**
   - Cross-functional team (iOS, Android, backend, design)
   - Team commits to sprint goal together
   - Retrospectives improve process
   - Team velocity stabilizes over time

**Scrum Implementation:**
```
Sprint Length: 2 weeks
Sprint Planning: 4 hours (2-week sprint)
Daily Stand-up: 15 minutes
Sprint Review: 2 hours (demo to stakeholders)
Retrospective: 1.5 hours

Sprint 1: User authentication and onboarding
Sprint 2: Core feature - Activity tracking
Sprint 3: Data visualization and reports
Sprint 4: Social features and sharing
Sprint 5: Performance optimization and polish
Sprint 6: Release to app stores
```

**Why Not Kanban:**
- ❌ Need coordinated releases (not continuous)
- ❌ Features have dependencies requiring planning
- ❌ Stakeholders expect regular demos
- ❌ Marketing needs predictable release dates

**Verdict:** ✅ **Scrum** - Structured sprints support planned releases and feature development.

---

### Scenario 2: IT Service Desk Handling Support Tickets

#### ✅ **RECOMMENDATION: Kanban**

**Why Kanban Wins:**

1. **Continuous Flow:**
   - Tickets arrive unpredictably throughout the day
   - No natural "sprint" boundary
   - Work must start immediately when tickets arrive
   - Cannot wait for sprint planning

2. **Variable Work Items:**
   - Tickets range from 5 minutes to days
   - Cannot estimate all tickets upfront
   - Priorities change constantly
   - Urgent issues must jump the queue

3. **No Fixed Commitment:**
   - Cannot commit to "sprint goal" with unpredictable work
   - Team responds to what comes in
   - SLA-driven (not feature-driven)
   - Must be flexible to handle critical issues

4. **WIP Limits Critical:**
   - Limit concurrent tickets per person (prevent overload)
   - Focus on resolving tickets, not starting more
   - Clear visualization of bottlenecks
   - Swarm on aged tickets

5. **Metrics Focus:**
   - **Lead time:** Time from ticket creation to resolution
   - **Cycle time:** Time spent actively working
   - **Throughput:** Tickets resolved per day
   - **SLA compliance:** % resolved within target time

**Kanban Implementation:**
```
Board Columns:
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│ Backlog  │ Triaged  │   Doing  │ Waiting  │   Done   │
│ (no lim) │ (WIP: 10)│ (WIP: 5) │ (WIP: 3) │ (no lim) │
└──────────┴──────────┴──────────┴──────────┴──────────┘

Priority Swimlanes:
- P0 (Critical): Max 1 hour response
- P1 (High): Same day
- P2 (Medium): Within 3 days
- P3 (Low): Best effort

Pull Rules:
1. Always pull from highest priority available
2. Can only pull if under WIP limit
3. Must move ticket forward before pulling new
4. Blocked tickets move to "Waiting"

Daily Stand-up:
- Focus on aged tickets
- Identify blockers
- Swarm on SLA risks
```

**Why Not Scrum:**
- ❌ Cannot plan "sprint backlog" with unpredictable tickets
- ❌ Sprint commitment meaningless with changing priorities
- ❌ Sprint review doesn't apply (no demo-able features)
- ❌ Fixed sprint length doesn't match ticket flow
- ❌ Velocity metric not useful for support tickets

**Kanban Advantages:**
- ✅ Immediate response to urgent issues
- ✅ Flexible prioritization
- ✅ Visual flow of work
- ✅ WIP limits prevent overload
- ✅ Continuous delivery (no waiting for sprint end)
- ✅ Metrics aligned with support goals (SLA compliance)

**Verdict:** ✅ **Kanban** - Continuous flow matches unpredictable support work.

---

### Scenario 3: Creating a Smart Home Device with Customer Feedback

#### ✅ **RECOMMENDATION: Scrum**

**Why Scrum Wins:**

1. **Iterative Product Development:**
   - Build MVP, get feedback, iterate
   - Beta testing between sprints
   - Customer feedback incorporated in next sprint
   - Product evolves based on learnings

2. **Regular Customer Engagement:**
   - Sprint review includes customer demos
   - Customer feedback shapes product backlog
   - Product Owner represents customer voice
   - Frequent touchpoints build customer confidence

3. **Feature-Based Development:**
   - Clear features to develop (motion detection, app control, scheduling)
   - Features can be prioritized by customer value
   - Each sprint delivers increment of functionality
   - MVP to full product over multiple sprints

4. **Cross-Functional Coordination:**
   - Hardware, firmware, app, cloud backend must align
   - Sprint planning coordinates all disciplines
   - Sprint goal unifies team efforts
   - Dependencies managed within sprint

5. **Learning and Adaptation:**
   - Retrospectives crucial for hardware-software learnings
   - Sprint reviews gather customer feedback
   - Adjust priorities based on real usage
   - Experiment with features in time-boxed sprints

**Scrum Implementation:**
```
Sprint 0 (2 weeks): 
- Research and prototyping
- Customer interviews
- Define MVP features

Sprint 1-2 (4 weeks):
- Basic hardware prototype
- Simple app (on/off control)
- Demo to pilot customers

Sprint 3-4 (4 weeks):
- Refined hardware
- Scheduling features in app
- Beta test with 10 customers
- Incorporate feedback

Sprint 5-6 (4 weeks):
- Advanced features (scenes, automation)
- Cloud integration
- Expanded beta (50 customers)

Sprint 7-8 (4 weeks):
- Polish and optimization
- Customer onboarding flow
- Prepare for production

Release: After Sprint 8 with manufacturing
```

**Customer Feedback Integration:**
- Sprint Review: Demo to customer advisory board
- Mid-sprint: Customer surveys and usage data
- Product Backlog: Prioritized by customer feedback
- Each sprint: Incorporate top 3 customer requests

**Why Not Kanban:**
- ❌ Need coordinated development across hardware/software
- ❌ Customer feedback cycles match sprint cadence
- ❌ Product development has natural phases
- ❌ Need planning to manage dependencies
- ❌ Value in team commitment to sprint goal

**Verdict:** ✅ **Scrum** - Iterative development with regular customer feedback loops.

---

### Scenario 4: DevOps Team Maintaining Infrastructure

#### ✅ **RECOMMENDATION: Kanban**

**Why Kanban Wins:**

1. **Reactive and Proactive Mix:**
   - Incidents (reactive, urgent)
   - Maintenance tasks (planned)
   - Improvements (when time allows)
   - Security patches (time-sensitive)
   - All need different handling

2. **Unpredictable Work Arrival:**
   - Infrastructure issues arise anytime
   - Cannot wait for sprint planning
   - Priorities shift based on criticality
   - Must respond immediately to outages

3. **Variable Work Duration:**
   - Incidents: Minutes to hours
   - Maintenance: Days
   - Major upgrades: Weeks
   - Cannot estimate uniformly

4. **Continuous Delivery:**
   - Infrastructure changes deployed continuously
   - No "sprint release"
   - Rolling updates and blue-green deployments
   - Cannot batch changes

5. **Service-Level Focus:**
   - SLAs for uptime and response time
   - Metrics: MTTR (Mean Time To Repair)
   - Availability targets (99.9%)
   - Not feature-driven

**Kanban Implementation:**
```
Board Columns:
┌────────────┬───────────┬────────────┬────────────┬───────┐
│  Backlog   │  Ready    │ In Progress│  Review    │ Done  │
│  (no lim)  │ (WIP: 8)  │  (WIP: 4)  │  (WIP: 2)  │       │
└────────────┴───────────┴────────────┴────────────┴───────┘

Swimlanes by Type:
┌─ Incidents (P0)     ─ [No WIP limit - always take]
├─ Urgent Changes (P1) ─ [High priority]  
├─ Planned Maintenance ─ [Pull when capacity]
└─ Improvements       ─ [Fill available capacity]

Service Classes:
- Incidents: Start immediately, no WIP limit
- Security patches: Next available capacity
- Planned work: Scheduled, can be delayed
- Improvements: Fill available time

Pull Policies:
1. Incidents always interrupt
2. Pull from highest priority non-incident
3. Limit non-incident WIP (allow focus)
4. Use "slack time" for improvements
```

**Metrics Dashboard:**
```
Key Metrics:
- Incident response time (target: <15 min)
- MTTR (target: <1 hour)
- System uptime (target: 99.9%)
- Lead time for changes (track trend)
- Number of deployments per week
- Failed deployment rate (target: <5%)

Kanban Metrics:
- Cycle time by work type
- Throughput (items/week)
- WIP distribution
- Blocker frequency and duration
```

**Why Not Scrum:**
- ❌ Cannot commit to "sprint goal" with incidents
- ❌ Sprint boundaries meaningless for infrastructure
- ❌ Fixed sprint planning doesn't fit interrupt-driven work
- ❌ "Sprint review" doesn't apply (no features to demo)
- ❌ Velocity not useful metric for DevOps
- ❌ Infrastructure work is continuous, not project-based

**Kanban Advantages:**
- ✅ Handles interrupts gracefully
- ✅ Flexible prioritization
- ✅ Visual work distribution
- ✅ Balance reactive and proactive work
- ✅ Continuous flow matches continuous operations

**Verdict:** ✅ **Kanban** - Interrupt-driven operational work needs flow-based approach.

---

### Scenario 5: Data Science Team Answering Ad-Hoc Questions

#### ✅ **RECOMMENDATION: Kanban** (with consideration for Scrum for major projects)

**Why Kanban Wins:**

1. **Unpredictable Requests:**
   - Business questions arrive continuously
   - Cannot predict all questions in sprint planning
   - Urgency varies (CEO question vs. nice-to-know)
   - Some questions quick (hours), others extended (weeks)

2. **Research Nature:**
   - Don't know effort until you start exploring
   - Estimation highly uncertain
   - May discover question unanswerable
   - Frequent pivots based on findings

3. **Variable Scope:**
   - Simple SQL query (30 min)
   - Exploratory analysis (2 days)
   - New model development (2 weeks)
   - Dashboard creation (1 week)

4. **Stakeholder-Driven Priorities:**
   - Business priority changes based on decisions
   - High-priority requests must jump queue
   - Cannot commit to "sprint backlog" that may become irrelevant
   - Flexibility essential

5. **Continuous Delivery:**
   - Insights delivered as ready
   - No natural "sprint release"
   - Stakeholders need answers ASAP
   - Cannot wait for sprint end

**Kanban Implementation:**
```
Board Columns:
┌───────────┬──────────┬──────────┬──────────┬──────────┐
│ Requests  │Clarifying│  Doing   │ Review   │Delivered │
│ (no lim)  │ (WIP: 5) │ (WIP: 3) │ (WIP: 2) │          │
└───────────┴──────────┴──────────┴──────────┴──────────┘

Types of Work:
🔴 Urgent (24-48 hours): Executive requests
🟡 Standard (1 week): Regular business questions  
🟢 Research (2-4 weeks): Exploratory projects
🔵 Infrastructure: Pipeline/dashboard maintenance

Size T-shirt Estimation:
- XS (< 4 hours): Quick query/report
- S (1-2 days): Analysis with existing data
- M (3-5 days): New analysis method
- L (1-2 weeks): Dashboard or new model
- XL (> 2 weeks): Split into smaller questions

Intake Process:
1. Question submitted with business context
2. Data scientist clarifies requirements
3. Estimate size and priority
4. Add to appropriate swimlane
5. Pull when capacity available
```

**Hybrid Approach for Major Projects:**
If data science team has **major model development** (multi-week projects), consider:

**Kanban for Ad-Hoc + Scrum for Projects:**
```
Team Split:
- 70% capacity: Kanban for ad-hoc questions
- 30% capacity: Scrum for major project

Example:
- 5 data scientists total
- 3-4 working on Kanban queue (ad-hoc)
- 1-2 working on Scrum project (new fraud model)
- Rotate quarterly to avoid siloing
```

**Or Pure Kanban with Expedite Lane:**
```
Swimlanes:
┌─ Expedite (urgent questions)  ─ WIP: 1, 24-hour SLA
├─ Standard (regular questions) ─ WIP: 3, 1-week SLA  
├─ Projects (major work)        ─ WIP: 1, multi-sprint
└─ Maintenance (infrastructure) ─ WIP: 1, ongoing
```

**Why Kanban Over Scrum:**
- ❌ Cannot plan sprint with unpredictable questions
- ❌ "Sprint commitment" broken by urgent requests
- ❌ Velocity meaningless with variable work sizes
- ❌ Sprint boundaries break flow of long analyses
- ✅ Kanban's continuous flow matches question arrival
- ✅ WIP limits prevent overcommitment
- ✅ Expedite lane for urgent requests
- ✅ Flexible prioritization by business value

**When to Consider Scrum Instead:**
- ✅ Team works primarily on long-term models/dashboards
- ✅ Ad-hoc requests < 20% of work
- ✅ Stakeholders accept sprint-boundary delays
- ✅ Work is project-like with defined features

**Verdict:** ✅ **Kanban preferred** - Ad-hoc nature benefits from flow. Consider hybrid for major projects.

---

### Scenario 6: Building a SaaS Product with Feature Roadmap

#### ✅ **RECOMMENDATION: Scrum**

**Why Scrum Wins:**

1. **Product Roadmap:**
   - Features planned quarters ahead
   - Roadmap communicated to customers
   - Sales needs predictable delivery dates
   - Marketing campaigns aligned with releases

2. **Regular Releases:**
   - Monthly or quarterly feature releases
   - Release notes for customers
   - Coordinated go-to-market strategy
   - Scrum sprints align with release cadence

3. **Feature-Based Work:**
   - Clear user stories (new feature, improvements)
   - Features can be estimated and prioritized
   - Product Owner prioritizes by business value
   - Sprint delivers shippable increment

4. **Cross-Functional Coordination:**
   - Frontend, backend, DevOps, QA must align
   - Sprint planning coordinates all teams
   - Sprint goal unifies team efforts
   - Dependencies managed within sprint or across sprints

5. **Stakeholder Communication:**
   - Sprint review demos to internal stakeholders
   - Product Owner represents customer needs
   - Regular feedback from sales/support
   - Clear progress tracking for leadership

**Scrum Implementation:**
```
Sprint Length: 2 weeks
Release Cadence: Every 4 sprints (8 weeks)

Sprint 1-2: Customer-requested feature A
Sprint 3-4: Platform improvement (performance)
Sprint 5-6: Customer-requested feature B  
Sprint 7-8: Bug fixes and polish
→ Release 1.5

Sprint 9-10: Enterprise feature (SSO)
Sprint 11-12: Analytics dashboard
Sprint 13-14: API improvements
Sprint 15-16: Polish and documentation
→ Release 1.6

Ceremonies:
- Sprint Planning: 4 hours every 2 weeks
- Daily Stand-up: 15 min (video call)
- Sprint Review: 2 hours (demo to company)
- Retrospective: 1.5 hours (continuous improvement)
- Backlog Refinement: 2 hours mid-sprint
```

**Product Backlog Management:**
```
Prioritization:
1. Customer-critical (P0): Blockers, security
2. High-value features (P1): Requested by multiple customers
3. Platform improvements (P2): Technical debt, performance
4. Nice-to-have (P3): Low-priority requests

Product Owner:
- Maintains product roadmap (6-month outlook)
- Prioritizes backlog by business value
- Balances customer requests vs. technical needs
- Communicates with sales and support

Development Team:
- Estimates stories during refinement
- Commits to realistic sprint goals
- Delivers potentially shippable increment
- Velocity: 40-50 story points per sprint (stabilized)
```

**Why Not Kanban:**
- ❌ Roadmap and releases need planned delivery
- ❌ Stakeholders expect predictable feature delivery
- ❌ Cross-team coordination benefits from sprint planning
- ❌ Marketing and sales need release dates
- ❌ Feature work fits well into sprints

**Scrum Advantages:**
- ✅ Predictable delivery for roadmap
- ✅ clear sprint goals align team
- ✅ Regular demos to stakeholders
- ✅ Velocity for forecasting future sprints
- ✅ retrospectives drive continuous improvement
- ✅ sprint boundaries create natural release points

**Hybrid Consideration:**
For mature SaaS with **continuous deployment**:
```
Scrumban:
- Scrum ceremonies (planning, review, retro)
- Kanban board for visualization
- WIP limits within sprint
- Continuous deployment (not waiting for sprint end)
- Features released when ready, not sprint boundaries
```

**Verdict:** ✅ **Scrum** - Product development with roadmap benefits from structured sprints and planning.

---

## Summary: Decision Matrix

| Scenario | Recommendation | Key Reason |
|----------|----------------|------------|
| **Mobile app development** | ✅ Scrum | Planned releases, feature-based, coordinated team |
| **IT service desk** | ✅ Kanban | Unpredictable tickets, continuous flow, SLA-driven |
| **Smart home device** | ✅ Scrum | Customer feedback cycles, iterative development |
| **DevOps infrastructure** | ✅ Kanban | Interrupt-driven, operational work, no sprints |
| **Data science ad-hoc** | ✅ Kanban | Unpredictable requests, variable scope, research |
| **SaaS product** | ✅ Scrum | Roadmap-driven, regular releases, feature-based |

---

## Decision Framework

### Choose **Scrum** when:
✅ Work is **project-based** or **feature-based**  
✅ Need **predictable delivery** dates  
✅ Stakeholders expect **regular demos**  
✅ Team can **commit to sprint goals**  
✅ Work has **natural planning boundaries**  
✅ Cross-functional **coordination** required  
✅ **Roadmap or release schedule** exists  
✅ Team benefits from **regular retrospectives**  

### Choose **Kanban** when:
✅ Work is **operational** or **support-based**  
✅ Requests arrive **unpredictably**  
✅ Priorities **change frequently**  
✅ Work items have **highly variable size**  
✅ **Continuous delivery** is the norm  
✅ SLA or **response time** is key metric  
✅ Team handles **interrupts** regularly  
✅ **Flow optimization** is priority  

### Consider **Hybrid (Scrumban)** when:
⚠️ Mix of **planned features** and **reactive work**  
⚠️ Want Scrum **structure** with Kanban **flexibility**  
⚠️ **Continuous deployment** but regular planning needed  
⚠️ Team needs **both** sprint goals and WIP limits  

---

## Key Takeaways

### Scrum Strengths:
- 📅 **Predictability:** Fixed sprints, regular releases
- 🎯 **Focus:** Sprint goal aligns team
- 📊 **Metrics:** Velocity for forecasting
- 🔄 **Improvement:** Retrospectives drive change
- 👥 **Roles:** Clear responsibilities (PO, SM, Dev Team)

### Kanban Strengths:
- 🔀 **Flexibility:** Priorities change anytime
- 📈 **Flow:** Optimize throughput and lead time
- 🚦 **WIP Limits:** Prevent overload
- ⚡ **Responsiveness:** Handle interrupts gracefully
- 📉 **Simplicity:** Less ceremony, more flow

### The Right Answer:
**There is no "one size fits all"**
- Context matters
- Team maturity matters
- Organizational culture matters  
- Type of work matters most

**Start with one, adapt later:**
- Begin with Scrum (more structure for learning)
- Or Kanban (simpler, fewer roles)
- Evolve to hybrid as team matures
- Regularly retrospect and adjust

**Remember the Agile Manifesto:**
> "Individuals and interactions over processes and tools"

Choose the approach that helps your **team deliver value**, not the one that fits a textbook definition.
