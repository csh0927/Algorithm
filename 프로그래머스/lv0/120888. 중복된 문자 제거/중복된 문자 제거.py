def solution(my_string):
    answer = ''
    st = []
    for i in my_string:
        if i not in st:
            st.append(i)
    return ''.join(st)