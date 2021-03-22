from database_module import CPU_DATA, CPU, CPU_NAMES, GPU_DATA, GPU, GPU_NAMES

#SE_REC = 0
#SE_MIN = 0
#ED_REC = 0
#ED_MIN = 0

#GAME = [
#['Grand Theft Auto V', [CPU[0][0], GPU[0][0], 8], [CPU[1][0], GPU[1][0], 6], 200],  # [(Ryzen 5 3600, Gtx 1070, 8gb), (I7 7700k, Radeon Rx 480, 6)]
#['Space Engineers', SE_REC, SE_MIN, 10],
#['Elite Dangerous', ED_REC, ED_MIN, 35]
#]

# Name, Reccommended Reqs, Min Reqs, Storage

cpu_input1 = input("Enter your CPU: ")
if cpu_input1.upper() in CPU_NAMES.keys():
    cpu_1 = CPU_NAMES.get(cpu_input1.upper())

cpu_input2 = input("Enter your CPU: ")
if cpu_input2.upper() in CPU_NAMES.keys():
    cpu_2 = CPU_NAMES.get(cpu_input2.upper())

    print("\nCPU #1 has a performance score of: " + cpu_1[0] + "\n\nCPU #1 has a price of £" + cpu_1[1] + ".\n")

    print("CPU #2 has a performance score of: " + cpu_2[0] + "\n\nCPU #2 has a price of £" + cpu_2[1] + ".\n")

#if cpu_input.upper() in CPU_NAMES.keys():
    #if CPU_NAMES.get(cpu_input.upper()) in CPU[0]:
        #print("True")
#gpu_input = input("Enter your GPU: ")
#ram_input = int(input("Please enter your amount of RAM: "))
#sto_input = int(input("Please enter your amount of storage capacity: "))