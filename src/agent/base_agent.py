from src.utils.temp_db import temp_data
from src.config.logger import Logger
from src.utils.webhook import call_webhook_with_error

logger = Logger()

# This is the base_agent function. This function is called when the agent is executed.
# You can also use the temp_data variable to store data that you want to use in other methods.
# You can use the call_webhook_with_success and call_webhook_with_error methods to call the webhook.
# You can use the logger variable to log your data.
# For return the response you can use see config/agent.json file output section.


def base_agent(payload):
    try:
        logger.info("base_agent() called with ", payload)
        inputs = payload.get("inputs")

        # Write your agent logic in this function and return the response.

        # Remove from here the below line and write your logic here.
        print("hello", payload)
        first_name = inputs[0].get("data")
        last_name = inputs[1].get("data")
        # Remove from here the below line and write your logic here.

        # Replace with your output name, type and data.
        resp = {
            "name": "greeting",
            "type": "shortText",
            "data": f"Wow! Hey {first_name} {last_name}, you've just rocked it by creating an awesome basic agent! 🚀✨"
        }

        return resp
    except Exception as e:
        logger.error('Getting Error in base_agent:', e)
        raise call_webhook_with_error(str(e), 500)
