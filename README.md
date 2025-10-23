# crewAI Banking Automation

> Multi-agent AI automation workflows for Alpine Capital Bank operations - continuously improving

Production-ready automation projects using the [crewAI framework](https://github.com/crewAIInc/crewAI) to orchestrate autonomous AI agents across banking and financial services operations.

## Overview

This repository contains **23 specialized automation projects** designed for Alpine Capital Bank, organized across four departments:

- **Human Resources** (10 projects): Recruitment, training, employer branding, social media
- **Operations** (5 projects): Customer engagement, VIP services, financial analysis
- **Information Technology** (4 projects): Documentation, policy validation, landing pages
- **Flows** (3 projects): Advanced orchestration with email, leads, and meetings

Each project leverages multi-agent collaboration where specialized AI agents work together autonomously to complete complex, multi-step tasks.

## Key Features

- **Banking-Focused Context**: All agents operate within Alpine Capital Bank environment with appropriate financial services terminology
- **Production-Ready**: Python packages with YAML configuration, dependency management, and testing support
- **Dual Architecture**: Educational Jupyter notebooks + enterprise Python packages
- **Advanced Orchestration**: Flow-based state management for continuous background operations
- **Compliance-Aware**: Designed for banking regulatory requirements and audit trails

## Quick Start

### Prerequisites

- Python 3.10-3.13
- UV or Poetry package manager
- OpenAI API key (or compatible LLM endpoint)

### Installation

```bash
# Clone repository
git clone https://github.com/SecureYourGear/crewAI-Banking-Automation.git
cd crewAI-Banking-Automation

# Install UV (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Navigate to a project
cd Alpine/Human-Resources-Department/Banking_Recruitment_Automation

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run the automation
uv run recruitment
```

## Projects by Department

### Human Resources Department

| Project | Type | Description |
|---------|------|-------------|
| **Banking_Recruitment_Automation** | Python Package | Multi-agent recruitment workflow with LinkedIn integration and candidate profiling |
| **Job_Posting_Generator** | Python Package | Automated banking job posting creation optimized for financial roles |
| **Resume_Job_Matcher** | Python Package | AI-powered candidate-role matching with scoring system |
| **Employer_Branding_Automation** | Python Package | Strategic employer branding and talent marketing campaign development |
| **Professional_Social_Media_Content** | Standalone Python | Tactical social media content for LinkedIn/Twitter banking communications |
| **Meeting_Preparation_Assistant** | Standalone Python | Meeting prep, agenda creation, and briefing materials |
| **Corporate_Travel_Planner** | Standalone Python | Employee travel coordination and itinerary generation |
| **Training_Video_Script_Generator** | Standalone Python | Employee training content and script generation |
| **Event_Planning_Automation** | Jupyter Notebook | Banking events, conferences, and corporate retreat planning |
| **Job_Application_Booster** | Jupyter Notebook | Resume screening with structured evaluation and scorecards |

### Operations Department

| Project | Type | Description |
|---------|------|-------------|
| **VIP_Client_Experience_Planner** | Python Package | High-net-worth client experience design and luxury event planning |
| **Stock_Analysis_Automation** | Python Package | Advanced financial analysis and trading strategy development |
| **Customer_Outreach_Campaign** | Jupyter Notebook | Customer engagement campaigns with segment-specific messaging |
| **Customer_Support_Automation** | Jupyter Notebook | Automated support ticket handling and response generation |
| **Financial_Analysis** | Jupyter Notebook | Stock analysis with hierarchical agent collaboration |

### Information Technology Department

| Project | Type | Description |
|---------|------|-------------|
| **Policy_Document_Validator** | Python Package | Compliance policy validation for markdown format documents |
| **Landing_Page_Generator** | Python Package | Marketing page generation and A/B testing optimization |
| **Article_Automation** | Jupyter Notebook | Internal documentation and knowledge base article generation |

### Alpine Flows

Advanced orchestration using crewAI Flows for state management and continuous operation:

| Flow | Description |
|------|-------------|
| **Email_Auto_Responder_Flow** | Automated email checking and draft response generation (Gmail API) |
| **Lead_Score_Flow** | Lead qualification, scoring, and automated follow-up |
| **Meeting_Assistant_Flow** | Meeting coordination and automated follow-up tasks |

## Architecture

### Project Types

**Python Packages** (17 projects):
- YAML-based agent/task configuration
- Production-ready with `pyproject.toml`
- Dependency management via UV/Poetry
- Enterprise-scale deployment ready

**Standalone Python** (3 projects):
- Self-contained scripts with `requirements.txt`
- Agents and tasks defined in separate `.py` files
- Suitable for rapid prototyping

**Jupyter Notebooks** (3 projects):
- Educational and exploratory workflows
- Inline code with markdown documentation
- Great for learning crewAI patterns

**Flow Packages** (3 projects):
- Event-driven architecture with state management
- Background workers for continuous operation
- Advanced multi-crew orchestration

## Running Projects

### Python Packages

```bash
cd Alpine/<Department>/<Package-Name>
uv sync                    # Install dependencies
uv run <package-name>      # Run automation
uv run train 5             # Train mode (if supported)
```

### Standalone Python

```bash
cd Alpine/<Department>/<Project-Name>
pip install -r requirements.txt
python main.py
```

### Jupyter Notebooks

```bash
cd Alpine/<Department>/<Project-Name>
pip install -r requirements.txt
jupyter notebook <notebook-file>.ipynb
```

### Flow Packages

```bash
cd Alpine-Flows/<Flow-Name>
uv sync
# Add credentials.json if required (e.g., Gmail API)
uv run kickoff  # Runs continuously in background
```

## Configuration

All projects require environment variables:

```bash
# Create .env file in project root
OPENAI_API_KEY=your-key-here
OPENAI_MODEL_NAME=gpt-4-turbo  # or gpt-3.5-turbo
SERPER_API_KEY=your-key-here   # For web search tools
```

**Project-Specific Requirements**:
- **Banking_Recruitment_Automation**: LinkedIn cookie (`LI_AT`)
- **Email_Auto_Responder_Flow**: Gmail API `credentials.json`
- **Resume_Job_Matcher**: Vector database setup

## Documentation

- **[CLAUDE.md](./CLAUDE.md)**: Comprehensive development guide with architecture details, project structures, and development workflows
- **[CREWAI_TUTORIAL.md](./CREWAI_TUTORIAL.md)**: Complete crewAI framework tutorial with examples and best practices
- **Project READMEs**: Each project has its own README with specific setup and usage instructions

## Example Use Cases

### Recruitment Automation
```bash
cd Alpine/Human-Resources-Department/Banking_Recruitment_Automation
uv run recruitment
# Input: Job position and LinkedIn search criteria
# Output: Candidate profiles, interview materials, coordination plans
```

### VIP Client Experience
```bash
cd Alpine/Operations-Department/VIP_Client_Experience_Planner
uv run surprise_trip
# Input: Client preferences, destination, dates
# Output: Luxury itinerary with Michelin dining, exclusive activities
```

### Employer Branding Campaign
```bash
cd Alpine/Human-Resources-Department/Employer_Branding_Automation
uv run employer_branding
# Input: Company values, target talent demographics
# Output: Strategic branding campaign with positioning framework
```

## Development

### Adding Custom Tools

```python
# src/<package>/tools/my_tool.py
from crewai_tools import BaseTool

class BankingAnalysisTool(BaseTool):
    name: str = "Banking Analysis Tool"
    description: str = "Analyzes banking data"

    def _run(self, data: str) -> str:
        # Implementation
        return result
```

### Modifying Agent Configuration

```yaml
# src/<package>/config/agents.yaml
financial_analyst:
  role: "Senior Financial Analyst"
  goal: "Provide accurate financial insights for Alpine Capital Bank"
  backstory: "FINRA-approved analyst with 15 years in banking"
  tools:
    - serper_tool
    - banking_analysis_tool
```

## Technology Stack

- **Framework**: [crewAI](https://github.com/crewAIInc/crewAI) - Multi-agent orchestration
- **LLM**: OpenAI GPT-4 / GPT-3.5 (configurable)
- **Tools**: SerperDev (search), custom banking tools
- **Package Management**: UV, Poetry
- **Notebooks**: Jupyter
- **Version Control**: Git

## Repository Structure

```
crewAI-Banking-Automation/
├── Alpine/
│   ├── Human-Resources-Department/     # 10 HR automation projects
│   ├── Operations-Department/          # 5 operations projects
│   └── Information-Technology-Department/  # 4 IT projects
├── Alpine-Flows/                       # 3 flow-based orchestrations
├── CLAUDE.md                           # Comprehensive development guide
├── CREWAI_TUTORIAL.md                  # Framework tutorial
└── README.md                           # This file
```

## Best Practices

1. **Start with notebooks** for learning crewAI patterns
2. **Use Python packages** for production deployments
3. **Review CLAUDE.md** for architecture decisions
4. **Set `verbose=True`** during development for debugging
5. **Enable memory** (`memory=True`) for context retention
6. **Use hierarchical mode** for complex multi-step tasks

## License

MIT License - See individual project directories for specific licensing.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow existing project structure patterns
4. Ensure all agents reference Alpine Capital Bank
5. Test with `verbose=True` mode
6. Submit pull request

## Resources

- [crewAI Documentation](https://docs.crewai.com/)
- [crewAI GitHub](https://github.com/crewAIInc/crewAI)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [CLAUDE.md](./CLAUDE.md) - Repository-specific development guide
- [CREWAI_TUTORIAL.md](./CREWAI_TUTORIAL.md) - Framework tutorial

---

**Alpine Capital Bank** - Transforming banking operations through intelligent automation
