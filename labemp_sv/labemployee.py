'''
Khai báo đối tượng Employee có:
Các thuộc tính (fields, states) sau
- mã số (code)
- tên (name)
- tuổi (age)
- lương (salary)
Các phương thức (behaviors, methods)
- Tổng thu nhập hằng năm sau thuế (income) biết rằng tax = 10%
- In ra thông tin của nhân viên (display)
- Tăng lương cho nhân viên (increaseSalary), biết rằng số lương tăng phải lớn hơn 0
- (Sinh viên tự viết) Giảm lương cho nhân viên (decreaseSalary), biết rằng số lương giảm phải lớn hơn 0 và không vượt quá 20% lương hiện tại
============= YÊU CẦU CHƯƠNG TRÌNH==============
Khai báo biến danh sách (list) nhân viên (dsNhanVien) để lưu trữ các nhân viên và viết chương trình menu thực hiện các chức năng bên dưới
- Opt-1: Tải danh sách nhân viên từ file dbemp_input.db
- Opt-2: Thêm nhân viên vào danh sách
- Opt-3: Hiển thị danh sách nhân viên
- Opt-4: Hiển thị thông tin của một nhân viên khi biết mã nhân viên
- Opt-5: Chỉnh sửa thông tin một nhân viên
- Opt-6: Xóa một nhân viên ra khỏi danh sách
- Opt-7: Tăng lương cho một nhân viên
- Opt-8: Giảm lương cho một nhân viên
- Opt-9: Tính số lượng nhân viên (countEmp) và xuất ra màn hình
- Opt-10: Tính tổng tiền lương của công ty phải trả hàng tháng (sumSalary) và xuất ra màn hình
- Opt-11: Tính trung bình lương của nhân viên (avgSalary) và xuất ra màn hình
- Opt-12: Tính độ tuổi trung bình của nhân viên (avgAge) và xuất ra màn hình
- Opt-13: Tính tuổi lớn nhất của các nhân viên (maxAge) và hiển thị danh sách nhân viên có tuổi lớn nhất
- Opt-14: Sắp xếp danh sách nhân viên tăng dần theo lương
- Opt-15: Vẽ biểu đồ tương quan lương theo độ tuổi
- Opt-16: Vẽ biểu đồ so sánh lương trung bình của các nhóm tuổi: nhỏ hơn 35, từ 35 đến 50, hơn 50 trở lên
- Opt-17: Vẽ biểu đồ thể hiện phần trăm tổng lương trên các nhóm tuổi như Opt-16
- Opt-18: Vẽ biểu đồ thể hiện phần trăm số lượng nhân viên theo các nhóm tuổi như Opt-16
- Opt-19: Lưu danh sách nhân viên xuống file dbemp_output.db, biết rằng mỗi nhân viên là một dòng và các thông tin nhân viên được phân cách bởi dấu '-'
- Opt-Khác: Thoát chương trình
'''

from keyword import kwlist
from turtle import color
import matplotlib.pyplot as plt
import Employee as emp
import numpy as np


menu_options = {
    1: 'Load data from file',
    2: 'Add new employee',
    3: 'Display list of employee',
    4: 'Show employee details',
    5: 'Update employee information',
    6: 'Delete employee',
    7: 'Increase salary of employee',
    8: 'Decrease salary of employee',
    9: 'Show total employee a month',
    10: 'Show total salary a month',
    11: 'Show average of salary a month',
    12: 'Show average of age',
    13: 'Show maximum age',
    14: 'Sort list of employee according to salary by ascending',
    15: 'Draw salary according to age',
    16: 'Draw average of salary chart by age group',
    17: 'Draw percentage of salary by age group',
    18: 'Draw percentage of total employee by age group',
    19: 'Store data to file',
    'Others': 'Exit program'
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


# Khai báo biến lưu trữ những nhân viên
dsNhanVien = []


def Search(maso, dsNV):  # tìm kiếm
    kq = -1
    for i in range(0, len(dsNV)):
        if dsNV[i].code == maso:
            return i
    else:
        return kq


def update(maso, dsNV): #update
    kq = Search(maso, dsNV)
    if kq < 0:
        print("Nothing here")
    else:
        ten = input("Input name: ")
        tuoi = int(input("Input age: "))
        luong = float(input("Input salary: "))
        nv = emp.Employee(maso, ten, tuoi, luong)
        dsNV[kq] = nv

def deleteEmp(maso, dsNV):
    kq = Search(maso, dsNV)
    if kq < 0:
        print("Nothing here")
    else:
        dsNV.pop(kq)

def myFunc(emp): #sắp xếp
    return emp.salary


def avg(sum, count):    #tính trung bình lương
    if count == 0:
        return sum
    else:
        return sum/count


def percent(avg, sum): #tính phần trăm
    if sum == 0:
        return 0
    else:
        return avg/sum * 100


while (True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Input choice: '))
    except:
        print('Invalid input, try again')
        continue
    # Check what choice was entered and act accordingly
    if userChoice == 1:  # load
        fr = open('D:\Ky - 5\phantichdulieu1\labemp_sv\labemp_sv\dbemp_input.db', mode='r', encoding='utf-8')
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            maso = ds[0]
            ten = ds[1]
            tuoi = int(ds[2])
            luong = float(ds[3])
            nv = emp.Employee(maso, ten, tuoi, luong)
            dsNhanVien.append(nv)
        fr.close()
    elif userChoice == 2:  # add
        maso = input("Input code: ")
        ten = input("Input name: ")
        tuoi = int(input("Input age: "))
        luong = float(input("Input salary: "))
        nv = emp.Employee(maso, ten, tuoi, luong)
        dsNhanVien.append(nv)
    elif userChoice == 3:  # show ds
        for item in dsNhanVien:
            item.display()
    elif userChoice == 4:  # show emp detail
        maso = input("Input code: ")
        kq = Search(maso, dsNhanVien)
        if kq < 0:
            print("Nothing here")
        else:
            dsNhanVien[kq].display()
    elif userChoice == 5:  # update
        maso = input("input code: ")
        update(maso, dsNhanVien)
    elif userChoice == 6:  # delete
        maso = input("Input code: ")
        deleteEmp(maso, dsNhanVien)
    elif userChoice == 7:  # Increase salary of employee
        maso = input("Input code: ")
        kq = Search(maso, dsNhanVien)
        if kq < 0:
            print("Nothing here")
        else:
            amount = (float(input("Input amount: ")))
            dsNhanVien[kq].increaseSalary(amount)
    elif userChoice == 8:  # Decrease salary of employee
        maso = input("Input code: ")
        kq = Search(maso, dsNhanVien)
        if kq < 0:
            print("Nothing here")
        else:
            amount = (int(input("Input amount: ")))
            dsNhanVien[kq].decreaseSalary(amount)
    elif userChoice == 9:  # Show total employee a month
        print(f'Number of employees: {len(dsNhanVien)}')
    elif userChoice == 10:  # Show total salary a month
        sumSalary = 0.0
        for item in dsNhanVien:
            sumSalary = sumSalary + item.salary
        print(f'Total salary a month: {sumSalary:.2f}')
    elif userChoice == 11:  # Show average of salary a month
        avgSalary = 0.0
        sumSalary = 0.0
        for item in dsNhanVien:
            sumSalary = sumSalary + item.salary
        avgSalary = sumSalary / len(dsNhanVien)
        print(f'Average of salary: {avgSalary:.2f}')
    elif userChoice == 12:  # Show average of age
        avgAge = 0.0
        sumAge = 0.0
        for item in dsNhanVien:
            sumAge = sumAge + item.age
        avgAge = sumAge / len(dsNhanVien)
        print(f'Average of age: {avgAge:.2f}')
    elif userChoice == 13:  # Show maximum age
        maxAge = dsNhanVien[0].age
        for item in dsNhanVien:
            if maxAge < item.age:
                maxAge = item.age
        print(f'Maximum age: {maxAge}')
    elif userChoice == 14:  # Sort list of employee according to salary by ascending
        dsNhanVien.sort(key=myFunc)
    elif userChoice == 15:  # Draw salary according to age
        arrTuoi = []
        arrLuong = []
        for item in dsNhanVien:
            arrTuoi.append(item.age)
            arrLuong.append(item.salary)
        # Vẽ đồ thị
        plt.figure(figsize=(15, 5))

        plt.title("Age and salary chart")
        plt.xlabel("Ox: age")
        plt.ylabel("Oy: salary")

        plt.plot(arrTuoi, arrLuong, "og")
        plt.show()
    elif userChoice == 16:  # Draw average of salary chart by age group
        arrLevel = ["less than 35", "from 35 to 50", "more than 50"]
        arrSalary = []
        sum1, sum2, sum3, count1, count2, count3 = 0, 0, 0, 0, 0, 0
        for item in dsNhanVien:
            if item.age < 35:
                sum1 += item.salary
                count1 += 1
            elif item.age >= 35 and item.age <= 50:
                sum2 += item.salary
                count2 += 1
            else:
                sum3 += item.salary
                count3 += 1
        arrSalary = [avg(sum1, count1), avg(sum2, count2), avg(sum3, count3)]
        # Vẽ đồ thị
        plt.figure(figsize=(15, 5))

        plt.title("Average Of Salary Chart By Age Group")
        plt.xlabel("Levels of age")
        plt.ylabel("Average of salary")

        plt.bar(arrLevel, arrSalary, width=0.5, color='green')
        plt.show()
    elif userChoice == 17:  # Draw percentage of salary by age group
        sum1, sum2, sum3, count1, count2, count3 = 0, 0, 0, 0, 0, 0
        arrLevel = ["less than 35", "from 35 to 50", "more than 50"]
        for item in dsNhanVien:
            if item.age < 35:
                sum1 += item.salary
                count1 += 1
            elif item.age >= 35 and item.age <= 50:
                sum2 += item.salary
                count2 += 1
            else:
                sum3 += item.salary
                count3 += 1
        arrSalary = [avg(sum1, sum1+sum2+sum3),avg(sum2, sum1+sum2+sum3),avg(sum3, sum1+sum2+sum3)]

        noibat = [0, 0.1, 0]
        color = ['blue', 'orange', 'green']

        plt.pie(arrSalary, explode=noibat, colors=color,
                labels=arrLevel, shadow=True, startangle=45)

        plt.axis("equal")

        plt.legend(title='Levels of age')

        plt.show()
    elif userChoice == 18: #Draw percentage of total employee by age group
            count1, count2, count3 = 0, 0, 0
            arrLevel = ["less than 35", "from 35 to 50", "more than 50"]
            for item in dsNhanVien:
                if item.age < 35:
                    count1 += 1
                elif item.age >= 35 and item.age <= 50:
                    count2 += 1
                else:
                    count3 += 1
            arrSL = [percent(count1, len(dsNhanVien)),percent(count2, len(dsNhanVien)),percent(count3, len(dsNhanVien))]

            noibat = [0,0.1,0]
            color = ['blue','orange','green']

            plt.pie(arrSL, explode=noibat, colors=color, labels=arrLevel, shadow=True, startangle=45)

            plt.axis("equal")

            plt.legend(title='Levels of age')
            plt.title("Percentage Of Total Employee By Age Group")

            plt.show()
    elif userChoice == 19:
        fw = open('D:\\Ky - 5\\phantichdulieu1\\labemp_sv\\labemp_sv\\dbemp_output.db', mode='w', encoding='utf-8')
        for item in dsNhanVien:
            fw.write(f'code: {item.code}, name: {item.name}, age: {item.age}, salary: {item.salary}, income: {item.income()}\n')
        fw.close()
    else:
        print('Thoát chương trình BYE BYE')
        break