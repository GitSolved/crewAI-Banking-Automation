# crewAI Framework Tutorial

Comprehensive guide to understanding and building multi-agent AI systems using the crewAI framework.

## Goal
Designing effective AI agents and organizing teams of AI agents to perform complex, multi-step tasks.

## Why AI Agents Are Better Than LLMs

### LLMs
Provide human feedback iteratively to fine-tune responses.

### AI Agents
When LLMs operate autonomously, they become agents. AI Agents ask and answer questions on their own.

**LLMs + Cognition = AI Agents**

## What is crewAI?

Framework for building multi-agent systems that are autonomous, role-playing, and collaborative.

**Crew**: A team of AI agents working together, each with a specific role.

## Why Multi-Agent Systems Rather Than Single Agent?

1. **Specialized Roles**: Assign specific roles and tasks to each agent for improved output. Example: One agent does exhaustive research while another does professional writing.
2. **LLM Flexibility**: Use different LLMs for specific tasks based on their strengths.

## Applications of Multi-Agent Systems

- Resume Strategist: Tailor resumes and interview prep
- Design, build and test websites
- Research, write and fact-check technical papers
- Automate customer support inquiries
- Conduct social media campaigns
- Perform financial analysis

## What is Agentic Automation?

A new way to write software. Provide fuzzy inputs, apply fuzzy transformations and get fuzzy outputs.

The reason people love ChatGPT: **Probabilistic nature**

## How Agentic Automation Improves Regular Automation

### Regular Automation (Regular Data Collection and Analysis)

- Capture information about the company
- Use classification to generate scores for company
- Prioritize for sales

### Agentic Automation (Data Collection and Analysis Using Crew)

- AI agent researches about company (via Google, internal database)
- AI agent compares companies (new ones, old ones)
- AI agent scores companies (based on parameters)
- AI agent provides intelligent questions to ask based on scores

## Key Components of AI Agent

- **Role**: Assign specialized roles to agents
- **Memory**: Provide agents with short-term, long-term and entity memory
- **Tools**: Assign pre-built and custom tools to each agent (e.g., for web search)
- **Focus**: Break down tasks, goals and tools and assign to multiple AI agents for better performance
- **Guardrails**: Effectively handle errors, hallucinations and infinite loops
- **Cooperation**: Perform tasks in series, in parallel and hierarchical fashion

### Role Playing

More specific role = Better response. Gives clear idea about agent's function in the crew.

**Example**: "You are a financial analyst" vs "You are a FINRA-approved financial analyst"

```python
from crewai import Agent

agent = Agent(
  role='Data Analyst',
  goal='Extract actionable insights',
  backstory="""You're a data analyst at a large company.
  You're responsible for analyzing data and providing insights
  to the business."""
)
```

### Focus

Assigning too many tasks, tools, or context to a single agent can cause loss of essential information and hallucination.

Therefore, break down tasks, goals and tools and assign to multiple AI agents for better performance.

```python
research_ai_task = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news',
    agent=research_agent,
    tools=[search_tool]
)

research_ops_task = Task(
    description='Find and summarize the latest AI Ops news',
    expected_output='A bullet list summary of the top 5 most important AI Ops news',
    agent=research_agent,
    tools=[search_tool]
)

write_blog_task = Task(
    description="Write a full blog post about the importance of AI and its latest news",
    expected_output='Full blog post that is 4 paragraphs long',
    agent=writer_agent,
    context=[research_ai_task, research_ops_task]
)
```

### Tools

Assign tools to AI Agents and Tasks for improving execution and performance.

```python
from crewai import Agent

researcher = Agent(
    role='Market Research Analyst',
    goal='Provide up-to-date market analysis of the AI industry',
    backstory='An expert analyst with a keen eye for market trends.',
    tools=[search_tool, web_rag_tool]
)
```

**Note**: Task-specific tools override an agent's default tools.

```python
task = Task(
  description='Find and summarize the latest AI news',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[search_tool]
)
```

### Collaboration

Agents collaborate to combine skills, share information, and delegate tasks to each other.

#### Sequential Collaboration

Ideal for projects requiring tasks to be completed in a specific order.

```python
report_crew = Crew(
  agents=[researcher, analyst, writer],
  tasks=[research_task, analysis_task, writing_task], # Tasks executed in order
  process=Process.sequential
)
```

#### Hierarchical Collaboration

- CrewAI automatically creates a manager agent, requiring specification of a manager language model (manager_llm)
- The manager allocates tasks among crew members based on their roles, tools and capabilities
- The manager evaluates outcomes to ensure they meet required standards
- Set Process attribute to `Process.hierarchical` for Crew object
- Set `manager_llm` for Crew Object (mandatory for hierarchical process)

```python
from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI

# Example: Creating a crew with a hierarchical process
# Ensure to provide a manager_llm
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-4")
)
```

#### Parallel Collaboration

Tasks can be executed asynchronously, allowing for parallel processing and efficiency improvements.

```python
list_ideas = Task(
    description="List of 5 interesting ideas to explore for an article about AI.",
    expected_output="Bullet point list of 5 ideas for an article.",
    agent=researcher,
    async_execution=True # Will be executed asynchronously
)

list_important_history = Task(
    description="Research the history of AI and give me the 5 most important events.",
    expected_output="Bullet point list of 5 important events.",
    agent=researcher,
    async_execution=True # Will be executed asynchronously
)

write_article = Task(
    description="Write an article about AI, its history, and interesting ideas.",
    expected_output="A 4 paragraph article about AI.",
    agent=writer,
    context=[list_ideas, list_important_history] # Waits for both tasks
)
```

### Guardrails

Implemented at framework level to prevent hallucinations, errors and infinite loops.

### Memory

CrewAI provides short-term memory, long-term memory, entity memory, and contextual memory to help AI agents remember, reason, and learn from past interactions.

**Advantages of Memory**:
- **More contextual awareness**, leading to more coherent and relevant responses
- **Experience accumulation**, learning from past actions to improve future decision-making and problem-solving
- **Entity understanding**, agents can recognize and remember key entities, enhancing understanding

Enable memory by setting `memory=True` in the Crew object's arguments.

```python
from crewai import Crew, Agent, Task, Process

# Assemble your crew with memory capabilities
my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True
)
```

## Mental Framework for Agent Creation

Think of yourself as a **Manager**.

Answer 3 questions:
1. What is the Goal?
2. What is the Process?
3. What kind of people would I like to hire to get the work done?

This will help create agents (roles, goals, backstory).

## What Makes a Great Tool?

- **Versatile**: Handle fuzzy inputs and provide strongly typed outputs
- **Caching Mechanism**: Reuse previous results. Caching layer prevents unnecessary requests, stays within rate limits, speeds up execution time
- **Error Handling**: Gracefully handle errors and exceptions by sending error messages to agent and asking agent to retry

**Note**: CrewAI supports both crewAI Toolkit and LangChain Tools.

## Mental Framework for Task Creation

Think of yourself as a **Manager**.

Ask what kind of process and tasks you expect individuals on your team to do.

Task requires minimum 3 things:
1. `description`
2. `expected_output`
3. `agent` that will perform the task

## Multi-Agent Collaboration Patterns

### Problem with Sequential Collaboration

Initial context fades away as tasks flow from agent to agent.

### Advantages of Hierarchical Collaboration

- Manager always remembers initial goal
- Automatically delegates tasks
- Asks agents for further improvement if required

---

For practical implementation examples, see the projects in this repository's `Alpine/` and `Alpine-Flows/` directories.
