from csv_loader import CsvLoader
from subway import Subway

def input_station(subway, message):
    name = input(message).strip()
    if name == '':
        print('[오류] 역 이름을 입력하지 않았습니다.')
        return ''

    name = subway.short_name(name)
    if subway.has_station(name):
        return name

    print('[오류] ' + name + ' 역이 없습니다.')
    return ''

def search(subway):
    start = input_station(subway, '출발역: ')
    if start == '':
        return
    end = input_station(subway, '도착역: ')
    if end == '':
        return
    if start == end:
        print('[오류] 출발역과 도착역이 같습니다.')
        return

    routes = subway.find_all_routes(start, end)
    if len(routes) == 0:
        print('[오류] 두 역을 잇는 경로가 없습니다.')
        return

    print()
    print(start + ' -> ' + end + ' 경로 ' + str(len(routes)) + '개 (빠른 순)')
    for i in range(len(routes)):
        print(str(i + 1) + '. ' + subway.route_to_text(routes[i]))


def main():
    loader = CsvLoader('daegu_subway_stations.csv')
    try: 
        stations = loader.load()
    except FileNotFoundError as e:
        print('[오류] CSV 파일이 없습니다: ' + str(e))
        return

    subway = Subway(stations)
    print('대구 지하철 길찾기 (역 ' + str(len(subway.graph)) + '개)')

    while True: 
        print()
        print('1. 경로 검색')
        print('2. 종료')
        menu = input('선택: ').strip()
        if menu == '1':
            search(subway)
        elif menu == '2':
            print('프로그램을 종료합니다.')
            break
        else:
            print('[오류] 1 또는 2를 입력하세요.')

main()
