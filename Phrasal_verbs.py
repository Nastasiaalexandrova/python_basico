import random

# Список вопросов и ответов (вопрос, варианты, правильный ответ, объяснение)
questions = [
    ("What does 'give up' mean?", 
     ["To continue", "To surrender", "To create", "To take"],
     "b",
     "'Give up' means to surrender or stop doing something."),
    
    ("What does 'run out of' mean?", 
     ["To finish a supply", "To escape", "To continue", "To start"],
     "a",
     "'Run out of' means to have no more of something left."),
    
    ("What does 'put off' mean?", 
     ["To delay", "To wear", "To complete", "To remove"],
     "a",
     "'Put off' means to postpone or delay something."),
    
    ("What does 'take after' mean?", 
     ["To resemble", "To chase", "To take care", "To learn"],
     "a",
     "'Take after' means to resemble a family member in appearance or behavior."),
    
    ("What does 'break down' mean?", 
     ["To repair", "To function", "To stop working", "To clean"],
     "c",
     "'Break down' means to stop functioning, especially for machines or vehicles."),
    
    ("What does 'look forward to' mean?", 
     ["To anticipate with pleasure", "To ignore", "To be afraid", "To forget"],
     "a",
     "'Look forward to' means to anticipate something with excitement or pleasure."),
    
    ("What does 'set up' mean?", 
     ["To destroy", "To arrange or establish", "To cancel", "To delay"],
     "b",
     "'Set up' means to arrange, organize, or establish something."),
    
    ("What does 'turn down' mean?", 
     ["To accept", "To refuse", "To increase", "To buy"],
     "b",
     "'Turn down' means to refuse or reject something."),
    
    ("What does 'come across' mean?", 
     ["To find unexpectedly", "To run away", "To create", "To demand"],
     "a",
     "'Come across' means to find something by chance."),
    
    ("What does 'give in' mean?", 
     ["To surrender", "To take away", "To ignore", "To push"],
     "a",
     "'Give in' means to surrender or yield."),
    
    ("What does 'call off' mean?", 
     ["To cancel", "To repeat", "To answer", "To continue"],
     "a",
     "'Call off' means to cancel an event or plan."),
    
    ("What does 'bring up' mean?", 
     ["To mention", "To go away", "To put down", "To clean"],
     "a",
     "'Bring up' means to mention a topic in conversation."),
    
    ("What does 'come up with' mean?", 
     ["To create or invent", "To go down", "To remove", "To fix"],
     "a",
     "'Come up with' means to create or invent something."),
    
    ("What does 'drop off' mean?", 
     ["To deliver or leave", "To hold", "To destroy", "To enter"],
     "a",
     "'Drop off' means to deliver or leave someone/something at a specific place."),
    
    ("What does 'get along with' mean?", 
     ["To have a good relationship", "To dislike", "To fight", "To ignore"],
     "a",
     "'Get along with' means to have a good relationship with someone."),
    
    ("What does 'keep up with' mean?", 
     ["To stay at the same level", "To lose", "To stop", "To ignore"],
     "a",
     "'Keep up with' means to stay at the same level as someone or something."),
    
    ("What does 'make up' mean?", 
     ["To invent", "To break", "To clean", "To understand"],
     "a",
     "'Make up' means to invent a story, excuse, or lie."),
    
    ("What does 'turn up' mean?", 
     ["To arrive unexpectedly", "To decrease", "To refuse", "To create"],
     "a",
     "'Turn up' means to arrive unexpectedly or increase the volume."),
    
    ("What does 'work out' mean?", 
     ["To exercise or solve a problem", "To fail", "To stop", "To sleep"],
     "a",
     "'Work out' means to exercise or solve a problem."),
    
    ("What does 'figure out' mean?", 
     ["To understand", "To delete", "To ignore", "To cry"],
     "a",
     "'Figure out' means to understand something or find a solution."),
]

# Перемешиваем вопросы
random.shuffle(questions)

# Подсчет правильных и неправильных ответов
correct_answers = 0
wrong_answers = 0

# Основной цикл викторины
for i, (question, options, correct_option, explanation) in enumerate(questions, 1):
    print(f"\n{i}. {question}")
    for idx, option in zip("abcd", options):
        print(f"   {idx}) {option}")
    
    while True:
        answer = input("Enter your answer (a/b/c/d): ").strip().lower()
        if answer == correct_option:
            print("✅ Correct!\n")
            correct_answers += 1
            break
        else:
            print("❌ Incorrect! Try again.")

# Итоговые результаты
print("\n🎉 Quiz Completed! 🎉")
print(f"✅ Correct answers: {correct_answers}")
print(f"❌ Wrong attempts: {wrong_answers}")

# Выводим объяснение к каждому вопросу
print("\n📌 Explanations:")
for i, (_, _, correct_option, explanation) in enumerate(questions, 1):
    print(f"{i}. {explanation}")