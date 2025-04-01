# Datacamp_Transcript_Cleaner
Removes timestamps and adds extra lines to transcripts you've copied from Datacamp videos

# Clean Clipboard

A simple Python utility that cleans and formats text from your clipboard.
This serves a specific use-case in copying transcripts from Datacamp.com videos into a notepad. 
I use this for speeding up my note taking process. 

## Features

- Removes timestamp lines (e.g., "00:00 - 00:08")
- Normalizes paragraph spacing
- Adds extra spacing between numbered sections
- Automatically copies the cleaned text back to your clipboard

## Requirements

- Python 3.x
- pyperclip library

## Installation

1. Clone this repository
2. Install the required dependency:
```bash
pip install pyperclip
```

## Usage

1. Copy the text you want to clean to your clipboard
2. Run the script:
```bash
python clean_clipboard.py
```
3. The cleaned text will automatically replace your clipboard content
4. The script will also print the processed text to the console for review

## How It Works

The script performs the following operations:
1. Removes any lines that contain timestamp patterns (e.g., "00:00 - 00:08")
2. Normalizes multiple blank lines to single blank lines
3. Adds extra spacing before numbered sections for better readability

## Example

Before:
```
00:00 - 00:08 Introduction
This is the first paragraph.

00:08 - 00:15 Main Content
This is the second paragraph.


1. First point
2. Second point
```

After:
```
This is the first paragraph.

This is the second paragraph.


1. First point

2. Second point
```
