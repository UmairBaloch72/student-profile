from datetime import datetime

def create_profile(name, student_id, bio):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('student_profile.txt', 'w') as f:
        f.write(f"Name: {name}\n")
        f.write(f"Student ID: {student_id}\n")
        f.write(f"Bio: {bio}\n")
        f.write(f"Generated: {timestamp}\n")
    print("Profile updated successfully")

if __name__ == "__main__":
    create_profile("Umair Ahmed", "22SE18", "I am learning Git and GitHub!")
