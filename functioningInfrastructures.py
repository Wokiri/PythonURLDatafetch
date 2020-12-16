import urllib.request
import json

def resourcesInfo(dataSource):
    placeVillageName = None
    number_water_points_per_community = 0
    community_ranking = 7
    list_communities = []
    numberOfFunctional = 0
    numberOfBroken = 0
    numberOfNew = 0
    numberOfUnderconstruction = 0
    numberOfAbandoned = 0
    numberOfNaNd = 0
    
    with urllib.request.urlopen(dataSource) as resourcesData:
        theData = resourcesData.read()
        jsonData = json.loads(theData)
        
        for i in range(0, len(jsonData)):
            placeVillageName = jsonData[i]['communities_villages']
            list_communities.append(placeVillageName)
            
            pointCondition = jsonData[i]['water_point_condition']
            
            if pointCondition == 'functioning':
                numberOfFunctional = numberOfFunctional + 1
                
            if pointCondition == 'broken':
                numberOfBroken = numberOfBroken + 1
                
            if pointCondition == 'newly_constructed':
                numberOfNew = numberOfNew + 1
                
            if pointCondition == 'under_construction':
                numberOfUnderconstruction = numberOfUnderconstruction + 1
                
            if pointCondition == 'abandoned':
                numberOfAbandoned = numberOfAbandoned + 1
                
            if pointCondition == 'na_dn':
                numberOfNaNd = numberOfNaNd + 1
                
        communities_json_data = {}
        for communities in list_communities:
            number_waterpoints = list_communities.count(communities)
            communities_json_data.update({communities : number_waterpoints})
        
        
        
        ranking_json_data = {}
        for communities in list_communities:
            numberBroken_perCommunity = 0
            
            for i in range(0, len(jsonData)):
                communityName = jsonData[i]['communities_villages']
                conditionOfResources = jsonData[i]['water_point_condition']
                
                if communities == communityName and conditionOfResources == 'broken':
                    numberBroken_perCommunity = numberBroken_perCommunity + 1
                    ranking = numberBroken_perCommunity*100/numberOfBroken
                    ranking_json_data.update({communities : f'{ranking} Percent'})
        
        
        
        resultsJson = {
            'number_functional': numberOfFunctional,
            'number_water_points': communities_json_data,
            'community_ranking': ranking_json_data
        }
        
        return json.dumps(resultsJson)
        

sourceURL = 'https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json'
print(resourcesInfo(sourceURL))