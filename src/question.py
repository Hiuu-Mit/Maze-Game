import random

questions = [
     {
        "question": "Quelle est la capitale de la France",
        "option": ["Lyon", "Paris", " Marseille", "Bordeaux"],
        "answer": "Paris"
    },
    {
        "question": "Quel est le symbole de la France",
        "option": ["Statue de la Liberté", "Tour de Pise", "Big Ben", "Tour Eiffel"],
        "answer": "Tour Eiffel"
    },
    {
        "question": "Où se situe le musée du Louvre",
        "option": ["Paris", "Cannes", "Bordeaux", "Lyon"],
        "answer": "Paris"
    },
    {
        "question": "Quelle est la devise nationale de la France",
        "option": ["Liberté, Bonheur, Paix", "Liberté, Égalité, Fraternité", "L'union fait la force", "Justice et Civilisation"],
        "answer": "Liberté, Égalité, Fraternité"
    },
    {
        "question": "Quand a lieu la fête nationale française",
        "option": ["2/9", "14/7", "15/7", "24/12"],
        "answer": "14/7"
    },
]

def get_random_question():
    return random.choice(questions)

def check(question, answer):
    return answer == question["answer"]
    