from os import _exit
import eel_functions
import ctypes
import eel
import os

path = os.getcwd()

# Funções
# _____________________________________________________________________________________________________________________#


# Função para obter a escala do monitor
def get_scale() -> float:
    try:
        user32 = ctypes.windll.user32
        hdc = user32.GetDC(0)
        gdi32 = ctypes.windll.gdi32

        dpi = gdi32.GetDeviceCaps(hdc, 88)
        scaling_factor = dpi / 96
        user32.ReleaseDC(0, hdc)
        return scaling_factor
    except Exception as e:
        print(f"{e}")
        return 1.0


# Função para obter a posição do centro da tela
def center_screen(window_width: int, window_height: int) -> tuple[int, int]:
    user32 = ctypes.windll.user32
    scaling = get_scale()

    screen_width = int(user32.GetSystemMetrics(0) / scaling)
    screen_height = int(user32.GetSystemMetrics(1) / scaling)

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    return x, y


# Função para fechar o código ao fechar o eel
def on_close_callback(route, sockets):
    _exit(0)


# Função para iniciar o eel
def start_eel():
    # Eel inicia a pasta chamada 'web' e o nome pode ser mudado se necessário
    eel.init('web')
    # Aqui é onde o eel inicia a tela de verdade, as únicas coisas que realmente não podem mudar são:
    #     block=True | mode='chrome' (não recomendo mudar) | close_callback=on_close_callback
    eel.start('app.html', size=(800, 600), block=True, mode='chrome', close_callback=on_close_callback,
              fullscreen=False, position=(350, 100))

# Main
# _____________________________________________________________________________________________________________________#


if __name__ == '__main__':
    if not os.path.exists('Login.txt'):
        with open(f'{path}\\Login.txt', 'w') as file:
            file.write(';')
    start_eel()
