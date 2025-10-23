from crewai import Task
from textwrap import dedent

class MarketingAnalysisTasks:
	def product_analysis(self, agent, product_website, product_details):
		return Task(description=dedent(f"""\
			Analyze the given product website: {product_website}.
			Extra details provided by the customer: {product_details}.

			Focus on identifying unique features, benefits,
			and the overall narrative presented.

			Your final report should clearly articulate the
			product's key selling points, its market appeal,
			and suggestions for enhancement or positioning.
			Emphasize the aspects that make the product stand out.

			Keep in mind, attention to detail is crucial for
			a comprehensive analysis. It's currenlty 2024.
			"""),
			agent=agent
		)

	def competitor_analysis(self, agent, product_website, product_details):
		return Task(description=dedent(f"""\
			Explore competitor of: {product_website}.
			Extra details provided by the customer: {product_details}.

			Identify the top 3 competitors and analyze their
			strategies, market positioning, and customer perception.

			Your final report MUST include BOTH all context about {product_website}
			and a detailed comparison to whatever competitor they have competitors.
			"""),
			agent=agent
		)

	def campaign_development(self, agent, product_website, product_details):
		return Task(description=dedent(f"""\
			You're creating a targeted marketing campaign for: {product_website}.
			Extra details provided by the customer: {product_details}.

			To start this campaing we will need a strategy and creative content ideas.
			It should be meticulously designed to captivate and engage
			the product's target audience.

			Based on your ideas your co-workers will create the content for the campaign.

			Your final answer MUST be ideas that will resonate with the audience and
			also include ALL context you have about the product and the customer.
			"""),
			agent=agent
		)

	def social_media_content(self, agent):
		return Task(description=dedent("""\
			Craft professional social media content for LinkedIn and Twitter.
			The content should be professional, informative, and compliant
			with banking industry standards while being engaging.

			Focus on creating messages that resonate with
			banking professionals and clients while highlighting
			key features and maintaining regulatory compliance.

			Content must be professional and should encourage engagement
			through likes, shares, and comments while maintaining
			the appropriate tone for financial services.

			Your final answer MUST be 3 options each for LinkedIn and Twitter (6 total posts):
			- 3 LinkedIn posts (professional, detailed, suitable for B2B audience)
			- 3 Twitter posts (concise, engaging, under 280 characters)
			All content must be compliant with financial services marketing standards.
			"""),
			agent=agent
		)

	def take_photograph_task(self, agent, copy, product_website, product_details):
		return Task(description=dedent(f"""\
			You are working on a new campaign for a super important customer,
			and you MUST take the most amazing photo ever for an instagram post
			regarding the product, you have the following copy:
			{copy}

			This is the product you are working with: {product_website}.
			Extra details provided by the customer: {product_details}.

			Imagine what the photo you wanna take describe it in a paragraph.
			Here are some examples for you follow:
			- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Think creatively and focus on how the image can capture the audience's
			attention. Don't show the actual product on the photo.

			Your final answer must be 3 options of photographs, each with 1 paragraph
			describing the photograph exactly like the examples provided above.
			"""),
			agent=agent
		)

	def review_photo(self, agent, product_website, product_details):
		return Task(description=dedent(f"""\
			Review the photos you got from the senior photographer.
			Make sure it's the best possible and aligned with the product's goals,
			review, approve, ask clarifying question or delegate follow up work if
			necessary to make decisions. When delegating work send the full draft
			as part of the information.

			This is the product you are working with: {product_website}.
			Extra details provided by the customer: {product_details}.

			Here are some examples on how the final photographs should look like:
			- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
			- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Your final answer must be 3 reviewed options of photographs,
			each with 1 paragraph description following the examples provided above.
			"""),
			agent=agent
		)