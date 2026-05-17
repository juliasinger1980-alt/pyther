

if __name__ == "__main__":
    n, c, k = map(int, input().split())
    monsters = list(map(int, (input().split())))


    for i in range(len(monsters)):
        print(i)
        if monsters[i] < c:
            while monsters[i] < c:
                if k > 0:
                    monsters[i] += 1
                    k -= 1
                else:
                    break
            c += monsters[i]
            #monsters.pop(i)
        
    
    print("maximale staerke: ", c)
        
        
