with open(r"C:\Sunny\Python\PythonProgramming\Questions.txt","r") as Questions, open(r"C:\Sunny\Python\PythonProgramming\Answers.txt","r") as Answers:
    for (Ques,Ans) in zip(Questions,Answers):
        print(Ques.rstrip("\n"))
        input("Press Enter to reveal the answer")
        print(f"Answer: {Ans}")
