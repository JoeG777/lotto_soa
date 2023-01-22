import requests
import time

import example_calls.register_bet as register_bet

# Precondition: empty database, running services and all processes
# Steps:
    # 1. register one/multiple bets -> winning_classe needs to be null
    # 2. trigger draw on drawing_service
        # - return a valid drawing result
        # - publish message to rabbitmq
        # - message consumed by customer_service
        # - view_results shows winning_class without "null" - corresponds to matching with result


BASE_URI = "http://localhost" 
# for native execution "http://localhost:8080"
# for docker standalone "http://drawing_service:8080"
# for compose "http://localhost:8088/draw_master_endpoint"
# for k8s "http://localhost"

def show_empty_database():
    available_bets_in_db = register_bet.check_for_registered_bet()
    #assert available_bets_in_db.content == b'{"message":"Something went wrong! - No entries available"}'
    return available_bets_in_db.content

def register_bet_local():
    return register_bet.register_bet().content

def trigger_draw():
    
    test_draw_response = requests.get(f"{BASE_URI}/trigger_draw")
    return test_draw_response

def show_results():
    now_available_results = register_bet.check_for_registered_bet()
    return now_available_results

if __name__ == '__main__':
    print(f"\n>>> Content in Database:\n")
    print(show_empty_database())

    print(f"\n>>> Register a bet in the database:\n")
    print(register_bet_local())

    print(f"\n>>> Trigger a Lotto Draw:\n")
    print(trigger_draw().content)

    print(f"\n>>> Sleep to give async listener chance to handle evaluation of bets:\n")
    time.sleep(3)

    print(f"\n>>> Show results of draw:\n")
    print(show_results().content)