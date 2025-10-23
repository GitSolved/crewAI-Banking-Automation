# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains multi-agent AI automation projects using the crewAI framework. It implements a **multi-architecture strategy** combining Jupyter notebooks, standalone Python projects, modern Python packages, and Flow-based orchestration for Alpine Capital Bank operations.

**Total Projects**: 21 projects across Alpine departments + 4 Flow packages
- 5 Jupyter Notebooks (.ipynb)
- 10 Python Packages (pyproject.toml with YAML config)
- 1 Standalone Python Project (requirements.txt with .py files)
- 1 Standalone Script (single .py file with config/)
- 4 Flow Packages (crewAI Flows with state management, 1 placeholder)

## Project Structure

### Alpine Banking Automation

**Note**: The `training/` directory has been reorganized. All projects are now in `Alpine/` departments organized by business function.

#### Human Resources Department (`Alpine/Human-Resources-Department/`) - 9 projects

**Python Packages** (5):
1. **Banking_Recruitment_Automation**: Multi-agent recruitment workflow with LinkedIn integration
2. **Job_Posting_Generator**: Automated job posting creation optimized for banking roles
3. **Resume_Job_Matcher**: AI-powered candidate-role matching and scoring
4. **Employer_Branding_Automation**: Employer branding and talent marketing campaigns
5. **Corporate_Travel_Planner**: Employee travel coordination and itinerary generation
6. **Professional_Social_Media_Content**: Corporate social media for LinkedIn/Twitter

**Standalone Python Projects** (1):
- **Meeting_Preparation_Assistant**: Meeting prep using agents.py/tasks.py/main.py pattern (requirements.txt)

**Standalone Scripts** (1):
- **Training_Video_Script_Generator**: Single screenplay_writer.py with config/ directory

**Jupyter Notebooks** (2):
- **Event_Planning_Automation.ipynb**: Banking events, conferences, corporate retreats
- **Job_Application_Booster.ipynb**: Resume tailoring and interview preparation

#### Operations Department (`Alpine/Operations-Department/`) - 4 projects

**Python Packages** (2):
1. **VIP_Client_Experience_Planner**: High-value client experience design and event planning
2. **Stock_Analysis_Automation**: Advanced financial analysis and trading strategy development

**Jupyter Notebooks** (2):
- **Customer_Outreach_Campaign.ipynb**: Customer engagement campaigns with segment-specific messaging
- **Customer_Support_Automation.ipynb**: Automated support ticket handling (legacy notebook structure)

#### Information Technology Department (`Alpine/Information-Technology-Department/`) - 3 projects

**Python Packages** (2):
1. **Policy_Document_Validator**: Compliance policy validation (markdown format validator)
2. **Landing_Page_Generator**: Marketing page generation and A/B testing optimization

**Jupyter Notebooks** (1):
- **Article_Automation/Research_Write_Article.ipynb**: Internal documentation and knowledge base article generation (sequential collaboration pattern)

### Alpine Flows (`Alpine-Flows/`) - 4 Flow Packages

Advanced orchestration using crewAI Flows for state management and background workers:
1. **Email_Auto_Responder_Flow**: Automated email checking and draft response generation (requires Gmail API)
2. **Lead_Score_Flow**: Lead qualification and scoring automation
3. **Meeting_Assistant_Flow**: Meeting coordination and follow-up automation (Slack + Trello integration)
4. **Content_Creator_Flow**: Placeholder directory (not yet implemented)

Flow packages use state management patterns for continuous operation and complex multi-step workflows.

## Development Workflow

### Requirements

**Python Version**: 3.10-3.13 (inclusive)

**Package Managers**:
- **UV** (recommended): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Poetry** (alternative): `pip install poetry`
- **Jupyter**: `pip install jupyter`

**API Keys Required**

All projects require environment variables:

**For Jupyter Notebooks** (set in notebook cells):
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-turbo"  # or gpt-3.5-turbo
os.environ["SERPER_API_KEY"] = "your-key"  # For web search
```

**For Python Packages** (create `.env` file):
```bash
# Copy example and edit
cp .env.example .env

# Required in .env file:
OPENAI_API_KEY=your-key
OPENAI_MODEL_NAME=gpt-4-turbo
SERPER_API_KEY=your-key
```

**Package-Specific Requirements**:
- **Banking_Recruitment_Automation**: LinkedIn cookie (`LI_AT` in `.env`)
- **Email_Auto_Responder_Flow**: Gmail API `credentials.json` file (see [Gmail API setup](https://developers.google.com/gmail/api/quickstart/python))
- **Meeting_Assistant_Flow**: Slack and Trello API tokens

## crewAI Architecture Fundamentals

### Agent Creation Pattern

All projects follow the same Agent instantiation pattern:

```python
from crewai import Agent

agent = Agent(
    role="Specific Role Name",
    goal="Clear objective the agent should achieve",
    backstory="Context about the agent's expertise and function",
    tools=[tool1, tool2],  # Optional: crewAI or LangChain tools
    verbose=True,
    allow_delegation=True  # Enable for hierarchical processes
)
```

**Python Package Pattern** (YAML-based configuration):
```yaml
# src/<package>/config/agents.yaml
research_manager:
  role: "Research Manager"
  goal: "Generate high-quality research insights"
  backstory: "Experienced analyst with 10+ years in banking"
  tools:
    - serper_tool
    - scrape_tool
```

### Task Definition Pattern

Tasks require three mandatory fields:

```python
from crewai import Task

task = Task(
    description="Detailed description with {variable_placeholders}",
    expected_output="Specific format and content expectations",
    agent=assigned_agent,
    output_file="output.md",  # Optional: save results to file
    context=[previous_task],  # Optional: dependencies on other tasks
    async_execution=True  # Optional: for parallel execution
)
```

**Python Package Pattern** (YAML-based configuration):
```yaml
# src/<package>/config/tasks.yaml
research_task:
  description: "Research {topic} and compile findings"
  expected_output: "Comprehensive report with 5+ sources"
  agent: research_manager
  output_file: "research_report.md"
```

### Crew Assembly and Execution

**Sequential Process** (default):
```python
from crewai import Crew

crew = Crew(
    agents=[agent1, agent2, agent3],
    tasks=[task1, task2, task3],  # Executed in order
    verbose=True,
    memory=True  # Optional: enable agent memory
)

result = crew.kickoff(inputs={"variable": "value"})
```

**Hierarchical Process** (with auto-created manager):
```python
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

crew = Crew(
    agents=[agent1, agent2, agent3],
    tasks=[task1, task2, task3],
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-3.5-turbo"),
    verbose=True
)
```

**Python Package Pattern**:
```python
# src/<package>/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MyCrew:
    """My automation crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config['researcher'])

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
```

## Project Structures

This repository uses five distinct project architectures:

**1. Python Packages (pyproject.toml)** - Production-ready packages
- Modern dependency management with UV/Poetry
- YAML-based configuration (agents.yaml, tasks.yaml) separate from code
- Standardized crew.py with @CrewBase decorator pattern
- Entry points defined in pyproject.toml for CLI execution
- **When to use**: Production deployments, team collaboration, maintainable codebases
- **Examples**: Banking_Recruitment_Automation, Stock_Analysis_Automation, Policy_Document_Validator

**2. Standalone Python Projects (requirements.txt)** - Simple scripts
- Traditional .py file structure without package boilerplate
- Direct agent/task instantiation in Python (no YAML)
- Simpler for small, focused automation tasks
- **When to use**: Quick prototypes, single-purpose tools
- **Example**: Meeting_Preparation_Assistant (agents.py, tasks.py, main.py)

**3. Standalone Scripts** - Minimal single-file projects
- Single .py file with optional config/ directory
- No package structure or requirements.txt in parent directory
- **When to use**: Very simple, focused utilities
- **Example**: Training_Video_Script_Generator (screenplay_writer.py with config/)

**4. Jupyter Notebooks (.ipynb)** - Interactive exploration
- Self-contained with inline code, markdown, and outputs
- Great for learning, experimentation, and demonstrations
- Sequential cell execution with immediate visual feedback
- **When to use**: Learning crewAI, proof-of-concepts, exploratory work
- **Examples**: Article_Automation, Customer_Outreach_Campaign, Event_Planning_Automation

**5. Flow Packages (crewAI Flows)** - Advanced orchestration
- State management with @start, @listen, @router decorators
- Background workers for continuous operation
- Multi-step workflows with complex conditional logic
- Located in `Alpine-Flows/` directory (separate from department structure)
- **When to use**: Event-driven systems, long-running processes, complex state machines
- **Examples**: Email_Auto_Responder_Flow, Lead_Score_Flow, Meeting_Assistant_Flow

## Python Package Structure (pyproject.toml)

Standard Python packages follow this directory structure:

```
Package-Name/
├── pyproject.toml          # Project metadata and dependencies
├── uv.lock                 # Locked dependencies (UV)
├── poetry.lock             # Locked dependencies (Poetry)
├── README.md               # Package-specific documentation
├── .env.example            # Environment variable template
├── credentials.json        # API credentials (gitignored, if needed)
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── main.py         # Entry point
│       ├── crew.py         # Crew definition with @CrewBase decorator
│       ├── config/
│       │   ├── agents.yaml # Agent configurations
│       │   └── tasks.yaml  # Task configurations
│       └── tools/          # Custom tool implementations (optional)
│           ├── __init__.py
│           └── custom_tool.py
```

**Key Features**:
- Code separated from configuration (YAML files)
- Dependency management with `pyproject.toml`
- Entry point via `uv run <package-name>` or `poetry run <package-name>`
- Custom tools in dedicated `tools/` directory
- Crew defined with `@CrewBase` decorator and `@agent`, `@task`, `@crew` methods

## Standalone Python Structure (requirements.txt)

Alternative structure without pyproject.toml:

```
Project-Name/
├── requirements.txt        # Dependencies
├── main.py                 # Entry point and execution
├── agents.py               # Agent definitions
├── tasks.py                # Task definitions
└── tools/                  # Custom tools (optional)
    ├── __init__.py
    └── custom_tool.py
```

**Key Features**:
- Direct agent and task instantiation in .py files (no YAML)
- Run with: `python main.py`
- Simple structure for smaller projects
- Example: Meeting_Preparation_Assistant

## Flow Package Structure (crewAI Flows)

Flow packages use state management and decorators for complex orchestration:

```
Flow-Name/
├── pyproject.toml          # Project metadata and dependencies
├── uv.lock                 # Locked dependencies
├── README.md               # Flow-specific documentation
├── .env.example            # Environment variable template
├── credentials.json        # API credentials (gitignored, for Gmail/Slack/etc)
├── src/
│   └── flow_name/
│       ├── __init__.py
│       ├── main.py         # Flow definition with @start, @listen, @router
│       ├── types.py        # State type definitions
│       ├── crews/          # Multiple crew definitions
│       │   └── crew_name/
│       │       ├── crew.py
│       │       └── config/
│       ├── tools/          # Custom tools
│       │   └── custom_tool.py
│       └── utils/          # Utility functions
│           └── helpers.py
```

**Key Features**:
- Entry point via `uv run kickoff` (runs continuously as background worker)
- State management with decorators: `@start`, `@listen`, `@router`
- Can orchestrate multiple crews within a single flow
- Designed for event-driven, long-running processes
- Example structure in Email_Auto_Responder_Flow:
  - `main.py`: Contains flow logic with state transitions
  - `crews/email_filter_crew/`: Crew for email filtering and response generation
  - `tools/`: Custom Gmail API integration tools
  - `types.py`: Defines state structure (EmailState, etc.)

## Common Tools Used

### crewAI Tools

- `SerperDevTool()`: Web search capabilities (requires SERPER_API_KEY)
- `ScrapeWebsiteTool()`: Extract content from URLs
- `FileReadTool(file_path="path.md")`: Read local files
- `DirectoryReadTool(directory="./path")`: Read directory contents
- `MDXSearchTool(mdx="path.md")`: Semantic search within markdown files

**Tool Usage Pattern in Notebooks**:
```python
from crewai_tools import SerperDevTool, FileReadTool

search_tool = SerperDevTool()
file_tool = FileReadTool(file_path="./resume.md")

agent = Agent(
    role="Researcher",
    tools=[search_tool, file_tool],
    # ... other parameters
)
```

**Tool Usage Pattern in Python Packages**:
```python
# src/package_name/tools/custom_tool.py
from crewai_tools import BaseTool

class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis Tool"
    description: str = "Analyzes sentiment of text"

    def _run(self, text: str) -> str:
        # Custom logic
        return "positive"
```

### Integration Notes

- Tasks can reference variables using `{variable_name}` syntax
- Variables are provided via the `inputs` parameter in `crew.kickoff()`
- Task outputs can serve as context for subsequent tasks using the `context` parameter
- `async_execution=True` allows tasks to run in parallel when they don't depend on each other

## Key Concepts

### Agent Collaboration Modes

- **Sequential**: Tasks execute in order, each receiving the previous task's output
- **Hierarchical**: A manager agent delegates and coordinates work among specialist agents
- **Parallel**: Independent tasks execute simultaneously using `async_execution=True`

### Memory System

When `memory=True` is set on a Crew:
- Short-term memory: Recent task outputs and interactions
- Long-term memory: Learning from past executions
- Entity memory: Recognition of key entities across conversations

### Task Dependencies

Tasks can be chained using the `context` parameter:
```python
task3 = Task(
    description="...",
    expected_output="...",
    agent=agent3,
    context=[task1, task2]  # Will wait for these to complete
)
```

## Project-Specific Patterns

### Notable Alpine Projects

#### Article_Automation (IT - Notebook)
- **Pattern**: Sequential collaboration (Content Planner → Writer → Editor)
- **Key Learning**: Basic sequential task flow with context passing
- **Output**: Blog article in markdown format
- **Location**: `Alpine/Information-Technology-Department/Article_Automation/`

#### Job_Application_Booster (HR - Notebook)
- **Pattern**: Parallel + Sequential hybrid
- **Agents**: Tech Job Researcher, Personal Profiler, Resume Strategist, Interview Preparer
- **Key Learning**: Async task execution where research tasks run in parallel
- **Output**: `tailored_resume.md`, `interview_materials.md`
- **Location**: `Alpine/Human-Resources-Department/Job_Application_Booster/`

#### Customer_Outreach_Campaign (Operations - Notebook)
- **Pattern**: Sequential with file-based resources
- **Key Learning**: Using external instruction files from `instructions/` directory
- **Supporting Files**: Enterprise, small business, and tech startup templates
- **Output**: Personalized outreach campaigns
- **Location**: `Alpine/Operations-Department/Customer_Outreach_Campaign/`

#### Event_Planning_Automation (HR - Notebook)
- **Pattern**: Parallel tasks with human input
- **Agents**: Venue Coordinator, Logistics Manager, Marketing Agent
- **Key Learning**: Async execution, human approval with `human_input=True`
- **Output**: `venue_details.json`, `marketing_report.md`
- **Location**: `Alpine/Human-Resources-Department/Event_Planning_Automation/`

#### Meeting_Preparation_Assistant (HR - Standalone Python)
- **Pattern**: Traditional Python with agents.py, tasks.py, main.py structure
- **Key Learning**: Alternative to pyproject.toml packages, uses requirements.txt
- **Tools**: Custom ExaSearchTool for enhanced web search
- **Location**: `Alpine/Human-Resources-Department/Meeting_Preparation_Assistant/`

### Alpine Production Projects (Python Packages with pyproject.toml)

#### Banking_Recruitment_Automation (HR)
- **Pattern**: Multi-step recruitment workflow with LinkedIn integration
- **Agents**: Researcher, Profiler, Coordinator, Interviewer
- **Tools**: Custom LinkedIn scraping tool (Selenium)
- **Setup**: Requires LinkedIn cookie (`LI_AT`) in `.env`
- **Commands**:
  ```bash
  cd Alpine/Human-Resources-Department/Banking_Recruitment_Automation
  uv sync
  uv run recruitment
  uv run train 5  # Training mode
  ```
- **Location**: `Alpine/Human-Resources-Department/Banking_Recruitment_Automation/`

#### Email_Auto_Responder_Flow (Flow)
- **Pattern**: Continuous background worker using Flows
- **Flow Steps**:
  1. Fetch new emails via Gmail API
  2. Generate draft responses for each email
- **Setup**: Requires Gmail API `credentials.json`
- **Commands**:
  ```bash
  cd Alpine-Flows/Email_Auto_Responder_Flow
  uv sync
  # Add credentials.json to root
  uv run kickoff
  ```
- **Location**: `Alpine-Flows/Email_Auto_Responder_Flow/`

#### Policy_Document_Validator (IT)
- **Pattern**: Markdown validation and compliance checking
- **Use Case**: Validate banking policy documents against standards
- **Commands**:
  ```bash
  cd Alpine/Information-Technology-Department/Policy_Document_Validator
  uv sync
  uv run markdown_validator
  ```
- **Location**: `Alpine/Information-Technology-Department/Policy_Document_Validator/`

#### VIP_Client_Experience_Planner (Operations)
- **Pattern**: Luxury experience design for high-value banking clients
- **Use Case**: Plan exclusive events and experiences
- **Commands**:
  ```bash
  cd Alpine/Operations-Department/VIP_Client_Experience_Planner
  uv sync
  uv run surprise_trip
  ```
- **Location**: `Alpine/Operations-Department/VIP_Client_Experience_Planner/`

## Modifying Projects

### Modifying Jupyter Notebooks

When creating or modifying agents in notebooks:
1. Define clear, specific roles (more specific = better performance)
2. Write actionable goals that guide decision-making
3. Provide detailed backstory for context
4. Assign only relevant tools to avoid agent confusion

When creating or modifying tasks in notebooks:
1. Use detailed descriptions with step-by-step instructions
2. Specify exact output format in `expected_output`
3. Use variable placeholders for dynamic inputs
4. Set appropriate task dependencies via `context`

### Modifying Python Packages

**To modify agent configuration**:
```bash
# Edit YAML file
vim src/<package>/config/agents.yaml

# Changes apply immediately on next run
uv run <package-name>
```

**To modify task configuration**:
```bash
# Edit YAML file
vim src/<package>/config/tasks.yaml

# Changes apply immediately on next run
uv run <package-name>
```

**To add custom tools**:
```python
# src/<package>/tools/my_tool.py
from crewai_tools import BaseTool

class MyCustomTool(BaseTool):
    name: str = "My Custom Tool"
    description: str = "What this tool does"

    def _run(self, argument: str) -> str:
        # Implementation
        return result
```

```yaml
# src/<package>/config/agents.yaml
my_agent:
  role: "Analyst"
  tools:
    - my_custom_tool  # Reference tool name
```

**To add dependencies**:
```bash
# Using UV
uv add <package-name>

# Using Poetry
poetry add <package-name>
```

## Working with Alpine Bank Automation Projects

### Creating New Banking Department Automations

**For Jupyter Notebooks**:
1. Navigate to department: `cd Alpine/<Department-Name>/`
2. Create project directory: `mkdir New_Project_Name`
3. Create notebook: `New_Project_Name.ipynb`
4. Copy `requirements.txt` from similar project
5. Follow crewAI patterns from training examples

**For Python Packages**:
1. Navigate to department: `cd Alpine/<Department-Name>/`
2. Create new package:
   ```bash
   crewai create <package-name>
   cd <package-name>
   ```
3. Modify `config/agents.yaml` and `config/tasks.yaml`
4. Implement custom tools in `tools/` if needed
5. Update `.env.example` with required keys

### Banking-Specific Considerations

Include these in all banking automation projects:
- **Regulatory compliance**: Ensure agents cite regulatory sources
- **Data privacy**: Never hardcode credentials, use `.env` files
- **Audit logging**: Enable verbose mode, log all decisions
- **Error handling**: Graceful failures for financial data
- **Bias reduction**: Structured evaluation for HR projects
- **Security**: Secure API key management, encrypted credentials

### Adapting Projects for Banking Use Cases

Existing Alpine projects can be adapted for new banking operations:
- **Article_Automation** (IT) → Internal policy documentation, regulatory updates
- **Job_Application_Booster** (HR) → Resume screening, candidate assessment
- **Customer_Outreach_Campaign** (Ops) → Product marketing, customer retention
- **Stock_Analysis_Automation** (Ops) → Investment advisory, portfolio analysis
- **Event_Planning_Automation** (HR) → Client events, corporate retreats
- **Banking_Recruitment_Automation** (HR) → Talent acquisition, onboarding workflows
- **Employer_Branding_Automation** (HR) → Employer branding, talent marketing
- **Meeting_Preparation_Assistant** (HR) → Client meetings, board preparation
- **VIP_Client_Experience_Planner** (Ops) → Luxury banking services, private client events

### Department-Specific Considerations

- **Operations**: Accuracy, reconciliation, fraud detection
- **HR**: Fairness, bias reduction, structured evaluation
- **IT**: Security, incident response, documentation

## Best Practices

### Agent Design

- **Role specificity matters**: "FINRA approved financial analyst" > "financial analyst"
- **Backstory provides context**: Include industry expertise, years of experience
- **Tool assignment**: Only assign tools relevant to the agent's role
- **Delegation**: Set `allow_delegation=False` for specialists, `True` for hierarchical

### Task Design

- **Step-by-step descriptions**: Break down complex tasks into numbered steps
- **Quantifiable outputs**: Specify exact format (e.g., "4 paragraph article")
- **Variable placeholders**: Use `{variable_name}` syntax
- **Context dependencies**: Use `context=[task1, task2]` for task chaining
- **Output files**: Specify `output_file="result.md"` to persist results

### Execution Patterns

- **Sequential**: Default mode, tasks execute in order
- **Parallel**: Set `async_execution=True` on independent tasks
- **Hierarchical**: Requires `process=Process.hierarchical` and `manager_llm`

### Debugging Tips

- Set `verbose=True` on Agent and Crew for detailed logs
- Test individual tasks: `task.execute()` before full crew
- Check agent config: `print(agent.role, agent.goal, agent.tools)`
- Use `verbose=2` on Crew for maximum logging

### Common Pitfalls

- **Missing API keys**: Always set `OPENAI_API_KEY`, `OPENAI_MODEL_NAME`, `SERPER_API_KEY`
- **Tool conflicts**: Avoid assigning too many tools to a single agent
- **Context fading**: In long chains, use hierarchical or explicit `context`
- **Task order**: In sequential mode, order matters; ensure dependencies are correct
- **Python version**: Must be 3.10-3.13; check with `python --version`
- **Environment files**: Copy `.env.example` to `.env` in package root
- **Locked dependencies**: Run `uv sync` or `poetry install` after cloning

## Testing Projects

### Testing Jupyter Notebooks

```python
# In notebook cell
# Test individual task
task_output = task.execute()
print(task_output)

# Test agent configuration
print(f"Role: {agent.role}")
print(f"Goal: {agent.goal}")
print(f"Tools: {[tool.name for tool in agent.tools]}")
```

### Testing Python Packages

```bash
# Run in test mode with verbose logging
cd Alpine/<Department>/<Package-Name>
uv run <package-name> --verbose

# Check configuration
cat src/<package>/config/agents.yaml
cat src/<package>/config/tasks.yaml

# Validate environment
cat .env  # Ensure all keys are set
```

### Training Mode

For packages with training support:
```bash
# Train for N iterations to optimize agent performance
uv run train <iterations>

# Example: Train recruitment crew for 5 iterations
cd Alpine/Human-Resources-Department/Banking_Recruitment_Automation
uv run train 5

# Training stores learned patterns in memory system
```

## Repository Organization

```
crewAI-Banking-Automation/
├── Alpine/
│   ├── Human-Resources-Department/    (9 projects: 5 packages, 1 standalone, 1 script, 2 notebooks)
│   ├── Operations-Department/         (4 projects: 2 packages, 2 notebooks)
│   └── Information-Technology-Department/ (3 projects: 2 packages, 1 notebook)
├── Alpine-Flows/                      (4 flow packages: 3 active, 1 placeholder)
├── README.md                          (crewAI educational content)
└── CLAUDE.md                          (this file)
```

**Total**: 16 Alpine projects + 4 Flow packages across 3 departments

## Quick Reference

### Running Projects

**Jupyter Notebooks**:
```bash
cd Alpine/<Department>/<Project-Name>
pip install -r requirements.txt
jupyter notebook <project>.ipynb
# Execute cells sequentially from top to bottom
```

**Python Packages**:
```bash
cd Alpine/<Department>/<Package-Name>
cp .env.example .env && vim .env  # Add API keys
uv sync
uv run <package-name>              # Normal execution
uv run train <iterations>          # Training mode (if supported)
```

**Standalone Python** (Meeting_Preparation_Assistant):
```bash
cd Alpine/Human-Resources-Department/Meeting_Preparation_Assistant
pip install -r requirements.txt
python main.py                     # Set env vars in code or export
```

**Flow Packages**:
```bash
cd Alpine-Flows/<Flow-Name>
cp .env.example .env && vim .env   # Add API keys
uv sync
uv run kickoff                     # Runs continuously
```

### Useful Commands

```bash
# Check Python version
python --version                   # Must be 3.10-3.13

# Find all packages
find Alpine -name "pyproject.toml" -type f

# Find all notebooks
find Alpine -name "*.ipynb" -type f
```

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'crewai'`
**Fix**: Run `pip install crewai` or `uv sync` in package directory

**Issue**: `OpenAI API key not found`
**Fix**: Set `OPENAI_API_KEY` in notebook or `.env` file

**Issue**: `Python version incompatible`
**Fix**: Use Python 3.10-3.13; check with `python --version`

**Issue**: `uv: command not found`
**Fix**: Install UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`

**Issue**: LinkedIn tool not working
**Fix**: Update `LI_AT` cookie in `.env` (expires periodically)

**Issue**: Gmail API authentication failed
**Fix**: Regenerate `credentials.json` from Google Cloud Console
