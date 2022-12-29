class question:
  def __init__(self, text, options, correctOption):
    self.text = text
    self.options = options
    self.correctOption = correctOption
  
questions = [
  question('Q1: What is the capital of South Korea?', ['1: Orlando', '2: Pyeongyang', '3: Seoul'], '3'),
  question('Q2: Name the capital of Germany', ['1: Washington', '2: Berlin', '3: New Yorkshire'], '2'),
  question('Q3: What is the capital of Indonesia?', ['1: Kansas city', '2: Jakarta', '3: Dublin'], '2'),
  question('Q4: What is the capital of China?', ['1: Beijing', '2: Pyeongyang', '3: Guinea'], '1'),
  question('Q5: What is the capital of Russia?', ['1: Siberia', '2: Taiwan', '3: Moscow'], '3'),
]

def startQuiz():
  score = 0
  for question in questions:
    print(question.text)
    print("Your options are: ", question.options)
    option_entered = input('Please enter the correct option: ')
    if (option_entered == question.correctOption):
      print("CORRECT ANSWER")
      score += 1
    else: 
      print("WRONG. BETTER LUCK NEXT TIME")
  
  print("You scored: ", score, "/", len(questions))
  input("THE QUIZ IS OVER. Press enter to exit")

print("This is a quiz testing you about world capitals. Good luck!")
start = input("PRESS S TO START QUIZ:  ")
 
if start == 'S':
  startQuiz()
else: 
  exit()
