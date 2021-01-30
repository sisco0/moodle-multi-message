# Moodle Multi Message

A tool for messaging users in groups at Moodle.

This application was developed with the purpose of aiding at the task of sending a message to the users of a Moodle group.

# Installation

```bash
# First add chromedriver to you path and install Google Chrome if needed
# After that, set environment (optional)
pipenv shell
# Afterwards, install packages needed
pip3 install -r requirements.txt
```

# Usage

Specify the parameters thrown at `python3 moodle_multi_message.py -h`.

Group ID and Course ID (or subject ID) are numeric and these could be grabbed from your platform grading table.

## Example

```bash
python3 moodle_multi_message.py -u my.login.user -p allyourbasearebelongtous -l https://mymoodle.site/ -c 49 -g 2016 -m 'Hello everyone, a new video is ready for you to watch at https://youtube.com/'
```

