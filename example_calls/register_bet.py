import requests

BASE_URI = "http://localhost"
# for native execution "http://localhost:8085"
# for docker standalone "http://drawing_service:8085"
# for compose "http://localhost:8088/customer_endpoint"
# for k8s "http://localhost"

def register_bet():
    test_bet = {
        "winning_numbers": [1, 2, 3, 4, 5, 6],
        "super_number": [0],
        "user": "123"
    }

    test_created_object = requests.post(f"{BASE_URI}/add_bet", json=test_bet)
    return test_created_object

def check_for_registered_bet():

    test_results = requests.get(f"{BASE_URI}/show_results")
    return test_results


if __name__ == "__main__":
    print(register_bet().content)
    print("Registered Bets: ")
    print(check_for_registered_bet().content)
