# Telegram Group History Text Extractor

A tool to extract raw message text from exported Telegram group history. 

From this:

     {
      "id": -999999455,
      "type": "message",
      "date": "2015-12-31T19:41:30",
      "from": "Sender",
      "from_id": "user012345678",
      "text": "Message text."
     }

to this:

    [2015-12-31 19:41:30] <Sender>: Message text.

## Usage:
    >>> python telegram_group_text_extractor.py input_file -o output_file
Where input_file is the path to your exported JSON file, and output_file is the path where output will be written.
Sample:

    >>> python telegram_group_text_extractor.py result.json -o output.txt