iplteam = {
    "states": [
        {
            "name": "Maharashtra",
            "team": {
                "name": "Mumbai Indians",
                "players": [
                    {"name": "Rohit Sharma", "role": "Captain"},
                    {"name": "Hardik Pandya", "role": "Vice Captain"},
                    {"name": "Suryakumar Yadav", "role": "Batsman"},
                    {"name": "Pollard", "role": "All-rounder"}
                ]
            }
        },
        {
            "name": "Punjab",
            "team": {
                "name": "Punjab Super Kings",
                "players": [
                    {"name": "Shreyas Iyer", "role": "Captain"},
                    {"name": "Butler", "role": "Vice Captain"},
                    {"name": "Prabhsimran", "role": "Batsman"},
                    {"name": "Stoinis", "role": "All-rounder"}
                ]
            }
        },
        {
            "name": "Tamil Nadu",
            "team": {
                "name": "Chennai Super Kings",
                "players": [
                    {"name": "MS Dhoni", "role": "Captain"},
                    {"name": "Ruturaj", "role": "Vice Captain"},
                    {"name": "Rayudu", "role": "Batsman"},
                    {"name": "Jadeja", "role": "All-rounder"}
                ]
            }
        }
    ]
}

#print(iplteam)

print(iplteam["states"][1]["team"]["players"][0])
