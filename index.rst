.. Back In Time documentation master file, created by
   sphinx-quickstart on Sun Mar 20 20:28:50 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Back In Time's documentation!
========================================

Contents:
+++++++++

.. toctree::
    :maxdepth: 2

    mainwindow
    settings
    snapshotsdialog
    log

------------

Introduction
++++++++++++

.. image:: _images/main_window.png
    :target: _images/main_window.png
    :alt:    Back In Time main window
    :align:  left

`Back In Time` is a simple backup solution for Linux Desktops. It is based on
``rsync`` and uses hard-links to reduce space used for unchanged files.
It comes with a Qt5 GUI which will run on both Gnome and KDE based Desktops.
`Back In Time` is written in Python3 and is licensed under GPL2.

Backups are stored in plain text. They can be browesed with a normal filebrowser
or in Terminal which makes it possible to restore files even without
`Back in Time`. Files ownership, group and permissions are stored in a
separate compressed plain text file (``fileinfo.bz2``). If the backup drive
does not support permissions `Back in Time` will restore permissions from
``fileinfo.bz2``. So if you restore files without `Back in Time`, permissions
could get lost.
