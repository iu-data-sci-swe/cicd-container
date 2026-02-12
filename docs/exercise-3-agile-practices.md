# Exercise 3: Agile Practices Evaluation and Scrum Suitability

## Part A: Evaluating Practices Against Agile/Scrum Principles

### Practice 1: Delivering Faster by Omitting Documentation Tasks

#### ❌ **NOT in Line with Agile/Scrum**

**Agile Values Violated:**
- **"Working software over comprehensive documentation"** does NOT mean zero documentation
- Agile values documentation that serves a purpose
- Sustainable pace principle violated (creates technical debt)

**Scrum Principles Violated:**
- **Definition of Done** should include necessary documentation
- **Transparency** principle requires shared understanding (documentation helps)
- **Empiricism** requires learning from past work (needs documentation)

**Why This is Problematic:**

1. **Short-term Gain, Long-term Pain:**
   - Initial velocity spike followed by decline
   - Increasing time spent understanding old code
   - Higher defect rates from misunderstandings

2. **Knowledge Silos:**
   - Only original developers understand the code
   - Bus factor = 1 (high risk)
   - Difficult onboarding for new team members

3. **Technical Debt Accumulation:**
   - Maintenance becomes increasingly difficult
   - Refactoring becomes risky
   - Code becomes "legacy" quickly

4. **Definition of Done Compromise:**
   - Incomplete work called "done"
   - Quality standards lowered
   - Sprint retrospectives should address this

**Agile-Aligned Approach:**

✅ **Right Balance:**
- **Just enough documentation** - no more, no less
- **Living documentation** - kept up to date, not outdated PDFs
- **Documentation as code** - API docs from code comments, automated
- **Working examples** - tests serve as documentation
- **User stories and acceptance criteria** - document requirements
- **ADRs (Architecture Decision Records)** - for significant decisions
- **README files** - for setup and contribution guidelines

✅ **Scrum Alignment:**
- Include documentation in Definition of Done
- Documentation is part of the sprint work
- Time-box documentation activities
- Review documentation in sprint reviews
- Improve documentation practices in retrospectives

**Verdict:** ❌ Not agile-aligned. True agile delivers **working documented software**, not undocumented software faster.

---

### Practice 2: Daily Status Updates in Group Chat ("Virtual Stand-ups")

#### ⚠️ **PARTIALLY in Line with Agile/Scrum** (Context-Dependent)

**When It Works (✅):**
- **Distributed/remote teams** across time zones
- **Asynchronous communication preferred** by team
- **Documented discussions** for reference
- **Supplement to, not replacement for** synchronous stand-ups
- Team has **strong written communication** culture

**When It Doesn't Work (❌):**
- **Complete replacement** for face-to-face interaction
- **Low engagement** - people just copy-paste updates
- **Lacks real-time collaboration** and problem-solving
- **Misses non-verbal cues** and team dynamics
- **Delayed responses** to blockers

**Scrum Stand-up Purpose:**
- **Synchronize** team activities (hard to do asynchronously)
- **Identify blockers** and solve them immediately
- **Inspect progress** toward Sprint Goal as a team
- **Adapt plan** for the day
- **Build team cohesion** through daily interaction

**Comparison:**

| Aspect | Traditional Stand-up | Chat Updates |
|--------|---------------------|-------------|
| **Synchronization** | ✅ Real-time | ⚠️ Delayed |
| **Blocker resolution** | ✅ Immediate | ❌ Delayed |
| **Team building** | ✅ Strong | ⚠️ Weak |
| **Documentation** | ❌ None | ✅ Searchable |
| **Time zone flexibility** | ❌ Difficult | ✅ Easy |
| **Engagement** | ✅ Present | ⚠️ Variable |
| **Problem-solving** | ✅ Collaborative | ❌ Limited |

**Agile-Aligned Approach:**

✅ **Hybrid Model:**
1. **Primary:** Synchronous video stand-ups (15 min daily)
   - Mandatory attendance
   - Camera-on for engagement
   - Focus on three questions:
     - What did I complete yesterday?
     - What will I do today?
     - What blockers do I have?

2. **Supplement:** Async updates in chat
   - For detailed information
   - For timezone-distributed team members
   - As preparation for sync stand-up
   - For reference and documentation

3. **Best Practices:**
   - Keep sync stand-up at same time daily
   - Use chat for deep-dive problem solving after stand-up
   - Video record stand-ups for absent members
   - Rotate facilitator role

**Verdict:** ⚠️ Acceptable as **supplement**, not replacement. Scrum emphasizes face-to-face communication as most effective.

---

### Practice 3: Developers Helping with Quality Assurance

#### ✅ **STRONGLY in Line with Agile/Scrum**

**Agile Values Supported:**
- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation (quality enables this)
- **Customer collaboration** (quality prevents rework)
- **Responding to change** (quality makes refactoring safer)

**Scrum Principles Supported:**
- **Cross-functional teams** - team has all skills needed
- **Collective ownership** - everyone responsible for quality
- **Sustainable pace** - quality reduces technical debt
- **Built-in quality** - not a separate phase

**Why This is Excellent:**

1. **Shift-Left Quality:**
   - Catch defects earlier (cheaper to fix)
   - Prevent defects rather than find them
   - Quality is everyone's responsibility

2. **Breaks Down Silos:**
   - No "throw it over the wall" mentality
   - Developers understand user perspective
   - QA understands technical constraints
   - Faster feedback loops

3. **T-Shaped Skills:**
   - Developers learn testing expertise
   - QA learns development practices
   - Team becomes more resilient
   - Better collaboration and empathy

4. **Continuous Improvement:**
   - Developers see consequences of poor code
   - QA provides immediate feedback
   - Test automation becomes priority
   - Definition of Done includes QA

**Implementation Approaches:**

✅ **Pair Testing:**
- Developer and QA work together
- Test cases designed together
- Immediate feedback and learning

✅ **Test-Driven Development (TDD):**
- Developers write tests first
- Quality built into development
- Comprehensive test coverage

✅ **Behavior-Driven Development (BDD):**
- Developers, QA, and PO collaborate
- Executable specifications
- Shared understanding

✅ **Shift-Left Testing:**
- Testing throughout sprint
- Developers run all tests before commit
- Automated testing in CI/CD
- Peer review includes test review

✅ **Collective Code Ownership:**
- Anyone can fix any part of codebase
- Everyone responsible for test suite
- Shared quality standards

**Alternative Models:**

| Model | Agile Alignment | Notes |
|-------|----------------|-------|
| **Separate QA Team** | ❌ Waterfall | Handoffs, delays, silos |
| **QA in Scrum Team** | ✅ Good | Dedicated QA, but can create dependency |
| **Developers Do QA** | ✅ Best | Shift-left, shared ownership |
| **QA as Coach** | ✅ Excellent | QA teaches developers testing |

**Verdict:** ✅ Highly agile-aligned. This is a hallmark of mature agile teams.

---

## Part B: Project Suitability for Scrum

### Project 1: Development of a Mobile Fitness App

#### ✅ **EXCELLENT FIT for Scrum**

**Why Scrum Works Well:**

1. **Iterative Development:**
   - Features can be released incrementally
   - MVP can be tested with real users quickly
   - Feedback incorporated in next sprint

2. **Clear Sprint Goals:**
   - Sprint 1: User registration and basic tracking
   - Sprint 2: Workout logging
   - Sprint 3: Progress visualization
   - Sprint 4: Social features

3. **Regular User Feedback:**
   - Demo to stakeholders every 2 weeks
   - Beta testing groups provide feedback
   - Pivot based on user response

4. **Defined Product Backlog:**
   - Features well-understood (standard app features)
   - Can be prioritized by business value
   - User stories easy to write

5. **Stable Team:**
   - iOS devs, Android devs, backend devs, designers
   - Team can commit to sprint goals
   - Velocity predictable over time

6. **Time-Boxed Releases:**
   - Target app store release dates
   - Regular feature updates
   - Coordinated with marketing

**Recommended Scrum Setup:**
- 2-week sprints
- Sprint planning, daily stand-ups, sprint review, retrospective
- Product backlog groomed weekly
- Definition of Done includes app store guidelines

**Verdict:** ✅ Perfect Scrum project

---

### Project 2: In-House Development of a Sales Dashboard

#### ✅ **EXCELLENT FIT for Scrum**

**Why Scrum Works Well:**

1. **Evolving Requirements:**
   - Sales team discovers needs as they use it
   - Can't know all requirements upfront
   - Agile embraces changing requirements

2. **Frequent Releases:**
   - Deploy new features weekly/bi-weekly
   - Get immediate feedback from sales team
   - Adjust priorities based on actual usage

3. **Close Stakeholder Collaboration:**
   - Sales managers are accessible
   - Product Owner from sales department
   - Demo to actual users each sprint

4. **Incremental Value:**
   - Basic dashboard in Sprint 1
   - Add reports incrementally
   - Each sprint delivers usable features

5. **Internal Users:**
   - Easy to gather feedback
   - Forgiving of early versions
   - Can iterate rapidly

**Recommended Scrum Setup:**
- 1-week sprints (fast feedback)
- Product Owner from sales department
- Weekly demos to sales team
- Continuous deployment to staging

**Potential Challenges:**
- ⚠️ Many stakeholders with different priorities (need strong PO)
- ⚠️ Feature creep risk (need disciplined backlog management)

**Verdict:** ✅ Ideal Scrum scenario

---

### Project 3: Development of a Smart Home Air Quality Sensor

#### ⚠️ **MODERATE FIT for Scrum** (Hybrid Approach)

**Why Scrum is Challenging:**

1. **Hardware-Software Integration:**
   - Hardware changes are expensive
   - Long lead times for prototypes
   - Can't iterate hardware every sprint

2. **Regulatory Requirements:**
   - Certifications needed (FCC, CE, etc.)
   - Compliance testing not iterative
   - Documentation extensive and formal

3. **Manufacturing Constraints:**
   - Tooling requires upfront design
   - Inventory and supply chain planning
   - Physical prototypes slow to produce

4. **Longer Feedback Cycles:**
   - Can't deploy firmware updates as easily initially
   - Hardware bugs expensive to fix post-manufacturing
   - Beta testing requires physical units

**Why Scrum Can Work:**

1. **Software Development Portion:**
   - Mobile app: Fully scrumable
   - Cloud backend: Fully scrumable
   - Firmware: Partially scrumable (with hardware simulator)

2. **Prototyping Phase:**
   - Early prototypes can iterate
   - User testing on prototypes
   - Feature prioritization based on feedback

**Recommended Hybrid Approach:**

✅ **Modified Scrum:**
- **Hardware:** Waterfall phases with gates
  - Requirements → Design → Prototype → Test → Manufacture
- **Software:** Agile sprints
  - Continuous integration and deployment
  - Rapid iteration even after hardware locked in
- **Integration:** Regular sync points
  - Hardware milestones inform software sprints
  - Software sprints test hardware assumptions

**Sprint Structure:**
- **Phase 1 (Prototyping - 3 months):**
  - 2-week sprints for firmware and app development
  - Hardware in parallel waterfall track
  - Integration testing each sprint with prototype
  
- **Phase 2 (Manufacturing - 2 months):**
  - Hardware locked, software continues sprints
  - App and cloud backend development
  - Firmware frozen for certification

**Verdict:** ⚠️ Hybrid Scrum-Waterfall. Use Scrum for software, modified approach for hardware.

---

### Project 4: Development of a Train Door

#### ❌ **POOR FIT for Scrum**

**Why Scrum Doesn't Work:**

1. **Safety-Critical System:**
   - **Human lives at risk** if door fails
   - Cannot "fail fast" or "embrace change"
   - Formal verification required
   - Extensive testing and certification

2. **Regulatory Requirements:**
   - **Heavy documentation** mandated by regulations
   - **Formal approval processes** at each stage
   - **Traceability** required for every requirement
   - **Change control boards** for any modifications

3. **Long Development Cycles:**
   - **Years of testing** and certification
   - Cannot release "MVP" and iterate
   - Physical prototypes expensive
   - Integration with train systems complex

4. **Predictive Planning Required:**
   - **Budget and timeline** must be known upfront
   - Contract-driven development
   - Stakeholders need certainty
   - Late changes extremely costly

5. **Formal Verification:**
   - Mathematical proofs of correctness
   - Exhaustive testing scenarios
   - Fault tree analysis
   - Failure Mode and Effects Analysis (FMEA)

**Better Approach:**

✅ **V-Model or Waterfall:**
- Requirements → Specification → Design → Implementation → Testing → Validation
- Formal reviews and sign-offs at each phase
- Extensive documentation
- Rigorous change management

✅ **Or Hybrid:**
- Use **waterfall for critical safety components**
- Use **agile for non-critical features** (e.g., monitoring dashboard, diagnostics)
- Strict interface definitions between parts

**Why Not Scrum:**
| Scrum Principle | Train Door Reality |
|-----------------|-------------------|
| Embrace change | Changes = recertification ($$$) |
| Working software | Working door = years of testing |
| Customer collaboration | Customer = regulatory bodies |
| Rapid iterations | Iterations = months/years |
| Cross-functional team | Specialists required (safety engineers) |
| Minimal documentation | Extensive documentation mandated |

**Verdict:** ❌ Not suitable for Scrum. Use traditional engineering methods (V-Model, Waterfall).

---

### Project 5: Development of a Data-Driven AI Tool

#### ✅ **EXCELLENT FIT for Scrum**

**Why Scrum Works Exceptionally Well:**

1. **Experimental Nature:**
   - Don't know if ML approach will work upfront
   - Need to try multiple algorithms
   - Iterate based on model performance
   - Fail fast on approaches that don't work

2. **Incremental Model Development:**
   - Sprint 1: Baseline model (logistic regression)
   - Sprint 2: Feature engineering
   - Sprint 3: Advanced model (Random Forest)
   - Sprint 4: Hyperparameter tuning
   - Sprint 5: Model deployment

3. **Continuous Evaluation:**
   - Model performance metrics each sprint
   - A/B testing in production
   - Feedback from data changes
   - Retrain and improve continuously

4. **Unclear Requirements:**
   - Business problem understood, solution not clear
   - Discover through experimentation
   - Requirements evolve as data understood
   - Stakeholders learn what's possible

5. **Cross-Functional Team:**
   - Data scientists, ML engineers, DevOps
   - Collaboration essential
   - Knowledge sharing in daily stand-ups
   - Pair programming for complex algorithms

6. **Continuous Deployment:**
   - MLOps pipelines for automatic retraining
   - Canary releases for model updates
   - Rollback if performance degrades
   - Real-time monitoring

**Recommended Scrum Setup:**

✅ **AI/ML-Specific Practices:**
- **Sprint goals:** Focus on model metrics (accuracy, precision, recall)
- **Definition of Done:** Includes model evaluation and documentation
- **Sprint review:** Demo model performance, not just features
- **Retrospectives:** Discuss data quality issues, model drift
- **Spike stories:** For research and experimentation
- **Model versioning:** Track models like code

✅ **Typical Sprint Breakdown:**
- **Sprint 0:** Data collection and EDA
- **Sprint 1-2:** Baseline models
- **Sprint 3-4:** Feature engineering and advanced models
- **Sprint 5-6:** Model optimization and deployment
- **Sprint 7+:** Monitoring, retraining, improvements

**Special Considerations:**
- ⚠️ **Data availability:** May need longer lead time for data collection
- ⚠️ **Compute resources:** Training time may affect sprint cadence
- ⚠️ **Model drift:** Ongoing maintenance beyond initial "done"
- ⚠️ **Explainability:** May need time for interpretability work

**Verdict:** ✅ Perfect for Scrum. ML development is inherently iterative and experimental.

---

## Summary: Scrum Suitability

| Project | Scrum Fit | Reasoning |
|---------|-----------|-----------|
| **Mobile Fitness App** | ✅ Excellent | Iterative features, user feedback, incremental releases |
| **Sales Dashboard** | ✅ Excellent | Internal users, evolving needs, frequent releases |
| **Air Quality Sensor** | ⚠️ Moderate | Software: Scrum. Hardware: Waterfall. Hybrid approach. |
| **Train Door** | ❌ Poor | Safety-critical, regulatory heavy, predictive planning needed |
| **AI Tool** | ✅ Excellent | Experimental, iterative, continuous improvement |

---

## Key Takeaways

### Scrum Works Best When:
✅ Requirements are **uncertain or evolving**  
✅ **Rapid feedback** is possible  
✅ Features can be delivered **incrementally**  
✅ **Experimentation** and learning are needed  
✅ Team is **cross-functional** and co-located (or well-distributed)  
✅ Stakeholders are **accessible** and collaborative  

### Scrum Struggles When:
❌ **Safety-critical** systems with formal verification  
❌ **Heavy regulatory** requirements  
❌ **Hardware** development with long lead times  
❌ Requirements are **fixed and known** upfront  
❌ **Predictive contracts** with fixed scope/time/cost  
❌ Stakeholders demand **extensive upfront documentation**  

### Agile Practice Alignment:
✅ **Developers doing QA** - Excellent agile practice  
⚠️ **Virtual stand-ups** - OK as supplement, not replacement  
❌ **Omitting documentation** - Misinterpretation of agile values  

**Remember:** Agile is about **adaptability**, not **anarchy**. Balance flexibility with necessary structure.
