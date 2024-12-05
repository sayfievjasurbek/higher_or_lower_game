import random
import game_data
import art  # Importing the art module


# Function to get two random entities
def get_random_entities():
    """Randomly select two unique entities from the data list."""
    return random.sample(game_data.data, 2)

# Function to compare followers
def compare_followers(entity_a, entity_b, user_guess):
    """
    Compare the follower counts of two entities.
    Return True if the user guessed correctly, otherwise False.
    """
    if user_guess == "A" and entity_a["follower_count"] > entity_b["follower_count"]:
        return True
    elif user_guess == "B" and entity_b["follower_count"] > entity_a["follower_count"]:
        return True
    return False

# Game loop
def higher_or_lower_game():
    print(art.logo)  # Display the game logo at the start

    score = 0
    game_continue = True

    # Get the first two random entities
    entity_a, entity_b = get_random_entities()

    while game_continue:
        # Display entities to the user
        print(f"Compare A: {entity_a['name']}, a {entity_a['description']}, from {entity_a['country']}.")
        print("VS")
        print(f"Against B: {entity_b['name']}, a {entity_b['description']}, from {entity_b['country']}.")

        # Ask the user to guess
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Check if the user guessed correctly
        is_correct = compare_followers(entity_a, entity_b, user_guess)

        if is_correct:
            score += 1
            # print(art.correct)  # Show "Correct!" art if it exists
            print(f"You're right! Current score: {score}.")
            # Replace the lower entity with a new random one
            entity_a = entity_b
            entity_b = random.choice(game_data.data)
            while entity_a == entity_b:  # Ensure the two entities are not the same
                entity_b = random.choice(game_data.data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False

# Run the game
higher_or_lower_game()
