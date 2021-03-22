CPU_DATA = [  # [Performance, Price]
['90', '200', 'r5'], 
['85', '349', 'i7'], 
['75', '1499', 'tr']
]

CPU = {
'R5-3600': CPU_DATA[0],
'I7-7700K': CPU_DATA[1],
'TR-2990WX': CPU_DATA[2]
}

CPU_NAMES = {
"RYZEN 5 3600": CPU['R5-3600'],
"INTEL I7 7700K": CPU['I7-7700K'],
"THREADRIPPER 2990WX": CPU['TR-2990WX']
}

GPU_DATA = [  # [Performance, Price]
['70', '379', 'gx'],
['50', '239', 'rx'],
['75', '349', 'rt']
]

GPU = {
'GTX-1070': GPU_DATA[0],
'RX-480': GPU_DATA[1],
'RTX-2060': GPU_DATA[2]
}

GPU_NAMES = {
"GEFORCE GTX 1070": GPU['GTX-1070'], 
"RADEON RX 480": GPU['RX-480'], 
"GEFORCE RTX 2060": GPU['RTX-2060']
}

GAME_DATA = [ # CPU_Min, GPU_Min, RAM_Min, CPU_Rec, GPU_Rec, RAM_Rec, Storage
[CPU['R5-3600'], GPU['RX-480'], 6, CPU['I7-7700K'], GPU['GTX-1070'], 8, 200]
] 

GAME = {
'GTV': GAME_DATA[0]
}

GAME_NAMES = {
"GRAND THEFT AUTO V": GAME['GTV']
}
