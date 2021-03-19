# ------------------------------------------------------------
# Name: Krish Gandhi
# ID: 1621641
# CMPUT 274, Fall 2020
#
# Weekly Exercise #7: Dr. Moneybags
# ------------------------------------------------------------


def get_input():
    """ Prompts the user to enter the number of applicants,
        and the net worth of each applicant.

    Arguments:
        None

    Return:
        applicants (integer): number of applicants to the club
        networth_list (list of integers): sorted list of the net worth
        of all the applicants (in ascending order)
    """
    applicants = int(input())

    # use list comprehension to obtain the net worth, in millons of
    # dollars, for each applicant
    networth_list = [int(input()) for i in range(applicants)]

    # sort the applicants net worth in ascending order
    networth_list.sort()

    return(applicants, networth_list)


def get_threshold(applicants, networth_list):
    """ Finds the largest threshold number N such that there are at
        least N applicants with at least N million dollars.

    Arguments:
        applicants (integer): number of applicants to the club
        networth_list (list of integers): sorted list of the net worth
        of all the applicants (in ascending order)

    Return:
        threshold (integer): minimum millions of dollars for an applicant
        to join Dr. Moneybag's elite club
    """

    # initialize threshold (default value if zero applicants or list
    # of applicants all have a net worth equal to zero)
    threshold = 0

    for i in range(applicants):
        # iterate through the networth_list in reverse until the net worth
        # of an applicant is equal to or less than the threshold
        # for each net worth that is larger than the threshold,
        # increase the threshold by 1
        if networth_list[-1-i] > threshold:
            threshold += 1
        else:
            break

    return threshold


def main():
    """ Main function that calls get_input() function to get the number of
        applicants and the net worth of each applicant. These two information
        are passed as parameters in the call to get_threshold() function to
        obtain the minimum millions of dollars required for an applicant to
        join Dr. Moneybag's elite club.

        Arguments:
            None

        Return:
            None (prints bigN, the minimum millions of dollars required
            for an applicant to join Dr. Moneybag's elite club)
    """

    applicants, networth_list = get_input()
    bigN = get_threshold(applicants, networth_list)

    print(bigN)


if __name__ == "__main__":
    main()
