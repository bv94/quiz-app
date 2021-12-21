import random
from data import question_data
from question_model import Question
import quiz_brain

questions = []
lst = []
for question in question_data:
	question_text = question["question"]
	question_answer = question["correct_answer"]
	lst.append((question_text,question_answer))
	questions.append(Question(question_text, question_answer))
print(lst)

# random.shuffle(questions)
quiz = quiz_brain.Quizbrain(questions)
should_continue = True

while should_continue :
	if not quiz.still_has_questions():
		print("you win")
	guess = quiz.next_question()
	should_continue = quiz.evaluator(guess, questions[quiz.score-1].answer)


print(f'your score is {quiz.score}')
exit()
