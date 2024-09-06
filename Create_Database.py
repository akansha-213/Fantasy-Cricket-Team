import sqlite3

con=sqlite3.connect('Fantasy_Game.db')
cur=con.cursor()

#Creating Table for Match

#cur.execute('''create table Match1(
    #Player string(30) primary key,
    #Scored integer not null,
    #Faced integer not null,
    #Fours integer,
    #Sixes integer,
    #Bowled integer,
    #Maiden integer,
    #Given integer,
    #Wickets integer,
    #Catches integer,
    #Stumping integer,
    #Run_out integer)''')

#Creating Table for Teams

#cur.execute('''create table Teams(
    #Players string(30) References Match(Player),
    #Name string(30) not null,
    #Value integer)''')

#Creating Table for Stats

#cur.execute('''create table Stats(
    #Players string(30) References Match(Player),
    #Matches integer,
    #Runs integer,
    #"100s" integer,
    #"50s" integer,
    #Value integer,
    #Category text)''')

con.commit()

#for x in range(11):
    #plr=input("Enter Player Name: ")
    #sco=int(input("Enter Runs Scored: "))
    #fac=int(input("Enter Ball_Faced: "))
    #fou=int(input("Enter Fours hit: "))
    #six=int(input("Enter sixes hit: "))
    #bow=int(input("Enter Bowled: "))
    #mai=int(input("Enter Maiden: "))
    #giv=int(input("Enter Runs Given: "))
    #wkt=int(input("Enter Wickets Taken: "))
    #cat=int(input("Enter Catches Taken: "))
    #stu=int(input("Enter Stumping done: "))
    #run=int(input("Enter Run Out done: "))
    #sql="insert into Match1 (Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wickets,Catches,Stumping,Run_out) values ('"+plr+"','"+str(sco)+"','"+str(fac)+"','"+str(fou)+"','"+str(six)+"','"+str(bow)+"','"+str(mai)+"','"+str(giv)+"','"+str(wkt)+"','"+str(cat)+"','"+str(stu)+"','"+str(run)+"');"

    #try:
        #cur=con.cursor()
        #cur.execute(sql)
        #con.commit()
        #print("One Record Added Successfully")
    #except:
        #print("Error in Operation")
        #con.rollback()

#for x in range(6):
    #plr=input("Enter Player Name: ")
    #mat=int(input("Enter Matches Played: "))
    #run=int(input("Enter Runs Scored: "))
    #hun=int(input("Enter 100s: "))
    #fif=int(input("Enter 50s: "))
    #val=int(input("Enter Value of Player: "))
    #ctg=input("Enter Category of Players: ")
    #sql="insert into Stats (Players,Matches,Runs,'100s','50s',Value,Category) values ('"+plr+"','"+str(mat)+"','"+str(run)+"','"+str(hun)+"','"+str(fif)+"','"+str(val)+"','"+ctg+"');"

    #try:
        #cur=con.cursor()
        #cur.execute(sql)
        #con.commit()
        #print("Record Added Successfully")
    #except:
        #print("Error in Operation")
        #con.rollback()
        

con.close()


