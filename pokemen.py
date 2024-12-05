import requests
import math

# Helper functions to calculate stats
def calculate_stat(base_stat, level=50, iv=31, ev=252):
    return math.floor(((2 * base_stat + iv + (ev // 4)) * level) / 100) + 5

def calculate_hp(base_stat, level=50, iv=31, ev=252):
    return math.floor(((2 * base_stat + iv + (ev // 4)) * level) / 100) + level + 10

# Function to fetch Pokémon data from PokeAPI
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data for {pokemon_name}. Status code: {response.status_code}")
    return response.json()

# Function to get Pokémon stats
def get_pokemon_stats(pokemon_data):
    stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
    return {
        'hp': calculate_hp(stats['hp']),
        'attack': calculate_stat(stats['attack']),
        'defense': calculate_stat(stats['defense']),
        'speed': calculate_stat(stats['speed'])
    }

# Function to simulate the battle
def battle_simulation(pokemon1_name, pokemon2_name):
    # Fetch data for both Pokémon
    pokemon1_data = fetch_pokemon_data(pokemon1_name)
    pokemon2_data = fetch_pokemon_data(pokemon2_name)

    # Get stats
    pokemon1_stats = get_pokemon_stats(pokemon1_data)
    pokemon2_stats = get_pokemon_stats(pokemon2_data)

    # Initialize battle
    print(f"Battle Start! {pokemon1_name.capitalize()} vs {pokemon2_name.capitalize()}")
    print(f"Initial HP: {pokemon1_name.capitalize()} - {pokemon1_stats['hp']}, {pokemon2_name.capitalize()} - {pokemon2_stats['hp']}\n")

    # Determine first attacker
    if pokemon1_stats['speed'] > pokemon2_stats['speed']:
        attacker_name, attacker_stats = pokemon1_name, pokemon1_stats
        defender_name, defender_stats = pokemon2_name, pokemon2_stats
    else:
        attacker_name, attacker_stats = pokemon2_name, pokemon2_stats
        defender_name, defender_stats = pokemon1_name, pokemon1_stats

    print(f"{attacker_name.capitalize()} attacks first!\n")

    # Battle loop
    round_counter = 1
    while attacker_stats['hp'] > 0 and defender_stats['hp'] > 0:
        print(f"Round {round_counter}")
        damage = max(1, attacker_stats['attack'] - defender_stats['defense'])
        defender_stats['hp'] -= damage
        print(f"{attacker_name.capitalize()} deals {damage} damage to {defender_name.capitalize()}. Remaining HP: {defender_stats['hp']}\n")

        if defender_stats['hp'] <= 0:
            print(f"{defender_name.capitalize()} fainted!")
            print(f"Winner: {attacker_name.capitalize()}!")
            return

        # Swap roles
        attacker_name, defender_name = defender_name, attacker_name
        attacker_stats, defender_stats = defender_stats, attacker_stats
        round_counter += 1

# Example usage
battle_simulation("pikachu", "bulbasaur")
