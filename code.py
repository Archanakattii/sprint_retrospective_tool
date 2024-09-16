from datetime import datetime

class Session:
    def _init_(self):
        self.sid = 0
        self.sessions = {}

    def create_session(self):
        self.sid += 1 
        session_name = input("Enter session name: ")
        goals = input("Enter goals for the session: ").split(',')
        self.sessions[self.sid] = {
            'name': session_name,
            'goals': set([goal.strip() for goal in goals]),
            'achievements': set(), 
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def add_goals(self, sid, goals):
        if sid in self.sessions:
            # goals = input("Enter goals to add: ").split(',')
            self.sessions[sid]['goals'].update([goal.strip() for goal in goals])
        else:
            print(f"Session {sid} does not exist.")

    def remove_goals(self, sid, goals):
        if sid in self.sessions:
            # goals = input("Enter goals to remove: ").split(',')
            self.sessions[sid]['goals'].difference_update([goal.strip() for goal in goals])
        else:
            print(f"Session {sid} does not exist.")

    def add_achievements(self, sid, achievements):
        # achievements = input("Enter achievements: ").split(',') 
        if 'achievements' not in self.sessions[sid] : 
            self.sessions[sid]['achievements'] = set() 
        self.sessions[sid]['achievements'] |= set([achievement.strip() for achievement in achievements])

    def remove_achievements(self, sid, achievements):
        # achievements = input("Enter achievements to remove: ").split(',')
        for achievement in achievements:
            if achievement in self.sessions[sid]['achievements']:
                self.sessions[sid]['achievements'].remove(achievement.strip())

    def improvements(self, sid, goa, aor, fb): 
        if sid in self.sessions:
            if goa and aor: 
              self.add_goals(sid, fb)
            elif not goa and aor:
                self.add_achievements(sid, fb)
            elif not goa and not aor: 
                self.remove_achievements(sid, fb)
            else:
                self.remove_goals(sid, fb)                  

    def success_rate(self, sid):
        goals_count = len(self.sessions[sid]['goals'])
        achievements_count = len(self.sessions[sid]['achievements'])

        if goals_count == 0:
            return 0.0

        return (achievements_count / goals_count) * 100

    def print_sessions(self):
        for sid, session_data in self.sessions.items():
            print(f"Session {sid} ({session_data['datetime']}):")
            print(f"  Name: {session_data['name']}")
            print(f"  Goals: {session_data['goals']}")
            print(f"  Achievements: {session_data['achievements']}")
            print(f"  Success Rate: {self.success_rate(sid):.2f}%")
            print()


s = Session()
s.create_session()

while True:
    operation = int(input("Enter operation (1-add_goals, 2-remove_goals, 3-add_achievements, 4-remove_achievements, 5-improvements 6- to quit): "))

    if operation == 6:
        break
    sid = int(input("Enter session ID: "))

    match operation: 
        case 1:
            goals = input("Enter goals to add (comma-separated): ").split(',')
            s.add_goals(sid,goals) 
        case 2:
            goals = input("Enter goals to remove (comma-separated): ").split(',')
            s.remove_goals(sid,goals)
        case 3:
            achievements = input("Enter achievements to add (comma-separated): ").split(',')
            s.add_achievements(sid,achievements)
        case 4:
            achievements = input("Enter achievements to remove (comma-separated): ").split(',')
            s.remove_achievements(sid,achievements)
        case 5: 
            fb = input("Enter goals or achievements : ").split(',')
            goa = input("Enter 1 if you want to change goals and 0 for achiements : ")
            goa = True if goa=='1' else False 
            aor = input("Enter 1 if you want to add and 0 to remove feedback : ")
            aor = True if aor=='1' else False 
            s.improvements(sid, goa, aor, fb) 
        case _: 
            print("Invalid operation. Please try again.")

s.print_sessions()
