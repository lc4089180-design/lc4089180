#Given the following code for a class UserProfile, extend it to create an InfluencerProfile subclass that adds a followers attribute and a method get_influencer_level() which returns 'Micro', 'Macro', or 'Mega' based on the number of followers.<br><br><em><strong>Hint:</strong> Micro: < 10,000, Macro: 10,000–1,000,000, Mega: > 1,000,000</em>
class UserProfile:
    def __init__(self, username):
        self.username = username

    def display_profile(self):
        print("Username:", self.username)


class InfluencerProfile(UserProfile):
    def __init__(self, username, followers):
        super().__init__(username)
        self.followers = followers

    def get_influencer_level(self):
        if self.followers < 10000:
            return "Micro"
        elif self.followers <= 1000000:
            return "Macro"
        else:
            return "Mega"


user1 = InfluencerProfile("kavita123", 8500)
user2 = InfluencerProfile("fashion_star", 50000)
user3 = InfluencerProfile("celebrity", 1500000)

print(user1.username, "-", user1.get_influencer_level())
print(user2.username, "-", user2.get_influencer_level())
print(user3.username, "-", user3.get_influencer_level())