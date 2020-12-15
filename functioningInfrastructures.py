import urllib.request
import json

def resourcesInfo(dataSource):
    numberOfFunctional = 0
    with urllib.request.urlopen(dataSource) as resourcesData:
        theData = resourcesData.read()
        jsonData = json.loads(theData)
        
        for i in range(0, len(jsonData)):
            placeVillageName = jsonData[i]['communities_villages']
            placeWardName = jsonData[i]['locations_wards']
            pointCondition = jsonData[i]['water_point_condition']
            if pointCondition == 'functioning':
                numberOfFunctional = numberOfFunctional + 1
            print(f'For village: {placeVillageName.title()} of ward: {placeWardName.title()}, the resource condition is: {pointCondition.title()}')
            
            
        print(f'\nThere are a total of {numberOfFunctional} functional water points out of a possible {len(jsonData)}.')
        

sourceURL = 'https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json'
resourcesInfo(sourceURL)