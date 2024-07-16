

questions=[
    {
        "prompt":"what is the capital city of france?",
         "options":["A. paris","B. nairobi","C. new york","D. mombasa "],
         "answer":"A"

},
    {
        "prompt":"who is the greatest of all time?",
        "options":["A.Messi","B.Mbappe","C.Neymar","D.Ronaldo"],
        "answer":"D"
    },
    {
        "prompt":"Elon musk is the CEO of?",
        "options":["A.Apple","B.Sumsang","C.HP","D.Tesla"],
        "answer":"D"
    },
    {
        "prompt":"What is the smallest prime number?",
        "options":["A.1","B.2","C.6","D.8"],
        "answer":"B"


    }
]
def run_quiz(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer(A, B, C or D):")
        if answer == question["answer"]:
            print("correct,Hooray!!\n")
            score += 1
        else:
            print("wrong, The correct answer was",questions["answer"],"\n")
    print(f"you got{score} out of {len(questions)} questions correct.")


run_quiz(questions)