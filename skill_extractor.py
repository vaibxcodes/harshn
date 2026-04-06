import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python","java","c","c++","sql","html","css","javascript",
    "machine learning","deep learning","ai","cybersecurity",
    "linux","nmap","networking","flask","django"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return list(set(found))


