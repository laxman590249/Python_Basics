

def main():
    test_cases = input("")

    for j in range(0, int(test_cases)):
        n_memebrs = input("")
        team_1 = input("")
        team_2 = input("")

        list_team_1 = team_1.strip().split(" ")
        list_team_2 = team_2.strip().split(" ")

        list_team_1 = list(map(int, list_team_1))
        list_team_2 = list(map(int, list_team_2))

        list_team_1.sort()
        list_team_2.sort(reverse=True)
        win_count = 0
        list_result = []
        list_result_back = []

        max_count = 0

        for i in range(0, int(n_memebrs)):
            if list_team_1[len(list_team_1)-(1+max_count)] <= list_team_2[i]:
                list_result.append(list_team_2[i])
            else:
                max_count += 1
                list_result_back.append(list_team_2[i])

        list_result_back.reverse()


        list_result.extend(list_result_back)
        for i in range(0, int(n_memebrs)):
            if list_team_1[i] > list_result[i]:
                win_count += 1


        print(win_count)

main()
