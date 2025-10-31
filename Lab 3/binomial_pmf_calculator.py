import random

# given problem variables
n = 7 # trials
p = 0.6 # probability joe plays
q = 0.7 # probability joe wins
s = 100000 # simulations

def perform_trials():
    """Performs the experiment outlined in the lab handout with (n) trials (s) 
    number of times. Returns a list of (s) 2-tuples containing the number of games 
    joe plaed x, and the number of games he won y."""
    l = [] # list of trial results (x, y)
    i = 0 
    
    # 100,000 simulations
    while i < s:
        x, y = 0, 0

        # n trials per simulation
        for j in range(n):
            flip_outcome_p = random.random()
            # does Joe play this week
            if flip_outcome_p < p:
                x += 1
                flip_outcome_q = random.random()
                # does joe win this played game
                if flip_outcome_q < q:
                    y += 1

        l.append((x, y))
        i += 1

    # print(l)
    return l

def calculate_joint(trials):
    """Takes a list of 2-tuples (x, y) that contain the number of games joe plaed (x), and the 
    number of games he won (y). The list contains (s) tuples, where (s) is the number of 
    simulations performed. Returns a dict that has a tuple as a key and the prob that tuple 
    happened during the experiment as the value."""
    pair_dict = {} # key = pair (x,y), value = count n
    pair = () # (x, y)

    for i in range(len(trials)):
        pair = (trials[i][0], trials[i][1])
        if pair not in pair_dict:
            pair_dict[pair] = 1
        else:
            pair_dict[pair] += 1
        
    prob_dict = {} # key = pair (x, y), value = prob of pair per 100k sims

    for key, value in pair_dict.items():
        prob = value / s
        prob_dict[key] = prob

    return prob_dict

def calculate_marginal_x(joint_dict):
    """Calculates the marginal PMF of x by summing the probability over the range of x.
    Takes a dictionary containing the joint PMF table and returns a dictionary containing 
    marginal PMF table."""
    marginal_dict = {} # keys = x value, values = sum(prob)

    # for every value of x, we sum the probabilities
    for coords, prob in joint_dict.items():
        for x in range(n+1):
            if coords[0] == x:
                if x not in marginal_dict.keys():
                    marginal_dict[x] = prob
                else:
                    marginal_dict[x] += prob
    
    return marginal_dict

def calculate_marginal_y(joint_dict):
    """Calculates the marginal PMF of y by summing the probability over the range of y.
    Takes a dictionary containing the joint PMF table and returns a dictionary containing 
    marginal PMF table."""
    marginal_dict = {} # keys = y value, values = sum(prob)

    # for every value of y, we sum the probabilities
    for coords, prob in joint_dict.items():
        for y in range(n+1):
            if coords[1] == y: 
                if y not in marginal_dict.keys():
                    marginal_dict[y] = prob
                else:
                    marginal_dict[y] += prob
    
    return marginal_dict

def calculate_conditional_xy(joint_dict, marginal_y_dict):
    """Calculates the conditional PMF X|Y by dividing every joint PMF by the respective
    marginal y PMF. Takes 2 dictionarys containing the joint PMF table and the marginal 
    y PMF table. Returns a dictionary containing the conditional xy PMF table."""
    cond_dict = {} # keys = pair (x, y), value = prob

    for coords, joint_prob in joint_dict.items():
        x, y = coords[0], coords[1]

        # adds conditional probabilities X|Y to dict
        if coords[0] == x:  
            if (x, y) not in cond_dict.keys():
                cond_dict[(x,y)] = joint_prob / marginal_y_dict[y]
            else:
                cond_dict[(x,y)] += joint_prob / marginal_y_dict[y]

    return cond_dict

def calculate_conditional_yx(joint_dict, marginal_x_dict):
    """Calculates the conditional PMF Y|X by dividing every joint PMF by the respective
    marginal y PMF. Takes 2 dictionarys containing the joint PMF table and the marginal 
    y PMF table. Returns a dictionary containing the conditional yx PMF table."""
    cond_dict = {} # keys = pair (x, y), value = prob

    for coords, joint_prob in joint_dict.items():
        x, y = coords[0], coords[1]

        # adds conditional probabilities Y|X to dict
        if coords[0] == x:
            if (x, y) not in cond_dict.keys():
                cond_dict[(x,y)] = joint_prob / marginal_x_dict[x]
            else:
                cond_dict[(x,y)] += joint_prob / marginal_x_dict[x]

    return cond_dict

def print_pmfs(joint_dict, cond_xy_dict, cond_yx_dict):
    """Prints the joint, marginal, and conditional PMF tables. Takes 3 dictionarys 
    as arguments, one containing the joint PMF table, one containing the conditional 
    PMF table of X|Y, and one containing the conditional PMF table Y|X. Returns None."""

    # prints joint PMF
    # header
    print("Joint PMF of X and Y")
    print(f"{'  y:':<7}", end="")
    for y in range(n+1):
        print(f"{y:<8}", end="")
    print()
    print(f"{'x '}{'-'*10}{'-'*n*8}")
    
    # values
    for x in range(n + 1):
        print(f"{x} |", end="")
        for y in range(x + 1):
            if (x, y) in joint_dict.keys():
                print(f"  {joint_dict[(x, y)]:.4f}", end="")
            else:
                print(f"  0.0000", end="")
        print()
    print("\n")

    # prints conditional PMF X|Y
    # header
    print("Conditional PMF of X given Y")
    print(f"{'  y:':<7}", end="")
    for y in range(n+1):
        print(f"{y:<8}", end="")
    print()
    print(f"{'x '}{'-'*10}{'-'*n*8}")
    
    # values
    for x in range(n + 1):
        print(f"{x} |", end="")
        for y in range(x + 1):
            if (x, y) in cond_xy_dict.keys():
                print(f"  {cond_xy_dict[(x, y)]:.4f}", end="")
            else:
                print(f"  0.0000", end="")
        print()
    print("\n")

    # prints conditional PMF Y|X
    # header
    print("Conditional PMF of Y given X")
    print(f"{'  y:':<7}", end="")
    for y in range(n+1):
        print(f"{y:<8}", end="")
    print()
    print(f"{'x '}{'-'*10}{'-'*n*8}")
    
    # values
    for x in range(n + 1):
        print(f"{x} |", end="")
        for y in range(x + 1):
            if (x, y) in cond_yx_dict.keys():
                print(f"  {cond_yx_dict[(x, y)]:.4f}", end="")
            else:
                print(f"  0.0000", end="")
        print()
    print("\n")

    return None

trials = perform_trials()
joint = calculate_joint(trials)
marginal_x = calculate_marginal_x(joint)
marginal_y = calculate_marginal_y(joint)
conditional_xy = calculate_conditional_xy(joint, marginal_y)
conditional_yx = calculate_conditional_yx(joint, marginal_x)
print_pmfs(joint, conditional_xy, conditional_yx)