
# AI Crew for Employer Branding Automation
## Introduction
This project demonstrates the use of the CrewAI framework to automate the creation of employer branding and talent marketing strategies. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

## Project Focus: Strategic Employer Branding

**Purpose**: This project focuses on **strategic planning** for employer branding and talent acquisition marketing campaigns. It develops comprehensive strategies, brand positioning, and campaign frameworks.

**Use Case**: Use this when you need to:
- Develop overall employer branding strategy
- Plan talent marketing campaigns
- Create brand positioning for recruitment
- Design comprehensive talent acquisition frameworks

**Complementary Project**: For tactical execution of individual social media posts, see `Professional_Social_Media_Content`.

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Contributing](#contributing)
- [Support and Contact](#support-and-contact)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to create a comprehensive employer branding strategy and develop compelling talent marketing content.

## Running the Script
It uses GPT-4o by default so you should have access to that to run it.

***Disclaimer:** This will use gpt-4o unless you change it to use a different model, and by doing so it may incur in different costs.*

- **Configure Environment**: Copy `.env.example` and set up the environment variables for [OpenAI](https://platform.openai.com/api-keys) and other tools as needed, like [Serper](serper.dev).
- **Install Dependencies**: Run `poetry lock && poetry install`.
- **Customize**: Modify `src/employer_branding/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/employer_branding/config/agents.yaml` to update your agents and `src/employer_branding/config/tasks.yaml` to update your tasks.
- **Execute the Script**: Run `poetry run employer_branding` and input your project details.

## Details & Explanation
- **Running the Script**: Execute `poetry run employer_branding`. The script will leverage the CrewAI framework to generate a comprehensive employer branding strategy, including market analysis, strategic positioning, and campaign frameworks for talent acquisition.
- **Key Components**:
  - `src/employer_branding/main.py`: Main script file.
  - `src/employer_branding/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/employer_branding/config/agents.yaml`: Configuration file for defining agents.
  - `src/employer_branding/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/employer_branding/tools`: Contains tool classes used by the agents.

## License
This project is released under the MIT License.
