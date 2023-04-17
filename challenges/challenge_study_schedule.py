def study_schedule(permanence_periods, target_time):

    max_students = 0

    for start_time, end_time in permanence_periods:
        try:
            if start_time <= target_time <= end_time:
                max_students += 1
        except (ValueError, TypeError):
            return None
    return max_students
