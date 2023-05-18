from Question import Question

question_prompts = [
    "Apples are:\na) Blue\nb) Red\nc) Brown\n",
    "Bananas are:\na) Yellow\nb) Orange\nc) Purple\n",
    "Oranges are:\na) Black\nb) Orange\nc) Blue\n"
]
test_questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt + "Enter an answer (a/b/c): ")
        if user_answer == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect! Correct answer is: " + question.answer + "\n")
    print("Correct answers: " + str(score) + "/" + str(len(questions)))


run_test(test_questions)

"""
question_prompts = [
    "Apples are:\na) Blue\nb) Red\nc) Brown",
    "Bananas are:\na) Yellow\nb) Orange\nc) Purple",
    "Oranges are:\na) Black\nb) Orange\nc) Blue"
]
answers = ["b", "a", "b"]
correct_count = 0

for i in range(len(question_prompts)):
    print(question_prompts[i])
    user_answer = input("Enter an answer (a/b/c): ")
    if user_answer == answers[i]:
        print("Correct!\n")
        correct_count += 1
    else:
        print("Incorrect! Correct answer is: " + answers[i] + "\n")

print("Correct answers: " + str(correct_count) + "/" + str(len(answers)))
"""
