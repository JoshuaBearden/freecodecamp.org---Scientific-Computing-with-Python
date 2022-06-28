def arithmetic_arranger(problems, displayAnswer=False):
  
  if len(problems) > 5:
    return "Error: Too many problems."
    
  # instantiate lists of 1st or 2nd operands, and operators to be parsed through and evaluated for errors.
  firstOperand = []
  operator = []
  secondOperand = []

  # use a for loop to create list of individual elements and append operators and operands to their respective lists.
  for problem in problems:
    problemAtElementN = problem.split()
    firstOperand.append(problemAtElementN[0])
    operator.append(problemAtElementN[1])
    secondOperand.append(problemAtElementN[2])
  
  if "/" in operator or "*" in operator:
    return "Error: Operator must be '+' or '-'."

  for num in range(len(firstOperand)):
    if not (firstOperand[num].isdigit() and secondOperand[num].isdigit()):
      return "Error: Numbers must only contain digits."

  for num in range(len(firstOperand)):
    if len(firstOperand[num]) > 4 or len(secondOperand[num]) > 4:
      return "Error: Numbers cannot be more than four digits."

  firstNum = []
  secondNum = []
  line = []
  answer = []

  for i in range(len(firstOperand)):
    if len(firstOperand[i]) > len(secondOperand[i]):
      firstNum.append(" "*2 + firstOperand[i])
    else:
      firstNum.append(" "*(len(secondOperand[i]) - len(firstOperand[i]) + 2) + firstOperand[i])

  for i in range(len(secondOperand)):
    if len(secondOperand[i]) > len(firstOperand[i]):
      secondNum.append(operator[i] + " " + secondOperand[i])
    else:
      secondNum.append(operator[i] + " "*(len(firstOperand[i]) - len(secondOperand[i]) + 1) + secondOperand[i])

  for i in range(len(firstOperand)):
    line.append("-"*(max(len(firstOperand[i]), len(secondOperand[i])) + 2))

  if displayAnswer:
    for i in range(len(firstOperand)):
      if operator[i] == "+":
        ans = str(int(firstOperand[i]) + int(secondOperand[i]))
      else:
        ans = str(int(firstOperand[i]) - int(secondOperand[i]))

      if len(ans) > max(len(firstOperand[i]), len(secondOperand[i])):
        answer.append(" " + ans)
      else:
        answer.append(" "*(max(len(firstOperand[i]), len(secondOperand[i])) - len(ans) + 2) + ans)
    arranged_problems = "    ".join(firstNum) + "\n" + "    ".join(secondNum) + "\n" + "    ".join(line) + "\n" + "    ".join(answer)
  else:
    arranged_problems = "    ".join(firstNum) + "\n" + "    ".join(secondNum) + "\n" + "    ".join(line)
  return arranged_problems
