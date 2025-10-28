# export QT_PLUGIN_PATH=$(python3 -c "import PySide6; import os; print(os.path.join(os.path.dirname(PySide6.__file__), 'plugins'))")
# export QML2_IMPORT_PATH=$(python3 -c "import PySide6; import os; print(os.path.join(os.path.dirname(PySide6.__file__), 'qml'))")
# export DYLD_LIBRARY_PATH=$(python3 -c "import PySide6; import os; print(os.path.dirname(PySide6.__file__))")
export LD_LIBRARY_PATH=$(python3 -c "import qt6_applications, os; print(os.path.join(os.path.dirname(qt6_applications.__file__), 'Qt', 'lib'))")
export QT_DEBUG_PLUGINS=1