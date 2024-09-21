import sqlite3

conn = sqlite3.connect("Youtube-manager.db")

cursor = conn.cursor()

cursor.execute(''' 
 CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')



# list all videos
def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
   
# add a video fucntion
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?) ", (name ,time))
    conn.commit()


    
# update a video
def update_video(video_id, name ,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (
        name, time, video_id
    ) )
    conn.commit()
   

# delete a video
def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()
     

# user stater print statement 

def main():
    while True:
        print("\n Yootube manager")
        print("1. LIST ALL YOUR YOUTUBE VIDEOS")
        print("2. ADD A YOUTUBE VIDEO")
        print("3. UPDATE YOUTUBE VIDEO DETAIL")
        print("4. DELETE A YOUTUBE VIDEO")
        print("5. EXIT THE APP")
        choice = input("Enter your Choice = ")
        

        match choice:
            case '1':
                list_all_videos()
            case '2': 
                name = input("Enter the name of youtube video")
                time = input("Enter the time ")

                add_video(name, time)
            case '3':
                video_id = input("Enter the ID = ")
                name = input("Enter the Name =  ")
                time = input("Enter the time = ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the ID")
                delete_video(video_id)
            case '5':
                break
            case _: 
                print("Invalid choice")
    conn.close()            


if __name__ == "__main__":
    main()