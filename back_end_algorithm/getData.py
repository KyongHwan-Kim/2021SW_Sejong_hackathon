import requests
import random
import json

def get_camera_StudentHall():
    url = "http://203.250.148.52:20516/Mobius/sw_hackathon/opencv_person_num/StudentHall/la"

    payload={}
    headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_res = json.loads(response.text)
    return json_res['m2m:cin']['con']

def get_camera_Gunja():
    url = "http://203.250.148.52:20516/Mobius/sw_hackathon/opencv_person_num/Gunja/la"

    payload={}
    headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_res = json.loads(response.text)
    return json_res['m2m:cin']['con']

def get_camera_DaeyangAI():
    url = "http://203.250.148.52:20516/Mobius/sw_hackathon/opencv_person_num/DaeyangAI/la"

    payload={}
    headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_res = json.loads(response.text)
    return json_res['m2m:cin']['con']


####---------------------------------건물 내 예상 이동 시간 알고리즘---------------------------------####

# 엘레베이터 예상 시간-----인원 수,엘레베이터 수, 갈 수 있는 층수가 정해진 엘레베이터를 고려하여 복잡도를 부여하여 예측
# 제약이 있는 엘레베이터는 능률을 절반으로 취급

def getComplexity(buildingName):

    pauseTimeOfEV = 8 #(s)
    populationStrainPerEV = 20 #()
    complexity = 0
    efficiency = 0

    if buildingName == "DaeyangAI":
        numOfEV = 6
        population = get_camera_DaeyangAI()
        howManyStrained = 0
    elif buildingName == "Gunja":
        numOfEV = 6
        howManyStrained = 0
        population = get_camera_Gunja()
    elif buildingName == "StudentHall":
        numOfEV = 2
        howManyStrained == 1
        population = get_camera_StudentHall()
    
    efficiency = (numOfEV-howManyStrained)+0.5*(howManyStrained)

    if population > populationStrainPerEV:
        complexity += 60
    else:
        complexity += pauseTimeOfEV*(population/efficiency)

    return complexity

def timeOfEV(getComplexity):

    time = 0

    sumOfFloor = abs(targetFloor - startFloor)
    timePerFloor = 5

    time += sumOfFloor * 5 + getComplexity

    return time

# 1층 이동하는 데 걸리는 시간; 달리는 경우: 7sec, 걷는 경우: 16sec
# 반환값은 튜플 형태로 (걷는 경우, 뛰는 경우)

def timeOfStair(startFloor, targetFloor):

    return (16*abs(targetFloor-startFloor), 7*abs(targetFloor-startFloor))


if __name__ in "__main__":

    # 입구와 같은 층에 위치한 목적지를 갈 때는 코드를 다르게 짜야 함
    if entranceFloor == targetFloor:
        pass

    # 그 외의 경우 아닌 경우는 엘레베이터, 계단 쪽에 가까운 곳을 우선적으로 가야 함
    # 계단과 엘레베이터를 선택하는 코드
    else:
        walkTime,runTime = timeOfStair(startFloor, targetFloor)
        if timeOfEV(getComplexity) > walkTime:
            pass
    
    #걷는 거 뛰는 거 추천

    print(get_camera_DaeyangAI())
    print(get_camera_StudentHall())
    print(get_camera_Gunja())