def four_d_five_s(num, location=0):

    def main(num_coped):
        if int(str(num_coped).split(".")[1][0]) in [1, 2, 3, 4]:
            return int(num_coped)
        if int(str(num_coped).split(".")[1][0]) in [5, 6, 7, 8, 9]:
            return int(num_coped) + 1

    if location == 0:
        return main(num)

    if location != 0:
        return main(num*location) / location

