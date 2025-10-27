import random

def ball_probability(total_balls, trials):
    """Runs a specified number of trials for differing probabilities 
    of ball color"""
    last_ball_azure_proportion = 0

    for i in range(10, 51, 10):

        azure_count = 0
        carmine_count = 0
        azure_balls = i
        carmine_balls = total_balls - i

        for j in range(trials):
            
            color = compute_ball_color(azure_balls, carmine_balls, total_balls)
            
            if color == "azure":
                azure_count += 1
            else:
                carmine_count += 1
        
        last_ball_azure_proportion = azure_count / trials

        return last_ball_azure_proportion
           

def compute_ball_color(azure_balls, carmine_balls, total_balls, ball_color=None):
    """A function that computes the probability of an azure ball 
    being picked last for a single trial."""
    
    while total_balls > 1:

        choice_probability = random.random()

        # first ball picked or ball got replaced
        if ball_color == None:
            if choice_probability <= (azure_balls / total_balls):
                ball_color = "azure" 
                total_balls -= 1
                azure_balls -= 1
                choice_probability = random.random()

            else:
                ball_color = "carmine"
                total_balls -= 1
                carmine_balls -= 1
                choice_probability = random.random()

           
        
        # if current ball is azure and previous ball is azure
        if (azure_balls / total_balls) >= choice_probability and ball_color == "azure":
            if azure_balls > 0:
                ball_color = "azure"
                total_balls -= 1
                azure_balls -= 1
                choice_probability = random.random()
            else:
                ball_color = None
                continue

        # if current ball is carmine and previous ball is carmine
        elif (carmine_balls / total_balls) >= choice_probability and ball_color == "carmine":
            if carmine_balls > 0:
                ball_color = "carmine"
                total_balls -= 1
                carmine_balls -= 1
                choice_probability = random.random()
            else:
                ball_color = None
                continue

        # ball color and previous ball color do not match
        else:
            ball_color = None
            continue
    
    else:
        return ball_color
    

prob = ball_probability(100, 2000)
print(prob)

