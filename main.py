from mcp.server.fastmcp import FastMCP
from educhain.core.educhain import Educhain
from dotenv import load_dotenv
import json

load_dotenv() # Load environment variables

# Create an MCP server
mcp = FastMCP("EduChain")

# Instantiate Educhain
ec = Educhain()

# Tool: Generate MCQs
@mcp.tool()
def generate_mcqs(topic: str, num_questions: int) -> list:
    """Generate multiple-choice questions for a topic."""
    result = ec.qna_engine.generate_questions(topic, num=num_questions, question_type="Multiple Choice")
    mcqs = result.questions
    return [
        {
            "question": q.question,
            "options": q.options,
            "answer": q.answer,
            "explanation": q.explanation
        }
        for q in mcqs
    ]


# Resource: Lesson Plan
@mcp.resource("lessonplan://{topic}")
def get_lesson_plan(topic: str) -> dict:
    """Get a structured lesson plan for the given topic."""
    plan = ec.content_engine.generate_lesson_plan(topic)

    def simplify(obj):
        if isinstance(obj, list):
            return [simplify(i) for i in obj]
        elif hasattr(obj, "__dict__"):
            return {k: simplify(v) for k, v in obj.__dict__.items()}
        elif isinstance(obj, dict):
            return {k: simplify(v) for k, v in obj.items()}
        else:
            return obj

    return simplify(plan)

# Bonus tool - Flashcard Generator
@mcp.tool()
def generate_flashcards(topic: str, num_cards: int) -> list:
    """Generate flashcards for a topic."""
    result = ec.qna_engine.generate_questions(topic, num=num_cards, question_type="Flashcard")
    return [
        {
            "front": q.question,
            "back": q.answer
        }
        for q in result.questions
    ]