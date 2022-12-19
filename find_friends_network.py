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

    qu.append(name)
    done.add(name)

    while qu:
        p = qu.pop()
        for x in fr_info[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

    print(done)

print(find_friend_network('Summer'))
