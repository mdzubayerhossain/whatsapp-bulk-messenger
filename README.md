# WhatsApp Bulk Messenger

WhatsApp Bulk Messenger automates the sending of messages via WhatsApp Web. This tool can be used to send WhatsApp messages in bulk. The program runs through a list of numbers provided in `numbers.txt` and sends a predefined (but templated) message to each number in the list. It can also read other columns from the number CSV to populate template-specific words and send out a personalized message to the number.

**Note:** The current program is limited to sending only text messages.

**Note:** Another version of a similar project is available that supports sending media and documents along with text. 
## Requirements

- Python >= 3.6
- Chrome headless is installed by the program automatically

## Setup

1. Install Python (>= v3.6)
2. Run `pip install -r requirements.txt`

## Steps

1. Enter the message you want to send inside the `message.txt` file.
2. Enter the list of numbers, line-separated, in the `numbers.txt` file.
3. Run `python whatsapp_bulk_messenger.py message.txt numbers.txt --delay 30`.
4. Once the program starts, you'll see the message from `message.txt` and the count of numbers in the `numbers.txt` file.
5. After a while, Chrome should pop up and open [web.whatsapp.com](https://web.whatsapp.com).
6. Scan the QR code to log in to WhatsApp.
7. Press `Enter` to start sending out messages.
8. Sit back and relax!

