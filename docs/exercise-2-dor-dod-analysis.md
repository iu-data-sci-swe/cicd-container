# Exercise 2: Definition of Ready (DoR) and Definition of Done (DoD)

## Overview
Analyzing potential problems in agile development and how they relate to DoR (Definition of Ready) and DoD (Definition of Done).

---

## Problem Analysis

### Problem 1: Missing Acceptance Criteria in User Stories

#### 🔴 **Issue Type:** Definition of Ready (DoR) Violation

**Why this is a problem:**
- Team doesn't know what "done" looks like
- Impossible to verify if story is complete
- Leads to misaligned expectations
- Causes rework and scope creep
- Increases risk of rejections during review

**Impact:**
- Development starts without clear goals
- Testing becomes ambiguous
- Product Owner cannot validate completion
- Sprint velocity becomes unreliable

#### ✅ **Improved DoR Rule:**

**Before a story enters sprint, it MUST have:**
1. **Clear acceptance criteria** using Given-When-Then format:
   - Given [initial context]
   - When [action occurs]
   - Then [expected outcome]
2. **Specific, measurable, testable** criteria (minimum 2-3 criteria)
3. **Examples** of both positive and negative cases
4. **Reviewed and approved** by Product Owner and at least one developer

**Example:**
```
❌ BAD: "As a user, I want to log in"

✅ GOOD: "As a user, I want to log in so that I can access my account"

Acceptance Criteria:
1. Given I am on the login page
   When I enter valid credentials
   Then I am redirected to my dashboard
   
2. Given I am on the login page
   When I enter invalid credentials
   Then I see an error message "Invalid username or password"
   
3. Given I have entered wrong password 3 times
   When I attempt a 4th login
   Then my account is locked for 15 minutes
```

---

### Problem 2: Missing Story Points in Sprint Backlog

#### 🔴 **Issue Type:** Definition of Ready (DoR) Violation

**Why this is a problem:**
- Cannot plan sprint capacity
- No basis for velocity tracking
- Team cannot commit to realistic workload
- Sprint planning becomes guesswork
- Burndown charts are meaningless

**Impact:**
- Risk of over-commitment or under-commitment
- Cannot measure team performance trends
- Difficult to forecast future sprints
- Team accountability suffers

#### ✅ **Improved DoR Rule:**

**Before a story enters sprint backlog, it MUST have:**
1. **Story points estimated** using planning poker or similar technique
2. **Team consensus** on the estimate (not imposed by one person)
3. **Estimation done** by developers who will do the work
4. **Uncertainty documented** if estimate is uncertain (add spike story if needed)
5. **Stories > 13 points** must be split into smaller stories

**Estimation Guidelines:**
- 1 point = 1-2 hours
- 2 points = 2-4 hours  
- 3 points = 4-6 hours
- 5 points = 1 day
- 8 points = 2 days
- 13 points = Too large, must split

**Sprint Backlog Rule:**
- Sum of story points ≤ Team velocity (from previous sprints)
- Leave 20% buffer for unexpected work
- If story has no points, it cannot enter sprint

---

### Problem 3: Code Without Unit Tests Marked as Complete

#### 🔴 **Issue Type:** Definition of Done (DoD) Violation

**Why this is a problem:**
- Technical debt accumulates
- Bugs discovered later (more expensive to fix)
- Refactoring becomes risky
- Code quality deteriorates
- Regression testing is manual and slow

**Impact:**
- Future sprints slowed by bug fixes
- Confidence in releases decreases
- Team velocity drops over time
- Production incidents increase

#### ✅ **Improved DoD Rule:**

**Before a story is marked "Done", it MUST have:**

1. **Unit Tests:**
   - Minimum **80% code coverage**
   - All critical paths tested
   - Edge cases and error conditions tested
   - Tests pass in CI/CD pipeline

2. **Test Quality Checks:**
   - Tests are **meaningful**, not just for coverage
   - Tests follow AAA pattern (Arrange, Act, Assert)
   - Tests are **independent** (can run in any order)
   - Tests have **clear names** describing what they test

3. **Automated Verification:**
   - CI pipeline fails if coverage < 80%
   - Pull request cannot merge without passing tests
   - Code review includes test review

**Example DoD Checklist Item:**
```
✅ Unit tests written with ≥80% coverage
✅ All tests pass locally and in CI
✅ Tests reviewed by peer
✅ Integration tests added if applicable
✅ Test documentation updated
```

---

### Problem 4: Features Deployed Without Performance Testing

#### 🔴 **Issue Type:** Definition of Done (DoD) Violation

**Why this is a problem:**
- Performance issues discovered in production
- Poor user experience
- System crashes under load
- Expensive emergency fixes
- Reputation damage

**Impact:**
- Production incidents and downtime
- Customer complaints
- Need for hotfixes and rollbacks
- Loss of user trust
- Increased support burden

#### ✅ **Improved DoD Rule:**

**Before a feature is marked "Done", it MUST have:**

1. **Performance Requirements Defined:**
   - Response time targets (e.g., p95 < 200ms)
   - Throughput requirements (e.g., 1000 req/sec)
   - Resource usage limits (e.g., < 512MB memory)
   - Concurrent user capacity (e.g., 10,000 users)

2. **Performance Testing Completed:**
   - **Load testing** with expected traffic
   - **Stress testing** at 2x expected load
   - **Spike testing** for traffic surges
   - **Endurance testing** for memory leaks (if applicable)

3. **Performance Criteria Met:**
   - All performance requirements satisfied
   - No degradation of existing features
   - Performance reports documented
   - Monitoring dashboards configured

4. **Testing Automated:**
   - Performance tests in CI/CD pipeline (for critical paths)
   - Automated alerts for performance regressions
   - Staging environment mirrors production

**Example DoD Checklist:**
```
✅ Performance requirements documented
✅ Load testing completed (baseline + 2x load)
✅ Response time p95 < 200ms (verified)
✅ Memory usage < 512MB under load
✅ No performance regressions vs. previous version
✅ Performance monitoring enabled in production
✅ Rollback plan documented
```

---

### Problem 5: Incomplete Documentation Blocking Team Understanding

#### 🔴 **Issue Type:** Definition of Done (DoD) Violation

**Why this is a problem:**
- Knowledge silos created
- Onboarding new team members difficult
- Future maintenance is slow
- Decisions cannot be understood or challenged
- Technical debt grows

**Impact:**
- Dependency on specific developers
- Slower velocity for related features
- Increased risk when developers leave
- Code archaeology required

#### ✅ **Improved DoD Rule:**

**Before a story is marked "Done", it MUST have:**

1. **Code Documentation:**
   - **Public APIs** have JSDoc/docstrings with examples
   - **Complex algorithms** have explanation comments
   - **Configuration** files have inline comments
   - **No commented-out code** (use version control)

2. **Technical Documentation:**
   - **Architecture decisions** recorded (ADRs if significant)
   - **API changes** documented in changelog
   - **Database changes** in migration scripts with comments
   - **Dependencies** updated in package files

3. **User Documentation:**
   - **User-facing features** in user guide
   - **API endpoints** in API documentation (Swagger/OpenAPI)
   - **Configuration changes** in operations manual
   - **Screenshots/demos** for UI changes

4. **Team Knowledge:**
   - **Demo** given to team (not just Product Owner)
   - **Knowledge sharing** session for complex features
   - **README** updated with setup instructions
   - **Troubleshooting guide** for common issues

**Documentation Standards:**
- Documentation is **part of the work**, not an afterthought
- Written **before or during** development, not after
- Reviewed **along with code** in pull requests
- Updated **automatically** where possible (e.g., API docs from code)

**Example DoD Checklist:**
```
✅ Code comments added for complex logic
✅ API documentation updated (Swagger)
✅ README.md reflects new features
✅ Architecture decision recorded (if applicable)
✅ User guide updated
✅ Demo presented to team
✅ Peer reviewed documentation
```

---

## Summary: Improved DoR and DoD

### Definition of Ready (DoR) Checklist ✅

**A user story is READY for sprint when:**
1. ✅ User story follows format: "As a [role], I want [goal], so that [benefit]"
2. ✅ Acceptance criteria defined (Given-When-Then format, minimum 2-3)
3. ✅ Story points estimated by team consensus
4. ✅ Dependencies identified and resolved
5. ✅ Mockups/designs available (if UI work)
6. ✅ Performance requirements defined (if applicable)
7. ✅ Reviewed by Product Owner and tech lead
8. ✅ Small enough to complete in one sprint (≤13 points)
9. ✅ Team understands what needs to be built
10. ✅ No blockers or open questions

**If DoR not met → Story stays in backlog refinement**

---

### Definition of Done (DoD) Checklist ✅

**A user story is DONE when:**
1. ✅ All acceptance criteria met and verified
2. ✅ Code written and committed to version control
3. ✅ Code reviewed and approved by peer
4. ✅ Unit tests written with ≥80% coverage
5. ✅ All tests pass (unit, integration, E2E)
6. ✅ Performance testing completed (if applicable)
7. ✅ Security review completed (if applicable)
8. ✅ Documentation updated (code, API, user, technical)
9. ✅ Deployed to staging environment
10. ✅ Demonstrated to Product Owner and accepted
11. ✅ CI/CD pipeline passes
12. ✅ No critical bugs or technical debt
13. ✅ Monitoring/logging configured
14. ✅ Ready for production deployment

**If DoD not met → Story goes back to "In Progress"**

---

## Benefits of Strong DoR and DoD

### Definition of Ready Benefits:
- ✅ **Clear expectations** before work starts
- ✅ **No wasted effort** on unclear requirements  
- ✅ **Predictable velocity** with proper estimates
- ✅ **Reduced rework** from misunderstandings
- ✅ **Better sprint planning** with ready stories

### Definition of Done Benefits:
- ✅ **High quality** deliverables
- ✅ **Reduced technical debt**
- ✅ **Faster future development**
- ✅ **Fewer production issues**
- ✅ **Team confidence** in releases
- ✅ **Transparent progress** tracking

---

## Implementation Strategy

### Phase 1: Establish Baseline (Sprint 1)
1. Document current DoR and DoD
2. Get team agreement on rules
3. Train team on new standards

### Phase 2: Enforce (Sprint 2-3)
1. Use checklists in every story
2. Scrum Master enforces in ceremonies
3. Measure compliance

### Phase 3: Improve (Sprint 4+)
1. Retrospective reviews of DoR/DoD effectiveness
2. Adjust rules based on team feedback
3. Automate checks where possible (CI/CD)

---

## Key Takeaways

| Problem | Type | Fix |
|---------|------|-----|
| Missing acceptance criteria | DoR | Require Given-When-Then format |
| Missing story points | DoR | No points = no sprint entry |
| No unit tests | DoD | 80% coverage minimum |
| No performance testing | DoD | Load test before "Done" |
| Incomplete documentation | DoD | Docs required for completion |

**Remember:** DoR prevents starting the wrong thing. DoD prevents calling incomplete work "done."
