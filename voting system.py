nominee_list=[]
i=0
while True:
    i+=1
    a=input(f"{i} Enter nominee name:")
    if a in nominee_list:
        print("person exist")
    else:
        nominee_list.append(a)
        print("Congragulations your considered as a Competitor.\nAll the best!!")

    if(len(nominee_list)==3):
        print("the nominee list is completed")
        break

n_count1=0
n_count2=0
n_count3=0

voter_id=["561","562","563","564","565","566","567","568","569","570",
          "571","572","573","574","575","576","577","578","579","580",
          "581","582","583","584","585","586","587","588","589","590",
          "591","592","593","594","595","596","597","598","599","5A0",
          "5A1","5A2","5A3","5A4","5A5","5A6","5A7","5A8","5A9","5B0",
          "5B1","5B2","5B3","5B4","5B5","5B6","5B7","5B8","5B9","5C0"]

no_of_votes=len(voter_id)

while True:
    if voter_id==[]:
        print("voting session is over!!!")
        if(n_count1 > n_count2 and n_count1 > n_count3):
            percent=(n_count1/no_of_votes)*100
            print(f"{nominee_list[0]} has won the election with {percent} majority.")
            break
            
        elif(n_count2 > n_count1 and n_count2 > n_count3):
            percent=(n_count2/no_of_votes)*100
            print(f"{nominee_list[1]} has won the election with {percent} majority.")
            break

        elif(n_count3 > n_count1 and n_count3 > n_count2):
            percent=(n_count3/no_of_votes)*100
            print(f"{nominee_list[2]} has won the election with {percent} majority.")
            break

        elif(n_count1==n_count2):
            print(f"{nominee_list[0]} and {nominee_list[1]} are equal")
            break

        elif(n_count2==n_count3):
            print(f"{nominee_list[2]} and {nominee_list[3]} are equal")
            break

        elif(n_count3==n_count1):
            print(f"{nominee_list[3]} and {nominee_list[1]} are equal")
            break

        else:
            print("three of them has equal votes")
            break


        
            
    voter=input("\n\nEnter your id: ")
    if voter in voter_id:
        print("you are eligible for voting")
        voter_id.remove(voter)
        print("----------------------------")
        print(f"press 1 to vote for {nominee_list[0]}")
        print(f"press 2 to vote for {nominee_list[1]}")
        print(f"press 3 to vote for {nominee_list[2]}")
        print("----------------------------")

        vote=int(input("enter your precious vote"))

        if(vote==1):
            n_count1+=1
            print("thank you for your vote")
        elif(vote==2):
            n_count2+=1
            print("thank you for your vote")
        elif(vote==3):
            n_count3+=1
            print("thank you for your vote")
        elif(vote>3):
            print("check your pressed key!!")
    else:
        print("check whether your eligible to vote or might already voted")
        
        
    
    

