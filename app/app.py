def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("�������� ��������:")
print("1. ��������")
print("2. ���������")
print("3. ���������")
print("4. �������")

choice = input("������� ����� �������� (1/2/3/4): ")

num1 = float(input("������� ������ �����: "))
num2 = float(input("������� ������ �����: "))

result = 0

if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    print("�������� ��������!")

print("��� ���������: ", result)