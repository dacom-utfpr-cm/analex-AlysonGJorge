from automata.fa.Moore import Moore
import sys, os
from myerror import MyError
from alfabeto import alfabeto
from estados import estados
from transicoes import transicoes
from saidas import  alfabetoSaidas, tabelaSaidas

error_handler = MyError('LexerErrors')

global check_cm
global check_key

moore = Moore(
    estados,
    alfabeto,
    alfabetoSaidas,
    transicoes,
    'q0',
    tabelaSaidas
)


def main():
    check_cm = False
    check_key = False
    
    for idx, arg in enumerate(sys.argv):
        aux = arg.split('.')
        if aux[-1] == 'cm':
            check_cm = True
            idx_cm = idx

        if(arg == "-k"):
            check_key = True

    if(len(sys.argv) < 3):
        raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

    if not check_cm:
      raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
    elif not os.path.exists(sys.argv[idx_cm]):
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
    else:
        data = open(sys.argv[idx_cm])
        source_file = data.read()

        if not check_cm:
            print("Def")
            print(moore)
            print("Entrada:")
            print(source_file)
            print("Lista de Tokens:")
        
        print(moore.get_output_from_string(source_file))


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e)
    except (ValueError, TypeError):
        print(ValueError)