#coding:gbk
import random
def name_to_number(name):
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="��":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        print("Error:No Correct Name")
def number_to_name(number):
    if number in range(0,5):
        if number==0:
            return "ʯͷ"
        elif number==1:
            return "ʷ����"
        elif number==2:
            return "��"
        elif number==3:
            return "����"
        elif number==4:
            return "����"
        else:
            print("Error:No Corrcet Name")
            
player_choice=input("����������ѡ��:")
player_number=name_to_number(player_choice)
comp_number=random.randrange(0,5)
comp_choice=number_to_name(comp_number)
print("����ѡ����:",player_choice)
print("�������ѡ���ǣ�",comp_choice)
if player_number-comp_number in range(-4,-2) or range(1,3):  
    print("��Ӯ��")
elif player_number-comp_number in range(-2,0) or range(3,5):
    print("�����Ӯ��")
elif player_number-comp_number==0:
    print("ƽ��")



