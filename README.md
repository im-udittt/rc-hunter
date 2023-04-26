# **Discord Vehicle Registration Bot**

This Python script creates a Discord bot that allows users to query the Indian vehicle registration database by providing the RC number. The bot sends an HTTP request to the RapidAPI service to retrieve the details of the vehicle and saves the response to a JSON file. The script then uploads the file to the Discord server for users to access.

## **Installation**

1. Clone this repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory and add the following environment variables:

    ```
    TASK_ID=<your_task_id>
    GROUP_ID=<your_group_id>
    X-RAPIDAPI-KEY=<your_api_key>
    X-RAPIDAPI-HOST=<your_api_host>
    TOKEN=<discord_token>
    ```

4. Replace `<your_task_id>`, `<your_group_id>`, `<your_api_key>`, and `<your_api_host>` with your own values obtained from the RapidAPI service.
5. Run the script by running `python bot.py`.
6. Invite the bot to your Discord server and use the `!find` command to query vehicle details by RC number.

## **Usage**

To use the bot, type `!find <rc_number>` in a Discord channel where the bot is present. Replace `<rc_number>` with the RC number of the vehicle you want to query. The bot will send an HTTP request to the RapidAPI service and retrieve the vehicle details. The response will be saved to a JSON file and uploaded to the Discord server for users to access.

If you do not provide an RC number with the `!find` command, the bot will send a usage message with instructions.

## **Credits**

This script was created by [@im-udittt] . It uses the following libraries:

- discord
- dotenv
- requests

## **Contributions**

Contributions to this script are welcome! If you find a bug or want to suggest a new feature, feel free to submit a pull request or open an issue.
