from typing import Dict


def count_occurencies(input_value: str) -> Dict[str, int]:

    """
        Esta función cuenta las ocurrencias de cada caracter en el string

        :param input_value: Cadena de texto a contar
        :type input_value: str
    
    """

    result: Dict[str, int] = {}

    for char in input_value:

        result[char] = result.get(char, 0) + 1

    return result

def min_to_palindrome(input_value: str) -> int:

    """
        Esta función evalua el minimo número de caracteres insertados para convertir el string en un palindromo.

        :param input_value: Variable a determinar el minimo para ser palindromo
        :type input_value: str
    
    """

    result: int = 0
    length: int = len( input_value )

    if length > 1:

        is_par: bool = length % 2 == 0

        init_left: int = length // 2
        init_right: int = init_left if is_par else init_left + 1

        left_occurencies: Dict[str, int] = count_occurencies( input_value[0:init_left] )
        right_occurencies: Dict[str, int] = count_occurencies( input_value[init_right:length] )

        for chat in set(list(left_occurencies.keys()) + list(right_occurencies.keys())):

            result: int = result + abs ( left_occurencies.get(chat, 0) - right_occurencies.get(chat, 0) )

    return result

def main():

    N: int = input()
    string: str = input()
    
    print( min_to_palindrome(string) )

if __name__ == "__main__":
    main()
