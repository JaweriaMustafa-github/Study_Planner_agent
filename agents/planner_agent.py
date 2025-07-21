from tools.time_scheduler import create_schedule
from utils.gemini import get_motivational_quote


def generate_study_plan(start=8, end=20, topic="focus"):
    # Directly get the schedule dictionary from time_scheduler
    # This already includes "date", "day", and "blocks"
    schedule = create_schedule(start, end)

    # Get a motivational quote using the Gemini tool
    quote = get_motivational_quote(topic)

    # Return both without modifying or wrapping the schedule again
    return schedule, quote
