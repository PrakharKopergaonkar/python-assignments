players = {"batsmen":{"rohit sharma" : {"matches" : 205, "runs" : 25555, "highest score":"250", "average": 89},
                    "virat kohli" : {"matches": 2506, "runs" : 255613, "highest score": "187", "average": 98},
                    "shikhar dhawan" : {"matches": 2516, "runs" : 225613, "highest score": "217", "average": 96}}}
max = 0
for p_info in players.values():
    for stats in p_info.values():
        if(int(stats["highest score"]) > max):
             max = int(stats["highest score"])
print("max highest score is : {}".format(max))
