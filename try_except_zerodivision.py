def try_test():

    try:
        a,b = input('두수를 넣으세요').split()
        result=(int(a)/int(b))
        print(result)
    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다')
        return try_test()
    except TypeError:
        print('지원되자 않는 연산자를 사용한 오류입니다.')
        return try_test()
    except Exception as a:
        print('오류 종류 : {}'.format(a))
        return try_test()
    print('test')

try_test()