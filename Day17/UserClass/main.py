from data import question_data
from question_model import Question

list_of_QuestionObject = []
for dictionary in question_data:
    the_text_is = dictionary["text"]
    ans_val_is = dictionary["answer"]
    list_of_QuestionObject.append(Question(the_text_is, ans_val_is))


from quiz_brain import QuizBrain
qb=QuizBrain(list_of_QuestionObject)