def typeahead(usernames, queries):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    root = {}
    for name in usernames:
        i = 0
        d = root
        while i < len(name):
            tmp = d.get(name[i].lower())
            if tmp == None:
                d[name[i].lower()] = name
                break;
            else:
                if isinstance(tmp, str):
                    old = tmp
                    d[name[i].lower()] = {}
                    d = d[name[i].lower()]
                    i += 1 
                    d[old[i].lower()] = old
                else:
                    d = tmp
                    i += 1
    for query in queries:
        i = 0
        d = root
        while i < len(query):
            tmp = d.get(query[i].lower())
            if tmp == None:
                print -1
                break;
            else:
                if isinstance(tmp, str):
                    print tmp 
                else:
                    d = tmp
                    i += 1
                    

if __name__ == '__main__':
    typeahead(["Mitzi", "SandeeRudolph", "TenaLynetta", "IsabelleEllen", "BridgetDale"], ["IEab", "S", "TenALYne"])