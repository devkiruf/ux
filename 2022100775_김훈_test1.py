
ju_basics = 910
gong_basics = 1600
san_basics = 7300
ju_per = 88
gong_per = 182
san_per = 275
a = int(input("사용하시는 전력용도를 말해주세요 (1 : 주택용, 2 : 공업용, 3 : 산업용)"))
b = int(input("사용한 전기량을 입력해주세요"))
if a > 0:
    if a == 2:
        gong_ussed = gong_basics + (gong_per * b)
        print(f"용도:2, 사용량: {b:.2f}, 전기요금: , {gong_ussed:,.2f}원")
    elif a == 3:
        san_used = san_basics + (san_per * b)
        print(f"용도:3, 사용량:{b:.2f}, 전기요금: , {san_used:,.2f}원")
    elif a == 1:
        ju_used = ju_basics + (ju_per * b)
        print(f"용도:1, 사용량:{b:.2f}, 전기요금: , {ju_used:,.2f}원")
    else:
        print(f"잘못된 값을 입력하셨습니다")
else:
    print(f"잘못된 값을 입력하셨습니다")

    
        
        

        