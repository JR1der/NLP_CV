import pymupdf
import re


def extract_text_from_pdf(filename):
    doc = pymupdf.open(filename)
    return clean_text('\n'.join([page.get_text() for page in doc]))


def clean_text(text):
    # Patterns for emails and phone numbers
    email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    phone_pattern = r'\+?\d[\d\s\-\(\)]{8,}\d'

    # Extract emails and phone numbers
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    # Replace emails and phone numbers with placeholders
    for i, email in enumerate(emails):
        text = text.replace(email, f'__EMAIL_{i}__')

    for i, phone in enumerate(phones):
        text = text.replace(phone, f'__PHONE_{i}__')

    # Remove newlines
    text = re.sub(r'\r?\n', ' ', text)

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)

    # Remove unwanted characters (you can tweak this to allow some punctuation if needed)
    text = re.sub(r'[^\w\s]', ' ', text)

    # Normalize multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Restore emails and phone numbers
    for i, email in enumerate(emails):
        text = text.replace(f'__EMAIL_{i}__', email)

    for i, phone in enumerate(phones):
        text = text.replace(f'__PHONE_{i}__', phone)

    return text


if __name__ == '__main__':
    print('Extracting text from PDF...')
    # print(f"Dirty text: {extract_text_from_pdf('CV_IvanPopovych.pdf')}")
    print(f"Cleaned text: {extract_text_from_pdf('CV_IvanPopovych.pdf')}")
