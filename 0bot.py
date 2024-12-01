import random
import string
import time
import os
from datetime import datetime, timedelta
import telebot
from telebot import types
from concurrent.futures import ThreadPoolExecutor, as_completed
from gateway import Tele
from utils import cardResponseFilter, ccnMsg, cvvMsg, editMssg

token = "6657794620:AAF5POzqPoqdeclnaQlv1QWtRQha0V6liPM"
bot = telebot.TeleBot(token, parse_mode="HTML")
subscriber = [
    "6473717870",  # Your admin or authorized user IDs
]

premium_file = "premium.txt"  # Path to store premium users (mono text file)
codes_file = "codes.txt"  # Path to store generated codes (mono text file)

# Ensure the premium and codes file exist, create them if they don't
if not os.path.exists(premium_file):
    open(premium_file, "w").close()

if not os.path.exists(codes_file):
    open(codes_file, "w").close()

# Generate a random premium code
def generate_code(duration, amount):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Generates an 8-character code
    expiration_date = (datetime.now() + timedelta(days=duration)).strftime('%Y-%m-%d %H:%M:%S')  # Expiration date with time
    with open(codes_file, "a") as f:
        f.write(f"{code} {expiration_date} {amount}\n")  # Save the generated code with expiration and amount
    return code, expiration_date, amount

# Handle the /code command
@bot.message_handler(commands=["code"])
def code(message):
    try:
        params = message.text.split()[1:]  # Get the parameters after the command
        if len(params) != 2:
            bot.reply_to(message, "Invalid format. Usage: /code <duration_in_days> <amount>")
            return

        duration = int(params[0])
        amount = int(params[1])

        if duration <= 0 or amount <= 0:
            bot.reply_to(message, "Duration and amount must be positive integers.")
            return

        # Generate the code
        code, expiration_date, amount = generate_code(duration, amount)

        # Send formatted message with the code highlighted for easy copying
        bot.reply_to(message, f"""Generated premium code: <code>{code}</code>
Duration: {duration} day(s)
Amount: {amount} units
Expires on: {expiration_date}""")
    except Exception as e:
        bot.reply_to(message, f"Error generating code. Details: {str(e)}")

# Handle the /redeem command
@bot.message_handler(commands=["redeem"])
def redeem(message):
    try:
        # Extract code from message
        params = message.text.split(" ", 1)
        if len(params) < 2:
            bot.reply_to(message, "Usage: /redeem <code>")
            return

        code_to_redeem = params[1].strip()

        # Read available codes
        with open(codes_file, "r") as f:
            available_codes = f.read().splitlines()

        # Validate and process the code
        valid_code = None
        for available_code in available_codes:
            parts = available_code.split(maxsplit=2)  # Limit splitting to 3 parts
            if len(parts) != 3:
                continue  # Skip invalid lines
            code, expiration_date_str, amount = parts

            if code == code_to_redeem:
                valid_code = available_code

                # Parse the expiration date dynamically
                try:
                    expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d")

                # Check if the code is expired
                if expiration_date < datetime.now():
                    bot.reply_to(message, "This code has expired.")
                    return
                break

        if not valid_code:
            bot.reply_to(message, "Invalid or already redeemed code.")
            return

        # Grant premium access
        with open(premium_file, "a") as f:
            f.write(f"{message.chat.id}\n")
        available_codes.remove(valid_code)
        with open(codes_file, "w") as f:
            f.write("\n".join(available_codes))
        bot.reply_to(message, f"Premium access granted using code: <b>{code_to_redeem}</b>")
    except Exception as e:
        bot.reply_to(message, f"Error redeeming code. Details: {str(e)}")

# Handle the /start command for premium users
@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in subscriber and str(message.chat.id) not in get_premium_users():
        bot.reply_to(
            message, "You cannot use the bot. If you want to use it, contact developers (@chk1212) to purchase a bot subscription., 1 week :: 10$, 1 Month :: 30$"
        )
        return

    bot.reply_to(
        message,
        """Send the file to check CC.

To Scrape - scr username amount.
With bin - scr username amount bin.

Limit up to 10K per scrape🔥

Please wait...

All credit goes to owners."""
    )

# Function to get all premium users from the file
def get_premium_users():
    with open(premium_file, "r") as f:
        return f.read().splitlines()

# Rest of your existing card checking code...

@bot.message_handler(content_types=["document"])
def main(message):
    print(message)
    if str(message.chat.id) not in subscriber and str(message.chat.id) not in get_premium_users():
        bot.reply_to(
            message,
            "You cannot use the bot. If you want to use it, contact developers (@chk121213) to purchase a bot subscription., 1 week :: 10$, 1 Month :: 30$",
        )
        return

    # Acknowledge receipt of the file immediately
    msg_id = bot.reply_to(
        message, "File received. Starting to check your cards...⌛"
    ).message_id

    try:
        # Download and decode the file immediately
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        cc = downloaded_file.decode().splitlines()  # Split file into lines (cards)
    except Exception as e:
        bot.reply_to(message, "Error reading the file.")
        return

    live = charge = dd = 0  # Initialize counts

    # Provide initial message for checking status
    bot.edit_message_text(
        chat_id=message.chat.id, message_id=msg_id, text="Checking cards... ⏳",
        reply_markup=editMssg("cc", live, charge, dd, len(cc), "Wait", "0.0.0.0"),
    )

    # Start processing the cards asynchronously
    with ThreadPoolExecutor(max_workers=2) as executor:  # Increase workers if needed
        futures = [executor.submit(Tele, card) for card in cc]
        for future in as_completed(futures):
            ccx, result, ip = future.result()
            print(result)  # Get the result from the future
            code, mssg = cardResponseFilter(str(result), "2")

            if code < 400:
                if code == 300:
                    live += 1
                    bot.send_message(message.chat.id, ccnMsg(mssg, ccx, ip))
                    time.sleep(0.5)
                    bot.edit_message_text(
                        chat_id=message.chat.id,
                        message_id=msg_id,
                        text="Wait for processing\n 𝒃𝒚 ➜ @chk1212",
                        reply_markup=editMssg(ccx, live, charge, dd, len(cc), mssg, ip),
                    )
                elif code == 200:
                    charge += 1
                    bot.send_message(message.chat.id, cvvMsg(mssg, ccx, ip))
                    time.sleep(0.7)
                    bot.edit_message_text(
                        chat_id=message.chat.id,
                        message_id=msg_id,
                        text="Wait for processing\n 𝒃𝒚 ➜ @chk1212",
                        reply_markup=editMssg(ccx, live, charge, dd, len(cc), mssg, ip),
                    )
            else:
                dd += 1
                time.sleep(0.5)
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=msg_id,
                    text="Wait for processing\n 𝒃𝒚 ➜ @chk1212",
                    reply_markup=editMssg(ccx, live, charge, dd, len(cc), mssg, ip),
                )

    # Final message when done
    print("someone is done")
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=msg_id,
        text=f"Card checking completed! ✅\n\n𝗟𝗶𝘃𝗲: {live}, 𝗖𝗵𝗮𝗿𝗴𝗲: {charge}, 𝗗𝗲𝗮𝗱: {dd}",
    )


bot.polling()
