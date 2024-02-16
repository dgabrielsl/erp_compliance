import os, sys, sqlite3

from datetime import datetime
from plyer import notification

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

from util import *
# from deskpy_excel import *

os.system('cls')

class Main(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.ddbb()
        self.init()
        self.site()
        self.show()

    def ddbb(self):
        con = sqlite3.connect('hub.db')
        cur = con.cursor()
    
    # Users >>> CREATED / LAST_MODIFIED / CREATED_BY / USERNAME / FULLNAME / PASSWORD / DISABLED_USER / REQUESTS_PROCESSING / CREATE_NEW_LOGS / EDIT_ALL_FIELDS / DATA_LOAD_HDS / DATA_LOAD_SSD / MAKE_ASSIGNMENTS / MAKE_REPORTS / ADMIN_USERS / EDIT_DICT
        try:
            cur.execute('CREATE TABLE users(CREATED VARCHAR(12), LAST_MODIFIED VARCHAR(12), CREATED_BY VARCHAR(50), USERNAME VARCHAR(30) UNIQUE, FULLNAME VARCHAR(50), PASSWORD VARCHAR(20), DISABLED_USER BOOLEAN, REQUESTS_PROCESSING BOOLEAN, CREATE_NEW_LOGS BOOLEAN, EDIT_ALL_FIELDS BOOLEAN, DATA_LOAD_HDS BOOLEAN, DATA_LOAD_SSD BOOLEAN, MAKE_ASSIGNMENTS BOOLEAN, MAKE_REPORTS BOOLEAN, ADMIN_USERS BOOLEAN, EDIT_DICT BOOLEAN)')
            time_mark = datetime.now().strftime('%d/%m/%Y %H:%M:%SH')
            rec = f'INSERT INTO users VALUES ("{time_mark}", "{time_mark}", "Developer", "system.gabriel.solano", "Gabriel Solano", "root", 0, 1, 1, 1, 1, 1, 1, 1, 1, 1)'
            cur.execute(rec)
        except Exception as e: pass

    # Sysde >>> ID / EMAIL / PHONE
        try: cur.execute('CREATE TABLE sysde(ID VARCHAR(25) UNIQUE, EMAIL VARCHAR(99), PHONE VARCHAR(25))')
        except Exception as e: pass

    # Indicators >>> DATE_MARK / ASSIGNED / HD_REQUEST / USERNAME / START_TIME / END_TIME / CONSUMED_TIME
        try: cur.execute('CREATE TABLE indicators(DATE_MARK VARCHAR(12), ASSIGNED VARCHAR(12), HD_REQUEST VARCHAR(15), USERNAME VARCHAR(50), START_TIME VARCHAR(15), END_TIME VARCHAR(15), CONSUMED_TIME VARCHAR(3))')
        except Exception as e: pass

    # Core >>> CREATED / TAG_NAME / SYSTEM_ASSIGNED_TO / SYSTEM_STATUS / HELPDESK / ID / DOCUMENT / CODE / CLASS_CASE / STATUS / PRODUCT / INCOME_SOURCE / WARNING_AMOUNT / CUSTOMER_PROFILE / NOTIFICATION_TYPE / CONTACT_TYPE / CUSTOMER_ANSWER / AUTHOR / ASSIGNED_TO / RESULT / UPDATED / DEADLINE
        try: cur.execute('CREATE TABLE core(CREATED VARCHAR(12), TAG_NAME VARCHAR(150), SYSTEM_ASSIGNED_TO VARCHAR(30), SYSTEM_STATUS VARCHAR(20), HELPDESK VARCHAR(15) UNIQUE, ID VARCHAR(30), DOCUMENT VARCHAR(20), CODE VARCHAR(20), CLASS_CASE VARCHAR(150), STATUS VARCHAR(30), PRODUCT VARCHAR(20), INCOME_SOURCE VARCHAR(100), WARNING_AMOUNT VARCHAR(50), CUSTOMER_PROFILE VARCHAR(200), NOTIFICATION_TYPE VARCHAR(100), CONTACT_TYPE VARCHAR(150), CUSTOMER_ANSWER VARCHAR(150), AUTHOR VARCHAR(30), ASSIGNED_TO VARCHAR(30), RESULT VARCHAR(300), UPDATED VARCHAR(15), DEADLINE VARCHAR(15))')
        except Exception as e: pass

    # Trace-log >>> HELPDESK / TIME_MARK / OPERATIVE / DESCRIPTION
        try: cur.execute('CREATE TABLE tracelog(HELPDESK VARCHAR(12), TIME_MARK VARCHAR(12), OPERATIVE VARCHAR(99), DESCRIPTION VARCHAR(3000))')
        except Exception as e: pass

        con.commit()
        con.close()

    def init(self):
        self.setWindowIcon(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)))
        self.setWindowTitle('DeskPyL - ERP Compliance Operative Control')
        self.setMinimumWidth(1000)
        self.setMinimumHeight(500)
        # self.setWindowFlags(Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowMinimizeButtonHint)

        menubar = self.menuBar()
        menubar.setObjectName('menu-bar')

    # (1) File.
        opt_menu_1 = menubar.addMenu('&Archivo')
        opt_menu_1.setObjectName('opt_menu_1')
        opt_menu_1.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_1_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Inicio', self)
        self.action_1_1.setShortcut('F2')
        self.action_1_1.setStatusTip('Ir a la página de inicio.')
        self.action_1_1.triggered.connect(self.navigation)
        self.action_1_1.setDisabled(True)
        opt_menu_1.addAction(self.action_1_1)

        self.action_1_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Cerrar sesión', self)
        self.action_1_2.setShortcut('F11')
        self.action_1_2.setStatusTip('Cierra la sesión actual, debe ingresar las credenciales para volver a iniciar sesión.')
        self.action_1_2.triggered.connect(self.logout)
        self.action_1_2.setDisabled(True)
        opt_menu_1.addAction(self.action_1_2)

        self.action_1_3 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Salir', self)
        self.action_1_3.setShortcut('F12')
        self.action_1_3.setStatusTip('Cierra la aplicación.')
        self.action_1_3.triggered.connect(lambda:print(self.sender().text()))
        opt_menu_1.addAction(self.action_1_3)

    # (2) Requests.
        opt_menu_2 = menubar.addMenu('&Gestiones')
        opt_menu_2.setObjectName('opt_menu_2')
        opt_menu_2.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_2_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Mis solicitudes', self)
        self.action_2_1.setShortcut('F5')
        self.action_2_1.setStatusTip('Ver mi bandeja de gestiones asignadas activas (pendientes de procesar).')
        self.action_2_1.triggered.connect(self.navigation)
        self.action_2_1.setDisabled(True)
        opt_menu_2.addAction(self.action_2_1)

        self.action_2_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Registrar solicitud', self)
        self.action_2_2.setShortcut('F6')
        self.action_2_2.setStatusTip('Ingresar manualmente una nueva gestión.')
        self.action_2_2.triggered.connect(self.navigation)
        self.action_2_2.setDisabled(True)
        opt_menu_2.addAction(self.action_2_2)

    # (3) Settings.
        opt_menu_3 = menubar.addMenu('&Configuración')
        opt_menu_3.setObjectName('opt_menu_3')
        opt_menu_3.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_3_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Administrar usuarios', self)
        self.action_3_1.setShortcut('Ctrl+U')
        self.action_3_1.setStatusTip('Crear, modificar, eliminar y configurar permisos de usuarios.')
        self.action_3_1.triggered.connect(self.navigation)
        self.action_3_1.setDisabled(True)
        opt_menu_3.addAction(self.action_3_1)

        self.action_3_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Configurar diccionario', self)
        self.action_3_2.setShortcut('Ctrl+D')
        self.action_3_2.setStatusTip('Configurar las reglas del diccionario.')
        self.action_3_2.triggered.connect(self.navigation)
        self.action_3_2.setDisabled(True)
        opt_menu_3.addAction(self.action_3_2)

    # (4) Data analysis.
        opt_menu_4 = menubar.addMenu('&Datos')
        opt_menu_4.setObjectName('opt_menu_4')
        opt_menu_4.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_4_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Cargar reportes', self)
        self.action_4_1.setShortcut('Shift+F5')
        self.action_4_1.setStatusTip('Cargar reportes nuevos de Excel.')
        self.action_4_1.triggered.connect(self.navigation)
        self.action_4_1.setDisabled(True)
        opt_menu_4.addAction(self.action_4_1)

        self.action_4_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Generar reportes', self)
        self.action_4_2.setShortcut('Shift+F6')
        self.action_4_2.setStatusTip('Descargar reportes de gestiones.')
        self.action_4_2.triggered.connect(self.navigation)
        self.action_4_2.setDisabled(True)
        opt_menu_4.addAction(self.action_4_2)

        self.action_4_3 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Métricas', self)
        self.action_4_3.setShortcut('Shift+F7')
        self.action_4_3.setStatusTip('Números e indicadores operativos.')
        self.action_4_3.triggered.connect(self.navigation)
        self.action_4_3.setDisabled(True)
        opt_menu_4.addAction(self.action_4_3)

    # (5) Others.
        opt_menu_5 = menubar.addMenu('&Otros')
        opt_menu_5.setObjectName('opt_menu_5')
        opt_menu_5.setCursor(Qt.CursorShape.PointingHandCursor)
        opt_menu_5.setDisabled(True)

    # (6) Support.
        opt_menu_6 = menubar.addMenu('&Ayuda')
        opt_menu_6.setObjectName('opt_menu_6')
        opt_menu_6.setCursor(Qt.CursorShape.PointingHandCursor)

        self.action_6_1 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Ayuda', self)
        self.action_6_1.setShortcut('F1')
        self.action_6_1.setStatusTip('Ver el manual de uso.')
        self.action_6_1.triggered.connect(self.navigation)
        opt_menu_6.addAction(self.action_6_1)

        self.action_6_2 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Documentación', self)
        self.action_6_2.setShortcut('Ctrl+D')
        self.action_6_2.setStatusTip('.')
        self.action_6_2.triggered.connect(self.navigation)
        opt_menu_6.addAction(self.action_6_2)

        self.action_6_3 = QAction(QIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)), '&Acerca De', self)
        self.action_6_3.setShortcut('Ctrl+A')
        self.action_6_3.setStatusTip('.')
        self.action_6_3.triggered.connect(self.navigation)
        opt_menu_6.addAction(self.action_6_3)

        self.statusbar = self.statusBar()
        self.statusbar.setObjectName('status-bar')

    def site(self):
        central_widget = QWidget()
        _central_widget = QVBoxLayout()
        _central_widget.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        central_widget.setLayout(_central_widget)
        self.setCentralWidget(central_widget)

        _header = QVBoxLayout()
        _header.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        header = QWidget()
        header.setLayout(_header)
        header.setObjectName('header')
        _central_widget.addWidget(header)

        self.deskpyl_link = QPushButton('DeskPyL ↗')
        self.deskpyl_link.setObjectName('deskpyl-link')
        self.deskpyl_link.setCursor(Qt.CursorShape.PointingHandCursor)
        self.deskpyl_link.setStatusTip('Ir al sitio web.')
        self.deskpyl_link.clicked.connect(lambda:print(self.sender().text()))

        product_name = QLabel('ERP Control Operativa Cumplimiento')
        product_name.setObjectName('product-name')
        product_name.setStatusTip('Enterprise Resource Planning')

        self.about_user = QLabel('↓↑ desconectado')
        self.about_user.setObjectName('about-user')
        self.about_user.setStatusTip('Estado de la sesión.')

        top_bar = QHBoxLayout()
        top_bar.addWidget(self.deskpyl_link)
        top_bar.addWidget(product_name)
        top_bar.addWidget(self.about_user)
        _header.addLayout(top_bar)

        _site_info = QHBoxLayout()
        site_info = QWidget()
        site_info.setLayout(_site_info)
        site_info.setObjectName('site-info')
        _central_widget.addWidget(site_info)

        self.user_location = QLabel('INGRESAR CREDENCIALES')
        self.user_location.setObjectName('user-location')
        self.user_location.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        _site_info.addWidget(self.user_location)

        self._body = QStackedLayout()
        self._body.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        body = QWidget()
        body.setLayout(self._body)
        _central_widget.addWidget(body)

        # UI: Login page.
        self.ui_login = QWidget()

        self._ui_login = QVBoxLayout()
        self._ui_login.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_login.setLayout(self._ui_login)

        self._body.addWidget(self.ui_login)

        multimoney = QLabel('Financiera Multimoney')
        multimoney.setObjectName('multimoney')
        multimoney.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._ui_login.addWidget(multimoney)

        self.credential_username = QLineEdit('')
        self.credential_username.setObjectName('credential-username')
        self.credential_username.setPlaceholderText('username')
        self.credential_username.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.credential_username.setFixedWidth(400)
        self._ui_login.addWidget(self.credential_username)

        self.credential_password = QLineEdit('')
        self.credential_password.setObjectName('credential-password')
        self.credential_password.setPlaceholderText('password')
        self.credential_password.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.credential_password.setFixedWidth(400)
        self.credential_password.setEchoMode(QLineEdit.EchoMode.Password)
        self._ui_login.addWidget(self.credential_password)

        self.onoff_echo = QCheckBox('Mostrar contraseña')
        self.onoff_echo.setObjectName('onoff-echo')
        self.onoff_echo.setCursor(Qt.CursorShape.PointingHandCursor)
        self.onoff_echo.clicked.connect(self.echomode)
        self._ui_login.addWidget(self.onoff_echo)

        self.check_credentials = QPushButton('Ingresar')
        self.check_credentials.setFixedWidth(400)
        self.check_credentials.setCursor(Qt.CursorShape.PointingHandCursor)
        self.check_credentials.clicked.connect(self.get_logged)
        self._ui_login.addWidget(self.check_credentials)

        # UI: Logged page.
        self.ui_logged = QWidget()

        self._ui_logged = QVBoxLayout()
        self._ui_logged.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.ui_logged.setLayout(self._ui_logged)

        self._body.addWidget(self.ui_logged)
        self._ui_logged.addWidget(QLabel('Sesión iniciada correctamente'))














        self._body.setCurrentIndex(0)

        self.credential_username.setText('system.gabriel.solano')
        self.credential_password.setText('root')
        # self.check_credentials.click()

    def echomode(self):
        if self.onoff_echo.isChecked(): self.credential_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else: self.credential_password.setEchoMode(QLineEdit.EchoMode.Password)

    def get_logged(self):
        cred_username = self.credential_username.text()
        cred_password = self.credential_password.text()

        if cred_username.strip() != '' and cred_password.strip() != '':
            con = sqlite3.connect('hub.db')
            cur = con.cursor()
            cur.execute('SELECT disabled_user, username, password FROM users WHERE username = ?', (cred_username,))
            res = cur.fetchone()

            if res == None: QMessageBox.warning(self, 'DeskPyL', '\nEl nombre de usuario no existe.\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                if res[2] == cred_password:
                    if res[0] == 0:
                        cur.execute('SELECT username, requests_processing, create_new_logs, edit_all_fields, data_load_hds, data_load_ssd, make_assignments, make_reports, admin_users, edit_dict FROM users WHERE username = ?', (cred_username,))
                        self.connected_user = cur.fetchone()

                        self._body.setCurrentIndex(1)
                        self.user_location.setText('INICIO')
                        self.about_user.setText(f'↑↓ {self.connected_user[0]}')
                        self.about_user.setStyleSheet('color: #0f0;')
                        self.credential_username.setText('')
                        self.credential_password.setText('')
                        self.action_1_1.setDisabled(False)
                        self.action_1_2.setDisabled(False)

                        print(self.connected_user)





                    else: QMessageBox.warning(self, 'DeskPyL', '\nEste usuario se encuentra deshabilidado, por favor contacte un administrador.\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                else: QMessageBox.warning(self, 'DeskPyL', '\nLa contraseña es incorrecta.\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

            con.close()
        else: QMessageBox.warning(self, 'DeskPyL', '\nHay campos sin completar\t\t\n', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

    def logout(self):
        self._body.setCurrentIndex(0)
        self.user_location.setText('INGRESAR CREDENCIALES')
        self.about_user.setText(f'↓↑ desconectado')
        self.about_user.setStyleSheet('color: #f33;')

    def navigation(self):
        _sender = self.sender().text()
        print(_sender)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
            QWidget{
                background: #111;
                color: #fff;
            }
            QPushButton{
                padding: 10px;
                background: #003600;
                color: #0f0;
                font-size: 15px;
                border: 1px solid #0f0;
                border-radius: 5px;
            }
            QPushButton:hover{
                background: #050;
                color: #fff;
                border: 1px solid #fff;
            }
            QPushButton:focus{
                background: #003600;
                color: #0f0;
                border: 1px solid #0f0;
            }
            #menu-bar,
            #status-bar{
                padding: 3px;
                background: #021;
                color: #0fa;
                font-size: 13px;
                font-family: Segoe-UI;
            }
            #menu-bar::disabled{
                color: #0a5;
            }
            #menu-bar::item:selected{
                color: #0f0;
                border-bottom: 1px solid #0f0;
            }
            #opt_menu_1, #opt_menu_2, #opt_menu_3, #opt_menu_4, #opt_menu_5, #opt_menu_6{
                color: #0fa;
            }
            #opt_menu_1:item:selected, #opt_menu_2:item:selected, #opt_menu_3:item:selected, #opt_menu_4:item:selected, #opt_menu_5:item:selected, #opt_menu_6:item:selected{
                background: #fff;
                color: #000;
            }
            #opt_menu_1:item:disabled, #opt_menu_2:item:disabled, #opt_menu_3:item:disabled, #opt_menu_4:item:disabled, #opt_menu_5:item:disabled, #opt_menu_6:item:disabled{
                color: #0a5;
            }
            #opt_menu_1:item:disabled:selected, #opt_menu_2:item:disabled:selected, #opt_menu_3:item:disabled:selected, #opt_menu_4:item:disabled:selected, #opt_menu_5:item:disabled:selected, #opt_menu_6:item:disabled:selected{
                background: #111;
            }
            #header{
                background: #222;
                border-radius: 5px;
            }
            #deskpyl-link{
                background: #222;
                color: #ffd600;
                border: none;
            }
            #deskpyl-link:hover{
                color: #ffa600;
            }
            #product-name{
                background: #222;
                font-size: 15px;
            }
            #about-user{
                background: #222;
                color: #f33;
            }
            #site-info{
                background: #333;
                border-radius: 5px;
            }
            #user-location{
                padding: 12px;
                background: #333;
                font-size: 16px;
            }
            #multimoney{
                margin-top: 25px;
                padding: 5px;
                color: #333;
                font-weight: 500;
                letter-spacing: 3px;
                font-size: 25px;
            }
            #credential-username, #credential-password{
                margin: 5px;
                padding: 5px;
                background: #fff;
                color: #000;
                font-size: 14px;
                border-radius: 15px;
            }
            #onoff-echo{
                padding: 15px;
            }
        """)
    win = Main()
    sys.exit(app.exec())