
try: 
    Estatisticas = [] 
      
    while True: 
        Estatisticas.append(int(input()))
        
          
except: 
    print(max(Estatisticas))
    print(min(Estatisticas))
    print(len(Estatisticas))
    print(sum(Estatisticas)/len(Estatisticas))