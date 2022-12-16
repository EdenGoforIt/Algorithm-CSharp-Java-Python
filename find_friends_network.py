def find_friend_network() -> None:

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


print(find_friend_network())
