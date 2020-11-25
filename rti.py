def romantoint(s: str):
    alphabet = {'M': 1000, 'D': 500, 'C': 100,
                'L': 50, 'X': 10, 'V': 5, 'I': 1}
    s = list(s)
    k = 0
    key = list(alphabet.keys())
    val = list(alphabet.values())
    s = s[::-1]
    for i in range(len(s)):
        for q in range(7):
            if s[i] == key[q]:
                s[i] = val[q]
    for j in range(len(s) - 1):
        if s[j] <= s[j + 1]:
            k += s[j]
        else:
            k += s[j] - 2 * s[j + 1]
            j += 1
    k += s[len(s) - 1]
    print('А вот и Ваше преобразованное число: ', k)


romantoint(input('Введите число римскими цифрами, и мы тут же его переведём: '))
