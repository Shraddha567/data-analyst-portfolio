def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rose"],
            "answer": "C) Paris"
        },
        {
            "question": "What is the capital of India?",
            "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
            "answer": "B) New Delhi"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B) Mars"
        },
        {
            "question": "Who is known as the Father of Computers?",
            "options": ["A) Alan Turing", "B) Charles Babbage", "C) Bill Gates", "D) Steve Jobs"],
            "answer": "B) Charles Babbage"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
            "answer": "C) Carbon Dioxide"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D) Pacific Ocean"
        }
    ]
    '''
    enumerate function is used to get both index and value from the List.
    Example:
    for index, value in enumerate(['a', 'b', 'c']):
    print (index, value)
    The Output will be: 0 a
    '''
    score = 0
    print("Welcome to the Quiz App!\n")
    
    for index, q in enumerate(questions):
        #print (index,q)
        print(f"Question {index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer(A/B/C/D): ")
        
        if user_answer.strip().upper() == q['answer'][0]:
            print("is Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    
    print(f"Quiz Complete! Your score: {score}/{len(questions)}")

run_quiz()