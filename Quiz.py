'''
Simple quiz python code with score functioning 
        made by Dk

'''

   

q1 = {
    "question": 'Q1) Capital of India',
    "ans" : "delhi" or "Delhi"
}
q2 = {
    "question" : 'Q2) who invented bulb',
    "ans" : 'tomas edison'
}
q3 = {
    "question": 'Q3) what is 1 + 1 ?',
    "ans" : '2'
}

q4 = {
    "question" : 'Q4) Is DK pro Coder ( yes / no)', 
    "ans" : 'yes'
}

print("lets start")
print('\n')

while True:
    score = 0
    print(q1["question"])
    ans1 = input("answer: ")
    if ans1.lower() == q1["ans"]:
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG ANSWER")
        score = score - 1
    
    print(q2["question"])
    ans2 = input("answer: ")
    if ans2.lower() == q2["ans"]:
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG ANSWER")
        score = score - 1
    
    print(q3["question"])
    ans3 = input("answer: ")
    if ans3.lower() == q3["ans"]:
        print("CORRECT")
        score = score + 1
    else:
        print("WRONG ANSWER")
        score = score - 1
    print(q4["question"])
    ans4 = input("answer: ")
    if ans4.lower() == q4["ans"]:
        print('CORRECT')
        score = score = score + 1
    else:
        print('WRONG ANSWER,\n')
  

    print('Thank you for answering the test')

    percentage = input('Do you want to see your percentage and score: ')
    if percentage == 'yes':
        per = (score/4*100)
    else:
        pass
    print('score =',str(score))
    print('percentage =',str(per))
    break

    

