import random
import time
import pyttsx3

# Spanish phrases for ayahuasca travel
phrases = {
    "Hello": "Hola",
    "Thank you": "Gracias",
    "Where is the ayahuasca ceremony?": "¿Dónde es la ceremonia de ayahuasca?",
    "I want to become a shaman": "Quiero convertirme en chamán",
    "How much for the retreat?": "¿Cuánto cuesta el retiro?",
    "I need a taxi to the jungle": "Necesito un taxi a la selva"
}

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.say(text)
    engine.runAndWait()

def quiz():
    word, translation = random.choice(list(phrases.items()))
    print(f"Listen to: {translation}")
    speak(translation)
    guess = input(f"Translate '{word}' to Spanish: ")
    if guess.lower() == translation.lower():
        print("¡Correcto! Score +1")
        return True
    print(f"No, it's '{translation}'")
    return False

def travel_planner():
    print("Ayahuasca Travel Planner")
    destinations = [
        {"name": "Peru (Iquitos)", "cost": 1000, "days": 7},
        {"name": "Brazil (Santo Daime)", "cost": 1200, "days": 10},
        {"name": "Costa Rica (Blue Spirit)", "cost": 1500, "days": 8}
    ]
    print("Popular retreats:")
    for dest in destinations:
        print(f"- {dest['name']}: {dest['days']} days, ${dest['cost']}")
    budget = float(input("Enter budget (USD): "))
    affordable = [d for d in destinations if d['cost'] <= budget]
    if affordable:
        print("Affordable retreats:")
        for dest in affordable:
            print(f"- {dest['name']}: ${dest['cost']}")
    else:
        print(f"No retreats under ${budget}. Try Google!")
    print("Tip: Learn Spanish with this app to book directly!")

def main():
    print("Shamanic Spanish Learner")
    score = 0
    while True:
        action = input("Choose (quiz, planner, quit): ").lower()
        if action == "quit":
            print(f"Final score: {score}")
            break
        if action == "quiz":
            if quiz():
                score += 1
        if action == "planner":
            travel_planner()

if __name__ == "__main__":
    main()

# Spanish phrases for ayahuasca travel
phrases = {
    "Hello": "Hola",
    "Thank you": "Gracias",
    "Where is the ayahuasca ceremony?": "¿Dónde es la ceremonia de ayahuasca?",
    "I want to become a shaman": "Quiero convertirme en chamán",
    "How much for the retreat?": "¿Cuánto cuesta el retiro?",
    "I need a taxi to the jungle": "Necesito un taxi a la selva"
}

def quiz():
    word, translation = random.choice(list(phrases.items()))
    guess = input(f"Translate '{word}' to Spanish: ")
    if guess.lower() == translation.lower():
        print("¡Correcto! Score +1")
        return True
    print(f"No, it's '{translation}'")
    return False

def travel_planner():
    print("Ayahuasca Travel Planner")
    destinations = ["Peru (Iquitos)", "Brazil (Santo Daime)", "Costa Rica (Blue Spirit)"]
    print("Popular retreats:")
    for dest in destinations:
        print(f"- {dest}: 7-10 day ceremonies, $500-1500")
    budget = input("Enter budget (USD): ")
    print(f"Recommendations for ${budget}: Search 'ayahuasca retreats under ${budget}' on Google.")
    print("Tip: Learn Spanish with this app to book directly!")

def main():
    score = 0
    while True:
        action = input("Choose (quiz, planner, quit): ").lower()
        if action == "quit":
            print(f"Final score: {score}")
            break
        if action == "quiz":
            if quiz():
                score += 1
        if action == "planner":
            travel_planner()

if __name__ == "__main__":
    main()
