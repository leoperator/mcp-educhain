from main import get_lesson_plan

result = get_lesson_plan("Python")
import json
print(json.dumps(result, indent=2))
