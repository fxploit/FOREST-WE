import sql


def report(dbname, chain_numbers):
    for chain_number in chain_numbers:
        sql.select_chain_report(dbname, chain_number)