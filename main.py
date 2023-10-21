import random
from matplotlib import pyplot as plt
import pandas as pd

def lifeline(ran, opts, op, list_life):

    m = 1

    lifelines = ['Audience Poll', 'Fifty Fifty', 'Double dip', 'Flip the question']
    
    print("Lifelines are \t", lifelines[0], '\t', lifelines[1], '\t', lifelines[2], '\t', lifelines[3], '\n\n')
    
    if not list_life:
        print("You don't have lifelines remaining\t")
        return None
    
    print("Press 1 for audience, 2 for 50:50, 3 for double dip or 4 for flip the question\t")

    while m != 0:
        get = int(input())
        
        if get == 1:
            if get in list_life:
                m = 0
                list_life.remove(1)
                great = audience(ran, opts, op)
            else:
                print("You don't have audience poll\t")
        
        elif get == 2:
            if get in list_life:
                m = 0
                great = fifty(ran, op)
                list_life.remove(2)
            else:
                print("You don't have 50:50 \t")
        
        elif get == 3:
            if get in list_life:
                m = 0
                great = doubleDip(ran)
                list_life.remove(3)
            else:
                print("You don't have double dip\t")
        
        elif get == 4:
            if get in list_life:
                m = 0
                great = flip()
                list_life.remove(4)
            else:
                print("You don't have lifeline to flip the question\t")
        
        else:
            print("Choose correct option")

    return great

def audience(ran, opts, op):

    print("According to audience\n")
    s = pd.Series([opt1[ran], opt2[ran], opt3[ran], opt4[ran]], index=['1', '2', '3', '4'])
    s.plot.bar(figsize=(20, 10))
    plt.xlabel('Options')
    plt.ylabel('%')
    plt.title("Audience Poll")
    plt.show()

    print('1.', opts[0][ran], "%", '\t', '2.', opts[1][ran], "%", '\t', '3.', opts[2][ran], "%", '\t', '4.', opts[3][ran], "%", '\nenter your choice\t')
    
    print("Would you like to take lifeline again, if yes then press 9 or Press 0 to Quit\t")
    
    choice = int(input())
    
    if choice == 9:
        great = lifeline(ran, opts, op)
        return great
    
    elif choice == answer[ran]:
        great = 1
        print("Correct answer, well done!..")
    
    elif choice == 0:
        great = -2
    
    else:
        great = 0
        print("Incorrect")
        print("Correct Answer is :", options[answer[ran] - 1][ran])

    return great

def fifty(ran, op):

    print("Q." + questions[ran])
    
    for num, option in enumerate(op):
        print(str(num + 1) + "." + option[ran])
    choice_fifty = int(input("enter your choice \t"))

    if choice_fifty == answer[ran]:
        print("Correct Answer.....")
        great = 1
    
    else:
        great = 0
        print("wrong answer")
        print("Correct Answer is :", options[answer[ran] - 1][ran])
    
    return great

def doubleDip(ran):

    print("Select two options\n")
    trial1 = int(input())
    
    if answer[ran] == trial1:
        great = 1
        print("Correct Answer, well done....")
    
    else:
        print("Your first trial is wrong, choose another\t")
        trial2 = int(input())
        
        if answer[ran] == trial2:
            great = 1
            print("Correct Answer\t")
        
        else:
            print("Your second trial is also wrong..Better luck next time..\t")
            print("Correct Answer is :", options[answer[ran] - 1][ran])
            great = 0
    
    return great

def flip():
    return -1

def amount(correct_ans):
    print(amount_won[correct_ans - 1])
    
    if amount_won[correct_ans - 1] == 10000:
        print("Completed 1st stage")
    
    elif amount_won[correct_ans - 1] == 320000:
        print("Completed 2nd stage")
    
    elif amount_won[correct_ans - 1] == 70000000:
        print("You have won Rs 7 CRORE")
    
    return amount_won[correct_ans - 1]

questions = [
    'In ODI Cricket, who created the record of scoring the fastest century in just 31 balls ?',
    # ... (other questions)
]

option1 = ['Corey Anderson', 'Evil', '10', 'Srinagar', 'Hindi', 'Cricket', '1920', 'Bangladesh', 'polo', 'Virat Kohli', 'Tennis', 'Cricket', 'Australia', 'Kolkata', 'Wrestling', 'Bessemer', 'Sida', 'Polio', 'China', 'Thar', 'Magadh', 'Cataract', 'Israel', 'Tabla', 'Antonio Gramsci ', 'Arjan Singh', 'Parliament of India', 'Gangtok', 'Rabies', ' Mohd Hamid Ansari', 'P V Sindhu', 'Mahatma Gandhi', 'Hanuman']

option2 = ['AB De Villiers', 'Humble', '9', 'Jaisalmer', 'Palauan', 'Football', '1928', 'Kenya', 'Cricket', 'Yuvraj Singh', 'Cricket', 'Football', 'West Indies', 'Mumbai', 'Swimming', 'Rane Laennec', 'Tridax', 'Malaria', 'Taiwan', 'Sahara', 'Mahishmati', 'Gastric', 'Jordan', 'Santoor', 'Che Guevera', 'Pratap Chandra Lal', 'Tractor', 'Aizawl', 'Tetanus', ' I K Gujral', 'Aparna Balan', 'Swami Vivekananda ', 'Vishnu']

option3 = ['Shahid Afridi', 'Dishonest', '7', 'Amritsar', 'Sindhi', 'Badminton', '1972', 'Pakistan', 'Hockey', 'MS Dhoni', 'Hockey', 'Hockey', 'South Africa', 'Delhi', 'Boxing', 'Henry Becquerel', 'Tephrosia', 'Dermatitis', 'Japan', 'Gobi', 'Kalinga', 'Bypass', 'Saudi Arabia', 'Mridangam', ' Leon Trotsky ', 'Subroto Mukarjee', 'Red Fort', 'darjeeling', 'Japanese Encephalitis', 'Mohd Hidayatullah ', 'Saina Nehwal', 'Rabindranath Tagore ', 'Shiva']

option4 = ['Rohit Sharma', 'Miserly', '8', 'Udhampur', 'English', 'Hockey', '1976', 'Australia', 'Football', 'Zaheer Khan', 'Polo', 'Tennis', 'India', 'Jaipur', 'Running', 'None of these', 'Indigofera', 'Cholera', 'Australia', 'None of these', 'Badami', 'Debridement', 'Qatar', 'Dafli', 'Vladimir Lenin', 'Aspy Engineer', 'Mangalyaan', 'Kohima', 'Plague', 'Zakir Hussain', 'Jwala Gutta', 'Mother Teresa', 'Kamadeva']

options = [option1, option2, option3, option4]

# answer key
answer = [2, 4, 2, 3, 3, 1, 1, 4, 2, 2, 2, 2, 2, 2, 1, 3, 4, 3, 3, 1, 2, 3, 1, 4, 4, 1, 4, 3, 3, 1, 3, 4, 3]

amount_won = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

opt1 = [30, 24, 10, 0, 1, 72, 99, 0, 9, 2, 0, 2, 10, 1, 100, 1, 0, 3, 2, 98, 21, 35, 50, 40, 45, 65, 50, 48, 5, 70, 20, 30, 20]

opt2 = [60, 32, 80, 0, 2, 5, 1, 1, 91, 94, 95, 87, 90, 96, 0, 0, 2, 12, 13, 1, 60, 20, 30, 2, 0, 20, 0, 1, 10, 12, 20, 20, 10]

opt3 = [2, 4, 0, 100, 97, 0, 0, 1, 0, 2, 5, 11, 0, 3, 0, 99, 2, 82, 82, 0, 18, 40, 10, 4, 1, 10, 0, 50, 70, 15, 35, 10, 64]

opt4 = [8, 40, 10, 0, 0, 23, 0, 98, 0, 2, 0, 0, 0, 0, 0, 0, 96, 3, 3, 1, 1, 5, 10, 54, 54, 5, 50, 1, 15, 3, 25, 40, 6]

opts = [opt1, opt2, opt3, opt4]

list_life = [1, 2, 3, 4]

correct = 0
total_amt = 0

def play_game():
    global correct
    global total_amt
    
    while correct != 16 and questions:
        ran = random.randint(0, len(questions) - 1)
        print("\n\nQ.", correct + 1, ":-", end="")
        print(questions[ran])
        
        for num, option in enumerate(options):
            print(str(num + 1) + "." + option[ran])
        
        print("Would you like to take lifeline, if yes, press 9\n Choose any option: or you can quit by pressing 0 \t\t")
        give_answer = int(input())

        if give_answer == 9:
            if not lifeline(ran, opts, op, list_life):
                break
        
        elif give_answer == 0:
            if correct != 0:
                total_amt = amount(correct)
            break
        
        else:
            key = answer[ran]

            if key == give_answer:
                print("Correct answer.., You have won Rs.=", end="")
                correct += 1
                total_amt = amount(correct)
            else:
                print("Wrong Answer...Better luck next time...")
                print("Correct Answer is :", options[answer[ran] - 1][ran])
                if total_amt < 10000:
                    total_amt = 0
                elif total_amt < 320000:
                    total_amt = 10000
                elif total_amt < 70000000:
                    total_amt = 320000
                break

            del questions[ran]
            del option1[ran]
            del option2[ran]
            del option3[ran]
            del option4[ran]
            del answer[ran]
            del opts[0][ran]
            del opts[1][ran]
            del opts[2][ran]
            del opts[3][ran]

    if questions:
        print("Your winning amount is Rs. ", total_amt)
    else:
        print("Congratulations! You have answered all the questions correctly and won Rs. ", total_amt)

play_game()


play_game()
