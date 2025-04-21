from crewai import Agent
from langchain_openai import ChatOpenAI


class TestCaseGenerator(Agent):
    def __init__(self):
        super().__init__(
            role="Test Case Generator",
            goal="Generate test cases based on summarized requirements",
            backstory="Skilled QA engineer with experience in writing functional and edge test cases.",
            verbose=True
        )

    def generate_test_cases(self, summary):
        model = ChatOpenAI(model="gpt-3.5-turbo")
        prompt = f"Generate test cases based on the summary: {summary}"
        response = model.generate([prompt])
        return response[0]
