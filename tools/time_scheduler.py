from datetime import datetime, timedelta

def create_schedule(start_hour=8, end_hour=20, study_block=2, break_block=1):
    schedule = []
    current_time = datetime.now().replace(hour=start_hour, minute=0)

    # Get today's date and weekday
    date_str = current_time.strftime("%Y-%m-%D")
    weekday_str = current_time.strftime("%A")

    while current_time.hour < end_hour:
        end_study = current_time + timedelta(hours=study_block)
        schedule.append({
            "type": "Study",
            "start": current_time.strftime("%I:%M %p"),
            "end": end_study.strftime("%I:%M %p")
        })

        current_time = end_study
        if current_time.hour >= end_hour:
            break

        end_break = current_time + timedelta(hours=break_block)
        schedule.append({
            "type": "Break",
            "start": current_time.strftime("%I:%M %p"),
            "end": end_break.strftime("%I:%M %p")
        })

        current_time = end_break

    return schedule, date_str, weekday_str
