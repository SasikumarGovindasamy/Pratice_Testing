# database.py
activities = [
    {"id": 1, "title": "Activity 1", "completed": False},
    {"id": 2, "title": "Activity 2", "completed": True},
]

def get_all():
    return activities

def get_by_id(activity_id):
    return next((a for a in activities if a["id"] == activity_id), None)

def add(activity):
    activities.append(activity)
    return activity

def update(activity_id, new_data):
    activity = get_by_id(activity_id)
    if activity:
        activity.update(new_data)
    return activity

def delete(activity_id):
    global activities
    activities = [a for a in activities if a["id"] != activity_id]
    return True
