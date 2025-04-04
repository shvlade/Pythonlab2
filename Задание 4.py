import re
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

phone_numbers = re.findall(r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", text)

capitalized_words = re.findall(r"\b[A-ZА-ЯЁ][a-zа-яё]*\b", text)

with open("emails.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(emails))

with open("phones.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(phone_numbers))

with open("capital_words.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(capitalized_words))

print("Результаты сохранены в файлы emails.txt, phones.txt, capital_words.txt")