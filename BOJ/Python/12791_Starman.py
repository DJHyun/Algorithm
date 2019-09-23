# baekjoon source = "https://www.acmicpc.net/problem/12791"

T = int(input())
year = [1967,
        1969,
        1970,
        1971,
        1972,
        1973,
        1973,
        1974,
        1975,
        1976,
        1977,
        1977,
        1979,
        1980,
        1983,
        1984,
        1987,
        1993,
        1995,
        1997,
        1999,
        2002,
        2003,
        2013,
        2016
        ]
song = [
    'DavidBowie',
    'SpaceOddity',
    'TheManWhoSoldTheWorld',
    'HunkyDory',
    'TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars',
    'AladdinSane',
    'PinUps',
    'DiamondDogs',
    'YoungAmericans',
    'StationToStation',
    'Low',
    'Heroes',
    'Lodger',
    'ScaryMonstersAndSuperCreeps',
    'LetsDance',
    'Tonight',
    'NeverLetMeDown',
    'BlackTieWhiteNoise',
    '1.Outside',
    'Earthling',
    'Hours',
    'Heathen',
    'Reality',
    'TheNextDay',
    'BlackStar'
]
for test_case in range(T):
    s, e = map(int, input().split())
    result = []
    for i in range(len(year)):
        if s <= year[i] <= e:
            result.append(str(year[i]) +' '+ song[i])

    print(len(result))
    for i in result:
        print(i)