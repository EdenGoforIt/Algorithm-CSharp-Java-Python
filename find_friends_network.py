def find_friend_network(name: str) -> None:

    fr_info = {
        'Summer': ['John', 'Justin', 'Mike'],
        'John': ['Summer', 'Justin'],
        'Justin': ['John', 'Summer', 'Mike', 'May'],
        'Mike': ['Summer', 'Justin'],
        'May': ['Justin', 'Kim'],
        'Kim': ['May'],
        'Tom': ['Jerry'],
        'Jerry': ['Tom']
    }
    qu = []
    done = set()

    qu.append((name, 0))
    done.add(name)

    while qu:
        (p, d) = qu.pop()
        print(p, d)
        for x in fr_info[p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)

    print(done)


find_friend_network('Summer')
