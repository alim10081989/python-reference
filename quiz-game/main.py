from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q1 = Question(question['text'], question['answer'])
    question_bank.append(q1)

print(len(question_bank))

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

print('You have completed the quiz')
print(f'Your final score was : {qb.score}/{len(question_bank)}')
