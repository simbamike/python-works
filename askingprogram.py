def read_questions(filename):
    answers = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line != '':
                question, answer = line.split('=')
                answers[question.strip()] = answer.strip()
    return answers
read_questions('/Users/michael/Documents/questions.txt')
{'text displaying function': 'print', 'text asking function': 'input'}
print(answers)
