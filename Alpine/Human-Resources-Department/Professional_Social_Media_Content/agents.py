import os
from textwrap import dedent
from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from langchain.agents import load_tools

from langchain.llms import Ollama

class MarketingAnalysisAgents:
	def __init__(self):
		self.llm = Ollama(model=os.environ['MODEL'])

	def product_competitor_agent(self):
		return Agent(
			role="Lead Market Analyst",
			goal=dedent("""\
				Conduct amazing analysis of the products and
				competitors, providing in-depth insights to guide
				marketing strategies."""),
			backstory=dedent("""\
				As the Lead Market Analyst at a premier
				digital marketing firm, you specialize in dissecting
				online business landscapes."""),
			tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet
			],
			allow_delegation=False,
			llm=self.llm,
			verbose=True
		)

	def strategy_planner_agent(self):
		return Agent(
			role="Chief Banking Marketing Strategist",
			goal=dedent("""\
				Synthesize insights from banking product analysis
				to formulate compliant marketing strategies for financial services."""),
			backstory=dedent("""\
				You are the Chief Marketing Strategist at
				a leading banking institution, known for crafting
				compliant, professional strategies for financial products."""),
			tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_linkedin,
					SearchTools.search_twitter
			],
			llm=self.llm,
			verbose=True
		)

	def creative_content_creator_agent(self):
		return Agent(
			role="Banking Social Media Content Specialist",
			goal=dedent("""\
				Develop professional and compliant content
				for LinkedIn and Twitter campaigns, focusing on
				banking products while maintaining regulatory compliance."""),
			backstory=dedent("""\
				As a Banking Social Media Content Specialist at
				Alpine Capital Bank, you excel in crafting professional
				narratives that resonate with banking clients and professionals.
				Your expertise lies in turning financial product features
				into engaging, compliant content for LinkedIn and Twitter that
				maintains the appropriate tone for financial services."""),
			tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_linkedin,
					SearchTools.search_twitter
			],
			llm=self.llm,
			verbose=True
		)

	def senior_photographer_agent(self):
		return Agent(
				role="Banking Visual Content Specialist",
				goal=dedent("""\
					Create professional visual concepts for banking social media
					that convey trust, professionalism, and financial expertise."""),
				backstory=dedent("""\
					As a Banking Visual Content Specialist at Alpine Capital Bank,
					you are an expert at creating professional imagery concepts that
					align with banking brand standards and regulatory requirements.
					You work on campaigns for banking products ensuring all visuals
					maintain the appropriate professional tone."""),
				tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_linkedin,
					SearchTools.search_twitter
				],
				llm=self.llm,
				allow_delegation=False,
				verbose=True
		)

	def chief_creative_diretor_agent(self):
		return Agent(
				role="Chief Banking Marketing Officer",
				goal=dedent("""\
					Oversee banking marketing content to ensure compliance,
					professional standards, and alignment with banking regulations.
					Review, approve, ask clarifying questions or delegate follow up work
					to ensure all content meets financial services requirements."""),
				backstory=dedent("""\
					You're the Chief Marketing Officer at Alpine Capital Bank
					specialized in financial services branding. You're working on
					banking product campaigns, ensuring your team crafts compliant,
					professional content that meets regulatory standards."""),
				tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_linkedin,
					SearchTools.search_twitter
				],
				llm=self.llm,
				verbose=True
		)
