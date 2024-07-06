import psycopg2
def execute(command, param):
    account =  open("account_information.txt","r")
    conn = psycopg2.connect(database = str(account.readline().replace('\n', '')), 
                        user = str(account.readline().replace('\n', '')), 
                        host = str(account.readline().replace('\n', '')),
                        password = str(account.readline().replace('\n', '')),
                        port = int(account.readline()))
    account.close()

    cur = conn.cursor()
    # Execute a command:
    cur.execute(command,param)
    # Make the changes to the database  persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()
def search(command, param):
    account =  open("account_information.txt","r")
    conn = psycopg2.connect(database = str(account.readline().replace('\n', '')), 
                        user = str(account.readline().replace('\n', '')), 
                        host = str(account.readline().replace('\n', '')),
                        password = str(account.readline().replace('\n', '')),
                        port = int(account.readline()))
    account.close()

    cur = conn.cursor()
    # Execute a command:
    cur.execute(command,param)
    # Make the changes to the database  persistent
    print(cur.fetchall())
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()
def new_player(first_name, last_name, wins, losses, draws, email, phone_number, looking_for_match):
    execute("INSERT INTO players (first_name, last_name, wins, losses, draws, email, phone_number,looking_for_match) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, wins, losses, draws, email, phone_number,bool(looking_for_match)))

   
def update_player_phone_number(phone_number, id):
    execute("UPDATE players SET phone_number = %s where user_id = %s",(str(phone_number), str(id)))

def search_player(name):
    search("SELECT * FROM players WHERE first_name = %s OR last_name = %s;",(str(name),str(name)))

def update_player_email(email, id):
    execute("UPDATE players SET email = %s where user_id = %s",(str(email), str(id)))

def remove_player(id):
    execute("DELETE FROM players WHERE user_id = %s", (str(id),))

def update_match(match_id, id1,id2):
    execute("UPDATE players SET current_match_id = %s WHERE user_id = %s OR user_id = %s", (str(match_id),str(id1),str(id2)))

def check_in(id):
    execute("UPDATE players SET looking_for_match = true WHERE user_id = %s", (str(id),))
def check_out(id):
    execute("UPDATE players SET looking_for_match = false WHERE user_id = %s", (str(id),))
def check_out_all():
    execute("UPDATE players SET looking_for_match = false",None)
def new_tournament():
    print("Starting new tournament: \n")
#new_player("jenny", "smith", 0, 0, 0, "jenny.smith@gmail.com", "203-555-5555", 0)
#update_player_phone_number("555-555-5555",5)
#remove_player(5)

update_match(1,1,2)
check_out_all()
search_player("smith")
