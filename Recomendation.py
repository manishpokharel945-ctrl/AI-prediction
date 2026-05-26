# Simple AI Recommendation System

print("Welcome to Movie Recommendation System")
print("Choose your interest:")
print("1. Action")
print("2. Comedy")
print("3. Romance")
print("4. Horror")
print("5. Sci-Fi")

choice = input("Enter your favourite movie type: ").lower()

if choice == "action":
    print("Recommended Movies:")
    print("- John Wick")
    print("- Fast and Furious")
    print("- Mission Impossible")

elif choice == "comedy":
    print("Recommended Movies:")
    print("- Mr. Bean")
    print("- Home Alone")
    print("- The Mask")

elif choice == "romance":
    print("Recommended Movies:")
    print("- Titanic")
    print("- The Notebook")
    print("- Me Before You")

elif choice == "horror":
    print("Recommended Movies:")
    print("- The Conjuring")
    print("- Annabelle")
    print("- Insidious")

elif choice == "sci-fi":
    print("Recommended Movies:")
    print("- Interstellar")
    print("- Avatar")
    print("- Avengers")

else:
    print("Sorry, we do not have recommendations for this category.")
    print("Please try: action, comedy, romance, horror, or sci-fi.")