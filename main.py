from controller.controller_main import ControllerMain

if __name__ == "__main__":
    try:
        ControllerMain().menu_opcoes()
    except Exception as e:
        print(e)
