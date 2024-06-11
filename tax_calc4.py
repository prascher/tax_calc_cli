#!/usr/bin/env python3
#taxcalc cmd 4.0 alpha(for python 3) by Phillip D. Rascher
#Inspired by CIS 103
def formater():
    print('-----------')
def getTax():
    taxp = float(input('please input the tax of the point of purchase for your items '))
    tax = taxp/100
    return tax
def displayTotal(subtotal,tax):
    print("Subtotal: $",format(subtotal, ',.2f'))
    tax = subtotal * tax
    print("Tax: $",format(tax, ",.2f"))
    total =  tax + subtotal
    print("That comes to: $", format(total, ",.2f"))
def singleRate():
    cont = "Y"
    subtotal = 0.0
    while cont == "y" or cont =="Y":
        item = float(input('Please enter item price: '))
        subtotal += item
        cont = input("continue? (y/N)")
    tax = getTax()
    displayTotal(subtotal,tax)
def multiRate():
    cont = "Y"
    subtotal1 = 0.0
    while cont == "y" or cont =="Y":
        item = float(input('Please enter item prices at first rate: '))
        subtotal1 += item
        cont = input("continue? (y/N)")
    tax1 = getTax()
    displayTotal(subtotal1,tax1)
    cont = "Y"
    subtotal2 = 0.0
    while cont == "y" or cont =="Y":
        item = float(input('Please enter item price: '))
        subtotal2 += item
        cont = input("continue? (y/N)")
    tax2 = getTax()
    displayTotal(subtotal2,tax2)
def menu():
    sel = 0
    while sel != 9:
        print('1) Single rate tax')
        print('2) Multi rate tax')
        print('9) quit')
        sel = input('enter selection: ')
        formater()
        try:
            sel = int(sel)
        except:
            print('please enter a number')
            formater()
        if sel == 1:
            singleRate()
        elif sel == 2:
            multiRate()
        elif sel == 9:
            return
        else:
            print('invalid choice')
            formater()
def main():
    ans = 'N'
    while ans.upper() == 'N':
        menu()
        ans = input('are you sure you want to quit? (Y/n): ')
    formater()
    print('goodbye')
main()
