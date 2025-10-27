import random

num_coins = 300
p = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
trials = 1000

def relative_frequency(num_coins, head_prob, trials):
    bob_coins = num_coins + 1
    alice_coins = num_coins
    bob_most_heads = 0

    for i in range(trials):

        bob_heads = 0
        alice_heads = 0

        for j in range(bob_coins):
            toss = random.randint(1, 11) / 10
            if toss <= head_prob:
                bob_heads += 1

        for j in range(alice_coins):
            toss = random.randint(1, 11) / 10
            if toss <= head_prob:
                alice_heads += 1

        if bob_heads > alice_heads:
            bob_most_heads += 1

    return (bob_most_heads / trials)

def print_frequency(p=[0.5]):

    relative_frequency_dict = {}
    
    for i in p:
        relative_frequency_dict[i] = relative_frequency(num_coins, i, trials)

    print("-"*26)
    print("p\trelative frequency")
    print("-"*26)

    for i, j in relative_frequency_dict.items():
        print(f"{i}\t{j:.3f}")
        
print_frequency(p)