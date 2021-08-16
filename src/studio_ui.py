# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studio_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1410, 937)
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"QWidget {\n"
"	color: rgb(137, 137, 206);\n"
"	background-color:rgb(16, 24, 24);\n"
"}\n"
"\n"
"QFileDialog {\n"
"	color: rgb(137, 137, 206);\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 4px;\n"
"	padding-left: 4px;\n"
"	padding-right: 4px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:rgb(16, 24, 24);\n"
"	border: 2px solid rgb(137, 137, 206);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(80, 80, 126);\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(18, 30, 30);\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"	border: 2px solid rgb(25, 40, 40);\n"
"	border-radius: 4px;\n"
"\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 8px;\n"
"	padding-right: 4px;\n"
"	\n"
"	background-color: rgb(16, 24, 24);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"}\n"
"\n"
"QLineEdit:checked {\n"
"	color"
                        ": rgb(25, 40, 40);\n"
"	background-color: rgb(67, 67, 100);\n"
"}\n"
"\n"
"QLineEdit:checked:hover {\n"
"	border: 2px solid rgb(25, 40, 40);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#topBar .QLabel {\n"
"	font-size: 12pt;\n"
"}\n"
"\n"
"#ranges_accent_bar .QPushButton {\n"
"	padding: 0 0 0 0;\n"
"}\n"
"\n"
"#pair_lens_labels .QLabel {\n"
"	font-size: 12pt;\n"
"}")
        self.gridLayout = QGridLayout(self.stylesheet)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nav = QWidget(self.stylesheet)
        self.nav.setObjectName(u"nav")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav.sizePolicy().hasHeightForWidth())
        self.nav.setSizePolicy(sizePolicy)
        self.nav.setMinimumSize(QSize(150, 0))
        self.verticalLayout = QVBoxLayout(self.nav)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.compose_nav_btn = QPushButton(self.nav)
        self.compose_nav_btn.setObjectName(u"compose_nav_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.compose_nav_btn.sizePolicy().hasHeightForWidth())
        self.compose_nav_btn.setSizePolicy(sizePolicy1)
        self.compose_nav_btn.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(16)
        self.compose_nav_btn.setFont(font)

        self.verticalLayout.addWidget(self.compose_nav_btn)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.structure_nav_btn = QPushButton(self.nav)
        self.structure_nav_btn.setObjectName(u"structure_nav_btn")
        sizePolicy1.setHeightForWidth(self.structure_nav_btn.sizePolicy().hasHeightForWidth())
        self.structure_nav_btn.setSizePolicy(sizePolicy1)
        self.structure_nav_btn.setMinimumSize(QSize(0, 40))
        self.structure_nav_btn.setFont(font)

        self.verticalLayout.addWidget(self.structure_nav_btn)

        self.style_nav_btn = QPushButton(self.nav)
        self.style_nav_btn.setObjectName(u"style_nav_btn")
        sizePolicy1.setHeightForWidth(self.style_nav_btn.sizePolicy().hasHeightForWidth())
        self.style_nav_btn.setSizePolicy(sizePolicy1)
        self.style_nav_btn.setMinimumSize(QSize(0, 40))
        self.style_nav_btn.setFont(font)

        self.verticalLayout.addWidget(self.style_nav_btn)

        self.styleNav = QFrame(self.nav)
        self.styleNav.setObjectName(u"styleNav")
        self.styleNav.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.styleNav.sizePolicy().hasHeightForWidth())
        self.styleNav.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(12)
        self.styleNav.setFont(font1)
        self.styleNav.setFrameShape(QFrame.StyledPanel)
        self.styleNav.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.styleNav)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.rhythm_nav_btn = QPushButton(self.styleNav)
        self.rhythm_nav_btn.setObjectName(u"rhythm_nav_btn")
        sizePolicy1.setHeightForWidth(self.rhythm_nav_btn.sizePolicy().hasHeightForWidth())
        self.rhythm_nav_btn.setSizePolicy(sizePolicy1)
        self.rhythm_nav_btn.setMinimumSize(QSize(0, 30))
        self.rhythm_nav_btn.setFont(font1)

        self.verticalLayout_2.addWidget(self.rhythm_nav_btn)

        self.pitch_nav_btn = QPushButton(self.styleNav)
        self.pitch_nav_btn.setObjectName(u"pitch_nav_btn")
        sizePolicy1.setHeightForWidth(self.pitch_nav_btn.sizePolicy().hasHeightForWidth())
        self.pitch_nav_btn.setSizePolicy(sizePolicy1)
        self.pitch_nav_btn.setMinimumSize(QSize(0, 30))
        self.pitch_nav_btn.setFont(font1)

        self.verticalLayout_2.addWidget(self.pitch_nav_btn)

        self.aharmony_nav_btn = QPushButton(self.styleNav)
        self.aharmony_nav_btn.setObjectName(u"aharmony_nav_btn")
        sizePolicy1.setHeightForWidth(self.aharmony_nav_btn.sizePolicy().hasHeightForWidth())
        self.aharmony_nav_btn.setSizePolicy(sizePolicy1)
        self.aharmony_nav_btn.setMinimumSize(QSize(0, 30))
        self.aharmony_nav_btn.setFont(font1)

        self.verticalLayout_2.addWidget(self.aharmony_nav_btn)

        self.synopations_nav_btn = QPushButton(self.styleNav)
        self.synopations_nav_btn.setObjectName(u"synopations_nav_btn")
        sizePolicy1.setHeightForWidth(self.synopations_nav_btn.sizePolicy().hasHeightForWidth())
        self.synopations_nav_btn.setSizePolicy(sizePolicy1)
        self.synopations_nav_btn.setMinimumSize(QSize(0, 30))
        self.synopations_nav_btn.setFont(font1)

        self.verticalLayout_2.addWidget(self.synopations_nav_btn)


        self.verticalLayout.addWidget(self.styleNav)

        self.widget = QWidget(self.nav)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.verticalLayout.addWidget(self.widget)

        self.nav_v_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.nav_v_spacer)

        self.dialog_anchor = QWidget(self.nav)
        self.dialog_anchor.setObjectName(u"dialog_anchor")
        self.dialog_anchor.setEnabled(True)

        self.verticalLayout.addWidget(self.dialog_anchor)


        self.gridLayout.addWidget(self.nav, 1, 0, 1, 1)

        self.content = QFrame(self.stylesheet)
        self.content.setObjectName(u"content")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(8)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy3)
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_stack = QStackedWidget(self.content)
        self.content_stack.setObjectName(u"content_stack")
        self.content_stack.setStyleSheet(u"")
        self.style_page = QWidget()
        self.style_page.setObjectName(u"style_page")
        self.verticalLayout_4 = QVBoxLayout(self.style_page)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 0, 4, 4)
        self.style_stack = QStackedWidget(self.style_page)
        self.style_stack.setObjectName(u"style_stack")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.style_stack.sizePolicy().hasHeightForWidth())
        self.style_stack.setSizePolicy(sizePolicy4)
        self.rhythm_page = QWidget()
        self.rhythm_page.setObjectName(u"rhythm_page")
        self.verticalLayout_13 = QVBoxLayout(self.rhythm_page)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(4, 4, 4, 4)
        self.timing_arch_widget = QWidget(self.rhythm_page)
        self.timing_arch_widget.setObjectName(u"timing_arch_widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.timing_arch_widget.sizePolicy().hasHeightForWidth())
        self.timing_arch_widget.setSizePolicy(sizePolicy5)
        self.timing_arch_widget.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout = QHBoxLayout(self.timing_arch_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.timing_spacewidget = QWidget(self.timing_arch_widget)
        self.timing_spacewidget.setObjectName(u"timing_spacewidget")
        sizePolicy5.setHeightForWidth(self.timing_spacewidget.sizePolicy().hasHeightForWidth())
        self.timing_spacewidget.setSizePolicy(sizePolicy5)
        self.timing_spacewidget.setMaximumSize(QSize(16777215, 160))
        self.horizontalLayout_2 = QHBoxLayout(self.timing_spacewidget)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bpm_bar = QWidget(self.timing_spacewidget)
        self.bpm_bar.setObjectName(u"bpm_bar")
        self.horizontalLayout_31 = QHBoxLayout(self.bpm_bar)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.bpm_label = QLabel(self.bpm_bar)
        self.bpm_label.setObjectName(u"bpm_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bpm_label.sizePolicy().hasHeightForWidth())
        self.bpm_label.setSizePolicy(sizePolicy6)
        self.bpm_label.setMinimumSize(QSize(150, 40))
        self.bpm_label.setMaximumSize(QSize(150, 40))
        font2 = QFont()
        font2.setPointSize(11)
        self.bpm_label.setFont(font2)
        self.bpm_label.setStyleSheet(u"QLabel {\n"
"	padding-left: 6px;\n"
"}")
        self.bpm_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.bpm_label.setMargin(6)

        self.horizontalLayout_31.addWidget(self.bpm_label)

        self.bpm_entry = QLineEdit(self.bpm_bar)
        self.bpm_entry.setObjectName(u"bpm_entry")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.bpm_entry.sizePolicy().hasHeightForWidth())
        self.bpm_entry.setSizePolicy(sizePolicy7)
        self.bpm_entry.setMinimumSize(QSize(0, 26))
        self.bpm_entry.setMaximumSize(QSize(40, 16777215))
        self.bpm_entry.setFont(font1)
        self.bpm_entry.setStyleSheet(u"")
        self.bpm_entry.setMaxLength(3)
        self.bpm_entry.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.bpm_entry)

        self.timesig_widget = QWidget(self.bpm_bar)
        self.timesig_widget.setObjectName(u"timesig_widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.timesig_widget.sizePolicy().hasHeightForWidth())
        self.timesig_widget.setSizePolicy(sizePolicy8)
        self.timesig_widget.setMaximumSize(QSize(300, 114))
        self.timesig_bar = QHBoxLayout(self.timesig_widget)
        self.timesig_bar.setSpacing(2)
        self.timesig_bar.setObjectName(u"timesig_bar")
        self.timesig_bar.setContentsMargins(0, 0, 0, 0)
        self.timesig_label = QLabel(self.timesig_widget)
        self.timesig_label.setObjectName(u"timesig_label")
        sizePolicy6.setHeightForWidth(self.timesig_label.sizePolicy().hasHeightForWidth())
        self.timesig_label.setSizePolicy(sizePolicy6)
        self.timesig_label.setMinimumSize(QSize(150, 40))
        self.timesig_label.setMaximumSize(QSize(150, 40))
        self.timesig_label.setFont(font2)
        self.timesig_label.setStyleSheet(u"QLabel {\n"
"	padding-left: 6px;\n"
"}")
        self.timesig_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.timesig_label.setMargin(6)

        self.timesig_bar.addWidget(self.timesig_label)

        self.timesig_box = QWidget(self.timesig_widget)
        self.timesig_box.setObjectName(u"timesig_box")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.timesig_box.sizePolicy().hasHeightForWidth())
        self.timesig_box.setSizePolicy(sizePolicy9)
        self.verticalLayout_9 = QVBoxLayout(self.timesig_box)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.timesig_num = QLineEdit(self.timesig_box)
        self.timesig_num.setObjectName(u"timesig_num")
        sizePolicy7.setHeightForWidth(self.timesig_num.sizePolicy().hasHeightForWidth())
        self.timesig_num.setSizePolicy(sizePolicy7)
        self.timesig_num.setMinimumSize(QSize(0, 26))
        self.timesig_num.setMaximumSize(QSize(40, 16777215))
        self.timesig_num.setFont(font1)
        self.timesig_num.setStyleSheet(u"")
        self.timesig_num.setMaxLength(2)
        self.timesig_num.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.timesig_num)

        self.timesig_line = QFrame(self.timesig_box)
        self.timesig_line.setObjectName(u"timesig_line")
        sizePolicy6.setHeightForWidth(self.timesig_line.sizePolicy().hasHeightForWidth())
        self.timesig_line.setSizePolicy(sizePolicy6)
        self.timesig_line.setMinimumSize(QSize(40, 10))
        self.timesig_line.setMaximumSize(QSize(40, 10))
        font3 = QFont()
        font3.setPointSize(9)
        self.timesig_line.setFont(font3)
        self.timesig_line.setFrameShadow(QFrame.Plain)
        self.timesig_line.setLineWidth(2)
        self.timesig_line.setFrameShape(QFrame.HLine)

        self.verticalLayout_9.addWidget(self.timesig_line)

        self.widget_2 = QWidget(self.timesig_box)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.widget_2.setMaximumSize(QSize(60, 16777215))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(15, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_8)

        self.timesig_den = QComboBox(self.widget_2)
        self.timesig_den.addItem("")
        self.timesig_den.addItem("")
        self.timesig_den.addItem("")
        self.timesig_den.addItem("")
        self.timesig_den.addItem("")
        self.timesig_den.addItem("")
        self.timesig_den.setObjectName(u"timesig_den")
        self.timesig_den.setMaximumSize(QSize(50, 16777215))
        self.timesig_den.setFont(font1)

        self.horizontalLayout_35.addWidget(self.timesig_den)


        self.verticalLayout_9.addWidget(self.widget_2)


        self.timesig_bar.addWidget(self.timesig_box)


        self.horizontalLayout_31.addWidget(self.timesig_widget)


        self.horizontalLayout_2.addWidget(self.bpm_bar)

        self.beats_division_widget = QWidget(self.timing_spacewidget)
        self.beats_division_widget.setObjectName(u"beats_division_widget")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.beats_division_widget.sizePolicy().hasHeightForWidth())
        self.beats_division_widget.setSizePolicy(sizePolicy10)
        self.beats_division_widget.setMinimumSize(QSize(200, 0))
        self.verticalLayout_40 = QVBoxLayout(self.beats_division_widget)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.division_bar = QWidget(self.beats_division_widget)
        self.division_bar.setObjectName(u"division_bar")
        self.horizontalLayout_39 = QHBoxLayout(self.division_bar)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.division_label = QLabel(self.division_bar)
        self.division_label.setObjectName(u"division_label")
        self.division_label.setMaximumSize(QSize(80, 16777215))
        self.division_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.division_label)

        self.division_display = QLabel(self.division_bar)
        self.division_display.setObjectName(u"division_display")
        self.division_display.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.division_display)


        self.verticalLayout_40.addWidget(self.division_bar)

        self.beats_widget = QWidget(self.beats_division_widget)
        self.beats_widget.setObjectName(u"beats_widget")
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.beats_widget.sizePolicy().hasHeightForWidth())
        self.beats_widget.setSizePolicy(sizePolicy11)
        self.beats_widget.setMinimumSize(QSize(200, 40))
        self.horizontalLayout_38 = QHBoxLayout(self.beats_widget)
        self.horizontalLayout_38.setSpacing(2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(2, 2, 2, 2)

        self.verticalLayout_40.addWidget(self.beats_widget, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.beats_division_widget)

        self.widget_18 = QWidget(self.timing_spacewidget)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_59 = QVBoxLayout(self.widget_18)
        self.verticalLayout_59.setSpacing(2)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(2, 2, 2, 2)
        self.meter_str_widget = QWidget(self.widget_18)
        self.meter_str_widget.setObjectName(u"meter_str_widget")
        sizePolicy5.setHeightForWidth(self.meter_str_widget.sizePolicy().hasHeightForWidth())
        self.meter_str_widget.setSizePolicy(sizePolicy5)
        self.horizontalLayout_40 = QHBoxLayout(self.meter_str_widget)
        self.horizontalLayout_40.setSpacing(2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(2, 2, 2, 2)
        self.meter_str_label = QLabel(self.meter_str_widget)
        self.meter_str_label.setObjectName(u"meter_str_label")
        self.meter_str_label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_40.addWidget(self.meter_str_label)

        self.meter_str_slider_layout = QWidget(self.meter_str_widget)
        self.meter_str_slider_layout.setObjectName(u"meter_str_slider_layout")
        self.verticalLayout_61 = QVBoxLayout(self.meter_str_slider_layout)
        self.verticalLayout_61.setSpacing(4)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(4, 0, 2, 2)
        self.meter_str_display = QLabel(self.meter_str_slider_layout)
        self.meter_str_display.setObjectName(u"meter_str_display")
        sizePolicy5.setHeightForWidth(self.meter_str_display.sizePolicy().hasHeightForWidth())
        self.meter_str_display.setSizePolicy(sizePolicy5)
        self.meter_str_display.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_61.addWidget(self.meter_str_display)

        self.meter_str_slider = QSlider(self.meter_str_slider_layout)
        self.meter_str_slider.setObjectName(u"meter_str_slider")
        self.meter_str_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_61.addWidget(self.meter_str_slider)


        self.horizontalLayout_40.addWidget(self.meter_str_slider_layout)


        self.verticalLayout_59.addWidget(self.meter_str_widget)


        self.horizontalLayout_2.addWidget(self.widget_18, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(200, 179, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.timing_spacewidget)


        self.verticalLayout_13.addWidget(self.timing_arch_widget)

        self.weights_arch_widget = QWidget(self.rhythm_page)
        self.weights_arch_widget.setObjectName(u"weights_arch_widget")
        self.verticalLayout_5 = QVBoxLayout(self.weights_arch_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.weights_label = QLabel(self.weights_arch_widget)
        self.weights_label.setObjectName(u"weights_label")
        sizePolicy9.setHeightForWidth(self.weights_label.sizePolicy().hasHeightForWidth())
        self.weights_label.setSizePolicy(sizePolicy9)
        self.weights_label.setMinimumSize(QSize(100, 0))
        self.weights_label.setMaximumSize(QSize(100, 16777215))
        self.weights_label.setStyleSheet(u"QLabel {\n"
"	font-size:13pt;\n"
"}")

        self.horizontalLayout_45.addWidget(self.weights_label)

        self.rest_conversion_widget = QWidget(self.weights_arch_widget)
        self.rest_conversion_widget.setObjectName(u"rest_conversion_widget")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(2)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.rest_conversion_widget.sizePolicy().hasHeightForWidth())
        self.rest_conversion_widget.setSizePolicy(sizePolicy12)
        self.horizontalLayout_46 = QHBoxLayout(self.rest_conversion_widget)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.prime_roll_label_15 = QLabel(self.rest_conversion_widget)
        self.prime_roll_label_15.setObjectName(u"prime_roll_label_15")
        sizePolicy1.setHeightForWidth(self.prime_roll_label_15.sizePolicy().hasHeightForWidth())
        self.prime_roll_label_15.setSizePolicy(sizePolicy1)
        self.prime_roll_label_15.setMinimumSize(QSize(0, 40))
        self.prime_roll_label_15.setMaximumSize(QSize(16777215, 40))
        self.prime_roll_label_15.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_46.addWidget(self.prime_roll_label_15)

        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.rest_display = QLabel(self.rest_conversion_widget)
        self.rest_display.setObjectName(u"rest_display")
        sizePolicy1.setHeightForWidth(self.rest_display.sizePolicy().hasHeightForWidth())
        self.rest_display.setSizePolicy(sizePolicy1)
        self.rest_display.setMinimumSize(QSize(0, 20))
        self.rest_display.setMaximumSize(QSize(16777215, 20))
        self.rest_display.setFont(font2)
        self.rest_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_65.addWidget(self.rest_display)

        self.rest_slider = QSlider(self.rest_conversion_widget)
        self.rest_slider.setObjectName(u"rest_slider")
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.rest_slider.sizePolicy().hasHeightForWidth())
        self.rest_slider.setSizePolicy(sizePolicy13)
        self.rest_slider.setMinimumSize(QSize(140, 0))
        self.rest_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.rest_slider.setMinimum(0)
        self.rest_slider.setMaximum(100)
        self.rest_slider.setPageStep(5)
        self.rest_slider.setValue(9)
        self.rest_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_65.addWidget(self.rest_slider)


        self.horizontalLayout_46.addLayout(self.verticalLayout_65)

        self.snap_widget = QWidget(self.rest_conversion_widget)
        self.snap_widget.setObjectName(u"snap_widget")
        sizePolicy12.setHeightForWidth(self.snap_widget.sizePolicy().hasHeightForWidth())
        self.snap_widget.setSizePolicy(sizePolicy12)
        self.horizontalLayout_47 = QHBoxLayout(self.snap_widget)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.snap_label = QLabel(self.snap_widget)
        self.snap_label.setObjectName(u"snap_label")
        sizePolicy1.setHeightForWidth(self.snap_label.sizePolicy().hasHeightForWidth())
        self.snap_label.setSizePolicy(sizePolicy1)
        self.snap_label.setMinimumSize(QSize(0, 40))
        self.snap_label.setMaximumSize(QSize(16777215, 40))
        self.snap_label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_47.addWidget(self.snap_label)

        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.snap_display = QLabel(self.snap_widget)
        self.snap_display.setObjectName(u"snap_display")
        sizePolicy1.setHeightForWidth(self.snap_display.sizePolicy().hasHeightForWidth())
        self.snap_display.setSizePolicy(sizePolicy1)
        self.snap_display.setMinimumSize(QSize(0, 20))
        self.snap_display.setMaximumSize(QSize(16777215, 20))
        self.snap_display.setFont(font2)
        self.snap_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_66.addWidget(self.snap_display)

        self.snap_slider = QSlider(self.snap_widget)
        self.snap_slider.setObjectName(u"snap_slider")
        sizePolicy13.setHeightForWidth(self.snap_slider.sizePolicy().hasHeightForWidth())
        self.snap_slider.setSizePolicy(sizePolicy13)
        self.snap_slider.setMinimumSize(QSize(140, 0))
        self.snap_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.snap_slider.setMinimum(0)
        self.snap_slider.setMaximum(100)
        self.snap_slider.setPageStep(5)
        self.snap_slider.setValue(9)
        self.snap_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_66.addWidget(self.snap_slider)


        self.horizontalLayout_47.addLayout(self.verticalLayout_66)


        self.horizontalLayout_46.addWidget(self.snap_widget)


        self.horizontalLayout_45.addWidget(self.rest_conversion_widget)

        self.horizontalSpacer_4 = QSpacerItem(600, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_45)

        self.weights_widget = QWidget(self.weights_arch_widget)
        self.weights_widget.setObjectName(u"weights_widget")
        sizePolicy4.setHeightForWidth(self.weights_widget.sizePolicy().hasHeightForWidth())
        self.weights_widget.setSizePolicy(sizePolicy4)
        self.weights_widget.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.weights_widget)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.notes_images = QWidget(self.weights_widget)
        self.notes_images.setObjectName(u"notes_images")
        sizePolicy9.setHeightForWidth(self.notes_images.sizePolicy().hasHeightForWidth())
        self.notes_images.setSizePolicy(sizePolicy9)
        self.notes_images.setMinimumSize(QSize(100, 0))
        self.notes_images.setMaximumSize(QSize(100, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.notes_images)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 0, -1, 0)
        self.prime_weights_label_2 = QLabel(self.notes_images)
        self.prime_weights_label_2.setObjectName(u"prime_weights_label_2")
        sizePolicy1.setHeightForWidth(self.prime_weights_label_2.sizePolicy().hasHeightForWidth())
        self.prime_weights_label_2.setSizePolicy(sizePolicy1)
        self.prime_weights_label_2.setMinimumSize(QSize(0, 40))
        self.prime_weights_label_2.setMaximumSize(QSize(16777215, 40))
        self.prime_weights_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_19.addWidget(self.prime_weights_label_2)

        self.widget_6 = QWidget(self.notes_images)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.whole_weight_image_2 = QLabel(self.widget_6)
        self.whole_weight_image_2.setObjectName(u"whole_weight_image_2")
        sizePolicy6.setHeightForWidth(self.whole_weight_image_2.sizePolicy().hasHeightForWidth())
        self.whole_weight_image_2.setSizePolicy(sizePolicy6)
        self.whole_weight_image_2.setMinimumSize(QSize(50, 50))
        self.whole_weight_image_2.setMaximumSize(QSize(50, 50))
        self.whole_weight_image_2.setFont(font2)
        self.whole_weight_image_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.whole_weight_image_2.setPixmap(QPixmap(u"../data/images/whole.png"))
        self.whole_weight_image_2.setScaledContents(True)
        self.whole_weight_image_2.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.whole_weight_image_2)


        self.verticalLayout_19.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.notes_images)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.half_weight_image_2 = QLabel(self.widget_7)
        self.half_weight_image_2.setObjectName(u"half_weight_image_2")
        sizePolicy6.setHeightForWidth(self.half_weight_image_2.sizePolicy().hasHeightForWidth())
        self.half_weight_image_2.setSizePolicy(sizePolicy6)
        self.half_weight_image_2.setMinimumSize(QSize(50, 50))
        self.half_weight_image_2.setMaximumSize(QSize(50, 50))
        self.half_weight_image_2.setFont(font2)
        self.half_weight_image_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.half_weight_image_2.setPixmap(QPixmap(u"../data/images/half.png"))
        self.half_weight_image_2.setScaledContents(True)
        self.half_weight_image_2.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.half_weight_image_2)


        self.verticalLayout_19.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.notes_images)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.quarter_weight_image_2 = QLabel(self.widget_8)
        self.quarter_weight_image_2.setObjectName(u"quarter_weight_image_2")
        sizePolicy6.setHeightForWidth(self.quarter_weight_image_2.sizePolicy().hasHeightForWidth())
        self.quarter_weight_image_2.setSizePolicy(sizePolicy6)
        self.quarter_weight_image_2.setMinimumSize(QSize(50, 50))
        self.quarter_weight_image_2.setMaximumSize(QSize(50, 50))
        self.quarter_weight_image_2.setFont(font2)
        self.quarter_weight_image_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.quarter_weight_image_2.setPixmap(QPixmap(u"../data/images/quarter.png"))
        self.quarter_weight_image_2.setScaledContents(True)
        self.quarter_weight_image_2.setWordWrap(True)

        self.horizontalLayout_20.addWidget(self.quarter_weight_image_2)


        self.verticalLayout_19.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.notes_images)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.eighth_weight_image_2 = QLabel(self.widget_9)
        self.eighth_weight_image_2.setObjectName(u"eighth_weight_image_2")
        sizePolicy6.setHeightForWidth(self.eighth_weight_image_2.sizePolicy().hasHeightForWidth())
        self.eighth_weight_image_2.setSizePolicy(sizePolicy6)
        self.eighth_weight_image_2.setMinimumSize(QSize(50, 50))
        self.eighth_weight_image_2.setMaximumSize(QSize(50, 50))
        self.eighth_weight_image_2.setFont(font2)
        self.eighth_weight_image_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.eighth_weight_image_2.setPixmap(QPixmap(u"../data/images/eighth.png"))
        self.eighth_weight_image_2.setScaledContents(True)
        self.eighth_weight_image_2.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.eighth_weight_image_2)


        self.verticalLayout_19.addWidget(self.widget_9)

        self.eighth_box = QWidget(self.notes_images)
        self.eighth_box.setObjectName(u"eighth_box")
        self.quarter_weight_bar_2 = QHBoxLayout(self.eighth_box)
        self.quarter_weight_bar_2.setObjectName(u"quarter_weight_bar_2")
        self.sixteenth_weight_image_4 = QLabel(self.eighth_box)
        self.sixteenth_weight_image_4.setObjectName(u"sixteenth_weight_image_4")
        sizePolicy6.setHeightForWidth(self.sixteenth_weight_image_4.sizePolicy().hasHeightForWidth())
        self.sixteenth_weight_image_4.setSizePolicy(sizePolicy6)
        self.sixteenth_weight_image_4.setMinimumSize(QSize(50, 50))
        self.sixteenth_weight_image_4.setMaximumSize(QSize(50, 50))
        self.sixteenth_weight_image_4.setFont(font2)
        self.sixteenth_weight_image_4.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.sixteenth_weight_image_4.setPixmap(QPixmap(u"../data/images/sixteenth.png"))
        self.sixteenth_weight_image_4.setScaledContents(True)
        self.sixteenth_weight_image_4.setWordWrap(True)

        self.quarter_weight_bar_2.addWidget(self.sixteenth_weight_image_4)


        self.verticalLayout_19.addWidget(self.eighth_box)

        self.widget_11 = QWidget(self.notes_images)
        self.widget_11.setObjectName(u"widget_11")
        self.thirtysecond_weight_bar_2 = QHBoxLayout(self.widget_11)
        self.thirtysecond_weight_bar_2.setObjectName(u"thirtysecond_weight_bar_2")
        self.sixteenth_weight_image_5 = QLabel(self.widget_11)
        self.sixteenth_weight_image_5.setObjectName(u"sixteenth_weight_image_5")
        sizePolicy6.setHeightForWidth(self.sixteenth_weight_image_5.sizePolicy().hasHeightForWidth())
        self.sixteenth_weight_image_5.setSizePolicy(sizePolicy6)
        self.sixteenth_weight_image_5.setMinimumSize(QSize(50, 50))
        self.sixteenth_weight_image_5.setMaximumSize(QSize(50, 50))
        self.sixteenth_weight_image_5.setFont(font2)
        self.sixteenth_weight_image_5.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.sixteenth_weight_image_5.setPixmap(QPixmap(u"../data/images/thirty-second.png"))
        self.sixteenth_weight_image_5.setScaledContents(True)
        self.sixteenth_weight_image_5.setWordWrap(True)

        self.thirtysecond_weight_bar_2.addWidget(self.sixteenth_weight_image_5)


        self.verticalLayout_19.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.notes_images)
        self.widget_12.setObjectName(u"widget_12")
        self.sixtyfourth_weight_bar_2 = QHBoxLayout(self.widget_12)
        self.sixtyfourth_weight_bar_2.setObjectName(u"sixtyfourth_weight_bar_2")
        self.sixteenth_weight_image_6 = QLabel(self.widget_12)
        self.sixteenth_weight_image_6.setObjectName(u"sixteenth_weight_image_6")
        sizePolicy6.setHeightForWidth(self.sixteenth_weight_image_6.sizePolicy().hasHeightForWidth())
        self.sixteenth_weight_image_6.setSizePolicy(sizePolicy6)
        self.sixteenth_weight_image_6.setMinimumSize(QSize(50, 50))
        self.sixteenth_weight_image_6.setMaximumSize(QSize(50, 50))
        self.sixteenth_weight_image_6.setFont(font2)
        self.sixteenth_weight_image_6.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.sixteenth_weight_image_6.setPixmap(QPixmap(u"../data/images/sixty-fourth.png"))
        self.sixteenth_weight_image_6.setScaledContents(True)
        self.sixteenth_weight_image_6.setWordWrap(True)

        self.sixtyfourth_weight_bar_2.addWidget(self.sixteenth_weight_image_6)


        self.verticalLayout_19.addWidget(self.widget_12)


        self.horizontalLayout_12.addWidget(self.notes_images)

        self.prime_weights_widget = QWidget(self.weights_widget)
        self.prime_weights_widget.setObjectName(u"prime_weights_widget")
        sizePolicy14 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy14.setHorizontalStretch(7)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.prime_weights_widget.sizePolicy().hasHeightForWidth())
        self.prime_weights_widget.setSizePolicy(sizePolicy14)
        self.prime_weights_widget.setMinimumSize(QSize(400, 0))
        self.verticalLayout_16 = QVBoxLayout(self.prime_weights_widget)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 0, -1, 0)
        self.prime_roll_label = QLabel(self.prime_weights_widget)
        self.prime_roll_label.setObjectName(u"prime_roll_label")
        sizePolicy1.setHeightForWidth(self.prime_roll_label.sizePolicy().hasHeightForWidth())
        self.prime_roll_label.setSizePolicy(sizePolicy1)
        self.prime_roll_label.setMinimumSize(QSize(0, 40))
        self.prime_roll_label.setMaximumSize(QSize(16777215, 40))
        self.prime_roll_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_16.addWidget(self.prime_roll_label)

        self.whole_prime_bar = QWidget(self.prime_weights_widget)
        self.whole_prime_bar.setObjectName(u"whole_prime_bar")
        self.horizontalLayout_13 = QHBoxLayout(self.whole_prime_bar)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.whole_prime_display = QLabel(self.whole_prime_bar)
        self.whole_prime_display.setObjectName(u"whole_prime_display")
        self.whole_prime_display.setFont(font2)
        self.whole_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_24.addWidget(self.whole_prime_display)

        self.whole_prime_slider = QSlider(self.whole_prime_bar)
        self.whole_prime_slider.setObjectName(u"whole_prime_slider")
        self.whole_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.whole_prime_slider.setMinimum(0)
        self.whole_prime_slider.setMaximum(100)
        self.whole_prime_slider.setPageStep(5)
        self.whole_prime_slider.setValue(9)
        self.whole_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_24.addWidget(self.whole_prime_slider)


        self.horizontalLayout_13.addLayout(self.verticalLayout_24)

        self.dotted_10 = QLabel(self.whole_prime_bar)
        self.dotted_10.setObjectName(u"dotted_10")
        sizePolicy6.setHeightForWidth(self.dotted_10.sizePolicy().hasHeightForWidth())
        self.dotted_10.setSizePolicy(sizePolicy6)
        self.dotted_10.setMinimumSize(QSize(50, 50))
        self.dotted_10.setMaximumSize(QSize(50, 50))
        self.dotted_10.setFont(font2)
        self.dotted_10.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_10.setScaledContents(True)
        self.dotted_10.setWordWrap(True)

        self.horizontalLayout_13.addWidget(self.dotted_10)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.dwhole_prime_display = QLabel(self.whole_prime_bar)
        self.dwhole_prime_display.setObjectName(u"dwhole_prime_display")
        self.dwhole_prime_display.setFont(font2)
        self.dwhole_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_25.addWidget(self.dwhole_prime_display)

        self.dwhole_prime_slider = QSlider(self.whole_prime_bar)
        self.dwhole_prime_slider.setObjectName(u"dwhole_prime_slider")
        self.dwhole_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dwhole_prime_slider.setMinimum(0)
        self.dwhole_prime_slider.setMaximum(100)
        self.dwhole_prime_slider.setPageStep(5)
        self.dwhole_prime_slider.setValue(9)
        self.dwhole_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_25.addWidget(self.dwhole_prime_slider)


        self.horizontalLayout_13.addLayout(self.verticalLayout_25)


        self.verticalLayout_16.addWidget(self.whole_prime_bar)

        self.half_prime_bar = QWidget(self.prime_weights_widget)
        self.half_prime_bar.setObjectName(u"half_prime_bar")
        self.horizontalLayout_14 = QHBoxLayout(self.half_prime_bar)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.half_prime_display = QLabel(self.half_prime_bar)
        self.half_prime_display.setObjectName(u"half_prime_display")
        self.half_prime_display.setFont(font2)
        self.half_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_26.addWidget(self.half_prime_display)

        self.half_prime_slider = QSlider(self.half_prime_bar)
        self.half_prime_slider.setObjectName(u"half_prime_slider")
        self.half_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}\n"
"")
        self.half_prime_slider.setMinimum(0)
        self.half_prime_slider.setMaximum(100)
        self.half_prime_slider.setPageStep(5)
        self.half_prime_slider.setValue(19)
        self.half_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_26.addWidget(self.half_prime_slider)


        self.horizontalLayout_14.addLayout(self.verticalLayout_26)

        self.dotted_9 = QLabel(self.half_prime_bar)
        self.dotted_9.setObjectName(u"dotted_9")
        sizePolicy6.setHeightForWidth(self.dotted_9.sizePolicy().hasHeightForWidth())
        self.dotted_9.setSizePolicy(sizePolicy6)
        self.dotted_9.setMinimumSize(QSize(50, 50))
        self.dotted_9.setMaximumSize(QSize(50, 50))
        self.dotted_9.setFont(font2)
        self.dotted_9.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_9.setScaledContents(True)
        self.dotted_9.setWordWrap(True)

        self.horizontalLayout_14.addWidget(self.dotted_9)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.dhalf_prime_display = QLabel(self.half_prime_bar)
        self.dhalf_prime_display.setObjectName(u"dhalf_prime_display")
        self.dhalf_prime_display.setFont(font2)
        self.dhalf_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_27.addWidget(self.dhalf_prime_display)

        self.dhalf_prime_slider = QSlider(self.half_prime_bar)
        self.dhalf_prime_slider.setObjectName(u"dhalf_prime_slider")
        self.dhalf_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dhalf_prime_slider.setMinimum(0)
        self.dhalf_prime_slider.setMaximum(100)
        self.dhalf_prime_slider.setPageStep(5)
        self.dhalf_prime_slider.setValue(9)
        self.dhalf_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_27.addWidget(self.dhalf_prime_slider)


        self.horizontalLayout_14.addLayout(self.verticalLayout_27)


        self.verticalLayout_16.addWidget(self.half_prime_bar)

        self.quarter_prime_bar = QWidget(self.prime_weights_widget)
        self.quarter_prime_bar.setObjectName(u"quarter_prime_bar")
        self.horizontalLayout_15 = QHBoxLayout(self.quarter_prime_bar)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.quarter_prime_display = QLabel(self.quarter_prime_bar)
        self.quarter_prime_display.setObjectName(u"quarter_prime_display")
        self.quarter_prime_display.setFont(font2)
        self.quarter_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_28.addWidget(self.quarter_prime_display)

        self.quarter_prime_slider = QSlider(self.quarter_prime_bar)
        self.quarter_prime_slider.setObjectName(u"quarter_prime_slider")
        self.quarter_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.quarter_prime_slider.setMinimum(0)
        self.quarter_prime_slider.setMaximum(100)
        self.quarter_prime_slider.setPageStep(5)
        self.quarter_prime_slider.setValue(29)
        self.quarter_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.quarter_prime_slider)


        self.horizontalLayout_15.addLayout(self.verticalLayout_28)

        self.dotted_3 = QLabel(self.quarter_prime_bar)
        self.dotted_3.setObjectName(u"dotted_3")
        sizePolicy6.setHeightForWidth(self.dotted_3.sizePolicy().hasHeightForWidth())
        self.dotted_3.setSizePolicy(sizePolicy6)
        self.dotted_3.setMinimumSize(QSize(50, 50))
        self.dotted_3.setMaximumSize(QSize(50, 50))
        self.dotted_3.setFont(font2)
        self.dotted_3.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_3.setScaledContents(True)
        self.dotted_3.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.dotted_3)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.dquarter_prime_display = QLabel(self.quarter_prime_bar)
        self.dquarter_prime_display.setObjectName(u"dquarter_prime_display")
        self.dquarter_prime_display.setFont(font2)
        self.dquarter_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_29.addWidget(self.dquarter_prime_display)

        self.dquarter_prime_slider = QSlider(self.quarter_prime_bar)
        self.dquarter_prime_slider.setObjectName(u"dquarter_prime_slider")
        self.dquarter_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dquarter_prime_slider.setMinimum(0)
        self.dquarter_prime_slider.setMaximum(100)
        self.dquarter_prime_slider.setPageStep(5)
        self.dquarter_prime_slider.setValue(9)
        self.dquarter_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_29.addWidget(self.dquarter_prime_slider)


        self.horizontalLayout_15.addLayout(self.verticalLayout_29)


        self.verticalLayout_16.addWidget(self.quarter_prime_bar)

        self.eighth_prime_bar = QWidget(self.prime_weights_widget)
        self.eighth_prime_bar.setObjectName(u"eighth_prime_bar")
        self.horizontalLayout_16 = QHBoxLayout(self.eighth_prime_bar)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.eighth_prime_display = QLabel(self.eighth_prime_bar)
        self.eighth_prime_display.setObjectName(u"eighth_prime_display")
        self.eighth_prime_display.setFont(font2)
        self.eighth_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_30.addWidget(self.eighth_prime_display)

        self.eighth_prime_slider = QSlider(self.eighth_prime_bar)
        self.eighth_prime_slider.setObjectName(u"eighth_prime_slider")
        self.eighth_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.eighth_prime_slider.setMinimum(0)
        self.eighth_prime_slider.setMaximum(100)
        self.eighth_prime_slider.setPageStep(5)
        self.eighth_prime_slider.setValue(29)
        self.eighth_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_30.addWidget(self.eighth_prime_slider)


        self.horizontalLayout_16.addLayout(self.verticalLayout_30)

        self.dotted_8 = QLabel(self.eighth_prime_bar)
        self.dotted_8.setObjectName(u"dotted_8")
        sizePolicy6.setHeightForWidth(self.dotted_8.sizePolicy().hasHeightForWidth())
        self.dotted_8.setSizePolicy(sizePolicy6)
        self.dotted_8.setMinimumSize(QSize(50, 50))
        self.dotted_8.setMaximumSize(QSize(50, 50))
        self.dotted_8.setFont(font2)
        self.dotted_8.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_8.setScaledContents(True)
        self.dotted_8.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.dotted_8)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.deighth_prime_display = QLabel(self.eighth_prime_bar)
        self.deighth_prime_display.setObjectName(u"deighth_prime_display")
        self.deighth_prime_display.setFont(font2)
        self.deighth_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_31.addWidget(self.deighth_prime_display)

        self.deighth_prime_slider = QSlider(self.eighth_prime_bar)
        self.deighth_prime_slider.setObjectName(u"deighth_prime_slider")
        self.deighth_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.deighth_prime_slider.setMinimum(0)
        self.deighth_prime_slider.setMaximum(100)
        self.deighth_prime_slider.setPageStep(5)
        self.deighth_prime_slider.setValue(9)
        self.deighth_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_31.addWidget(self.deighth_prime_slider)


        self.horizontalLayout_16.addLayout(self.verticalLayout_31)


        self.verticalLayout_16.addWidget(self.eighth_prime_bar)

        self.sixteenth_prime_bar = QWidget(self.prime_weights_widget)
        self.sixteenth_prime_bar.setObjectName(u"sixteenth_prime_bar")
        self.quarter_weight_bar = QHBoxLayout(self.sixteenth_prime_bar)
        self.quarter_weight_bar.setObjectName(u"quarter_weight_bar")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.sixteenth_prime_display = QLabel(self.sixteenth_prime_bar)
        self.sixteenth_prime_display.setObjectName(u"sixteenth_prime_display")
        self.sixteenth_prime_display.setFont(font2)
        self.sixteenth_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_32.addWidget(self.sixteenth_prime_display)

        self.sixteenth_prime_slider = QSlider(self.sixteenth_prime_bar)
        self.sixteenth_prime_slider.setObjectName(u"sixteenth_prime_slider")
        self.sixteenth_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.sixteenth_prime_slider.setMinimum(0)
        self.sixteenth_prime_slider.setMaximum(100)
        self.sixteenth_prime_slider.setPageStep(5)
        self.sixteenth_prime_slider.setValue(9)
        self.sixteenth_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_32.addWidget(self.sixteenth_prime_slider)


        self.quarter_weight_bar.addLayout(self.verticalLayout_32)

        self.dotted_7 = QLabel(self.sixteenth_prime_bar)
        self.dotted_7.setObjectName(u"dotted_7")
        sizePolicy6.setHeightForWidth(self.dotted_7.sizePolicy().hasHeightForWidth())
        self.dotted_7.setSizePolicy(sizePolicy6)
        self.dotted_7.setMinimumSize(QSize(50, 50))
        self.dotted_7.setMaximumSize(QSize(50, 50))
        self.dotted_7.setFont(font2)
        self.dotted_7.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_7.setScaledContents(True)
        self.dotted_7.setWordWrap(True)

        self.quarter_weight_bar.addWidget(self.dotted_7)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.dsixteenth_prime_display = QLabel(self.sixteenth_prime_bar)
        self.dsixteenth_prime_display.setObjectName(u"dsixteenth_prime_display")
        self.dsixteenth_prime_display.setFont(font2)
        self.dsixteenth_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_33.addWidget(self.dsixteenth_prime_display)

        self.dsixteenth_prime_slider = QSlider(self.sixteenth_prime_bar)
        self.dsixteenth_prime_slider.setObjectName(u"dsixteenth_prime_slider")
        self.dsixteenth_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dsixteenth_prime_slider.setMinimum(0)
        self.dsixteenth_prime_slider.setMaximum(100)
        self.dsixteenth_prime_slider.setPageStep(5)
        self.dsixteenth_prime_slider.setValue(9)
        self.dsixteenth_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_33.addWidget(self.dsixteenth_prime_slider)


        self.quarter_weight_bar.addLayout(self.verticalLayout_33)


        self.verticalLayout_16.addWidget(self.sixteenth_prime_bar)

        self.thirtysecond_prime_bar = QWidget(self.prime_weights_widget)
        self.thirtysecond_prime_bar.setObjectName(u"thirtysecond_prime_bar")
        self.thirtysecond_weight_bar = QHBoxLayout(self.thirtysecond_prime_bar)
        self.thirtysecond_weight_bar.setObjectName(u"thirtysecond_weight_bar")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.thirtysecond_prime_display = QLabel(self.thirtysecond_prime_bar)
        self.thirtysecond_prime_display.setObjectName(u"thirtysecond_prime_display")
        self.thirtysecond_prime_display.setFont(font2)
        self.thirtysecond_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_45.addWidget(self.thirtysecond_prime_display)

        self.thirtysecond_prime_slider = QSlider(self.thirtysecond_prime_bar)
        self.thirtysecond_prime_slider.setObjectName(u"thirtysecond_prime_slider")
        self.thirtysecond_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.thirtysecond_prime_slider.setMinimum(0)
        self.thirtysecond_prime_slider.setMaximum(100)
        self.thirtysecond_prime_slider.setPageStep(5)
        self.thirtysecond_prime_slider.setValue(9)
        self.thirtysecond_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_45.addWidget(self.thirtysecond_prime_slider)


        self.thirtysecond_weight_bar.addLayout(self.verticalLayout_45)

        self.dotted_11 = QLabel(self.thirtysecond_prime_bar)
        self.dotted_11.setObjectName(u"dotted_11")
        sizePolicy6.setHeightForWidth(self.dotted_11.sizePolicy().hasHeightForWidth())
        self.dotted_11.setSizePolicy(sizePolicy6)
        self.dotted_11.setMinimumSize(QSize(50, 50))
        self.dotted_11.setMaximumSize(QSize(50, 50))
        self.dotted_11.setFont(font2)
        self.dotted_11.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_11.setScaledContents(True)
        self.dotted_11.setWordWrap(True)

        self.thirtysecond_weight_bar.addWidget(self.dotted_11)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.dthirtysecond_prime_display = QLabel(self.thirtysecond_prime_bar)
        self.dthirtysecond_prime_display.setObjectName(u"dthirtysecond_prime_display")
        self.dthirtysecond_prime_display.setFont(font2)
        self.dthirtysecond_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_46.addWidget(self.dthirtysecond_prime_display)

        self.dthirtysecond_prime_slider = QSlider(self.thirtysecond_prime_bar)
        self.dthirtysecond_prime_slider.setObjectName(u"dthirtysecond_prime_slider")
        self.dthirtysecond_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dthirtysecond_prime_slider.setMinimum(0)
        self.dthirtysecond_prime_slider.setMaximum(100)
        self.dthirtysecond_prime_slider.setPageStep(5)
        self.dthirtysecond_prime_slider.setValue(9)
        self.dthirtysecond_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_46.addWidget(self.dthirtysecond_prime_slider)


        self.thirtysecond_weight_bar.addLayout(self.verticalLayout_46)


        self.verticalLayout_16.addWidget(self.thirtysecond_prime_bar)

        self.sixtyfourth_prime_bar = QWidget(self.prime_weights_widget)
        self.sixtyfourth_prime_bar.setObjectName(u"sixtyfourth_prime_bar")
        self.sixtyfourth_weight_bar = QHBoxLayout(self.sixtyfourth_prime_bar)
        self.sixtyfourth_weight_bar.setObjectName(u"sixtyfourth_weight_bar")
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.sixtyfourth_prime_display = QLabel(self.sixtyfourth_prime_bar)
        self.sixtyfourth_prime_display.setObjectName(u"sixtyfourth_prime_display")
        self.sixtyfourth_prime_display.setFont(font2)
        self.sixtyfourth_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_47.addWidget(self.sixtyfourth_prime_display)

        self.sixtyfourth_prime_slider = QSlider(self.sixtyfourth_prime_bar)
        self.sixtyfourth_prime_slider.setObjectName(u"sixtyfourth_prime_slider")
        self.sixtyfourth_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.sixtyfourth_prime_slider.setMinimum(0)
        self.sixtyfourth_prime_slider.setMaximum(100)
        self.sixtyfourth_prime_slider.setPageStep(5)
        self.sixtyfourth_prime_slider.setValue(9)
        self.sixtyfourth_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_47.addWidget(self.sixtyfourth_prime_slider)


        self.sixtyfourth_weight_bar.addLayout(self.verticalLayout_47)

        self.dotted_12 = QLabel(self.sixtyfourth_prime_bar)
        self.dotted_12.setObjectName(u"dotted_12")
        sizePolicy6.setHeightForWidth(self.dotted_12.sizePolicy().hasHeightForWidth())
        self.dotted_12.setSizePolicy(sizePolicy6)
        self.dotted_12.setMinimumSize(QSize(50, 50))
        self.dotted_12.setMaximumSize(QSize(50, 50))
        self.dotted_12.setFont(font2)
        self.dotted_12.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_12.setScaledContents(True)
        self.dotted_12.setWordWrap(True)

        self.sixtyfourth_weight_bar.addWidget(self.dotted_12)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.dsixtyfourth_prime_display = QLabel(self.sixtyfourth_prime_bar)
        self.dsixtyfourth_prime_display.setObjectName(u"dsixtyfourth_prime_display")
        self.dsixtyfourth_prime_display.setFont(font2)
        self.dsixtyfourth_prime_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_48.addWidget(self.dsixtyfourth_prime_display)

        self.dsixtyfourth_prime_slider = QSlider(self.sixtyfourth_prime_bar)
        self.dsixtyfourth_prime_slider.setObjectName(u"dsixtyfourth_prime_slider")
        self.dsixtyfourth_prime_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dsixtyfourth_prime_slider.setMinimum(0)
        self.dsixtyfourth_prime_slider.setMaximum(100)
        self.dsixtyfourth_prime_slider.setPageStep(5)
        self.dsixtyfourth_prime_slider.setValue(9)
        self.dsixtyfourth_prime_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_48.addWidget(self.dsixtyfourth_prime_slider)


        self.sixtyfourth_weight_bar.addLayout(self.verticalLayout_48)


        self.verticalLayout_16.addWidget(self.sixtyfourth_prime_bar)


        self.horizontalLayout_12.addWidget(self.prime_weights_widget)

        self.pair_weights_widget = QWidget(self.weights_widget)
        self.pair_weights_widget.setObjectName(u"pair_weights_widget")
        sizePolicy14.setHeightForWidth(self.pair_weights_widget.sizePolicy().hasHeightForWidth())
        self.pair_weights_widget.setSizePolicy(sizePolicy14)
        self.pair_weights_widget.setMinimumSize(QSize(400, 0))
        self.verticalLayout_34 = QVBoxLayout(self.pair_weights_widget)
        self.verticalLayout_34.setSpacing(6)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, 0, -1, 0)
        self.pair_weights_label = QLabel(self.pair_weights_widget)
        self.pair_weights_label.setObjectName(u"pair_weights_label")
        sizePolicy1.setHeightForWidth(self.pair_weights_label.sizePolicy().hasHeightForWidth())
        self.pair_weights_label.setSizePolicy(sizePolicy1)
        self.pair_weights_label.setMinimumSize(QSize(0, 40))
        self.pair_weights_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_34.addWidget(self.pair_weights_label)

        self.whole_roll_bar = QWidget(self.pair_weights_widget)
        self.whole_roll_bar.setObjectName(u"whole_roll_bar")
        self.horizontalLayout_25 = QHBoxLayout(self.whole_roll_bar)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.whole_pair_display = QLabel(self.whole_roll_bar)
        self.whole_pair_display.setObjectName(u"whole_pair_display")
        self.whole_pair_display.setFont(font2)
        self.whole_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_55.addWidget(self.whole_pair_display)

        self.whole_pair_slider = QSlider(self.whole_roll_bar)
        self.whole_pair_slider.setObjectName(u"whole_pair_slider")
        self.whole_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.whole_pair_slider.setMinimum(0)
        self.whole_pair_slider.setMaximum(100)
        self.whole_pair_slider.setPageStep(5)
        self.whole_pair_slider.setValue(9)
        self.whole_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_55.addWidget(self.whole_pair_slider)


        self.horizontalLayout_25.addLayout(self.verticalLayout_55)

        self.dotted_5 = QLabel(self.whole_roll_bar)
        self.dotted_5.setObjectName(u"dotted_5")
        sizePolicy6.setHeightForWidth(self.dotted_5.sizePolicy().hasHeightForWidth())
        self.dotted_5.setSizePolicy(sizePolicy6)
        self.dotted_5.setMinimumSize(QSize(50, 50))
        self.dotted_5.setMaximumSize(QSize(50, 50))
        self.dotted_5.setFont(font2)
        self.dotted_5.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_5.setScaledContents(True)
        self.dotted_5.setWordWrap(True)

        self.horizontalLayout_25.addWidget(self.dotted_5)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.dwhole_pair_display = QLabel(self.whole_roll_bar)
        self.dwhole_pair_display.setObjectName(u"dwhole_pair_display")
        self.dwhole_pair_display.setEnabled(True)
        self.dwhole_pair_display.setFont(font2)
        self.dwhole_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_56.addWidget(self.dwhole_pair_display)

        self.dwhole_pair_slider = QSlider(self.whole_roll_bar)
        self.dwhole_pair_slider.setObjectName(u"dwhole_pair_slider")
        self.dwhole_pair_slider.setEnabled(True)
        self.dwhole_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dwhole_pair_slider.setMinimum(0)
        self.dwhole_pair_slider.setMaximum(100)
        self.dwhole_pair_slider.setPageStep(5)
        self.dwhole_pair_slider.setValue(9)
        self.dwhole_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_56.addWidget(self.dwhole_pair_slider)


        self.horizontalLayout_25.addLayout(self.verticalLayout_56)


        self.verticalLayout_34.addWidget(self.whole_roll_bar)

        self.half_roll_bar = QWidget(self.pair_weights_widget)
        self.half_roll_bar.setObjectName(u"half_roll_bar")
        self.horizontalLayout_26 = QHBoxLayout(self.half_roll_bar)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.half_pair_display = QLabel(self.half_roll_bar)
        self.half_pair_display.setObjectName(u"half_pair_display")
        self.half_pair_display.setFont(font2)
        self.half_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_57.addWidget(self.half_pair_display)

        self.half_pair_slider = QSlider(self.half_roll_bar)
        self.half_pair_slider.setObjectName(u"half_pair_slider")
        self.half_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.half_pair_slider.setMinimum(0)
        self.half_pair_slider.setMaximum(100)
        self.half_pair_slider.setPageStep(5)
        self.half_pair_slider.setValue(9)
        self.half_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_57.addWidget(self.half_pair_slider)


        self.horizontalLayout_26.addLayout(self.verticalLayout_57)

        self.dotted_6 = QLabel(self.half_roll_bar)
        self.dotted_6.setObjectName(u"dotted_6")
        sizePolicy6.setHeightForWidth(self.dotted_6.sizePolicy().hasHeightForWidth())
        self.dotted_6.setSizePolicy(sizePolicy6)
        self.dotted_6.setMinimumSize(QSize(50, 50))
        self.dotted_6.setMaximumSize(QSize(50, 50))
        self.dotted_6.setFont(font2)
        self.dotted_6.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_6.setScaledContents(True)
        self.dotted_6.setWordWrap(True)

        self.horizontalLayout_26.addWidget(self.dotted_6)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.dhalf_pair_display = QLabel(self.half_roll_bar)
        self.dhalf_pair_display.setObjectName(u"dhalf_pair_display")
        self.dhalf_pair_display.setEnabled(True)
        self.dhalf_pair_display.setFont(font2)
        self.dhalf_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_58.addWidget(self.dhalf_pair_display)

        self.dhalf_pair_slider = QSlider(self.half_roll_bar)
        self.dhalf_pair_slider.setObjectName(u"dhalf_pair_slider")
        self.dhalf_pair_slider.setEnabled(True)
        self.dhalf_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dhalf_pair_slider.setMinimum(0)
        self.dhalf_pair_slider.setMaximum(100)
        self.dhalf_pair_slider.setPageStep(5)
        self.dhalf_pair_slider.setValue(9)
        self.dhalf_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_58.addWidget(self.dhalf_pair_slider)


        self.horizontalLayout_26.addLayout(self.verticalLayout_58)


        self.verticalLayout_34.addWidget(self.half_roll_bar)

        self.sixteenth_roll_bar_2 = QWidget(self.pair_weights_widget)
        self.sixteenth_roll_bar_2.setObjectName(u"sixteenth_roll_bar_2")
        self.horizontalLayout_24 = QHBoxLayout(self.sixteenth_roll_bar_2)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.quarter_pair_display = QLabel(self.sixteenth_roll_bar_2)
        self.quarter_pair_display.setObjectName(u"quarter_pair_display")
        self.quarter_pair_display.setFont(font2)
        self.quarter_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_53.addWidget(self.quarter_pair_display)

        self.quarter_pair_slider = QSlider(self.sixteenth_roll_bar_2)
        self.quarter_pair_slider.setObjectName(u"quarter_pair_slider")
        self.quarter_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.quarter_pair_slider.setMinimum(0)
        self.quarter_pair_slider.setMaximum(100)
        self.quarter_pair_slider.setPageStep(5)
        self.quarter_pair_slider.setValue(9)
        self.quarter_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_53.addWidget(self.quarter_pair_slider)


        self.horizontalLayout_24.addLayout(self.verticalLayout_53)

        self.dotted_4 = QLabel(self.sixteenth_roll_bar_2)
        self.dotted_4.setObjectName(u"dotted_4")
        sizePolicy6.setHeightForWidth(self.dotted_4.sizePolicy().hasHeightForWidth())
        self.dotted_4.setSizePolicy(sizePolicy6)
        self.dotted_4.setMinimumSize(QSize(50, 50))
        self.dotted_4.setMaximumSize(QSize(50, 50))
        self.dotted_4.setFont(font2)
        self.dotted_4.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_4.setScaledContents(True)
        self.dotted_4.setWordWrap(True)

        self.horizontalLayout_24.addWidget(self.dotted_4)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.dquarter_pair_display = QLabel(self.sixteenth_roll_bar_2)
        self.dquarter_pair_display.setObjectName(u"dquarter_pair_display")
        self.dquarter_pair_display.setEnabled(True)
        self.dquarter_pair_display.setFont(font2)
        self.dquarter_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_54.addWidget(self.dquarter_pair_display)

        self.dquarter_pair_slider = QSlider(self.sixteenth_roll_bar_2)
        self.dquarter_pair_slider.setObjectName(u"dquarter_pair_slider")
        self.dquarter_pair_slider.setEnabled(True)
        self.dquarter_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dquarter_pair_slider.setMinimum(0)
        self.dquarter_pair_slider.setMaximum(100)
        self.dquarter_pair_slider.setPageStep(5)
        self.dquarter_pair_slider.setValue(9)
        self.dquarter_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_54.addWidget(self.dquarter_pair_slider)


        self.horizontalLayout_24.addLayout(self.verticalLayout_54)


        self.verticalLayout_34.addWidget(self.sixteenth_roll_bar_2)

        self.eighth_roll_bar = QWidget(self.pair_weights_widget)
        self.eighth_roll_bar.setObjectName(u"eighth_roll_bar")
        self.horizontalLayout_21 = QHBoxLayout(self.eighth_roll_bar)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.eighth_pair_display = QLabel(self.eighth_roll_bar)
        self.eighth_pair_display.setObjectName(u"eighth_pair_display")
        self.eighth_pair_display.setFont(font2)
        self.eighth_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_41.addWidget(self.eighth_pair_display)

        self.eighth_pair_slider = QSlider(self.eighth_roll_bar)
        self.eighth_pair_slider.setObjectName(u"eighth_pair_slider")
        self.eighth_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.eighth_pair_slider.setMinimum(0)
        self.eighth_pair_slider.setMaximum(100)
        self.eighth_pair_slider.setPageStep(5)
        self.eighth_pair_slider.setValue(29)
        self.eighth_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_41.addWidget(self.eighth_pair_slider)


        self.horizontalLayout_21.addLayout(self.verticalLayout_41)

        self.dotted = QLabel(self.eighth_roll_bar)
        self.dotted.setObjectName(u"dotted")
        sizePolicy6.setHeightForWidth(self.dotted.sizePolicy().hasHeightForWidth())
        self.dotted.setSizePolicy(sizePolicy6)
        self.dotted.setMinimumSize(QSize(50, 50))
        self.dotted.setMaximumSize(QSize(50, 50))
        self.dotted.setFont(font2)
        self.dotted.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted.setScaledContents(True)
        self.dotted.setWordWrap(True)

        self.horizontalLayout_21.addWidget(self.dotted)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.deighth_pair_display = QLabel(self.eighth_roll_bar)
        self.deighth_pair_display.setObjectName(u"deighth_pair_display")
        self.deighth_pair_display.setEnabled(True)
        self.deighth_pair_display.setFont(font2)
        self.deighth_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_42.addWidget(self.deighth_pair_display)

        self.deighth_pair_slider = QSlider(self.eighth_roll_bar)
        self.deighth_pair_slider.setObjectName(u"deighth_pair_slider")
        self.deighth_pair_slider.setEnabled(True)
        self.deighth_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.deighth_pair_slider.setMinimum(0)
        self.deighth_pair_slider.setMaximum(100)
        self.deighth_pair_slider.setPageStep(5)
        self.deighth_pair_slider.setValue(9)
        self.deighth_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_42.addWidget(self.deighth_pair_slider)


        self.horizontalLayout_21.addLayout(self.verticalLayout_42)


        self.verticalLayout_34.addWidget(self.eighth_roll_bar)

        self.sixteenth_roll_bar = QWidget(self.pair_weights_widget)
        self.sixteenth_roll_bar.setObjectName(u"sixteenth_roll_bar")
        self.horizontalLayout_22 = QHBoxLayout(self.sixteenth_roll_bar)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.sixteenth_pair_display = QLabel(self.sixteenth_roll_bar)
        self.sixteenth_pair_display.setObjectName(u"sixteenth_pair_display")
        self.sixteenth_pair_display.setFont(font2)
        self.sixteenth_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_43.addWidget(self.sixteenth_pair_display)

        self.sixteenth_pair_slider = QSlider(self.sixteenth_roll_bar)
        self.sixteenth_pair_slider.setObjectName(u"sixteenth_pair_slider")
        self.sixteenth_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.sixteenth_pair_slider.setMinimum(0)
        self.sixteenth_pair_slider.setMaximum(100)
        self.sixteenth_pair_slider.setPageStep(5)
        self.sixteenth_pair_slider.setValue(9)
        self.sixteenth_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_43.addWidget(self.sixteenth_pair_slider)


        self.horizontalLayout_22.addLayout(self.verticalLayout_43)

        self.dotted_2 = QLabel(self.sixteenth_roll_bar)
        self.dotted_2.setObjectName(u"dotted_2")
        sizePolicy6.setHeightForWidth(self.dotted_2.sizePolicy().hasHeightForWidth())
        self.dotted_2.setSizePolicy(sizePolicy6)
        self.dotted_2.setMinimumSize(QSize(50, 50))
        self.dotted_2.setMaximumSize(QSize(50, 50))
        self.dotted_2.setFont(font2)
        self.dotted_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_2.setScaledContents(True)
        self.dotted_2.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.dotted_2)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.dsixteenth_pair_display = QLabel(self.sixteenth_roll_bar)
        self.dsixteenth_pair_display.setObjectName(u"dsixteenth_pair_display")
        self.dsixteenth_pair_display.setEnabled(True)
        self.dsixteenth_pair_display.setFont(font2)
        self.dsixteenth_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_44.addWidget(self.dsixteenth_pair_display)

        self.dsixteenth_pair_slider = QSlider(self.sixteenth_roll_bar)
        self.dsixteenth_pair_slider.setObjectName(u"dsixteenth_pair_slider")
        self.dsixteenth_pair_slider.setEnabled(True)
        self.dsixteenth_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dsixteenth_pair_slider.setMinimum(0)
        self.dsixteenth_pair_slider.setMaximum(100)
        self.dsixteenth_pair_slider.setPageStep(5)
        self.dsixteenth_pair_slider.setValue(9)
        self.dsixteenth_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_44.addWidget(self.dsixteenth_pair_slider)


        self.horizontalLayout_22.addLayout(self.verticalLayout_44)


        self.verticalLayout_34.addWidget(self.sixteenth_roll_bar)

        self.thirtysecond_pair_bar_2 = QWidget(self.pair_weights_widget)
        self.thirtysecond_pair_bar_2.setObjectName(u"thirtysecond_pair_bar_2")
        self.thirtysecond_pair_bar = QHBoxLayout(self.thirtysecond_pair_bar_2)
        self.thirtysecond_pair_bar.setObjectName(u"thirtysecond_pair_bar")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.thirtysecond_pair_display = QLabel(self.thirtysecond_pair_bar_2)
        self.thirtysecond_pair_display.setObjectName(u"thirtysecond_pair_display")
        self.thirtysecond_pair_display.setFont(font2)
        self.thirtysecond_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_49.addWidget(self.thirtysecond_pair_display)

        self.thirtysecond_pair_slider = QSlider(self.thirtysecond_pair_bar_2)
        self.thirtysecond_pair_slider.setObjectName(u"thirtysecond_pair_slider")
        self.thirtysecond_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.thirtysecond_pair_slider.setMinimum(0)
        self.thirtysecond_pair_slider.setMaximum(100)
        self.thirtysecond_pair_slider.setPageStep(5)
        self.thirtysecond_pair_slider.setValue(9)
        self.thirtysecond_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_49.addWidget(self.thirtysecond_pair_slider)


        self.thirtysecond_pair_bar.addLayout(self.verticalLayout_49)

        self.dotted_13 = QLabel(self.thirtysecond_pair_bar_2)
        self.dotted_13.setObjectName(u"dotted_13")
        sizePolicy6.setHeightForWidth(self.dotted_13.sizePolicy().hasHeightForWidth())
        self.dotted_13.setSizePolicy(sizePolicy6)
        self.dotted_13.setMinimumSize(QSize(50, 50))
        self.dotted_13.setMaximumSize(QSize(50, 50))
        self.dotted_13.setFont(font2)
        self.dotted_13.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_13.setScaledContents(True)
        self.dotted_13.setWordWrap(True)

        self.thirtysecond_pair_bar.addWidget(self.dotted_13)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.dthirtysecond_pair_display = QLabel(self.thirtysecond_pair_bar_2)
        self.dthirtysecond_pair_display.setObjectName(u"dthirtysecond_pair_display")
        self.dthirtysecond_pair_display.setEnabled(True)
        self.dthirtysecond_pair_display.setFont(font2)
        self.dthirtysecond_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_50.addWidget(self.dthirtysecond_pair_display)

        self.dthirtysecond_pair_slider = QSlider(self.thirtysecond_pair_bar_2)
        self.dthirtysecond_pair_slider.setObjectName(u"dthirtysecond_pair_slider")
        self.dthirtysecond_pair_slider.setEnabled(True)
        self.dthirtysecond_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dthirtysecond_pair_slider.setMinimum(0)
        self.dthirtysecond_pair_slider.setMaximum(100)
        self.dthirtysecond_pair_slider.setPageStep(5)
        self.dthirtysecond_pair_slider.setValue(9)
        self.dthirtysecond_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_50.addWidget(self.dthirtysecond_pair_slider)


        self.thirtysecond_pair_bar.addLayout(self.verticalLayout_50)


        self.verticalLayout_34.addWidget(self.thirtysecond_pair_bar_2)

        self.sixtyfourth_pair_bar_2 = QWidget(self.pair_weights_widget)
        self.sixtyfourth_pair_bar_2.setObjectName(u"sixtyfourth_pair_bar_2")
        self.sixtyfourth_pair_bar = QHBoxLayout(self.sixtyfourth_pair_bar_2)
        self.sixtyfourth_pair_bar.setObjectName(u"sixtyfourth_pair_bar")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.sixtyfourth_pair_display = QLabel(self.sixtyfourth_pair_bar_2)
        self.sixtyfourth_pair_display.setObjectName(u"sixtyfourth_pair_display")
        self.sixtyfourth_pair_display.setFont(font2)
        self.sixtyfourth_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_51.addWidget(self.sixtyfourth_pair_display)

        self.sixtyfourth_pair_slider = QSlider(self.sixtyfourth_pair_bar_2)
        self.sixtyfourth_pair_slider.setObjectName(u"sixtyfourth_pair_slider")
        self.sixtyfourth_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.sixtyfourth_pair_slider.setMinimum(0)
        self.sixtyfourth_pair_slider.setMaximum(100)
        self.sixtyfourth_pair_slider.setPageStep(5)
        self.sixtyfourth_pair_slider.setValue(9)
        self.sixtyfourth_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_51.addWidget(self.sixtyfourth_pair_slider)


        self.sixtyfourth_pair_bar.addLayout(self.verticalLayout_51)

        self.dotted_14 = QLabel(self.sixtyfourth_pair_bar_2)
        self.dotted_14.setObjectName(u"dotted_14")
        sizePolicy6.setHeightForWidth(self.dotted_14.sizePolicy().hasHeightForWidth())
        self.dotted_14.setSizePolicy(sizePolicy6)
        self.dotted_14.setMinimumSize(QSize(50, 50))
        self.dotted_14.setMaximumSize(QSize(50, 50))
        self.dotted_14.setFont(font2)
        self.dotted_14.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_14.setScaledContents(True)
        self.dotted_14.setWordWrap(True)

        self.sixtyfourth_pair_bar.addWidget(self.dotted_14)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.dsixtyfourth_pair_display = QLabel(self.sixtyfourth_pair_bar_2)
        self.dsixtyfourth_pair_display.setObjectName(u"dsixtyfourth_pair_display")
        self.dsixtyfourth_pair_display.setEnabled(True)
        self.dsixtyfourth_pair_display.setFont(font2)
        self.dsixtyfourth_pair_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.verticalLayout_52.addWidget(self.dsixtyfourth_pair_display)

        self.dsixtyfourth_pair_slider = QSlider(self.sixtyfourth_pair_bar_2)
        self.dsixtyfourth_pair_slider.setObjectName(u"dsixtyfourth_pair_slider")
        self.dsixtyfourth_pair_slider.setEnabled(True)
        self.dsixtyfourth_pair_slider.setStyleSheet(u"QSlider {\n"
"	selection-background-color: rgb(137, 137, 206);\n"
"}")
        self.dsixtyfourth_pair_slider.setMinimum(0)
        self.dsixtyfourth_pair_slider.setMaximum(100)
        self.dsixtyfourth_pair_slider.setPageStep(5)
        self.dsixtyfourth_pair_slider.setValue(9)
        self.dsixtyfourth_pair_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_52.addWidget(self.dsixtyfourth_pair_slider)


        self.sixtyfourth_pair_bar.addLayout(self.verticalLayout_52)


        self.verticalLayout_34.addWidget(self.sixtyfourth_pair_bar_2)


        self.horizontalLayout_12.addWidget(self.pair_weights_widget)

        self.pair_len_weights_widget = QWidget(self.weights_widget)
        self.pair_len_weights_widget.setObjectName(u"pair_len_weights_widget")
        sizePolicy15 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.pair_len_weights_widget.sizePolicy().hasHeightForWidth())
        self.pair_len_weights_widget.setSizePolicy(sizePolicy15)
        self.pair_len_weights_widget.setMaximumSize(QSize(280, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.pair_len_weights_widget)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pair_len_label = QLabel(self.pair_len_weights_widget)
        self.pair_len_label.setObjectName(u"pair_len_label")
        sizePolicy1.setHeightForWidth(self.pair_len_label.sizePolicy().hasHeightForWidth())
        self.pair_len_label.setSizePolicy(sizePolicy1)
        self.pair_len_label.setMaximumSize(QSize(16777215, 40))
        self.pair_len_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.pair_len_label)

        self.dotted_15 = QLabel(self.pair_len_weights_widget)
        self.dotted_15.setObjectName(u"dotted_15")
        sizePolicy4.setHeightForWidth(self.dotted_15.sizePolicy().hasHeightForWidth())
        self.dotted_15.setSizePolicy(sizePolicy4)
        self.dotted_15.setMinimumSize(QSize(50, 50))
        self.dotted_15.setMaximumSize(QSize(16777215, 16777215))
        self.dotted_15.setFont(font2)
        self.dotted_15.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_15.setScaledContents(True)
        self.dotted_15.setAlignment(Qt.AlignCenter)
        self.dotted_15.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.dotted_15)

        self.dotted_16 = QLabel(self.pair_len_weights_widget)
        self.dotted_16.setObjectName(u"dotted_16")
        sizePolicy4.setHeightForWidth(self.dotted_16.sizePolicy().hasHeightForWidth())
        self.dotted_16.setSizePolicy(sizePolicy4)
        self.dotted_16.setMinimumSize(QSize(50, 50))
        self.dotted_16.setMaximumSize(QSize(16777215, 16777215))
        self.dotted_16.setFont(font2)
        self.dotted_16.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.dotted_16.setScaledContents(True)
        self.dotted_16.setAlignment(Qt.AlignCenter)
        self.dotted_16.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.dotted_16)

        self.pair_lens_labels = QWidget(self.pair_len_weights_widget)
        self.pair_lens_labels.setObjectName(u"pair_lens_labels")
        sizePolicy4.setHeightForWidth(self.pair_lens_labels.sizePolicy().hasHeightForWidth())
        self.pair_lens_labels.setSizePolicy(sizePolicy4)
        self.pair_lens_labels.setMinimumSize(QSize(50, 50))
        self.pair_lens_labels.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.pair_lens_labels)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.pair_lens_labels)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setUnderline(False)
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_8 = QLabel(self.pair_lens_labels)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_6 = QLabel(self.pair_lens_labels)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.pair_lens_labels)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_9 = QLabel(self.pair_lens_labels)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_10 = QLabel(self.pair_lens_labels)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_11 = QLabel(self.pair_lens_labels)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_11)


        self.verticalLayout_6.addWidget(self.pair_lens_labels)

        self.eighth_pair_len_bar = QWidget(self.pair_len_weights_widget)
        self.eighth_pair_len_bar.setObjectName(u"eighth_pair_len_bar")
        sizePolicy4.setHeightForWidth(self.eighth_pair_len_bar.sizePolicy().hasHeightForWidth())
        self.eighth_pair_len_bar.setSizePolicy(sizePolicy4)
        self.horizontalLayout_5 = QHBoxLayout(self.eighth_pair_len_bar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.eighth_len_two = QLineEdit(self.eighth_pair_len_bar)
        self.eighth_len_two.setObjectName(u"eighth_len_two")
        sizePolicy7.setHeightForWidth(self.eighth_len_two.sizePolicy().hasHeightForWidth())
        self.eighth_len_two.setSizePolicy(sizePolicy7)
        self.eighth_len_two.setMinimumSize(QSize(36, 26))
        self.eighth_len_two.setMaximumSize(QSize(40, 16777215))
        self.eighth_len_two.setFont(font1)
        self.eighth_len_two.setStyleSheet(u"")
        self.eighth_len_two.setCursorPosition(0)
        self.eighth_len_two.setAlignment(Qt.AlignCenter)
        self.eighth_len_two.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.eighth_len_two)

        self.eighth_len_three = QLineEdit(self.eighth_pair_len_bar)
        self.eighth_len_three.setObjectName(u"eighth_len_three")
        sizePolicy7.setHeightForWidth(self.eighth_len_three.sizePolicy().hasHeightForWidth())
        self.eighth_len_three.setSizePolicy(sizePolicy7)
        self.eighth_len_three.setMinimumSize(QSize(36, 26))
        self.eighth_len_three.setMaximumSize(QSize(40, 16777215))
        self.eighth_len_three.setFont(font1)
        self.eighth_len_three.setStyleSheet(u"")
        self.eighth_len_three.setMaxLength(2)
        self.eighth_len_three.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.eighth_len_three)

        self.eighth_len_four = QLineEdit(self.eighth_pair_len_bar)
        self.eighth_len_four.setObjectName(u"eighth_len_four")
        sizePolicy7.setHeightForWidth(self.eighth_len_four.sizePolicy().hasHeightForWidth())
        self.eighth_len_four.setSizePolicy(sizePolicy7)
        self.eighth_len_four.setMinimumSize(QSize(36, 26))
        self.eighth_len_four.setMaximumSize(QSize(40, 16777215))
        self.eighth_len_four.setFont(font1)
        self.eighth_len_four.setStyleSheet(u"")
        self.eighth_len_four.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.eighth_len_four)

        self.eighth_len_five = QLineEdit(self.eighth_pair_len_bar)
        self.eighth_len_five.setObjectName(u"eighth_len_five")
        sizePolicy7.setHeightForWidth(self.eighth_len_five.sizePolicy().hasHeightForWidth())
        self.eighth_len_five.setSizePolicy(sizePolicy7)
        self.eighth_len_five.setMinimumSize(QSize(36, 26))
        self.eighth_len_five.setMaximumSize(QSize(40, 16777215))
        self.eighth_len_five.setFont(font1)
        self.eighth_len_five.setStyleSheet(u"")
        self.eighth_len_five.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.eighth_len_five)

        self.eighth_len_six = QLineEdit(self.eighth_pair_len_bar)
        self.eighth_len_six.setObjectName(u"eighth_len_six")
        sizePolicy7.setHeightForWidth(self.eighth_len_six.sizePolicy().hasHeightForWidth())
        self.eighth_len_six.setSizePolicy(sizePolicy7)
        self.eighth_len_six.setMinimumSize(QSize(36, 26))
        self.eighth_len_six.setMaximumSize(QSize(40, 16777215))
        self.eighth_len_six.setFont(font1)
        self.eighth_len_six.setStyleSheet(u"")
        self.eighth_len_six.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.eighth_len_six)

        self.eighth_len_seven = QLineEdit(self.eighth_pair_len_bar)
        self.eighth_len_seven.setObjectName(u"eighth_len_seven")
        sizePolicy7.setHeightForWidth(self.eighth_len_seven.sizePolicy().hasHeightForWidth())
        self.eighth_len_seven.setSizePolicy(sizePolicy7)
        self.eighth_len_seven.setMinimumSize(QSize(36, 26))
        self.eighth_len_seven.setMaximumSize(QSize(40, 16777215))
        self.eighth_len_seven.setFont(font1)
        self.eighth_len_seven.setStyleSheet(u"")
        self.eighth_len_seven.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.eighth_len_seven)

        self.eighth_len_eight = QLineEdit(self.eighth_pair_len_bar)
        self.eighth_len_eight.setObjectName(u"eighth_len_eight")
        sizePolicy7.setHeightForWidth(self.eighth_len_eight.sizePolicy().hasHeightForWidth())
        self.eighth_len_eight.setSizePolicy(sizePolicy7)
        self.eighth_len_eight.setMinimumSize(QSize(36, 26))
        self.eighth_len_eight.setMaximumSize(QSize(40, 16777215))
        self.eighth_len_eight.setFont(font1)
        self.eighth_len_eight.setStyleSheet(u"")
        self.eighth_len_eight.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.eighth_len_eight)


        self.verticalLayout_6.addWidget(self.eighth_pair_len_bar)

        self.sixteenth_pair_len_bar = QWidget(self.pair_len_weights_widget)
        self.sixteenth_pair_len_bar.setObjectName(u"sixteenth_pair_len_bar")
        self.horizontalLayout_6 = QHBoxLayout(self.sixteenth_pair_len_bar)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sixteenth_len_one = QLineEdit(self.sixteenth_pair_len_bar)
        self.sixteenth_len_one.setObjectName(u"sixteenth_len_one")
        sizePolicy7.setHeightForWidth(self.sixteenth_len_one.sizePolicy().hasHeightForWidth())
        self.sixteenth_len_one.setSizePolicy(sizePolicy7)
        self.sixteenth_len_one.setMinimumSize(QSize(36, 26))
        self.sixteenth_len_one.setMaximumSize(QSize(40, 16777215))
        self.sixteenth_len_one.setFont(font1)
        self.sixteenth_len_one.setStyleSheet(u"")
        self.sixteenth_len_one.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.sixteenth_len_one)

        self.sixteenth_len_three = QLineEdit(self.sixteenth_pair_len_bar)
        self.sixteenth_len_three.setObjectName(u"sixteenth_len_three")
        sizePolicy7.setHeightForWidth(self.sixteenth_len_three.sizePolicy().hasHeightForWidth())
        self.sixteenth_len_three.setSizePolicy(sizePolicy7)
        self.sixteenth_len_three.setMinimumSize(QSize(36, 26))
        self.sixteenth_len_three.setMaximumSize(QSize(40, 16777215))
        self.sixteenth_len_three.setFont(font1)
        self.sixteenth_len_three.setStyleSheet(u"")
        self.sixteenth_len_three.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.sixteenth_len_three)

        self.sixteenth_len_four = QLineEdit(self.sixteenth_pair_len_bar)
        self.sixteenth_len_four.setObjectName(u"sixteenth_len_four")
        sizePolicy7.setHeightForWidth(self.sixteenth_len_four.sizePolicy().hasHeightForWidth())
        self.sixteenth_len_four.setSizePolicy(sizePolicy7)
        self.sixteenth_len_four.setMinimumSize(QSize(36, 26))
        self.sixteenth_len_four.setMaximumSize(QSize(40, 16777215))
        self.sixteenth_len_four.setFont(font1)
        self.sixteenth_len_four.setStyleSheet(u"")
        self.sixteenth_len_four.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.sixteenth_len_four)

        self.sixteenth_len_five = QLineEdit(self.sixteenth_pair_len_bar)
        self.sixteenth_len_five.setObjectName(u"sixteenth_len_five")
        sizePolicy7.setHeightForWidth(self.sixteenth_len_five.sizePolicy().hasHeightForWidth())
        self.sixteenth_len_five.setSizePolicy(sizePolicy7)
        self.sixteenth_len_five.setMinimumSize(QSize(36, 26))
        self.sixteenth_len_five.setMaximumSize(QSize(40, 16777215))
        self.sixteenth_len_five.setFont(font1)
        self.sixteenth_len_five.setStyleSheet(u"")
        self.sixteenth_len_five.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.sixteenth_len_five)

        self.sixteenth_len_six = QLineEdit(self.sixteenth_pair_len_bar)
        self.sixteenth_len_six.setObjectName(u"sixteenth_len_six")
        sizePolicy7.setHeightForWidth(self.sixteenth_len_six.sizePolicy().hasHeightForWidth())
        self.sixteenth_len_six.setSizePolicy(sizePolicy7)
        self.sixteenth_len_six.setMinimumSize(QSize(36, 26))
        self.sixteenth_len_six.setMaximumSize(QSize(40, 16777215))
        self.sixteenth_len_six.setFont(font1)
        self.sixteenth_len_six.setStyleSheet(u"")
        self.sixteenth_len_six.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.sixteenth_len_six)

        self.sixteenth_len_seven = QLineEdit(self.sixteenth_pair_len_bar)
        self.sixteenth_len_seven.setObjectName(u"sixteenth_len_seven")
        sizePolicy7.setHeightForWidth(self.sixteenth_len_seven.sizePolicy().hasHeightForWidth())
        self.sixteenth_len_seven.setSizePolicy(sizePolicy7)
        self.sixteenth_len_seven.setMinimumSize(QSize(36, 26))
        self.sixteenth_len_seven.setMaximumSize(QSize(40, 16777215))
        self.sixteenth_len_seven.setFont(font1)
        self.sixteenth_len_seven.setStyleSheet(u"")
        self.sixteenth_len_seven.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.sixteenth_len_seven)

        self.sixteenth_len_eight = QLineEdit(self.sixteenth_pair_len_bar)
        self.sixteenth_len_eight.setObjectName(u"sixteenth_len_eight")
        sizePolicy7.setHeightForWidth(self.sixteenth_len_eight.sizePolicy().hasHeightForWidth())
        self.sixteenth_len_eight.setSizePolicy(sizePolicy7)
        self.sixteenth_len_eight.setMinimumSize(QSize(36, 26))
        self.sixteenth_len_eight.setMaximumSize(QSize(40, 16777215))
        self.sixteenth_len_eight.setFont(font1)
        self.sixteenth_len_eight.setStyleSheet(u"")
        self.sixteenth_len_eight.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.sixteenth_len_eight)


        self.verticalLayout_6.addWidget(self.sixteenth_pair_len_bar)

        self.thirtysecond_pair_len_bar = QWidget(self.pair_len_weights_widget)
        self.thirtysecond_pair_len_bar.setObjectName(u"thirtysecond_pair_len_bar")
        self.horizontalLayout_7 = QHBoxLayout(self.thirtysecond_pair_len_bar)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.thirtysecond_len_two = QLineEdit(self.thirtysecond_pair_len_bar)
        self.thirtysecond_len_two.setObjectName(u"thirtysecond_len_two")
        sizePolicy7.setHeightForWidth(self.thirtysecond_len_two.sizePolicy().hasHeightForWidth())
        self.thirtysecond_len_two.setSizePolicy(sizePolicy7)
        self.thirtysecond_len_two.setMinimumSize(QSize(36, 26))
        self.thirtysecond_len_two.setMaximumSize(QSize(40, 16777215))
        self.thirtysecond_len_two.setFont(font1)
        self.thirtysecond_len_two.setStyleSheet(u"")
        self.thirtysecond_len_two.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.thirtysecond_len_two)

        self.thirtysecond_len_three = QLineEdit(self.thirtysecond_pair_len_bar)
        self.thirtysecond_len_three.setObjectName(u"thirtysecond_len_three")
        sizePolicy7.setHeightForWidth(self.thirtysecond_len_three.sizePolicy().hasHeightForWidth())
        self.thirtysecond_len_three.setSizePolicy(sizePolicy7)
        self.thirtysecond_len_three.setMinimumSize(QSize(36, 26))
        self.thirtysecond_len_three.setMaximumSize(QSize(40, 16777215))
        self.thirtysecond_len_three.setFont(font1)
        self.thirtysecond_len_three.setStyleSheet(u"")
        self.thirtysecond_len_three.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.thirtysecond_len_three)

        self.thirtysecond_len_four = QLineEdit(self.thirtysecond_pair_len_bar)
        self.thirtysecond_len_four.setObjectName(u"thirtysecond_len_four")
        sizePolicy7.setHeightForWidth(self.thirtysecond_len_four.sizePolicy().hasHeightForWidth())
        self.thirtysecond_len_four.setSizePolicy(sizePolicy7)
        self.thirtysecond_len_four.setMinimumSize(QSize(36, 26))
        self.thirtysecond_len_four.setMaximumSize(QSize(40, 16777215))
        self.thirtysecond_len_four.setFont(font1)
        self.thirtysecond_len_four.setStyleSheet(u"")
        self.thirtysecond_len_four.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.thirtysecond_len_four)

        self.thirtysecond_len_five = QLineEdit(self.thirtysecond_pair_len_bar)
        self.thirtysecond_len_five.setObjectName(u"thirtysecond_len_five")
        sizePolicy7.setHeightForWidth(self.thirtysecond_len_five.sizePolicy().hasHeightForWidth())
        self.thirtysecond_len_five.setSizePolicy(sizePolicy7)
        self.thirtysecond_len_five.setMinimumSize(QSize(36, 26))
        self.thirtysecond_len_five.setMaximumSize(QSize(40, 16777215))
        self.thirtysecond_len_five.setFont(font1)
        self.thirtysecond_len_five.setStyleSheet(u"")
        self.thirtysecond_len_five.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.thirtysecond_len_five)

        self.thirtysecond_len_six = QLineEdit(self.thirtysecond_pair_len_bar)
        self.thirtysecond_len_six.setObjectName(u"thirtysecond_len_six")
        sizePolicy7.setHeightForWidth(self.thirtysecond_len_six.sizePolicy().hasHeightForWidth())
        self.thirtysecond_len_six.setSizePolicy(sizePolicy7)
        self.thirtysecond_len_six.setMinimumSize(QSize(36, 26))
        self.thirtysecond_len_six.setMaximumSize(QSize(40, 16777215))
        self.thirtysecond_len_six.setFont(font1)
        self.thirtysecond_len_six.setStyleSheet(u"")
        self.thirtysecond_len_six.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.thirtysecond_len_six)

        self.thirtysecond_len_seven = QLineEdit(self.thirtysecond_pair_len_bar)
        self.thirtysecond_len_seven.setObjectName(u"thirtysecond_len_seven")
        sizePolicy7.setHeightForWidth(self.thirtysecond_len_seven.sizePolicy().hasHeightForWidth())
        self.thirtysecond_len_seven.setSizePolicy(sizePolicy7)
        self.thirtysecond_len_seven.setMinimumSize(QSize(36, 26))
        self.thirtysecond_len_seven.setMaximumSize(QSize(40, 16777215))
        self.thirtysecond_len_seven.setFont(font1)
        self.thirtysecond_len_seven.setStyleSheet(u"")
        self.thirtysecond_len_seven.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.thirtysecond_len_seven)

        self.thirtysecond_len_eight = QLineEdit(self.thirtysecond_pair_len_bar)
        self.thirtysecond_len_eight.setObjectName(u"thirtysecond_len_eight")
        sizePolicy7.setHeightForWidth(self.thirtysecond_len_eight.sizePolicy().hasHeightForWidth())
        self.thirtysecond_len_eight.setSizePolicy(sizePolicy7)
        self.thirtysecond_len_eight.setMinimumSize(QSize(36, 26))
        self.thirtysecond_len_eight.setMaximumSize(QSize(40, 16777215))
        self.thirtysecond_len_eight.setFont(font1)
        self.thirtysecond_len_eight.setStyleSheet(u"")
        self.thirtysecond_len_eight.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.thirtysecond_len_eight)


        self.verticalLayout_6.addWidget(self.thirtysecond_pair_len_bar)

        self.sxityfourth_pair_len_bar = QWidget(self.pair_len_weights_widget)
        self.sxityfourth_pair_len_bar.setObjectName(u"sxityfourth_pair_len_bar")
        self.horizontalLayout_17 = QHBoxLayout(self.sxityfourth_pair_len_bar)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.sixtyfourth_timesig_two = QLineEdit(self.sxityfourth_pair_len_bar)
        self.sixtyfourth_timesig_two.setObjectName(u"sixtyfourth_timesig_two")
        sizePolicy7.setHeightForWidth(self.sixtyfourth_timesig_two.sizePolicy().hasHeightForWidth())
        self.sixtyfourth_timesig_two.setSizePolicy(sizePolicy7)
        self.sixtyfourth_timesig_two.setMinimumSize(QSize(36, 26))
        self.sixtyfourth_timesig_two.setMaximumSize(QSize(40, 16777215))
        self.sixtyfourth_timesig_two.setFont(font1)
        self.sixtyfourth_timesig_two.setStyleSheet(u"")
        self.sixtyfourth_timesig_two.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.sixtyfourth_timesig_two)

        self.sixtyfourth_timesig_three = QLineEdit(self.sxityfourth_pair_len_bar)
        self.sixtyfourth_timesig_three.setObjectName(u"sixtyfourth_timesig_three")
        sizePolicy7.setHeightForWidth(self.sixtyfourth_timesig_three.sizePolicy().hasHeightForWidth())
        self.sixtyfourth_timesig_three.setSizePolicy(sizePolicy7)
        self.sixtyfourth_timesig_three.setMinimumSize(QSize(36, 26))
        self.sixtyfourth_timesig_three.setMaximumSize(QSize(40, 16777215))
        self.sixtyfourth_timesig_three.setFont(font1)
        self.sixtyfourth_timesig_three.setStyleSheet(u"")
        self.sixtyfourth_timesig_three.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.sixtyfourth_timesig_three)

        self.sixtyfourth_timesig_four = QLineEdit(self.sxityfourth_pair_len_bar)
        self.sixtyfourth_timesig_four.setObjectName(u"sixtyfourth_timesig_four")
        sizePolicy7.setHeightForWidth(self.sixtyfourth_timesig_four.sizePolicy().hasHeightForWidth())
        self.sixtyfourth_timesig_four.setSizePolicy(sizePolicy7)
        self.sixtyfourth_timesig_four.setMinimumSize(QSize(36, 26))
        self.sixtyfourth_timesig_four.setMaximumSize(QSize(40, 16777215))
        self.sixtyfourth_timesig_four.setFont(font1)
        self.sixtyfourth_timesig_four.setStyleSheet(u"")
        self.sixtyfourth_timesig_four.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.sixtyfourth_timesig_four)

        self.sixtyfourth_timesig_five = QLineEdit(self.sxityfourth_pair_len_bar)
        self.sixtyfourth_timesig_five.setObjectName(u"sixtyfourth_timesig_five")
        sizePolicy7.setHeightForWidth(self.sixtyfourth_timesig_five.sizePolicy().hasHeightForWidth())
        self.sixtyfourth_timesig_five.setSizePolicy(sizePolicy7)
        self.sixtyfourth_timesig_five.setMinimumSize(QSize(36, 26))
        self.sixtyfourth_timesig_five.setMaximumSize(QSize(40, 16777215))
        self.sixtyfourth_timesig_five.setFont(font1)
        self.sixtyfourth_timesig_five.setStyleSheet(u"")
        self.sixtyfourth_timesig_five.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.sixtyfourth_timesig_five)

        self.sixtyfourth_timesig_six = QLineEdit(self.sxityfourth_pair_len_bar)
        self.sixtyfourth_timesig_six.setObjectName(u"sixtyfourth_timesig_six")
        sizePolicy7.setHeightForWidth(self.sixtyfourth_timesig_six.sizePolicy().hasHeightForWidth())
        self.sixtyfourth_timesig_six.setSizePolicy(sizePolicy7)
        self.sixtyfourth_timesig_six.setMinimumSize(QSize(36, 26))
        self.sixtyfourth_timesig_six.setMaximumSize(QSize(40, 16777215))
        self.sixtyfourth_timesig_six.setFont(font1)
        self.sixtyfourth_timesig_six.setStyleSheet(u"")
        self.sixtyfourth_timesig_six.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.sixtyfourth_timesig_six)

        self.sixtyfourth_timesig_seven = QLineEdit(self.sxityfourth_pair_len_bar)
        self.sixtyfourth_timesig_seven.setObjectName(u"sixtyfourth_timesig_seven")
        sizePolicy7.setHeightForWidth(self.sixtyfourth_timesig_seven.sizePolicy().hasHeightForWidth())
        self.sixtyfourth_timesig_seven.setSizePolicy(sizePolicy7)
        self.sixtyfourth_timesig_seven.setMinimumSize(QSize(36, 26))
        self.sixtyfourth_timesig_seven.setMaximumSize(QSize(40, 16777215))
        self.sixtyfourth_timesig_seven.setFont(font1)
        self.sixtyfourth_timesig_seven.setStyleSheet(u"")
        self.sixtyfourth_timesig_seven.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.sixtyfourth_timesig_seven)

        self.sixtyfourth_timesig_eight = QLineEdit(self.sxityfourth_pair_len_bar)
        self.sixtyfourth_timesig_eight.setObjectName(u"sixtyfourth_timesig_eight")
        sizePolicy7.setHeightForWidth(self.sixtyfourth_timesig_eight.sizePolicy().hasHeightForWidth())
        self.sixtyfourth_timesig_eight.setSizePolicy(sizePolicy7)
        self.sixtyfourth_timesig_eight.setMinimumSize(QSize(36, 26))
        self.sixtyfourth_timesig_eight.setMaximumSize(QSize(40, 16777215))
        self.sixtyfourth_timesig_eight.setFont(font1)
        self.sixtyfourth_timesig_eight.setStyleSheet(u"")
        self.sixtyfourth_timesig_eight.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.sixtyfourth_timesig_eight)


        self.verticalLayout_6.addWidget(self.sxityfourth_pair_len_bar)


        self.horizontalLayout_12.addWidget(self.pair_len_weights_widget)


        self.verticalLayout_5.addWidget(self.weights_widget)


        self.verticalLayout_13.addWidget(self.weights_arch_widget)

        self.style_stack.addWidget(self.rhythm_page)
        self.pitch_page = QWidget()
        self.pitch_page.setObjectName(u"pitch_page")
        self.verticalLayout_11 = QVBoxLayout(self.pitch_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.keysig_arch_widget = QWidget(self.pitch_page)
        self.keysig_arch_widget.setObjectName(u"keysig_arch_widget")
        self.horizontalLayout_32 = QHBoxLayout(self.keysig_arch_widget)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.keysig_widget = QWidget(self.keysig_arch_widget)
        self.keysig_widget.setObjectName(u"keysig_widget")
        sizePolicy16 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy16.setHorizontalStretch(1)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.keysig_widget.sizePolicy().hasHeightForWidth())
        self.keysig_widget.setSizePolicy(sizePolicy16)
        self.verticalLayout_23 = QVBoxLayout(self.keysig_widget)
        self.verticalLayout_23.setSpacing(12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.keysig_widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(0, 34))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_23.addWidget(self.label_3)

        self.keysig_component_bar = QWidget(self.keysig_widget)
        self.keysig_component_bar.setObjectName(u"keysig_component_bar")
        self.horizontalLayout_33 = QHBoxLayout(self.keysig_component_bar)
        self.horizontalLayout_33.setSpacing(6)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.keysig_pitch_combo = QComboBox(self.keysig_component_bar)
        self.keysig_pitch_combo.addItem("")
        self.keysig_pitch_combo.addItem("")
        self.keysig_pitch_combo.addItem("")
        self.keysig_pitch_combo.addItem("")
        self.keysig_pitch_combo.addItem("")
        self.keysig_pitch_combo.addItem("")
        self.keysig_pitch_combo.addItem("")
        self.keysig_pitch_combo.setObjectName(u"keysig_pitch_combo")
        self.keysig_pitch_combo.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setPointSize(10)
        self.keysig_pitch_combo.setFont(font5)

        self.horizontalLayout_33.addWidget(self.keysig_pitch_combo)

        self.keysig_acc_combo = QComboBox(self.keysig_component_bar)
        self.keysig_acc_combo.addItem("")
        self.keysig_acc_combo.addItem("")
        self.keysig_acc_combo.addItem("")
        self.keysig_acc_combo.setObjectName(u"keysig_acc_combo")
        self.keysig_acc_combo.setMinimumSize(QSize(0, 40))
        self.keysig_acc_combo.setFont(font5)

        self.horizontalLayout_33.addWidget(self.keysig_acc_combo)

        self.keysig_scale_combo = QComboBox(self.keysig_component_bar)
        self.keysig_scale_combo.addItem("")
        self.keysig_scale_combo.addItem("")
        self.keysig_scale_combo.addItem("")
        self.keysig_scale_combo.addItem("")
        self.keysig_scale_combo.setObjectName(u"keysig_scale_combo")
        self.keysig_scale_combo.setMinimumSize(QSize(0, 40))
        self.keysig_scale_combo.setFont(font5)

        self.horizontalLayout_33.addWidget(self.keysig_scale_combo)


        self.verticalLayout_23.addWidget(self.keysig_component_bar)

        self.atonal_check = QCheckBox(self.keysig_widget)
        self.atonal_check.setObjectName(u"atonal_check")
        self.atonal_check.setFont(font1)

        self.verticalLayout_23.addWidget(self.atonal_check)


        self.horizontalLayout_32.addWidget(self.keysig_widget)

        self.keysig_spacewidget = QWidget(self.keysig_arch_widget)
        self.keysig_spacewidget.setObjectName(u"keysig_spacewidget")
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy17.setHorizontalStretch(5)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.keysig_spacewidget.sizePolicy().hasHeightForWidth())
        self.keysig_spacewidget.setSizePolicy(sizePolicy17)

        self.horizontalLayout_32.addWidget(self.keysig_spacewidget)


        self.verticalLayout_11.addWidget(self.keysig_arch_widget)

        self.anchors_ranges_arch_widget = QWidget(self.pitch_page)
        self.anchors_ranges_arch_widget.setObjectName(u"anchors_ranges_arch_widget")
        sizePolicy4.setHeightForWidth(self.anchors_ranges_arch_widget.sizePolicy().hasHeightForWidth())
        self.anchors_ranges_arch_widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_4 = QHBoxLayout(self.anchors_ranges_arch_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ranges_widget = QWidget(self.anchors_ranges_arch_widget)
        self.ranges_widget.setObjectName(u"ranges_widget")
        sizePolicy18 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy18.setHorizontalStretch(6)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.ranges_widget.sizePolicy().hasHeightForWidth())
        self.ranges_widget.setSizePolicy(sizePolicy18)
        self.ranges_widget.setMaximumSize(QSize(1000, 475))
        self.ranges_widget.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.ranges_widget)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(4, 0, 4, 4)
        self.ranges_accent_bar_2 = QWidget(self.ranges_widget)
        self.ranges_accent_bar_2.setObjectName(u"ranges_accent_bar_2")
        sizePolicy1.setHeightForWidth(self.ranges_accent_bar_2.sizePolicy().hasHeightForWidth())
        self.ranges_accent_bar_2.setSizePolicy(sizePolicy1)
        self.ranges_accent_bar_2.setMaximumSize(QSize(16777215, 40))
        self.ranges_accent_bar_2.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.ranges_accent_bar_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ranges_label_2 = QLabel(self.ranges_accent_bar_2)
        self.ranges_label_2.setObjectName(u"ranges_label_2")
        sizePolicy4.setHeightForWidth(self.ranges_label_2.sizePolicy().hasHeightForWidth())
        self.ranges_label_2.setSizePolicy(sizePolicy4)
        self.ranges_label_2.setMaximumSize(QSize(16777215, 16777215))
        self.ranges_label_2.setFont(font2)
        self.ranges_label_2.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")
        self.ranges_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.ranges_label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.sharp_ranges = QPushButton(self.ranges_accent_bar_2)
        self.sharp_ranges.setObjectName(u"sharp_ranges")
        sizePolicy6.setHeightForWidth(self.sharp_ranges.sizePolicy().hasHeightForWidth())
        self.sharp_ranges.setSizePolicy(sizePolicy6)
        self.sharp_ranges.setMinimumSize(QSize(30, 30))
        self.sharp_ranges.setMaximumSize(QSize(60, 60))
        font6 = QFont()
        font6.setPointSize(14)
        self.sharp_ranges.setFont(font6)
        self.sharp_ranges.setStyleSheet(u"QPushButton {\n"
"	padding: 0 0 4 0;\n"
"}")
        self.sharp_ranges.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.sharp_ranges)

        self.flat_ranges = QPushButton(self.ranges_accent_bar_2)
        self.flat_ranges.setObjectName(u"flat_ranges")
        sizePolicy4.setHeightForWidth(self.flat_ranges.sizePolicy().hasHeightForWidth())
        self.flat_ranges.setSizePolicy(sizePolicy4)
        self.flat_ranges.setMinimumSize(QSize(30, 30))
        self.flat_ranges.setMaximumSize(QSize(60, 60))
        self.flat_ranges.setFont(font6)
        self.flat_ranges.setStyleSheet(u"QPushButton {\n"
"	padding: 0 0 4 0;\n"
"}")
        self.flat_ranges.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.flat_ranges)


        self.verticalLayout_15.addWidget(self.ranges_accent_bar_2)

        self.right_ranges_box_2 = QWidget(self.ranges_widget)
        self.right_ranges_box_2.setObjectName(u"right_ranges_box_2")
        self.verticalLayout_17 = QVBoxLayout(self.right_ranges_box_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.right_range_labels_bar_2 = QWidget(self.right_ranges_box_2)
        self.right_range_labels_bar_2.setObjectName(u"right_range_labels_bar_2")
        sizePolicy1.setHeightForWidth(self.right_range_labels_bar_2.sizePolicy().hasHeightForWidth())
        self.right_range_labels_bar_2.setSizePolicy(sizePolicy1)
        self.right_range_labels_bar_2.setMinimumSize(QSize(0, 30))
        self.right_range_labels_bar_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_10 = QHBoxLayout(self.right_range_labels_bar_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.right_range_label = QLabel(self.right_range_labels_bar_2)
        self.right_range_label.setObjectName(u"right_range_label")
        sizePolicy5.setHeightForWidth(self.right_range_label.sizePolicy().hasHeightForWidth())
        self.right_range_label.setSizePolicy(sizePolicy5)
        self.right_range_label.setMaximumSize(QSize(16777215, 30))
        self.right_range_label.setFont(font2)
        self.right_range_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.horizontalLayout_10.addWidget(self.right_range_label)

        self.right_lower_display = QLabel(self.right_range_labels_bar_2)
        self.right_lower_display.setObjectName(u"right_lower_display")
        sizePolicy5.setHeightForWidth(self.right_lower_display.sizePolicy().hasHeightForWidth())
        self.right_lower_display.setSizePolicy(sizePolicy5)
        self.right_lower_display.setMaximumSize(QSize(16777215, 30))
        self.right_lower_display.setFont(font2)
        self.right_lower_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.horizontalLayout_10.addWidget(self.right_lower_display)

        self.dash_3 = QLabel(self.right_range_labels_bar_2)
        self.dash_3.setObjectName(u"dash_3")
        sizePolicy5.setHeightForWidth(self.dash_3.sizePolicy().hasHeightForWidth())
        self.dash_3.setSizePolicy(sizePolicy5)
        self.dash_3.setMaximumSize(QSize(16777215, 30))
        self.dash_3.setFont(font2)
        self.dash_3.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.horizontalLayout_10.addWidget(self.dash_3)

        self.right_upper_display = QLabel(self.right_range_labels_bar_2)
        self.right_upper_display.setObjectName(u"right_upper_display")
        sizePolicy5.setHeightForWidth(self.right_upper_display.sizePolicy().hasHeightForWidth())
        self.right_upper_display.setSizePolicy(sizePolicy5)
        self.right_upper_display.setMaximumSize(QSize(16777215, 30))
        self.right_upper_display.setFont(font2)
        self.right_upper_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"}")

        self.horizontalLayout_10.addWidget(self.right_upper_display)

        self.length_label_5 = QLabel(self.right_range_labels_bar_2)
        self.length_label_5.setObjectName(u"length_label_5")
        sizePolicy5.setHeightForWidth(self.length_label_5.sizePolicy().hasHeightForWidth())
        self.length_label_5.setSizePolicy(sizePolicy5)
        self.length_label_5.setMinimumSize(QSize(0, 0))
        self.length_label_5.setMaximumSize(QSize(16777215, 30))
        self.length_label_5.setFont(font2)
        self.length_label_5.setMouseTracking(False)
        self.length_label_5.setStyleSheet(u"color: rgb(137, 137, 206);")
        self.length_label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.length_label_5.setWordWrap(False)
        self.length_label_5.setMargin(0)

        self.horizontalLayout_10.addWidget(self.length_label_5)

        self.right_span_display = QLabel(self.right_range_labels_bar_2)
        self.right_span_display.setObjectName(u"right_span_display")
        sizePolicy5.setHeightForWidth(self.right_span_display.sizePolicy().hasHeightForWidth())
        self.right_span_display.setSizePolicy(sizePolicy5)
        self.right_span_display.setMaximumSize(QSize(16777215, 30))
        self.right_span_display.setFont(font2)
        self.right_span_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.horizontalLayout_10.addWidget(self.right_span_display)


        self.verticalLayout_17.addWidget(self.right_range_labels_bar_2)

        self.rh_range1_box_2 = QVBoxLayout()
        self.rh_range1_box_2.setObjectName(u"rh_range1_box_2")
        self.rh_range1_note_display_2 = QHBoxLayout()
        self.rh_range1_note_display_2.setObjectName(u"rh_range1_note_display_2")
        self.right_lower_label = QLabel(self.right_ranges_box_2)
        self.right_lower_label.setObjectName(u"right_lower_label")
        self.right_lower_label.setFont(font2)
        self.right_lower_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.rh_range1_note_display_2.addWidget(self.right_lower_label)

        self.rh_range1_spacerr_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rh_range1_note_display_2.addItem(self.rh_range1_spacerr_2)


        self.rh_range1_box_2.addLayout(self.rh_range1_note_display_2)

        self.right_lower_slider = QSlider(self.right_ranges_box_2)
        self.right_lower_slider.setObjectName(u"right_lower_slider")
        self.right_lower_slider.setMinimumSize(QSize(0, 0))
        self.right_lower_slider.setLayoutDirection(Qt.LeftToRight)
        self.right_lower_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.right_lower_slider.setMaximum(87)
        self.right_lower_slider.setPageStep(1)
        self.right_lower_slider.setValue(2)
        self.right_lower_slider.setTracking(True)
        self.right_lower_slider.setOrientation(Qt.Horizontal)
        self.right_lower_slider.setInvertedAppearance(False)
        self.right_lower_slider.setTickPosition(QSlider.NoTicks)
        self.right_lower_slider.setTickInterval(0)

        self.rh_range1_box_2.addWidget(self.right_lower_slider)


        self.verticalLayout_17.addLayout(self.rh_range1_box_2)

        self.rh_range2_box_2 = QVBoxLayout()
        self.rh_range2_box_2.setObjectName(u"rh_range2_box_2")
        self.rh_range2_display_2 = QHBoxLayout()
        self.rh_range2_display_2.setObjectName(u"rh_range2_display_2")
        self.right_upper_label = QLabel(self.right_ranges_box_2)
        self.right_upper_label.setObjectName(u"right_upper_label")
        self.right_upper_label.setFont(font2)
        self.right_upper_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.rh_range2_display_2.addWidget(self.right_upper_label)

        self.rh_range2_spacerr_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.rh_range2_display_2.addItem(self.rh_range2_spacerr_2)


        self.rh_range2_box_2.addLayout(self.rh_range2_display_2)

        self.right_upper_slider = QSlider(self.right_ranges_box_2)
        self.right_upper_slider.setObjectName(u"right_upper_slider")
        self.right_upper_slider.setMinimumSize(QSize(0, 0))
        self.right_upper_slider.setLayoutDirection(Qt.LeftToRight)
        self.right_upper_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.right_upper_slider.setMaximum(87)
        self.right_upper_slider.setPageStep(1)
        self.right_upper_slider.setValue(2)
        self.right_upper_slider.setTracking(True)
        self.right_upper_slider.setOrientation(Qt.Horizontal)
        self.right_upper_slider.setInvertedAppearance(False)
        self.right_upper_slider.setTickPosition(QSlider.NoTicks)
        self.right_upper_slider.setTickInterval(0)

        self.rh_range2_box_2.addWidget(self.right_upper_slider)


        self.verticalLayout_17.addLayout(self.rh_range2_box_2)


        self.verticalLayout_15.addWidget(self.right_ranges_box_2)

        self.left_ranges_box_3 = QWidget(self.ranges_widget)
        self.left_ranges_box_3.setObjectName(u"left_ranges_box_3")
        self.verticalLayout_18 = QVBoxLayout(self.left_ranges_box_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.left_range_labels_bar = QWidget(self.left_ranges_box_3)
        self.left_range_labels_bar.setObjectName(u"left_range_labels_bar")
        sizePolicy1.setHeightForWidth(self.left_range_labels_bar.sizePolicy().hasHeightForWidth())
        self.left_range_labels_bar.setSizePolicy(sizePolicy1)
        self.left_range_labels_bar.setMinimumSize(QSize(0, 30))
        self.left_range_labels_bar.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.left_range_labels_bar)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.left_range_label = QLabel(self.left_range_labels_bar)
        self.left_range_label.setObjectName(u"left_range_label")
        self.left_range_label.setFont(font2)
        self.left_range_label.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.horizontalLayout_11.addWidget(self.left_range_label)

        self.left_lower_display = QLabel(self.left_range_labels_bar)
        self.left_lower_display.setObjectName(u"left_lower_display")
        self.left_lower_display.setFont(font2)
        self.left_lower_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.horizontalLayout_11.addWidget(self.left_lower_display)

        self.dash_5 = QLabel(self.left_range_labels_bar)
        self.dash_5.setObjectName(u"dash_5")
        self.dash_5.setFont(font2)
        self.dash_5.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.dash_5)

        self.left_upper_display = QLabel(self.left_range_labels_bar)
        self.left_upper_display.setObjectName(u"left_upper_display")
        self.left_upper_display.setFont(font2)
        self.left_upper_display.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.left_upper_display)

        self.left_span_label = QLabel(self.left_range_labels_bar)
        self.left_span_label.setObjectName(u"left_span_label")
        self.left_span_label.setMinimumSize(QSize(60, 0))
        self.left_span_label.setMaximumSize(QSize(16777215, 50))
        self.left_span_label.setFont(font2)
        self.left_span_label.setStyleSheet(u"")
        self.left_span_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.left_span_label.setWordWrap(True)
        self.left_span_label.setMargin(0)

        self.horizontalLayout_11.addWidget(self.left_span_label)

        self.left_span_display = QLabel(self.left_range_labels_bar)
        self.left_span_display.setObjectName(u"left_span_display")
        self.left_span_display.setFont(font2)
        self.left_span_display.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.horizontalLayout_11.addWidget(self.left_span_display)


        self.verticalLayout_18.addWidget(self.left_range_labels_bar)

        self.lh_range1_box_4 = QVBoxLayout()
        self.lh_range1_box_4.setObjectName(u"lh_range1_box_4")
        self.lh_range1_display_4 = QHBoxLayout()
        self.lh_range1_display_4.setObjectName(u"lh_range1_display_4")
        self.lh_range1_label_4 = QLabel(self.left_ranges_box_3)
        self.lh_range1_label_4.setObjectName(u"lh_range1_label_4")
        self.lh_range1_label_4.setFont(font2)
        self.lh_range1_label_4.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.lh_range1_display_4.addWidget(self.lh_range1_label_4)

        self.lh_range1_spacerr_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.lh_range1_display_4.addItem(self.lh_range1_spacerr_4)


        self.lh_range1_box_4.addLayout(self.lh_range1_display_4)

        self.left_lower_slider = QSlider(self.left_ranges_box_3)
        self.left_lower_slider.setObjectName(u"left_lower_slider")
        self.left_lower_slider.setMinimumSize(QSize(0, 0))
        self.left_lower_slider.setLayoutDirection(Qt.LeftToRight)
        self.left_lower_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.left_lower_slider.setMaximum(87)
        self.left_lower_slider.setPageStep(1)
        self.left_lower_slider.setValue(2)
        self.left_lower_slider.setTracking(True)
        self.left_lower_slider.setOrientation(Qt.Horizontal)
        self.left_lower_slider.setInvertedAppearance(False)
        self.left_lower_slider.setTickPosition(QSlider.NoTicks)
        self.left_lower_slider.setTickInterval(0)

        self.lh_range1_box_4.addWidget(self.left_lower_slider)


        self.verticalLayout_18.addLayout(self.lh_range1_box_4)

        self.lh_range2_box_4 = QVBoxLayout()
        self.lh_range2_box_4.setObjectName(u"lh_range2_box_4")
        self.lh_range2_display_4 = QHBoxLayout()
        self.lh_range2_display_4.setObjectName(u"lh_range2_display_4")
        self.lef = QLabel(self.left_ranges_box_3)
        self.lef.setObjectName(u"lef")
        self.lef.setFont(font2)
        self.lef.setStyleSheet(u"QLabel {\n"
"	color:rgb(137, 137, 206)\n"
"	\n"
"}")

        self.lh_range2_display_4.addWidget(self.lef)

        self.lh_range2_spacerr_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.lh_range2_display_4.addItem(self.lh_range2_spacerr_4)


        self.lh_range2_box_4.addLayout(self.lh_range2_display_4)

        self.left_upper_slider = QSlider(self.left_ranges_box_3)
        self.left_upper_slider.setObjectName(u"left_upper_slider")
        self.left_upper_slider.setMinimumSize(QSize(0, 0))
        self.left_upper_slider.setLayoutDirection(Qt.LeftToRight)
        self.left_upper_slider.setStyleSheet(u"QSlider {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-color: rgb(255, 85, 255);\n"
"	selection-background-color: rgb(11, 17, 17);\n"
"}")
        self.left_upper_slider.setMaximum(87)
        self.left_upper_slider.setPageStep(1)
        self.left_upper_slider.setValue(2)
        self.left_upper_slider.setTracking(True)
        self.left_upper_slider.setOrientation(Qt.Horizontal)
        self.left_upper_slider.setInvertedAppearance(False)
        self.left_upper_slider.setTickPosition(QSlider.NoTicks)
        self.left_upper_slider.setTickInterval(0)

        self.lh_range2_box_4.addWidget(self.left_upper_slider)


        self.verticalLayout_18.addLayout(self.lh_range2_box_4)


        self.verticalLayout_15.addWidget(self.left_ranges_box_3)


        self.horizontalLayout_4.addWidget(self.ranges_widget)

        self.spacerwidget_2 = QWidget(self.anchors_ranges_arch_widget)
        self.spacerwidget_2.setObjectName(u"spacerwidget_2")
        sizePolicy19 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy19.setHorizontalStretch(1)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.spacerwidget_2.sizePolicy().hasHeightForWidth())
        self.spacerwidget_2.setSizePolicy(sizePolicy19)
        self.verticalLayout_21 = QVBoxLayout(self.spacerwidget_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.verticalLayout_21.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_4.addWidget(self.spacerwidget_2)

        self.anchors_arch_widget = QWidget(self.anchors_ranges_arch_widget)
        self.anchors_arch_widget.setObjectName(u"anchors_arch_widget")
        sizePolicy20 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy20.setHorizontalStretch(6)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.anchors_arch_widget.sizePolicy().hasHeightForWidth())
        self.anchors_arch_widget.setSizePolicy(sizePolicy20)
        self.anchors_arch_widget.setMaximumSize(QSize(762, 475))
        self.verticalLayout_7 = QVBoxLayout(self.anchors_arch_widget)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.anchors_top_bar = QWidget(self.anchors_arch_widget)
        self.anchors_top_bar.setObjectName(u"anchors_top_bar")
        self.horizontalLayout_9 = QHBoxLayout(self.anchors_top_bar)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.anchors_label_widget = QWidget(self.anchors_top_bar)
        self.anchors_label_widget.setObjectName(u"anchors_label_widget")
        self.verticalLayout_20 = QVBoxLayout(self.anchors_label_widget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.anchors_label = QLabel(self.anchors_label_widget)
        self.anchors_label.setObjectName(u"anchors_label")
        sizePolicy4.setHeightForWidth(self.anchors_label.sizePolicy().hasHeightForWidth())
        self.anchors_label.setSizePolicy(sizePolicy4)
        self.anchors_label.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.anchors_label.setFont(font7)
        self.anchors_label.setStyleSheet(u"QLabel {\n"
"	font-size: 12pt;\n"
"}")
        self.anchors_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_20.addWidget(self.anchors_label)


        self.horizontalLayout_9.addWidget(self.anchors_label_widget)

        self.templates_widget = QWidget(self.anchors_top_bar)
        self.templates_widget.setObjectName(u"templates_widget")
        self.verticalLayout_14 = QVBoxLayout(self.templates_widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.anchor_templates_label = QLabel(self.templates_widget)
        self.anchor_templates_label.setObjectName(u"anchor_templates_label")
        sizePolicy15.setHeightForWidth(self.anchor_templates_label.sizePolicy().hasHeightForWidth())
        self.anchor_templates_label.setSizePolicy(sizePolicy15)
        self.anchor_templates_label.setMaximumSize(QSize(16777215, 20))
        self.anchor_templates_label.setFont(font2)
        self.anchor_templates_label.setStyleSheet(u"QLabel {\n"
"	font-size: 11pt;\n"
"}")
        self.anchor_templates_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.anchor_templates_label.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.anchor_templates_label)

        self.anchors_template_bar = QWidget(self.templates_widget)
        self.anchors_template_bar.setObjectName(u"anchors_template_bar")
        sizePolicy8.setHeightForWidth(self.anchors_template_bar.sizePolicy().hasHeightForWidth())
        self.anchors_template_bar.setSizePolicy(sizePolicy8)
        self.anchors_template_bar.setMaximumSize(QSize(520, 80))
        self.horizontalLayout_27 = QHBoxLayout(self.anchors_template_bar)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.anchors_config_combo = QComboBox(self.anchors_template_bar)
        self.anchors_config_combo.addItem("")
        self.anchors_config_combo.addItem("")
        self.anchors_config_combo.addItem("")
        self.anchors_config_combo.addItem("")
        self.anchors_config_combo.addItem("")
        self.anchors_config_combo.setObjectName(u"anchors_config_combo")
        sizePolicy21 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy21.setHorizontalStretch(2)
        sizePolicy21.setVerticalStretch(0)
        sizePolicy21.setHeightForWidth(self.anchors_config_combo.sizePolicy().hasHeightForWidth())
        self.anchors_config_combo.setSizePolicy(sizePolicy21)
        self.anchors_config_combo.setMaximumSize(QSize(300, 25))
        self.anchors_config_combo.setFont(font5)

        self.horizontalLayout_27.addWidget(self.anchors_config_combo)

        self.anchors_save_template = QPushButton(self.anchors_template_bar)
        self.anchors_save_template.setObjectName(u"anchors_save_template")
        sizePolicy22 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy22.setHorizontalStretch(1)
        sizePolicy22.setVerticalStretch(0)
        sizePolicy22.setHeightForWidth(self.anchors_save_template.sizePolicy().hasHeightForWidth())
        self.anchors_save_template.setSizePolicy(sizePolicy22)
        self.anchors_save_template.setMaximumSize(QSize(16777215, 40))
        self.anchors_save_template.setFont(font5)

        self.horizontalLayout_27.addWidget(self.anchors_save_template)

        self.anchors_refresh_template = QPushButton(self.anchors_template_bar)
        self.anchors_refresh_template.setObjectName(u"anchors_refresh_template")
        sizePolicy23 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy23.setHorizontalStretch(1)
        sizePolicy23.setVerticalStretch(0)
        sizePolicy23.setHeightForWidth(self.anchors_refresh_template.sizePolicy().hasHeightForWidth())
        self.anchors_refresh_template.setSizePolicy(sizePolicy23)
        self.anchors_refresh_template.setMaximumSize(QSize(16777215, 40))
        self.anchors_refresh_template.setFont(font5)

        self.horizontalLayout_27.addWidget(self.anchors_refresh_template)

        self.anchors_delete_template = QPushButton(self.anchors_template_bar)
        self.anchors_delete_template.setObjectName(u"anchors_delete_template")
        sizePolicy23.setHeightForWidth(self.anchors_delete_template.sizePolicy().hasHeightForWidth())
        self.anchors_delete_template.setSizePolicy(sizePolicy23)
        self.anchors_delete_template.setMaximumSize(QSize(16777215, 40))
        self.anchors_delete_template.setFont(font5)

        self.horizontalLayout_27.addWidget(self.anchors_delete_template)


        self.verticalLayout_14.addWidget(self.anchors_template_bar)


        self.horizontalLayout_9.addWidget(self.templates_widget)


        self.verticalLayout_7.addWidget(self.anchors_top_bar)

        self.anchors_widget = QWidget(self.anchors_arch_widget)
        self.anchors_widget.setObjectName(u"anchors_widget")
        sizePolicy4.setHeightForWidth(self.anchors_widget.sizePolicy().hasHeightForWidth())
        self.anchors_widget.setSizePolicy(sizePolicy4)
        self.anchors_widget.setMaximumSize(QSize(750, 320))
        self.anchors_widget.setStyleSheet(u"QWidget {\n"
"	margin-top: 15px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.anchors_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(12)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gravity_label = QLabel(self.anchors_widget)
        self.gravity_label.setObjectName(u"gravity_label")
        sizePolicy1.setHeightForWidth(self.gravity_label.sizePolicy().hasHeightForWidth())
        self.gravity_label.setSizePolicy(sizePolicy1)
        self.gravity_label.setMinimumSize(QSize(0, 0))
        self.gravity_label.setMaximumSize(QSize(16777215, 35))
        self.gravity_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.gravity_label, 0, 1, 1, 1)

        self.tertiary_spawn = QHBoxLayout()
        self.tertiary_spawn.setObjectName(u"tertiary_spawn")
        self.tertiary_spawn_dial = QDial(self.anchors_widget)
        self.tertiary_spawn_dial.setObjectName(u"tertiary_spawn_dial")
        sizePolicy15.setHeightForWidth(self.tertiary_spawn_dial.sizePolicy().hasHeightForWidth())
        self.tertiary_spawn_dial.setSizePolicy(sizePolicy15)
        self.tertiary_spawn_dial.setMaximumSize(QSize(65, 16777215))
        self.tertiary_spawn_dial.setMaximum(30)
        self.tertiary_spawn_dial.setPageStep(5)
        self.tertiary_spawn_dial.setWrapping(False)
        self.tertiary_spawn_dial.setNotchesVisible(True)

        self.tertiary_spawn.addWidget(self.tertiary_spawn_dial)

        self.tertiary_spawn_display = QLabel(self.anchors_widget)
        self.tertiary_spawn_display.setObjectName(u"tertiary_spawn_display")
        sizePolicy15.setHeightForWidth(self.tertiary_spawn_display.sizePolicy().hasHeightForWidth())
        self.tertiary_spawn_display.setSizePolicy(sizePolicy15)
        self.tertiary_spawn_display.setMaximumSize(QSize(40, 16777215))
        self.tertiary_spawn_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tertiary_spawn_display.setWordWrap(False)

        self.tertiary_spawn.addWidget(self.tertiary_spawn_display)


        self.gridLayout_3.addLayout(self.tertiary_spawn, 3, 3, 1, 1)

        self.secondary_spawn = QHBoxLayout()
        self.secondary_spawn.setObjectName(u"secondary_spawn")
        self.secondary_spawn_dial = QDial(self.anchors_widget)
        self.secondary_spawn_dial.setObjectName(u"secondary_spawn_dial")
        sizePolicy15.setHeightForWidth(self.secondary_spawn_dial.sizePolicy().hasHeightForWidth())
        self.secondary_spawn_dial.setSizePolicy(sizePolicy15)
        self.secondary_spawn_dial.setMaximumSize(QSize(65, 16777215))
        self.secondary_spawn_dial.setMaximum(30)
        self.secondary_spawn_dial.setPageStep(5)
        self.secondary_spawn_dial.setWrapping(False)
        self.secondary_spawn_dial.setNotchesVisible(True)

        self.secondary_spawn.addWidget(self.secondary_spawn_dial)

        self.secondary_spawn_display = QLabel(self.anchors_widget)
        self.secondary_spawn_display.setObjectName(u"secondary_spawn_display")
        sizePolicy15.setHeightForWidth(self.secondary_spawn_display.sizePolicy().hasHeightForWidth())
        self.secondary_spawn_display.setSizePolicy(sizePolicy15)
        self.secondary_spawn_display.setMaximumSize(QSize(40, 16777215))
        self.secondary_spawn_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.secondary_spawn_display.setWordWrap(False)

        self.secondary_spawn.addWidget(self.secondary_spawn_display)


        self.gridLayout_3.addLayout(self.secondary_spawn, 2, 3, 1, 1)

        self.secondary_longevity = QHBoxLayout()
        self.secondary_longevity.setObjectName(u"secondary_longevity")
        self.secondary_longevity_dial = QDial(self.anchors_widget)
        self.secondary_longevity_dial.setObjectName(u"secondary_longevity_dial")
        sizePolicy15.setHeightForWidth(self.secondary_longevity_dial.sizePolicy().hasHeightForWidth())
        self.secondary_longevity_dial.setSizePolicy(sizePolicy15)
        self.secondary_longevity_dial.setMaximumSize(QSize(65, 16777215))
        self.secondary_longevity_dial.setMaximum(30)
        self.secondary_longevity_dial.setPageStep(5)
        self.secondary_longevity_dial.setWrapping(False)
        self.secondary_longevity_dial.setNotchesVisible(True)

        self.secondary_longevity.addWidget(self.secondary_longevity_dial)

        self.secondary_longevity_display = QLabel(self.anchors_widget)
        self.secondary_longevity_display.setObjectName(u"secondary_longevity_display")
        sizePolicy15.setHeightForWidth(self.secondary_longevity_display.sizePolicy().hasHeightForWidth())
        self.secondary_longevity_display.setSizePolicy(sizePolicy15)
        self.secondary_longevity_display.setMaximumSize(QSize(40, 16777215))
        self.secondary_longevity_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.secondary_longevity_display.setWordWrap(False)

        self.secondary_longevity.addWidget(self.secondary_longevity_display)


        self.gridLayout_3.addLayout(self.secondary_longevity, 2, 4, 1, 1)

        self.spawn_label = QLabel(self.anchors_widget)
        self.spawn_label.setObjectName(u"spawn_label")
        sizePolicy1.setHeightForWidth(self.spawn_label.sizePolicy().hasHeightForWidth())
        self.spawn_label.setSizePolicy(sizePolicy1)
        self.spawn_label.setMaximumSize(QSize(16777215, 35))
        self.spawn_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.spawn_label, 0, 3, 1, 1)

        self.tertiary_longevity = QHBoxLayout()
        self.tertiary_longevity.setObjectName(u"tertiary_longevity")
        self.tertiary_longevity_dial = QDial(self.anchors_widget)
        self.tertiary_longevity_dial.setObjectName(u"tertiary_longevity_dial")
        sizePolicy15.setHeightForWidth(self.tertiary_longevity_dial.sizePolicy().hasHeightForWidth())
        self.tertiary_longevity_dial.setSizePolicy(sizePolicy15)
        self.tertiary_longevity_dial.setMaximumSize(QSize(65, 16777215))
        self.tertiary_longevity_dial.setMaximum(30)
        self.tertiary_longevity_dial.setPageStep(5)
        self.tertiary_longevity_dial.setWrapping(False)
        self.tertiary_longevity_dial.setNotchesVisible(True)

        self.tertiary_longevity.addWidget(self.tertiary_longevity_dial)

        self.tertiary_longevity_display = QLabel(self.anchors_widget)
        self.tertiary_longevity_display.setObjectName(u"tertiary_longevity_display")
        sizePolicy15.setHeightForWidth(self.tertiary_longevity_display.sizePolicy().hasHeightForWidth())
        self.tertiary_longevity_display.setSizePolicy(sizePolicy15)
        self.tertiary_longevity_display.setMaximumSize(QSize(40, 16777215))
        self.tertiary_longevity_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tertiary_longevity_display.setWordWrap(False)

        self.tertiary_longevity.addWidget(self.tertiary_longevity_display)


        self.gridLayout_3.addLayout(self.tertiary_longevity, 3, 4, 1, 1)

        self.primary_label = QLabel(self.anchors_widget)
        self.primary_label.setObjectName(u"primary_label")
        sizePolicy15.setHeightForWidth(self.primary_label.sizePolicy().hasHeightForWidth())
        self.primary_label.setSizePolicy(sizePolicy15)
        self.primary_label.setMaximumSize(QSize(350, 16777215))
        self.primary_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.primary_label, 1, 0, 1, 1)

        self.primary_gravity = QHBoxLayout()
        self.primary_gravity.setObjectName(u"primary_gravity")
        self.primary_gravity_dial = QDial(self.anchors_widget)
        self.primary_gravity_dial.setObjectName(u"primary_gravity_dial")
        sizePolicy15.setHeightForWidth(self.primary_gravity_dial.sizePolicy().hasHeightForWidth())
        self.primary_gravity_dial.setSizePolicy(sizePolicy15)
        self.primary_gravity_dial.setMaximumSize(QSize(65, 16777215))
        self.primary_gravity_dial.setMaximum(30)
        self.primary_gravity_dial.setPageStep(5)
        self.primary_gravity_dial.setWrapping(False)
        self.primary_gravity_dial.setNotchesVisible(True)

        self.primary_gravity.addWidget(self.primary_gravity_dial)

        self.primary_gravity_display = QLabel(self.anchors_widget)
        self.primary_gravity_display.setObjectName(u"primary_gravity_display")
        sizePolicy15.setHeightForWidth(self.primary_gravity_display.sizePolicy().hasHeightForWidth())
        self.primary_gravity_display.setSizePolicy(sizePolicy15)
        self.primary_gravity_display.setMaximumSize(QSize(40, 16777215))
        self.primary_gravity_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.primary_gravity_display.setWordWrap(False)

        self.primary_gravity.addWidget(self.primary_gravity_display)


        self.gridLayout_3.addLayout(self.primary_gravity, 1, 1, 1, 1)

        self.secondary_label = QLabel(self.anchors_widget)
        self.secondary_label.setObjectName(u"secondary_label")
        sizePolicy15.setHeightForWidth(self.secondary_label.sizePolicy().hasHeightForWidth())
        self.secondary_label.setSizePolicy(sizePolicy15)
        self.secondary_label.setMaximumSize(QSize(350, 16777215))
        self.secondary_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.secondary_label, 2, 0, 1, 1)

        self.secondary_gravity = QHBoxLayout()
        self.secondary_gravity.setObjectName(u"secondary_gravity")
        self.secondary_gravity_dial = QDial(self.anchors_widget)
        self.secondary_gravity_dial.setObjectName(u"secondary_gravity_dial")
        sizePolicy15.setHeightForWidth(self.secondary_gravity_dial.sizePolicy().hasHeightForWidth())
        self.secondary_gravity_dial.setSizePolicy(sizePolicy15)
        self.secondary_gravity_dial.setMaximumSize(QSize(65, 16777215))
        self.secondary_gravity_dial.setMaximum(30)
        self.secondary_gravity_dial.setPageStep(5)
        self.secondary_gravity_dial.setWrapping(False)
        self.secondary_gravity_dial.setNotchesVisible(True)

        self.secondary_gravity.addWidget(self.secondary_gravity_dial)

        self.secondary_gravity_display = QLabel(self.anchors_widget)
        self.secondary_gravity_display.setObjectName(u"secondary_gravity_display")
        sizePolicy15.setHeightForWidth(self.secondary_gravity_display.sizePolicy().hasHeightForWidth())
        self.secondary_gravity_display.setSizePolicy(sizePolicy15)
        self.secondary_gravity_display.setMaximumSize(QSize(40, 16777215))
        self.secondary_gravity_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.secondary_gravity_display.setWordWrap(False)

        self.secondary_gravity.addWidget(self.secondary_gravity_display)


        self.gridLayout_3.addLayout(self.secondary_gravity, 2, 1, 1, 1)

        self.tertiary_label = QLabel(self.anchors_widget)
        self.tertiary_label.setObjectName(u"tertiary_label")
        sizePolicy15.setHeightForWidth(self.tertiary_label.sizePolicy().hasHeightForWidth())
        self.tertiary_label.setSizePolicy(sizePolicy15)
        self.tertiary_label.setMaximumSize(QSize(350, 16777215))
        self.tertiary_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.tertiary_label, 3, 0, 1, 1)

        self.NA = QLabel(self.anchors_widget)
        self.NA.setObjectName(u"NA")
        font8 = QFont()
        font8.setPointSize(26)
        self.NA.setFont(font8)
        self.NA.setStyleSheet(u"QLabel {\n"
"	font-size: 26pt;\n"
"}")
        self.NA.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.NA, 1, 3, 1, 1)

        self.tertiary_gravity = QHBoxLayout()
        self.tertiary_gravity.setObjectName(u"tertiary_gravity")
        self.tertiary_gravity_dial = QDial(self.anchors_widget)
        self.tertiary_gravity_dial.setObjectName(u"tertiary_gravity_dial")
        sizePolicy15.setHeightForWidth(self.tertiary_gravity_dial.sizePolicy().hasHeightForWidth())
        self.tertiary_gravity_dial.setSizePolicy(sizePolicy15)
        self.tertiary_gravity_dial.setMaximumSize(QSize(65, 16777215))
        self.tertiary_gravity_dial.setMaximum(30)
        self.tertiary_gravity_dial.setPageStep(5)
        self.tertiary_gravity_dial.setWrapping(False)
        self.tertiary_gravity_dial.setNotchesVisible(True)

        self.tertiary_gravity.addWidget(self.tertiary_gravity_dial)

        self.tertiary_gravity_display = QLabel(self.anchors_widget)
        self.tertiary_gravity_display.setObjectName(u"tertiary_gravity_display")
        sizePolicy15.setHeightForWidth(self.tertiary_gravity_display.sizePolicy().hasHeightForWidth())
        self.tertiary_gravity_display.setSizePolicy(sizePolicy15)
        self.tertiary_gravity_display.setMaximumSize(QSize(40, 16777215))
        self.tertiary_gravity_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tertiary_gravity_display.setWordWrap(False)

        self.tertiary_gravity.addWidget(self.tertiary_gravity_display)


        self.gridLayout_3.addLayout(self.tertiary_gravity, 3, 1, 1, 1)

        self.NA2 = QLabel(self.anchors_widget)
        self.NA2.setObjectName(u"NA2")
        self.NA2.setStyleSheet(u"QLabel {\n"
"	font-size: 26pt;\n"
"}")
        self.NA2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.NA2, 1, 4, 1, 1)

        self.longevity_label = QLabel(self.anchors_widget)
        self.longevity_label.setObjectName(u"longevity_label")
        sizePolicy1.setHeightForWidth(self.longevity_label.sizePolicy().hasHeightForWidth())
        self.longevity_label.setSizePolicy(sizePolicy1)
        self.longevity_label.setMaximumSize(QSize(16777215, 35))
        self.longevity_label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.longevity_label, 0, 4, 1, 1)

        self.tertiary_velocity = QHBoxLayout()
        self.tertiary_velocity.setObjectName(u"tertiary_velocity")
        self.tertiary_velocity_dial = QDial(self.anchors_widget)
        self.tertiary_velocity_dial.setObjectName(u"tertiary_velocity_dial")
        sizePolicy15.setHeightForWidth(self.tertiary_velocity_dial.sizePolicy().hasHeightForWidth())
        self.tertiary_velocity_dial.setSizePolicy(sizePolicy15)
        self.tertiary_velocity_dial.setMinimumSize(QSize(0, 0))
        self.tertiary_velocity_dial.setMaximumSize(QSize(65, 16777215))
        self.tertiary_velocity_dial.setMaximum(30)
        self.tertiary_velocity_dial.setPageStep(5)
        self.tertiary_velocity_dial.setWrapping(False)
        self.tertiary_velocity_dial.setNotchesVisible(True)

        self.tertiary_velocity.addWidget(self.tertiary_velocity_dial)

        self.tertiary_velocity_display = QLabel(self.anchors_widget)
        self.tertiary_velocity_display.setObjectName(u"tertiary_velocity_display")
        sizePolicy15.setHeightForWidth(self.tertiary_velocity_display.sizePolicy().hasHeightForWidth())
        self.tertiary_velocity_display.setSizePolicy(sizePolicy15)
        self.tertiary_velocity_display.setMaximumSize(QSize(40, 16777215))
        self.tertiary_velocity_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tertiary_velocity_display.setWordWrap(False)

        self.tertiary_velocity.addWidget(self.tertiary_velocity_display)


        self.gridLayout_3.addLayout(self.tertiary_velocity, 3, 2, 1, 1)

        self.secondary_velocity = QHBoxLayout()
        self.secondary_velocity.setObjectName(u"secondary_velocity")
        self.secondary_velocity_dial = QDial(self.anchors_widget)
        self.secondary_velocity_dial.setObjectName(u"secondary_velocity_dial")
        sizePolicy15.setHeightForWidth(self.secondary_velocity_dial.sizePolicy().hasHeightForWidth())
        self.secondary_velocity_dial.setSizePolicy(sizePolicy15)
        self.secondary_velocity_dial.setMaximumSize(QSize(65, 16777215))
        self.secondary_velocity_dial.setMaximum(30)
        self.secondary_velocity_dial.setPageStep(5)
        self.secondary_velocity_dial.setWrapping(False)
        self.secondary_velocity_dial.setNotchesVisible(True)

        self.secondary_velocity.addWidget(self.secondary_velocity_dial)

        self.secondary_velocity_display = QLabel(self.anchors_widget)
        self.secondary_velocity_display.setObjectName(u"secondary_velocity_display")
        sizePolicy15.setHeightForWidth(self.secondary_velocity_display.sizePolicy().hasHeightForWidth())
        self.secondary_velocity_display.setSizePolicy(sizePolicy15)
        self.secondary_velocity_display.setMaximumSize(QSize(40, 16777215))
        self.secondary_velocity_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.secondary_velocity_display.setWordWrap(False)

        self.secondary_velocity.addWidget(self.secondary_velocity_display)


        self.gridLayout_3.addLayout(self.secondary_velocity, 2, 2, 1, 1)

        self.anchor_strength_label_22 = QLabel(self.anchors_widget)
        self.anchor_strength_label_22.setObjectName(u"anchor_strength_label_22")
        sizePolicy1.setHeightForWidth(self.anchor_strength_label_22.sizePolicy().hasHeightForWidth())
        self.anchor_strength_label_22.setSizePolicy(sizePolicy1)
        self.anchor_strength_label_22.setMaximumSize(QSize(16777215, 35))
        self.anchor_strength_label_22.setWordWrap(True)

        self.gridLayout_3.addWidget(self.anchor_strength_label_22, 0, 2, 1, 1)

        self.primary_velocity = QHBoxLayout()
        self.primary_velocity.setObjectName(u"primary_velocity")
        self.primary_velocity_dial = QDial(self.anchors_widget)
        self.primary_velocity_dial.setObjectName(u"primary_velocity_dial")
        sizePolicy15.setHeightForWidth(self.primary_velocity_dial.sizePolicy().hasHeightForWidth())
        self.primary_velocity_dial.setSizePolicy(sizePolicy15)
        self.primary_velocity_dial.setMaximumSize(QSize(65, 16777215))
        self.primary_velocity_dial.setMaximum(30)
        self.primary_velocity_dial.setPageStep(5)
        self.primary_velocity_dial.setWrapping(False)
        self.primary_velocity_dial.setNotchesVisible(True)

        self.primary_velocity.addWidget(self.primary_velocity_dial)

        self.primary_velocity_display = QLabel(self.anchors_widget)
        self.primary_velocity_display.setObjectName(u"primary_velocity_display")
        sizePolicy15.setHeightForWidth(self.primary_velocity_display.sizePolicy().hasHeightForWidth())
        self.primary_velocity_display.setSizePolicy(sizePolicy15)
        self.primary_velocity_display.setMaximumSize(QSize(40, 16777215))
        self.primary_velocity_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.primary_velocity_display.setWordWrap(False)

        self.primary_velocity.addWidget(self.primary_velocity_display)


        self.gridLayout_3.addLayout(self.primary_velocity, 1, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.anchors_widget)


        self.horizontalLayout_4.addWidget(self.anchors_arch_widget)

        self.spacerwidget = QWidget(self.anchors_ranges_arch_widget)
        self.spacerwidget.setObjectName(u"spacerwidget")
        sizePolicy24 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy24.setHorizontalStretch(2)
        sizePolicy24.setVerticalStretch(0)
        sizePolicy24.setHeightForWidth(self.spacerwidget.sizePolicy().hasHeightForWidth())
        self.spacerwidget.setSizePolicy(sizePolicy24)
        self.verticalLayout_12 = QVBoxLayout(self.spacerwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")

        self.horizontalLayout_4.addWidget(self.spacerwidget)


        self.verticalLayout_11.addWidget(self.anchors_ranges_arch_widget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.style_stack.addWidget(self.pitch_page)
        self.aharmony_page = QWidget()
        self.aharmony_page.setObjectName(u"aharmony_page")
        self.style_stack.addWidget(self.aharmony_page)

        self.verticalLayout_4.addWidget(self.style_stack)

        self.content_stack.addWidget(self.style_page)
        self.compose_page = QWidget()
        self.compose_page.setObjectName(u"compose_page")
        self.widget_3 = QWidget(self.compose_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 50, 1121, 261))
        sizePolicy15.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy15)
        self.horizontalLayout_28 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_22 = QVBoxLayout(self.widget_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_2 = QFrame(self.widget_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	border: 2px solid rgb(25, 40, 40);\n"
"	border-radius: 4px;\n"
"	background-color: rgb(16, 24, 24);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(137, 137, 206);\n"
"	background-color:rgb(16, 24, 24);\n"
"	border: 0px solid;\n"
"}\n"
"")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.compose_active_configuration_label = QLabel(self.frame_2)
        self.compose_active_configuration_label.setObjectName(u"compose_active_configuration_label")
        sizePolicy15.setHeightForWidth(self.compose_active_configuration_label.sizePolicy().hasHeightForWidth())
        self.compose_active_configuration_label.setSizePolicy(sizePolicy15)

        self.horizontalLayout_30.addWidget(self.compose_active_configuration_label)

        self.compose_active_configuration_display = QLabel(self.frame_2)
        self.compose_active_configuration_display.setObjectName(u"compose_active_configuration_display")

        self.horizontalLayout_30.addWidget(self.compose_active_configuration_display)


        self.verticalLayout_22.addWidget(self.frame_2)

        self.loaf_config_btn = QPushButton(self.widget_4)
        self.loaf_config_btn.setObjectName(u"loaf_config_btn")
        self.loaf_config_btn.setMinimumSize(QSize(0, 40))
        self.loaf_config_btn.setMaximumSize(QSize(400, 16777215))
        self.loaf_config_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"")

        self.verticalLayout_22.addWidget(self.loaf_config_btn)

        self.save_config_btn = QPushButton(self.widget_4)
        self.save_config_btn.setObjectName(u"save_config_btn")
        self.save_config_btn.setMinimumSize(QSize(0, 40))
        self.save_config_btn.setMaximumSize(QSize(400, 16777215))
        self.save_config_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"")

        self.verticalLayout_22.addWidget(self.save_config_btn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_5)


        self.horizontalLayout_28.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy15.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy15)
        self.verticalLayout_36 = QVBoxLayout(self.widget_5)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)
        self.label.setMaximumSize(QSize(70, 40))
        self.label.setPixmap(QPixmap(u"data/images/right_arrows.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_36.addWidget(self.label)

        self.verticalSpacer_6 = QSpacerItem(20, 246, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_6)


        self.horizontalLayout_28.addWidget(self.widget_5)

        self.widget_15 = QWidget(self.widget_3)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_37 = QVBoxLayout(self.widget_15)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.composition_name_entry = QLineEdit(self.widget_15)
        self.composition_name_entry.setObjectName(u"composition_name_entry")
        sizePolicy1.setHeightForWidth(self.composition_name_entry.sizePolicy().hasHeightForWidth())
        self.composition_name_entry.setSizePolicy(sizePolicy1)
        self.composition_name_entry.setMinimumSize(QSize(0, 40))
        self.composition_name_entry.setMaximumSize(QSize(16777215, 40))
        self.composition_name_entry.setFont(font2)

        self.verticalLayout_37.addWidget(self.composition_name_entry)

        self.compose_btn = QPushButton(self.widget_15)
        self.compose_btn.setObjectName(u"compose_btn")
        self.compose_btn.setMinimumSize(QSize(0, 40))
        self.compose_btn.setMaximumSize(QSize(400, 16777215))
        self.compose_btn.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(67, 67, 100);\n"
"	border-radius: 10px;\n"
"	color: rgb(137, 137, 206);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	\n"
"	background-color: rgb(25, 40, 40);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(36, 36, 54);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	border: rgb(85, 170, 255);\n"
"	background-color: rgb(24, 40, 40);\n"
"}\n"
"\n"
"")

        self.verticalLayout_37.addWidget(self.compose_btn)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_7)


        self.horizontalLayout_28.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_3)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy15.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy15)
        self.verticalLayout_38 = QVBoxLayout(self.widget_16)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_2 = QLabel(self.widget_16)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
        self.label_2.setMaximumSize(QSize(70, 40))
        self.label_2.setPixmap(QPixmap(u"data/images/right_arrows.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_38.addWidget(self.label_2)

        self.verticalSpacer_8 = QSpacerItem(20, 246, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_8)


        self.horizontalLayout_28.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_3)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_39 = QVBoxLayout(self.widget_17)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.filepath_display = QLabel(self.widget_17)
        self.filepath_display.setObjectName(u"filepath_display")
        sizePolicy1.setHeightForWidth(self.filepath_display.sizePolicy().hasHeightForWidth())
        self.filepath_display.setSizePolicy(sizePolicy1)
        self.filepath_display.setMinimumSize(QSize(0, 40))
        self.filepath_display.setMaximumSize(QSize(16777215, 40))
        self.filepath_display.setFont(font6)
        self.filepath_display.setStyleSheet(u"QLabel {\n"
"	font-size:14pt;\n"
"}")

        self.verticalLayout_39.addWidget(self.filepath_display)

        self.verticalSpacer_9 = QSpacerItem(20, 246, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_9)


        self.horizontalLayout_28.addWidget(self.widget_17)

        self.content_stack.addWidget(self.compose_page)
        self.structure_page = QWidget()
        self.structure_page.setObjectName(u"structure_page")
        self.verticalLayout_10 = QVBoxLayout(self.structure_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.length_bar = QWidget(self.structure_page)
        self.length_bar.setObjectName(u"length_bar")
        sizePolicy5.setHeightForWidth(self.length_bar.sizePolicy().hasHeightForWidth())
        self.length_bar.setSizePolicy(sizePolicy5)
        self.length_bar.setMaximumSize(QSize(300, 40))
        self.measures_bar_2 = QHBoxLayout(self.length_bar)
        self.measures_bar_2.setSpacing(4)
        self.measures_bar_2.setObjectName(u"measures_bar_2")
        self.length_label = QLabel(self.length_bar)
        self.length_label.setObjectName(u"length_label")
        sizePolicy6.setHeightForWidth(self.length_label.sizePolicy().hasHeightForWidth())
        self.length_label.setSizePolicy(sizePolicy6)
        self.length_label.setMinimumSize(QSize(200, 40))
        self.length_label.setMaximumSize(QSize(200, 40))
        self.length_label.setFont(font2)
        self.length_label.setStyleSheet(u"QLabel {\n"
"	padding-left: 6px;\n"
"}")
        self.length_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.measures_bar_2.addWidget(self.length_label)

        self.length_hSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.measures_bar_2.addItem(self.length_hSpacer)

        self.length_entry = QLineEdit(self.length_bar)
        self.length_entry.setObjectName(u"length_entry")
        self.length_entry.setMinimumSize(QSize(0, 30))
        self.length_entry.setMaximumSize(QSize(50, 16777215))
        self.length_entry.setFont(font1)
        self.length_entry.setStyleSheet(u"")
        self.length_entry.setMaxLength(2)
        self.length_entry.setAlignment(Qt.AlignCenter)

        self.measures_bar_2.addWidget(self.length_entry)


        self.verticalLayout_10.addWidget(self.length_bar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.content_stack.addWidget(self.structure_page)

        self.verticalLayout_3.addWidget(self.content_stack)


        self.gridLayout.addWidget(self.content, 1, 1, 1, 1)

        self.topBar = QWidget(self.stylesheet)
        self.topBar.setObjectName(u"topBar")
        sizePolicy1.setHeightForWidth(self.topBar.sizePolicy().hasHeightForWidth())
        self.topBar.setSizePolicy(sizePolicy1)
        self.topBar.setMinimumSize(QSize(0, 40))
        self.topBar.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_29 = QHBoxLayout(self.topBar)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.corner_logo = QLabel(self.topBar)
        self.corner_logo.setObjectName(u"corner_logo")
        sizePolicy6.setHeightForWidth(self.corner_logo.sizePolicy().hasHeightForWidth())
        self.corner_logo.setSizePolicy(sizePolicy6)
        self.corner_logo.setMinimumSize(QSize(60, 60))
        self.corner_logo.setMaximumSize(QSize(60, 60))
        self.corner_logo.setPixmap(QPixmap(u"../data/images/avante-note.png"))
        self.corner_logo.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.corner_logo)

        self.version_display = QLabel(self.topBar)
        self.version_display.setObjectName(u"version_display")
        sizePolicy15.setHeightForWidth(self.version_display.sizePolicy().hasHeightForWidth())
        self.version_display.setSizePolicy(sizePolicy15)
        self.version_display.setFont(font3)
        self.version_display.setStyleSheet(u"QLabel {\n"
"	font-size: 9pt;\n"
"	color:rgb(54, 54, 85);\n"
"}")
        self.version_display.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.version_display.setWordWrap(True)
        self.version_display.setMargin(6)

        self.horizontalLayout_29.addWidget(self.version_display)

        self.active_states = QWidget(self.topBar)
        self.active_states.setObjectName(u"active_states")
        self.active_states.setStyleSheet(u"QLabel {\n"
"	font-size: 10pt;\n"
"}")
        self.verticalLayout_35 = QVBoxLayout(self.active_states)
        self.verticalLayout_35.setSpacing(2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.active_states)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(40, 0, 0, 0)
        self.active_style_label = QLabel(self.widget_10)
        self.active_style_label.setObjectName(u"active_style_label")
        sizePolicy9.setHeightForWidth(self.active_style_label.sizePolicy().hasHeightForWidth())
        self.active_style_label.setSizePolicy(sizePolicy9)
        self.active_style_label.setMinimumSize(QSize(220, 0))
        self.active_style_label.setFont(font5)
        self.active_style_label.setStyleSheet(u"")

        self.horizontalLayout_34.addWidget(self.active_style_label)

        self.active_configuration_label = QLabel(self.widget_10)
        self.active_configuration_label.setObjectName(u"active_configuration_label")
        self.active_configuration_label.setFont(font5)
        self.active_configuration_label.setStyleSheet(u"")

        self.horizontalLayout_34.addWidget(self.active_configuration_label)


        self.verticalLayout_35.addWidget(self.widget_10)

        self.widget_13 = QWidget(self.active_states)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(40, 0, 0, 0)
        self.topBar_active_style_display = QLabel(self.widget_13)
        self.topBar_active_style_display.setObjectName(u"topBar_active_style_display")
        sizePolicy9.setHeightForWidth(self.topBar_active_style_display.sizePolicy().hasHeightForWidth())
        self.topBar_active_style_display.setSizePolicy(sizePolicy9)
        self.topBar_active_style_display.setMinimumSize(QSize(220, 0))
        self.topBar_active_style_display.setFont(font5)
        self.topBar_active_style_display.setStyleSheet(u"QLabel {\n"
"	color: rgb(161, 239, 119);\n"
"}")

        self.horizontalLayout_36.addWidget(self.topBar_active_style_display)

        self.topBar_active_configuration_display = QLabel(self.widget_13)
        self.topBar_active_configuration_display.setObjectName(u"topBar_active_configuration_display")
        self.topBar_active_configuration_display.setFont(font5)
        self.topBar_active_configuration_display.setStyleSheet(u"QLabel {\n"
"	color: rgb(161, 239, 119);\n"
"}")

        self.horizontalLayout_36.addWidget(self.topBar_active_configuration_display)


        self.verticalLayout_35.addWidget(self.widget_13)


        self.horizontalLayout_29.addWidget(self.active_states)

        self.widget_14 = QWidget(self.topBar)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")

        self.horizontalLayout_29.addWidget(self.widget_14)


        self.gridLayout.addWidget(self.topBar, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.content_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.compose_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.structure_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Structure", None))
        self.style_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.rhythm_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Rhythm", None))
        self.pitch_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.aharmony_nav_btn.setText(QCoreApplication.translate("MainWindow", u"(A)harmony", None))
        self.synopations_nav_btn.setText(QCoreApplication.translate("MainWindow", u"Syncopations", None))
        self.bpm_label.setText(QCoreApplication.translate("MainWindow", u"Beats per Minute", None))
        self.bpm_entry.setInputMask(QCoreApplication.translate("MainWindow", u"999", None))
        self.bpm_entry.setText("")
        self.bpm_entry.setPlaceholderText("")
        self.timesig_label.setText(QCoreApplication.translate("MainWindow", u"Time Signature:", None))
        self.timesig_num.setInputMask(QCoreApplication.translate("MainWindow", u"99", None))
        self.timesig_num.setText("")
        self.timesig_num.setPlaceholderText("")
        self.timesig_den.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.timesig_den.setItemText(1, QCoreApplication.translate("MainWindow", u"4", None))
        self.timesig_den.setItemText(2, QCoreApplication.translate("MainWindow", u"8", None))
        self.timesig_den.setItemText(3, QCoreApplication.translate("MainWindow", u"16", None))
        self.timesig_den.setItemText(4, QCoreApplication.translate("MainWindow", u"32", None))
        self.timesig_den.setItemText(5, QCoreApplication.translate("MainWindow", u"64", None))

        self.division_label.setText(QCoreApplication.translate("MainWindow", u"Beat Divisions:", None))
        self.division_display.setText(QCoreApplication.translate("MainWindow", u"///beats///", None))
        self.meter_str_label.setText(QCoreApplication.translate("MainWindow", u"Meter Strength:", None))
        self.meter_str_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.weights_label.setText(QCoreApplication.translate("MainWindow", u"Weights", None))
        self.prime_roll_label_15.setText(QCoreApplication.translate("MainWindow", u"Rest Conversion", None))
        self.rest_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.snap_label.setText(QCoreApplication.translate("MainWindow", u"Snap Level", None))
        self.snap_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.prime_weights_label_2.setText("")
        self.whole_weight_image_2.setText("")
        self.half_weight_image_2.setText("")
        self.quarter_weight_image_2.setText("")
        self.eighth_weight_image_2.setText("")
        self.sixteenth_weight_image_4.setText("")
        self.sixteenth_weight_image_5.setText("")
        self.sixteenth_weight_image_6.setText("")
        self.prime_roll_label.setText(QCoreApplication.translate("MainWindow", u"Prime Roll", None))
        self.whole_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_10.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dwhole_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.half_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_9.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dhalf_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.quarter_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_3.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dquarter_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.eighth_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_8.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.deighth_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.sixteenth_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_7.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dsixteenth_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.thirtysecond_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_11.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dthirtysecond_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.sixtyfourth_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_12.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dsixtyfourth_prime_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.pair_weights_label.setText(QCoreApplication.translate("MainWindow", u"Pair Roll", None))
        self.whole_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_5.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dwhole_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.half_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_6.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dhalf_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.quarter_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_4.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dquarter_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.eighth_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.deighth_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.sixteenth_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_2.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dsixteenth_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.thirtysecond_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_13.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dthirtysecond_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.sixtyfourth_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.dotted_14.setText(QCoreApplication.translate("MainWindow", u"dotted", None))
        self.dsixtyfourth_pair_display.setText(QCoreApplication.translate("MainWindow", u"1-100", None))
        self.pair_len_label.setText(QCoreApplication.translate("MainWindow", u"Pair Length", None))
        self.dotted_15.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.dotted_16.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.eighth_len_two.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.eighth_len_two.setText("")
        self.eighth_len_two.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.eighth_len_three.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.eighth_len_three.setText("")
        self.eighth_len_three.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.eighth_len_four.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.eighth_len_four.setText("")
        self.eighth_len_four.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.eighth_len_five.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.eighth_len_five.setText("")
        self.eighth_len_five.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.eighth_len_six.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.eighth_len_six.setText("")
        self.eighth_len_six.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.eighth_len_seven.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.eighth_len_seven.setText("")
        self.eighth_len_seven.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.eighth_len_eight.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.eighth_len_eight.setText("")
        self.eighth_len_eight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixteenth_len_one.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixteenth_len_one.setText("")
        self.sixteenth_len_one.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixteenth_len_three.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixteenth_len_three.setText("")
        self.sixteenth_len_three.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixteenth_len_four.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixteenth_len_four.setText("")
        self.sixteenth_len_four.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixteenth_len_five.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixteenth_len_five.setText("")
        self.sixteenth_len_five.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixteenth_len_six.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixteenth_len_six.setText("")
        self.sixteenth_len_six.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixteenth_len_seven.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixteenth_len_seven.setText("")
        self.sixteenth_len_seven.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixteenth_len_eight.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixteenth_len_eight.setText("")
        self.sixteenth_len_eight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.thirtysecond_len_two.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.thirtysecond_len_two.setText("")
        self.thirtysecond_len_two.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.thirtysecond_len_three.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.thirtysecond_len_three.setText("")
        self.thirtysecond_len_three.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.thirtysecond_len_four.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.thirtysecond_len_four.setText("")
        self.thirtysecond_len_four.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.thirtysecond_len_five.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.thirtysecond_len_five.setText("")
        self.thirtysecond_len_five.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.thirtysecond_len_six.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.thirtysecond_len_six.setText("")
        self.thirtysecond_len_six.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.thirtysecond_len_seven.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.thirtysecond_len_seven.setText("")
        self.thirtysecond_len_seven.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.thirtysecond_len_eight.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.thirtysecond_len_eight.setText("")
        self.thirtysecond_len_eight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixtyfourth_timesig_two.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixtyfourth_timesig_two.setText("")
        self.sixtyfourth_timesig_two.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixtyfourth_timesig_three.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixtyfourth_timesig_three.setText("")
        self.sixtyfourth_timesig_three.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixtyfourth_timesig_four.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixtyfourth_timesig_four.setText("")
        self.sixtyfourth_timesig_four.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixtyfourth_timesig_five.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixtyfourth_timesig_five.setText("")
        self.sixtyfourth_timesig_five.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixtyfourth_timesig_six.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixtyfourth_timesig_six.setText("")
        self.sixtyfourth_timesig_six.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixtyfourth_timesig_seven.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixtyfourth_timesig_seven.setText("")
        self.sixtyfourth_timesig_seven.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.sixtyfourth_timesig_eight.setInputMask(QCoreApplication.translate("MainWindow", u"00", None))
        self.sixtyfourth_timesig_eight.setText("")
        self.sixtyfourth_timesig_eight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Key Signature", None))
        self.keysig_pitch_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.keysig_pitch_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.keysig_pitch_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.keysig_pitch_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.keysig_pitch_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.keysig_pitch_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.keysig_pitch_combo.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))

        self.keysig_acc_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"\u266e", None))
        self.keysig_acc_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"\u266f", None))
        self.keysig_acc_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"\u266d", None))

        self.keysig_scale_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Major", None))
        self.keysig_scale_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Minor", None))
        self.keysig_scale_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Minor (harmonic)", None))
        self.keysig_scale_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Minor (melodic)", None))

        self.atonal_check.setText(QCoreApplication.translate("MainWindow", u"Atonal", None))
        self.ranges_label_2.setText(QCoreApplication.translate("MainWindow", u"Range Boundaries", None))
        self.sharp_ranges.setText(QCoreApplication.translate("MainWindow", u"\u266f", None))
        self.flat_ranges.setText(QCoreApplication.translate("MainWindow", u"\u266d", None))
        self.right_range_label.setText(QCoreApplication.translate("MainWindow", u"Right Hand:", None))
        self.right_lower_display.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.dash_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_upper_display.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.length_label_5.setText(QCoreApplication.translate("MainWindow", u"Span:", None))
        self.right_span_display.setText(QCoreApplication.translate("MainWindow", u"///", None))
        self.right_lower_label.setText(QCoreApplication.translate("MainWindow", u"Lower", None))
        self.right_upper_label.setText(QCoreApplication.translate("MainWindow", u"Upper", None))
        self.left_range_label.setText(QCoreApplication.translate("MainWindow", u"Left Hand:", None))
        self.left_lower_display.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.dash_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_upper_display.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.left_span_label.setText(QCoreApplication.translate("MainWindow", u"Span:", None))
        self.left_span_display.setText(QCoreApplication.translate("MainWindow", u"///", None))
        self.lh_range1_label_4.setText(QCoreApplication.translate("MainWindow", u"Lower", None))
        self.lef.setText(QCoreApplication.translate("MainWindow", u"Upper", None))
        self.anchors_label.setText(QCoreApplication.translate("MainWindow", u"Anchors", None))
        self.anchor_templates_label.setText(QCoreApplication.translate("MainWindow", u"Templates", None))
        self.anchors_config_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Tom's Standard", None))
        self.anchors_config_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Tight", None))
        self.anchors_config_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Loose", None))
        self.anchors_config_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"High Sprawl", None))
        self.anchors_config_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.anchors_save_template.setText(QCoreApplication.translate("MainWindow", u"Save New Custom", None))
        self.anchors_refresh_template.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.anchors_delete_template.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.gravity_label.setText(QCoreApplication.translate("MainWindow", u"Gravity", None))
        self.tertiary_spawn_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.secondary_spawn_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.secondary_longevity_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.spawn_label.setText(QCoreApplication.translate("MainWindow", u"Spawn Rate", None))
        self.tertiary_longevity_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.primary_label.setText(QCoreApplication.translate("MainWindow", u"Primary Anchor", None))
        self.primary_gravity_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.secondary_label.setText(QCoreApplication.translate("MainWindow", u"Secondary Anchor", None))
        self.secondary_gravity_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.tertiary_label.setText(QCoreApplication.translate("MainWindow", u"Tertiary Anchor", None))
        self.NA.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.tertiary_gravity_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.NA2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.longevity_label.setText(QCoreApplication.translate("MainWindow", u"Longevity", None))
        self.tertiary_velocity_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.secondary_velocity_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.anchor_strength_label_22.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.primary_velocity_display.setText(QCoreApplication.translate("MainWindow", u"###", None))
        self.compose_active_configuration_label.setText(QCoreApplication.translate("MainWindow", u"Configuration: ", None))
        self.compose_active_configuration_display.setText(QCoreApplication.translate("MainWindow", u"///placeholder///", None))
        self.loaf_config_btn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.save_config_btn.setText(QCoreApplication.translate("MainWindow", u"Save Active", None))
        self.label.setText("")
        self.composition_name_entry.setText("")
        self.composition_name_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Composition Name", None))
        self.compose_btn.setText(QCoreApplication.translate("MainWindow", u"Compose", None))
        self.label_2.setText("")
        self.filepath_display.setText(QCoreApplication.translate("MainWindow", u"Filepath", None))
        self.length_label.setText(QCoreApplication.translate("MainWindow", u"Segment Length (measures)", None))
        self.length_entry.setInputMask(QCoreApplication.translate("MainWindow", u"99", None))
        self.length_entry.setText("")
        self.length_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"#", None))
        self.corner_logo.setText("")
        self.version_display.setText(QCoreApplication.translate("MainWindow", u"Masterpiece Studio v 0.8", None))
        self.active_style_label.setText(QCoreApplication.translate("MainWindow", u"Active Syle:", None))
        self.active_configuration_label.setText(QCoreApplication.translate("MainWindow", u"Active Configuration:", None))
        self.topBar_active_style_display.setText(QCoreApplication.translate("MainWindow", u"///placeholder///", None))
        self.topBar_active_configuration_display.setText(QCoreApplication.translate("MainWindow", u"///placeholder///", None))
    # retranslateUi

