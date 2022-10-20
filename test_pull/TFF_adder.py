'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-09-03 11:55:00
LastEditors: tonyhsu bear541593@gmail.com
LastEditTime: 2022-10-09 17:07:02
FilePath: \LAB_code\basic.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import random
import csv
one_count=0
zero_count=0
num_reg=0
value_number=0
value_number2=0
mul_value=0
RMS=0
addition_number=50

bit_stream_length=1024

file = open('TFF_adder1024.csv',mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["y的值","理論結果","只經SNG後的結果","加入TFF_adder後的結果"])
for round in range (bit_stream_length):
    in_number=round
    print("Round",in_number,": ")
    TFF_state=False #TFF的initial state, s0時=0, s1時=1,
    value_number=0
    value_number2=0
    mul_value=0
    adder_value=0
    TFF_value=0
    TFF_adder_sum=0
    for number in range(bit_stream_length):
        random_number=random.randrange(bit_stream_length)
         
        #TFF的 x input-----------------------------------------------
        if int(in_number)>=random_number:
            out_number=1
        else:
            out_number=0

        if out_number==1:
            value_number=value_number + 1

        #TFF的 y input---------------------------------------------
        if addition_number>=random.randrange(bit_stream_length):
            out_number2=1
        else:
            out_number2=0
        
        if out_number2==1:
            value_number2=value_number2 + 1

        #--------------------------------------------
        # print("out_number=",out_number)
        # print("out_number2=",out_number2)
        
        # Bipolar的乘法(XNOR)---------------------------------------------------
        # if out_number==out_number2:
        #     mul=1
        # else:
        #     mul=0
        # if mul==1:
        #     mul_value=mul_value + 1
        #------------------------------------------------------------------------------
        
        #XOR----------------------------------------------
        if (out_number!=out_number2):
            xor_out=1
        else:
            xor_out=0

        #TFF的運作--------------------------------------------------
        if(xor_out!=1):
            TFF_out=out_number2
        else:
            TFF_out=TFF_state
            TFF_state=int(not TFF_state)

        #計算output value---------------------------------------------------
        if (TFF_out==1):
            TFF_value=TFF_value+1
        #-------------------------------------------------------------------    
    real_scaled_adder_sum=(round+addition_number)/2 #分子
    TFF_adder_sum=TFF_value #分子

    print("Real scaled adder sum= ",(2*(real_scaled_adder_sum)-bit_stream_length), "/", bit_stream_length)
    print("TFF adder sum= ",(2*(TFF_adder_sum)-bit_stream_length), "/", bit_stream_length) 
    
    out1=(2*(value_number)-bit_stream_length)/bit_stream_length   #2*(px)-1
    out2=(2*(value_number2)-bit_stream_length)/bit_stream_length  #2*(py)-1
    bipolar_out=2*(real_scaled_adder_sum/bit_stream_length)-1             #2*(expected sum)-1
    adder_sum=(2*(TFF_adder_sum)-bit_stream_length)/bit_stream_length   #2*(TFF_adder sum)-1
    writer.writerow([in_number,bipolar_out,(out1+out2)/2,adder_sum])


