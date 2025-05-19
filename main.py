import re

text = """
Contact me at email@example.com or visit https://www.example.com.
Call 123-456-7890. Use card number 1234-5678-9012-3456.
The meeting is at 2:30 PM. Price is $99.99. #simple
"""

# 1. Email
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

# 2. URL
urls = re.findall(r"https?://[^\s]+", text)

# 3. Phone
phones = re.findall(r"\d{3}[-.]\d{3}[-.]\d{4}", text)

# 4. Credit Card
cards = re.findall(r"\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}", text)

# 5. Time
times = re.findall(r"\d{1,2}:\d{2}\s?(AM|PM)", text)

# 6. Currency
money = re.findall(r"\$\d+(?:\.\d{2})?", text)

# 7. Hashtag
hashtags = re.findall(r"#\w+", text)

# Show results
print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phones)
print("Credit Cards:", cards)
print("Times:", times)
print("Currency:", money)
print("Hashtags:", hashtags)

