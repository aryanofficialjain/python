import json
filename = "Youtube.txt"
def load_data():
    try: 
        with open(filename, 'r') as file:
           return  json.load(file)
    except FileNotFoundError : 
        return []

def save_data_helper(videos):
    with open(filename, 'w') as file:
        json.dump(videos, file);

    
# list all videos
def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print("\n")
        print("*" * 70)
        print(f"{index}, {video['name']}, Duration, {video['time']}")

# add a video fucntion
def add_video(videos):
    name = input("Enter the name of the video")
    time = input("Enter the time of the video")
    videos.append({"name":name, "time": time })

    save_data_helper(videos)

# update a video
def update_video(videos):
    index = int(input("Enter the number of Video"))
    if( 1 <= index <=len(videos)):
        name = (input("Enter the video name "))
        time = (input("Enter the Time of that Video"))
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("invalid index")



    

# delete a video
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Number you want to delete"))
    if(1<= index <= len(videos)):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid video indexes")   

videos = load_data();
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
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2': 
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _: 
                print("Invalid choice")


if __name__ == "__main__":
    main()