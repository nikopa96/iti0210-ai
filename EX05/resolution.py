# k6ikide numbriga ruutude peal kutsun välja cnf_sweeper()
# enne peab olema teada kinniste naabrite list


#
# Author: Priit Järv
# Source: http://lambda.ee/wiki/Iti0120lab72cnf
#
def cnf_sweeper(m, neighbors):
    """CNF komponent ühe ruudu kohta
    parameetrid: m - miinide arv
                neighbors - naabrite list"""
    n = len(neighbors)
    cnf = []
    for i in range(2**n):
        binform = "{:0{n}b}".format(i, n=n)
        ones = 0
        clause = []
        for j in range(n):
            if binform[j] == "1":
                ones += 1
                clause.append(-neighbors[j])
            else:
                clause.append(neighbors[j])
        if ones != m:
            cnf.append(tuple(clause))
    return cnf


def resolve(c1, c2):
    new_disjunctions = []

    for literal in c1:
        if -literal in c2:
            temp_c1 = list(c1)
            temp_c2 = list(c2)

            if literal in temp_c1:
                temp_c1.remove(literal)
            if -literal in temp_c1:
                temp_c1.remove(-literal)
            if literal in temp_c2:
                temp_c2.remove(literal)
            if -literal in temp_c2:
                temp_c2.remove(-literal)

            temp_c1.extend(temp_c2)
            new_disjunction = temp_c1

            # removes duplicates
            new_disjunction = list(dict.fromkeys(new_disjunction))

            new_disjunctions.append(tuple(new_disjunction))

    return new_disjunctions


def resolution(kb, alpha):
    # kb - teadmusbaas CNF kujul
    # alpha - literaal, mida tahame kontrollida.

    candidates = kb
    candidates.append((-alpha,))

    processed = []

    is_not_subsume = True

    while candidates:
        next = candidates.pop()

        for p in processed:
            p_set = set(p)
            next_set = set(next)

            if p_set.issubset(next_set):
                is_not_subsume = False
                break
            else:
                is_not_subsume = True

        if is_not_subsume:
            for p in processed:
                resolvents = resolve(next, p)

                for r in resolvents:
                    if r == ():
                        return True
                    candidates.append(r)

            processed.append(next)

    return False


if __name__ == '__main__':
    #   1   1   0
    #   ?   1   ?
    #   1   1   0

    clauses = []

    clauses.extend(cnf_sweeper(1, [4]))
    clauses.extend(cnf_sweeper(1, [4, 6]))
    clauses.extend(cnf_sweeper(0, [6]))
    clauses.extend(cnf_sweeper(1, [4, 6]))
    clauses.extend(cnf_sweeper(1, [4]))
    clauses.extend(cnf_sweeper(1, [4, 6]))
    clauses.extend(cnf_sweeper(0, [6]))

    kb = clauses
    print(resolution(kb, 4))
