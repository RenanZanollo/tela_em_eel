import eel
import os

path = os.getcwd()

# Funções
# _____________________________________________________________________________________________________________________#


# Essa função serve para mudar entre uma tela e outra usando o "ID" da tela como parâmetro.
@eel.expose
def change_screen(screen_id: str) -> None:
    print('Mudando de tela')
    eel.showScreen(screen_id)


# Função para escrever o Login.txt.
@eel.expose
def login_txt_write(username: str, password: str) -> dict:
    if not username or not password:
        return {'Success': False, 'Message': 'Os parâmetros não foram preenchidos corretamente'}
    try:
        with open(f'{path}\\Login.txt', 'w') as file:
            file.write(f'{username};{password}')
        return {'Success': True}
    except Exception as e:
        return {'Success': False, 'Message': f'Algo deu errado ao salvar as credenciais no arquivo. Erro: {e}'}


# Essa função não deve ser usada para receber o "login" do txt. Serve apenas para determinar qual será a tela inicial.
@eel.expose
def login_txt() -> dict:
    try:
        with open(f'{path}\\Login.txt', 'r') as file:
            user, password = file.read().strip().split(';', 1)
            if not user or not password:
                return {'Success': False, 'Message': 'Uma das credênciais está vazia'}
        return {'Success': True, 'Message': 'Credenciais obtidas, redirecionando para a tela principal'}
    except FileNotFoundError:
        return {'Success': False, 'Message': 'O arquivo Login.txt não foi encontrado.'}
    except ValueError:
        return {'Success': False,
                'Message': 'Erro ao processar o conteúdo do arquivo Login.txt. Verifique se o formato está correto.'}
    except IOError:
        return {'Success': False,
                'Message': 'Erro ao ler o arquivo Login.txt. Verifique se você tem permissão para acessá-lo.'}
    except Exception as e:
        return {'Success': False, 'Message': f'Ocorreu um erro inesperado: {str(e)}'}
