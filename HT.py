def final_answer(f_input_name,f_output_name):
  import time
  start = time.time()
  with open(f_input_name) as fr:
    import xml.etree.ElementTree as et
    tree = et.ElementTree()
    tree.parse(fr)
    root = tree.getroot()
    nets_number = len(root.findall('net'))
    table = [[float('inf') for j in range(nets_number)]
         for i in range(nets_number)]
    for i in range(nets_number):
      table[i][i] = 0
    for resistor in root.findall('resistor'):
      i = int(resistor.attrib['net_from'])-1
      j = int(resistor.attrib['net_to'])-1
      try:
        table[i][j] = 1/(1/table[i][j] + 1/
                 float(resistor.attrib['resistance']))
      except ZeroDivisionError:
        if (float(resistor.attrib['resistance']) == 0) or (table[i][j]
                                   == 0):
          table[i][j] = 0
        else:
          table[i][j] = float('inf')
      table[j][i] = table[i][j]  
    for capactor in root.findall('capactor'):
      i = int(capactor.attrib['net_from'])-1
      j = int(capactor.attrib['net_to'])-1
      try:
        table[i][j] = 1/(1/table[i][j] + 1/
                 float(capactor.attrib['resistance']))
      except ZeroDivisionError:
        if (float(capactor.attrib['resistance']) == 0) or (table[i][j]
                                   == 0):
          table[i][j] = 0
        else:
          table[i][j] = float('inf')
      table[j][i] = table[i][j]
    for diode in root.findall('diode'):
      i = int(diode.attrib['net_from'])-1
      j = int(diode.attrib['net_to'])-1
      try:
        table[i][j] = 1/(1/table[i][j] + 1/
                 float(diode.attrib['resistance']))
      except ZeroDivisionError:
        if (float(diode.attrib['resistance']) == 0) or (table[i][j]
                                   == 0):
          table[i][j] = 0
        else:
          table[i][j] = float('inf')
      try:
        table[j][i] = 1/(1/table[j][i] + 1/
                 float(diode.attrib['reverse_resistance']))
      except ZeroDivisionError:
        if ((float(diode.attrib['reverse_resistance']) ==
           0) or (table[j][i] == 0)):
          table[j][i] = 0
        else:
          table[j][i] = float('inf')
    for k in range(nets_number):
      for i in range(nets_number):
        for j in range(nets_number):
          try:
            table[i][j] = 1/(1/table[i][j] + 1/(table[i][k]+table[k][j]))
          except ZeroDivisionError:
            if ((table[i][j] == 0) or ((table[i][k]+table[k][j]) == 0)):
              table[i][j] = 0
            else:
              table[i][j] = float('inf')
  with open(f_output_name, "w") as fw:
    for i in range(nets_number):
      for j in range(nets_number):
        print("%.6f" %(table[i][j]),end = ',',file = fw)
      print('\n',end = '',file = fw)
  finish = time.time()
  print((finish-start)*1000)
  return
  

