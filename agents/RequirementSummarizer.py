from langchain_openai import ChatOpenAI
from crewai import Agent


class RequirementSummarizer(Agent):
    def __init__(self):
        super().__init__(
            role="Requirement Summarizer",
            goal="Summarize API requirements for test automation",
            backstory="The system needs a summarized description of API requirements for effective test case generation.",
            llm=ChatOpenAI(model="gpt-3.5-turbo"),
            verbose=True
        )
