import json

class Engine:
    def __init__(self, json_data,fuels):
        self.name = json_data["name"]
        self.type = json_data["type"]
        self.efficiency= json_data["efficiency"]
        self.pmin = json_data["pmin"]
        self.pmax = json_data["pmax"]

        fuel_price= 0
        if( json_data["type"] != "windturbine" ):
            fuel_price = fuels[json_data["type"]]
        self.cost_per_unity = compute_cost(fuel_price,json_data["efficiency"],1)
        self.cost_prod = 0
        self.load = 0
    # Add cost to cost_prod
    def addCost(self,cost):
        self.cost_prod += cost
    def __str__(self):
        return "name :"+ self.name +" type :"+self.type +"load :"+ str(self.load) +" cost/u :"+str(self.cost_per_unity)+" eff : "+str(self.efficiency) + " pmin :"+str(self.pmin) +" pmax :"+str(self.pmax)


def production_data(data):
    var_load = data["load"]
    fuels = map_fuels(data["fuels"])

    list_powerplants = []
    #create a list of object engine
    for e in data["powerplants"] :
        engine_obj = Engine(e,fuels)
        list_powerplants.append(engine_obj)

    #sorted list pmin
    list_powerplants.sort(key=lambda x: x.cost_per_unity)
    # Algorithme
    value = 0
    index = 0
    while(value < var_load ):
        elem = list_powerplants[index]
        #Compute load of the pmax, ex: wind with 60% of efficiency
        p_val = compute_load(fuels, elem.type, elem.pmax)
        if(value+p_val < var_load):
            if(index+1 < len(list_powerplants)):
                if value+p_val+compute_load(fuels,elem.type,list_powerplants[index+1].pmin) > var_load:
                   rest = value+p_val+compute_load(fuels,elem.type,list_powerplants[index+1].pmin)-var_load
                   value += p_val-rest
                   elem.load = p_val - rest
                else:
                    value += p_val
                    elem.load = p_val
                list_powerplants[index] = elem
            index+=1
        elif (value+compute_load(fuels,elem.type,elem.pmin) <= var_load and value+p_val > var_load ):
            rest = var_load - value
            if(rest <= p_val):
                value += rest
                elem.load = rest
            else:
                value += compute_load(fuels,elem.type,elem.pmin)
                elem.load = compute_load(fuels,elem.type,elem.pmin)
            list_powerplants[index] = elem
            index+=1
    return create_json_response(list_powerplants)
#Create the response to send
def create_json_response(list_powerplants):
    list = []
    for e in list_powerplants:
        if(e.type == "windturbine"):
             list.append({"name": e.name, "p": e.load})
        else:
            list.append({"name": e.name, "p": e.load})

    return json.dumps(list)

#Compute the cost of fuel
def compute_cost(Fuel_price,efficiency,p):
    return Fuel_price*(p/efficiency)

def compute_load(fuels,type,p):
    if(type == "windturbine"):
        return p*fuels[type]/100
    else:
        return p
    #Mapping The different cost of fuel
def map_fuels(data):
    fuels = {}
    fuels["gasfired"] = data["gas(euro/MWh)"]
    fuels["turbojet"] = data["kerosine(euro/MWh)"]
    fuels["Co2"] = data["co2(euro/ton)"]
    fuels["windturbine"] = data["wind(%)"]
    return fuels
