# Castro-Perez
# 10/20/2026
# Assignment Name
# A brief description of the project

def main():
    num_scores = int(input("How many scores do you want to enter? "))
    print()
    
    valid_scores_list = []
    
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score #{i}: "))
        
        while score < 0 or score > 100:
            print("\nINVALID Score entered!")
            print("Score should be between 0 and 100")
            score = float(input(f"Enter score #{i} again: "))
        
        valid_scores_list.append(score)
        
    print()
    lowest_score = min(valid_scores_list)
    modified_scores_list = valid_scores_list.copy()
    modified_scores_list.remove(lowest_score)
    scores_average = sum(modified_scores_list) / len(modified_scores_list)
    if scores_average >= 90:
        grade = 'A'
    elif scores_average >= 80:
        grade = 'B'
    elif scores_average >= 70:
        grade = 'C'
    elif scores_average >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    print("-" * 12 + "Results" + "-" * 12)
    print(f"Lowest Score  : {lowest_score}")
    print(f"Modified List : {modified_scores_list}")
    print(f"Scores Average: {scores_average:.2f}")
    print(f"Grade         : {grade}")
    print("-" * 31)

if __name__ == "__main__":
    main()