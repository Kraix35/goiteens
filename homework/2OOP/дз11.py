class FClub:
    
    def __init__(self, name, city, points):
        self.club_name = name
        self.city = city
        self.points = points



class Tournament:
    
    def __init__(self, clubs, country, name):
        self.clubs = clubs
        self.country = country
        self.tournament_name = name

    def findOutsider(self):
        outsider = self.clubs[0]

        for club in self.clubs:
            if club.points < outsider.points:
                outsider = club 
        print(f'Outsider of {self.tournament_name} is {outsider.club_name} with points {outsider.points}')   

    def findLeader(self):
        leader = self.clubs[0] 

        for club in self.clubs:
            if club.points > leader.points:
                leader = club
        print(f'Leader of {self.tournament_name} is {leader.club_name} with points {leader.points}')

            


  
club1 = FClub('Dynamo', 'Kyiv', 40)    
club2 = FClub('Shahtar', 'Donetsk', 30)  
club3 = FClub('Real', 'Madrid', 10) 

clubs1 = [club1, club2, club3]

tournament1 = Tournament(clubs1, 'England', 'Premier League')

tournament1.findOutsider()
tournament1.findLeader()