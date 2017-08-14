start = '''
You hear about a summer program called Girls Who Code, and it's an opportunity to learn coding and make new friends!
'''


print(start)


print("Will you decide to sign up? Type 'yes' to go sign up or 'no' if you don't want to sign up.")
user_input = input()
if user_input == "yes":
    print("You signed up for Girls Who Code, and it's your first day today. You start to learn about coding and new concepts. Once you started learning new things, a thought comes to you head that it would be good to talk to new people. Type 'yes' to talk to new people and type 'no' if you don't want to talk to new people.") # finished the story by writing what happens
     user_input = input()
    if user_input == "yes":
      print ("You start talking to new people, and you slowly start to find people that are nice, fun, and probably share common interests with you. You've made new friends!")
      print ("The end! You learned new things, made new friends, and you enjoyed your experience at Girls Who Code!")
    elif user_input == "no":
      print ("You decide not to talk to new people, and as time goes by, you start to feel disconnected. People are starting to recognize that you probably feel left out and decide to approach you. DO you want to talk and get to know them?")
      user_input = input()
    if user_input == "yes":
        print ("You became friends with them! From then on you felt more connected with everyone there and you enjoyed your experience at Girls Who Code. The End!")
    elif user_input == "no":
        print ("You decide to ingnore people's efforts to talk to you, and you become isolated. Throughout the 7 weeks, you felt more lonely because people wouldn't approach you thinking that you don't want to make new friends. You ended up not enjoying your Girls Who Code experience as much as you wanted to. The End.")
elif user_input == "no":
    print("You choose to not sign up, and as your summer goes by you slowly become bored and you stay isolated in your own community. Maybe you should have joined! You would have had a great time learning new things and making new friends. The End.") # finished the story writing what happens
