# source = www.programmers.co.kr

def solution(phone_book):
    answer = True
    phone_book.sort()
    first = phone_book[0]

    for i in range(1, len(phone_book)):
        len_ = len(first)
        if len_ > len(phone_book[i]):
            continue

        for j in range(len_):
            if first[j] != phone_book[i][j]:
                break
        else:
            answer = False
            break

    print(answer)
    return answer

solution(['123', '12', '123', '133', '2123'])
solution(["12", "123", "1235", "567", "88"])
solution(["119", "97674223", "1195524421"])
solution(["123", "456", "789"])
