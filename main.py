my_dict = {
    'name': 'vishv',
    'academics': [
        {
            'subject': 'python',
            'code': '343412'
        },
        {
            'subject': 'java',
            'code': '3361602',
        },
    ],
    'age': '17',
    'department': 'IT'
}


# Hello, my name is vishv!
# I study two subjects python(343412) and java(3361602).
# I am 17 year old studying IT


# print(f'Hello,  my name is {my_dict["name"]}\n '
#       f'i study two subjects {my_dict["academics"][0]["subject"]}'
#       f'({my_dict["academics"][0]["code"]}) and {my_dict["academics"][1]["subject"]}'
#       f'({my_dict["academics"][1]["code"]}).\n'
#       f'i am {my_dict["age"]} year old studying {my_dict["department"]}')


# for value in my_dict.items():
#     print(f'Key: {value[0]} | Value: {value[1]}')

def add(a):
    result = 0
    for i in a:
        result += i
    total = len(a)
    average = result / total
    return average


x = [1, 5, 8, 1, 4, 7]
print(
    add(
        x
    )
)


def greet(firstname, lastname):
    return f'Hello {firstname} {lastname}'


print(greet("vishv", "munjapara"))


deposits = [100, 4000, 1220]
print("deposits:")
for i in deposits:
    print(f'     {deposits.index(i)+1}: {i}')