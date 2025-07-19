from tools.time_scheduler import create_schedule
from utils.gemini import get_motivational_quote

def generate_study_plan(start=8, end=20, topic="focus"):
    schedule = create_schedule(start, end)
    quote = get_motivational_quote(topic)
    return schedule, quote