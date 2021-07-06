import argparse
import json
from typing import List


def parse_message_strings_from_file(input_file) -> List[str]:
    message_strings = list()

    json_file = json.load(input_file)
    message_dicts = json_file['messages']
    for message_dict in message_dicts:
        message_string = get_message_string_from_dict(message_dict)
        if message_string:
            message_strings.append(message_string)
    return message_strings


def get_message_string_from_dict(msg) -> str:
    if msg.get('text'):
        return f'[{msg["date"].replace("T", " ")}] <{msg["from"]}>: {msg["text"]}'


def main():
    parser = argparse.ArgumentParser(
        description='Telegram supergroup text extractor',
        usage="telegram_group_text_extractor.py input_file -o output_file")
    parser.add_argument('input_file', type=str, help='input file path')
    parser.add_argument('-o', '--output', dest='output_file', help='output file path')
    options = parser.parse_args()

    with open(options.input_file, 'r', encoding='utf-8') as infile, open(options.output_file, 'w', encoding='utf-8') as outfile:
        message_strings = parse_message_strings_from_file(infile)
        outfile.writelines(f'{msg}\n' for msg in message_strings)


if __name__ == "__main__":
    main()
