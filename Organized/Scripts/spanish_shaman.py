import random
import time

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
