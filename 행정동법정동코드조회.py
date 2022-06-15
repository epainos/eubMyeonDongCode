import sqlite3  #pip install pysqlite3 
import re #정규식사용하게해주는 것


def myf질의행정동법정동코드(시도명, 시군구명, 읍면동명, 리명 = ' '): #사실 시도명은 필요없다. 리가 없는 것은 공백처리함
 
    if 리명 == ' ':  #경기도 용인시 처인구 포곡읍 신원리
        cur.execute('SELECT * FROM data where 시군구명 = "' +시군구명+  '" and  읍면동명 = "' +읍면동명+ '" and 삭제일자 IS NULL')
    else:   #경기도 성남시 수정구 수진동
        cur.execute('SELECT * FROM data where 시군구명 = "' +시군구명+ '" and  리명 = "' +리명+ '" and 삭제일자 IS NULL')


    rows = cur.fetchall()
    '''확인용
    for row in rows:
        print( row[0][0:5],row[0][5:10],   row)
    '''
    try:
        print( "행정동코드: ", rows[0][0][0:5], "   , 법정동코드: ", rows[0][0][5:10])
        return rows[0][0:5],rows[0][5:10]
    except:
        print(시도명, 시군구명, 읍면동명, 리명, "주소검색이 안되네요")
        return "",""
        

def myf주소나누기(전체주소):
    try:
        temp = re.search(' [0-9]', 전체주소).start()    #번지에서 자름
        my주소앞머리  = myString[0:temp]
        my번지 = myString[temp+1:100]
        try:
            temp = re.search('-', my번지).start()  #번지안에서 -에서 자름
            my번 = my번지[0:temp].strip()
            my지 = my번지[temp+1:100].strip()
        except:
            my번 = my번지.strip()
            my지 = ""
    except:
        my주소앞머리 = 전체주소 
        my번 = ""
        my지 = ""
    


    temp = my주소앞머리.split() #주소를 일단 쉼표에서 다 나눔
    if len(temp) == 5: #리가 있는 곳
        #print("---리가 있는 곳인가 보네요")
        my시도 = temp[0].strip()
        my시군 = temp[1].strip()
        my구 = temp[2].strip()
        my읍면동 = temp[3].strip()
        my리 = temp[4].strip()
    elif len(temp) == 4: #일반 주소
        #print("---주소를 나눕니다")
        my시도 = temp[0].strip()
        my시군 = temp[1].strip()
        my구 = temp[2].strip()
        my읍면동 = temp[3].strip()
        my리 = " "  #리가 없는 것은 공백처리
    elif len(temp) == 3: #구가 없는 곳
        #print("---주소를 나눕니다")
        my시도 = temp[0].strip()
        my시군 = temp[1].strip()
        my구 = ""
        my읍면동 = temp[2].strip()
        my리 = " "  #리가 없는 것은 공백처리
    else:   #오류있는 것
        print("주소나누기가 안되네요. 띄어쓰기 등을 확인해 보세요...    ", 전체주소)
        return "","","","","","",""

    print(전체주소,"를 다음처럼 변환했습니다.   ", my시도,"-", my시군,"-", my구,"-", my읍면동,"-", my리,"- 번지는 ",  my번,", ", my지 )
    return my시도, my시군, my구, my읍면동, my리, my번, my지


def myf행정동법정동코드변환(전체주소):
    temp = (myf주소나누기(전체주소))
    myf질의행정동법정동코드("", temp[1]+temp[2],temp[3], temp[4])


########################################################## 시작해보자
conn = sqlite3.connect("국토교통부_전국 법정동_20211217.sqlite")
cur = conn.cursor()



#myString = "경기도 용인시 처인구 포곡읍 신원리 10-1"
#myString = "경기도  성남시 수정구 수진동 10 -1"
myString = "경기도 구리시 수택동"

myString = "경기도 구리시 수택동 "
#myString = "경기도 수원시 팔달구 팔달로1가 1"

myf행정동법정동코드변환(myString)



conn.close()









