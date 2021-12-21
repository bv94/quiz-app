import os


class Quizbrain:
	def __init__(self, q_list):
		self.question_number = 0
		self.question_list = q_list
		self.score = 0

	def next_question(self):
		current_question = self.question_list[self.question_number - 1]

		self.question_number += 1
		return input(f'q.{self.question_number}: {current_question.text}(t,f)\n')

	def evaluator(self, guess, answer):
		guess = str(self.answer_corrector[guess])
		print(answer)
		if guess == answer:
			input("that's correct")
			# os.system("clear")
			self.score += 1
			return True
		else:
			input("that is wrong")
			# os.system("clear")
			return False

	def still_has_questions(self):
		return self.question_number < len(self.question_list)

	answer_corrector = {
		't': True,
		'f': False,
		"T": True,
		'F': False
	}
