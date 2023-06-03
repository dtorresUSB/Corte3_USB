import sys


from PyQt5.QtWidgets import QApplication


from view.main import RegisterView


def main():
    try:
        app = QApplication(sys.argv)
        _ = RegisterView()
        sys.exit(app.exec_())

    except ZeroDivisionError:
        print("No se puede dividir por cero")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
