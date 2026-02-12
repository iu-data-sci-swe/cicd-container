# Exercise 1: GitHub Project Board - Sprint Planning

## Task Overview
**Project Board:** https://github.com/orgs/iu-data-sci-swe/projects/2

## Activities
1. **Fill backlog** based on Model Development Lifecycle
2. **Prioritize** items
3. **Estimate** story points
4. **Sprint planning** (today's session only)
5. **Complete tasks** with peer review
6. **Observe workflow** through the board

---

## Model Development Lifecycle Phases

### 1. Problem Definition & Planning
**User Stories:**
- As a data scientist, I want to understand the business problem so that I can define appropriate ML objectives
- As a product owner, I want to define success metrics so that we can measure model performance
- As a team, we want to identify stakeholders so that we understand requirements

### 2. Data Collection & Preparation
**User Stories:**
- As a data engineer, I want to identify data sources so that we have training data
- As a data scientist, I want to perform data quality checks so that we work with clean data
- As an ML engineer, I want to set up data pipelines so that data is automatically collected
- As a data scientist, I want to perform exploratory data analysis so that I understand patterns

### 3. Feature Engineering
**User Stories:**
- As a data scientist, I want to create relevant features so that the model can learn patterns
- As an ML engineer, I want to implement feature scaling so that features are normalized
- As a data scientist, I want to handle missing values so that data is complete

### 4. Model Selection & Training
**User Stories:**
- As a data scientist, I want to evaluate multiple algorithms so that we choose the best approach
- As an ML engineer, I want to train baseline models so that we have performance benchmarks
- As a data scientist, I want to perform hyperparameter tuning so that we optimize model performance
- As an ML engineer, I want to implement cross-validation so that we avoid overfitting

### 5. Model Evaluation
**User Stories:**
- As a data scientist, I want to calculate accuracy metrics so that we assess model quality
- As an ML engineer, I want to analyze confusion matrix so that we understand errors
- As a product owner, I want to validate against business metrics so that the model meets objectives

### 6. Model Deployment
**User Stories:**
- As a DevOps engineer, I want to containerize the model so that it's deployable
- As an ML engineer, I want to create an API endpoint so that applications can use the model
- As a DevOps engineer, I want to set up CI/CD pipeline so that deployment is automated

### 7. Monitoring & Maintenance
**User Stories:**
- As an ML engineer, I want to monitor model performance so that we detect degradation
- As a DevOps engineer, I want to set up alerting so that we're notified of issues
- As a data scientist, I want to implement model retraining so that the model stays current

---

## Sprint Planning Guidelines

### Prioritization (MoSCoW Method)
- **Must Have:** Critical for sprint success
- **Should Have:** Important but not critical
- **Could Have:** Nice to have if time permits
- **Won't Have:** Out of scope for this sprint

### Story Point Estimation (Fibonacci Scale)
- **1 point:** Very simple, < 1 hour
- **2 points:** Simple, 1-2 hours
- **3 points:** Moderate, 2-4 hours
- **5 points:** Complex, 4-8 hours
- **8 points:** Very complex, full day
- **13 points:** Too large, needs to be split

### Sprint Selection (Today's Session Only)
**Recommended capacity:** 13-21 story points per person
- Focus on 2-3 high-priority items
- Leave buffer for reviews and unexpected issues
- Choose items that can be completed today

---

## Workflow Board Columns

1. **Backlog** → Items not yet started
2. **Ready** → Items meeting Definition of Ready
3. **In Progress** → Active work
4. **In Review** → Awaiting peer review
5. **Done** → Meets Definition of Done

---

## Team Collaboration Tips

### During Sprint
- **Update board** immediately when status changes
- **Ask for help** if blocked
- **Pair programming** for complex tasks
- **Quick check-ins** every 1-2 hours

### Review Process
- **Code review** by at least one teammate
- **Test coverage** verified
- **Documentation** updated
- **Acceptance criteria** validated

### Sprint Completion
- **Demo** completed work to team
- **Reflect** on what went well/poorly
- **Update velocity** for future planning

---

## Example Sprint Backlog (Today)

### High Priority (Must Have)
1. **Set up data pipeline** (5 points) - Foundation for everything
2. **Perform EDA** (3 points) - Understand our data
3. **Train baseline model** (5 points) - Initial benchmark

### Medium Priority (Should Have)
4. **Create model evaluation metrics** (3 points) - Assess quality
5. **Document findings** (2 points) - Share knowledge

### Low Priority (Could Have)
6. **Experiment with feature engineering** (3 points) - If time allows

**Total:** 21 points (realistic for one session)

---

## Notes for Team
- This is a **learning sprint** - focus on process as much as output
- **Communication is key** - over-communicate rather than under-communicate
- **Done is better than perfect** - aim for working software
- **Observe the flow** - notice how items move through the board
- **Help teammates** - we succeed together
