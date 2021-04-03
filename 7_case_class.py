from dataclasses import dataclass

@dataclass
class TravelLog:
    country: str
    visits: int
    cities: []

log1 = TravelLog("Netherlands", 12, ["Emmen","Assen"])
log2 = TravelLog("Turkey", 24, ["Ankara","Denizli"])

logs = []
logs.append(log1)
logs.append(log2)

for x in logs:
    print(x.country)