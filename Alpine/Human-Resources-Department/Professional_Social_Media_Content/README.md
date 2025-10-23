# AI Crew for Professional Banking Social Media Content
## Introduction
This project uses the CrewAI framework to automate the creation of professional social media content for banking and financial services. CrewAI orchestrates autonomous AI agents to collaborate on generating engaging, compliant content for LinkedIn and Twitter platforms.

## Project Focus: Tactical Social Media Execution

**Purpose**: This project focuses on **tactical execution** of professional social media content for day-to-day banking communications. It generates individual posts, announcements, and content pieces for LinkedIn and Twitter.

**Use Case**: Use this when you need to:
- Create daily social media posts
- Announce banking products or services
- Generate corporate communications content
- Produce compliance-aware social media copy

**Complementary Project**: For strategic employer branding campaigns, see `Employer_Branding_Automation`.

- [CrewAI Framework](#crewai-framework)
- [Running the script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Using Local Models with Ollama](#using-local-models-with-ollama)
- [License](#license)

## CrewAI Framework
CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to generate professional, compliant social media content suitable for banking industry standards on LinkedIn and Twitter.

## Running the Script
This example uses OpenHermes 2.5 through Ollama by default so you should to download [Ollama](ollama.ai) and [OpenHermes](https://ollama.ai/library/openhermes).

You can change the model by changing the `MODEL` env var in the `.env` file.

- **Configure Environment**: Copy ``.env.example` and set up the environment variables for [Browseless](https://www.browserless.io/), [Serper](https://serper.dev/).
- **Install Dependencies**: Run `poetry install --no-root` (uses crewAI==0.130.0).
- **Execute the Script**: Run `python main.py` and input your banking topic/announcement.

## Details & Explanation
- **Running the Script**: Execute `python main.py`` and input your banking topic when prompted. The script will leverage the CrewAI framework to generate professional social media content for LinkedIn and Twitter.
- **Key Components**:
  - `./main.py`: Main script file.
  - `./tasks.py`: Main file with the tasks prompts.
  - `./agents.py`: Main file with the agents creation.
  - `./tools/`: Contains tool classes used by the agents.

## Using Local Models with Ollama
This example run entirely local models, the CrewAI framework supports integration with both closed and local models, by using tools such as Ollama, for enhanced flexibility and customization. This allows you to utilize your own models, which can be particularly useful for specialized tasks or data privacy concerns.

### Setting Up Ollama
- **Install Ollama**: Ensure that Ollama is properly installed in your environment. Follow the installation guide provided by Ollama for detailed instructions.
- **Configure Ollama**: Set up Ollama to work with your local model. You will probably need to [tweak the model using a Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md), I'd recommend playing with `top_p` and `temperature`.

## License
This project is released under the MIT License.
