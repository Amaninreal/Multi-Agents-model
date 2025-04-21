from crewai import Agent
from langchain_openai import ChatOpenAI

class GapAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            role="Gap Analyzer",
            goal="Identify missing or unaddressed test scenarios in generated test cases",
            backstory="Works like a test strategist, ensuring full coverage of use cases and edge cases.",
            verbose=True
        )

    def analyze_gaps(self, test_cases):
        model = ChatOpenAI(model="gpt-3.5-turbo")
        prompt = f"Review these test cases and suggest any missing test scenarios: {test_cases}"
        response = model.generate([prompt])
        return response[0]
