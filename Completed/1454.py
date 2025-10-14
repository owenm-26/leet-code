import datetime
from collections import defaultdict

def mostActiveUser(activities: list[dict]) -> str:
    user_activity = defaultdict(lambda: [0, 0])

    for record in activities:
        total_time:int = record.get("logout_time").timestamp() - record.get("login_time").timestamp()
        user_id = record.get("user_id")

        user_activity[user_id][0] += total_time
        user_activity[user_id][1] += record.get("pageVisits")
    
    best_user:str = None

    for user in user_activity:
        if best_user == None:
            best_user = user
        
        if user_activity[user] > user_activity[best_user]:
            best_user = user
    
    return best_user


if __name__ == "__main__":
    example_input_1 = [
    {"user_id": "U1", "name": "Sped_owen", "login_time": datetime.datetime(2023, 10, 25, 10, 0, 0), "logout_time": datetime.datetime(2023, 10, 25, 10, 5, 0), "pageVisits": 10},
    {"user_id": "U2", "name": "Bob", "login_time": datetime.datetime(2023, 10, 25, 10, 0, 0), "logout_time": datetime.datetime(2023, 10, 25, 10, 10, 0), "pageVisits": 5},  
    {"user_id": "U1", "name": "Alice", "login_time": datetime.datetime(2023, 10, 25, 10, 5, 0), "logout_time": datetime.datetime(2023, 10, 25, 10, 10, 0), "pageVisits": 15},
    ]

    print(mostActiveUser(example_input_1))
