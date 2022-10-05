from functools import reduce
import itertools


def generate_combinations(width, max_caract, lista):
    combinations = []

    if width <= max_caract:
        combinations = list(itertools.combinations(lista, r=width))     
        combinations.extend(generate_combinations(width + 1, max_caract, lista))
    return combinations


def transform_combinations_into_string(combinations):
    """
    Given a lista of combinations:
        [(2,), (7,), (11,), (2, 7), (7, 11), (11, 2)]
    Returns a list of eval strings doing xor to all of them:
        ['0^2', '0^7', '0^11', '0^2^11', '0^7^11', '0^11^2']
    """
    
    return map(
        lambda combination: reduce(
            lambda prev, curr: f"{prev}^{str(curr)}", 
            combination, 
            "0"
        ), 
        combinations
    )


def get_max_xor(numero_de_items, items):
    combinations = generate_combinations(1, numero_de_items, items)
    eval_equations = transform_combinations_into_string(combinations)
    return max(map(lambda equation: eval(equation), eval_equations))


if __name__ == "__main__":
    entries = [
        [[2, [5, 3]], 6],
        [[3, [2, 7, 11]], 14],
        [[3, [18, 7, 26]], 29],
        [[4, [33554438, 21, 22, 9]], 33554458],
        [[10, [9168, 21776, 22487, 4160, 21042, 18226, 30005, 24994, 24997, 352]], 30709]
    ]

    for entry in entries:
        params, result = entry
        received_result = get_max_xor(*params)
        
        assert received_result == result
    