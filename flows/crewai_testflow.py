from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from crewai import Task, Crew
from agents.RequirementSummarizer import RequirementSummarizer
from agents.TestCaseGenerator import TestCaseGenerator
from agents.GapAnalyzer import GapAnalyzer

requirement_summarizer = RequirementSummarizer()
test_case_generator = TestCaseGenerator()
gap_analyzer = GapAnalyzer()

# requirement summarization
summarize_task = Task(
    description="Summarize this API requirement: 'POST /createUser should accept name, email, and password. Validate inputs and return a success or error response.'",
    expected_output="A bullet-point summary with input fields, validations, and expected response.",
    agent=requirement_summarizer
)

# Test Case Generation
generate_tests_task = Task(
    description="Based on the summary from the previous task, generate 5 functional and edge test cases.",
    expected_output="List of test cases with title, steps, and expected result.",
    agent=test_case_generator
)

# Gap Analysis
gap_analysis_task = Task(
    description="Review the test cases above and suggest any missing test scenarios.",
    expected_output="List of uncovered scenarios or recommendations.",
    agent=gap_analyzer
)

crew = Crew(
    agents=[requirement_summarizer, test_case_generator, gap_analyzer],  # Pass instantiated agents
    tasks=[summarize_task, generate_tests_task, gap_analysis_task],
    verbose=True
)

result = crew.kickoff()
print("\n Output:\n", result)
