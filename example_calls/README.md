# Example Calls to application

### [Register a test-bet and verify its presence](./register_bet.py)

This short skript registers a dummy bet at the `/register_bet` endpoint of the customer service. Consequently, the entirety of the registered bets in the databse is shown by calling the `/show_results` endpoint.

Before using this script it is necessary to adjust the `BASE_URI` where the service is currently running.

### [Example Calls to the whole application](./draw_and_show_results.py)

To test the whole application end-to-end some bets need to be registered in the database. 

Triggering the `/trigger_draw` endpoint creates the winning numbers which are delivered back to the caller and to the message broker who distributes them to the RabbitMQ listener in the customer_service. The bets are evaluated based on their winnings. 
Calling the `/show_resulsts` endpoint on the customer_service should display the bets with a `winning_class` expressed in numbers.

Before using this script it is necessary to adjust the `BASE_URI` where the service is currently running.

### [Example Call which publishes a message on the RabbitMQ broker](./publish_message.py)

To test the async listener with the customer_service on the RabbitMQ broker the execution of the script publishes a message directly to the queue which should be consumed by async listener.

To execute this script a running instance of RabbitMQ and customer_service is needed whose execution you can find in their respective directories or for RabbitMQ with the [main Readme](../README.md#docker-commands-for-infrastructure-services)