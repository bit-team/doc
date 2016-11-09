#!/usr/bin/env python3
#    Copyright (C) 2016 Germar Reitze
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import sys
import os
import subprocess
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from tempfile import TemporaryDirectory, NamedTemporaryFile
from time import sleep
from datetime import date, time, datetime, timedelta

os.environ['LANGUAGE'] = 'en_US.UTF-8'

sys.path.insert(0, '../backintime/common')
sys.path.insert(0, '../backintime/qt')
import app
import settingsdialog
import qttools
import config
import snapshots
from guiapplicationinstance import GUIApplicationInstance

def setScreenshotTimer(widget, filename, width = 720, hight = 480):
    widget.move(100, 50)
    widget.resize(width, hight)
    widget.show()
    scrTimer = QTimer(widget)
    scrTimer.setInterval(1000)
    scrTimer.setSingleShot(True)
    scrTimer.timeout.connect(lambda: takeScreenshot(filename))

    quitTimer = QTimer(widget)
    quitTimer.setInterval(1500)
    quitTimer.setSingleShot(True)
    quitTimer.timeout.connect(widget.close)

    scrTimer.start()
    quitTimer.start()
    qapp.exec_()

def takeScreenshot(filename):
    cmd = ['scrot', '-b', '-u', filename]
    # print(cmd)
    proc = subprocess.Popen(cmd)
    proc.communicate()

with TemporaryDirectory() as tmp:
    cfgFile = os.path.join(tmp, 'config')
    appInstanceFile = os.path.join(tmp, 'appinstance')
    cfg = config.Config(cfgFile)
    appInstance = GUIApplicationInstance(appInstanceFile, '')

    cfg.setSnapshotsPath(tmp)
    cfg.setInclude([('/home/janedoe', 0),])
    cfg.checkConfig()

    sn = snapshots.Snapshots(cfg)

    for d, t in ((date.today(), time(hour = 21, minute = 10, second = 14)),
                 (date.today(), time(hour = 17, minute = 53, second = 52)),
                 (date.today(), time(hour = 11, minute = 22, second = 3)),
                 (date.today() - timedelta(1), time(hour = 15, minute = 8,  second = 25)),
                 (date.today() - timedelta(3), time(hour = 19, minute = 43, second = 13)),
                 (date.today() - timedelta(4), time(hour = 16, minute = 25, second = 47)),
                 (date.today() - timedelta(13), time(hour = 14, minute = 38,  second = 11)),
                 ):
        sid = snapshots.SID(datetime.combine(d, t), cfg)
        sid.makeDirs()

    global qapp
    qapp = qttools.createQApplication(cfg.APP_NAME)
    translator = qttools.translator()
    qapp.installTranslator(translator)

    ###################
    ### Main Window ###
    ###################

    mainWindow = app.MainWindow(cfg, appInstance, qapp)
    mainWindow.openPath('/home/janedoe')
    # fix column width
    mainWindow.mainSplitter.setSizes([120, 450])
    mainWindow.secondSplitter.setSizes([110, 300])
    mainWindow.filesView.header().resizeSection(0, 135)
    mainWindow.filesView.header().resizeSection(1, 45)

    setScreenshotTimer(mainWindow, '_images/main_window.png')

    #################################
    ### Settings Dialog - General ###
    #################################

    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.editSnapshotsPath.setText('/media/janedoe/ExternalDrive')
    settings.txtHost.setText('testhost')
    settings.txtUser.setText('janedoe')
    settings.setComboValue(settings.comboSchedule, cfg._2_HOURS)

    setScreenshotTimer(settings, '_images/settings_general.png')

    # local encrypted
    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.setComboValue(settings.comboModes, 'local_encfs')
    settings.txtPassword1.setText('123456789012345678')

    settings.editSnapshotsPath.setText('/media/janedoe/ExternalDrive')
    settings.txtHost.setText('testhost')
    settings.txtUser.setText('janedoe')
    settings.setComboValue(settings.comboSchedule, cfg._2_HOURS)

    setScreenshotTimer(settings, '_images/settings_general_local_encrypted.png')

    # SSH
    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.setComboValue(settings.comboModes, 'ssh')
    settings.txtSshHost.setText('192.168.0.42')
    settings.txtSshUser.setText('jane')
    settings.txtSshPath.setText('/mnt/backup/')
    settings.txtSshPrivateKeyFile.setText('/home/janedoe/.ssh/id_rsa')
    settings.txtPassword1.setText('12345678901234')

    settings.txtHost.setText('testhost')
    settings.txtUser.setText('janedoe')
    settings.setComboValue(settings.comboSchedule, cfg._2_HOURS)

    setScreenshotTimer(settings, '_images/settings_general_ssh.png')

    # SSH encrypted
    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.setComboValue(settings.comboModes, 'ssh_encfs')
    settings.txtSshHost.setText('192.168.0.42')
    settings.txtSshUser.setText('jane')
    settings.txtSshPath.setText('/mnt/backup/')
    settings.txtSshPrivateKeyFile.setText('/home/janedoe/.ssh/id_rsa')
    settings.txtPassword1.setText('12345678901234')
    settings.txtPassword2.setText('123456789012345678')

    settings.txtHost.setText('testhost')
    settings.txtUser.setText('janedoe')
    settings.setComboValue(settings.comboSchedule, cfg._2_HOURS)

    setScreenshotTimer(settings, '_images/settings_general_ssh_encrypted.png')

    #################################
    ### Settings Dialog - Include ###
    #################################

    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.tabs.setCurrentIndex(1)

    setScreenshotTimer(settings, '_images/settings_include.png')

    #################################
    ### Settings Dialog - Exclude ###
    #################################

    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.tabs.setCurrentIndex(2)

    setScreenshotTimer(settings, '_images/settings_exclude.png')

    ####################################
    ### Settings Dialog - Autoremove ###
    ####################################

    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.tabs.setCurrentIndex(3)

    setScreenshotTimer(settings, '_images/settings_autoremove.png')

    #################################
    ### Settings Dialog - Options ###
    #################################

    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.tabs.setCurrentIndex(4)

    setScreenshotTimer(settings, '_images/settings_options.png')

    ########################################
    ### Settings Dialog - Expert Options ###
    ########################################

    settings = settingsdialog.SettingsDialog(mainWindow)
    settings.tabs.setCurrentIndex(5)

    setScreenshotTimer(settings, '_images/settings_expert_options.png',
                       hight = 650)
