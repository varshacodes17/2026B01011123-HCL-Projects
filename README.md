File "C:\Users\ACER\Desktop\Student_Performance_Project\main.py", line 63, in <module>
    df.to_excel("students.xlsx", index=False)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\ACER\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 2268, in to_excel
    formatter.write(
    ~~~~~~~~~~~~~~~^
        excel_writer,
        ^^^^^^^^^^^^^
    ...<6 lines>...
        engine_kwargs=engine_kwargs,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\ACER\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\formats\excel.py", line 1003, in write
    writer = ExcelWriter(
        writer,
    ...<2 lines>...
        engine_kwargs=engine_kwargs,
    )
  File "C:\Users\ACER\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 58, in __init__
    super().__init__(
    ~~~~~~~~~~~~~~~~^
        path,
        ^^^^^
    ...<3 lines>...
        engine_kwargs=engine_kwargs,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\ACER\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\excel\_base.py", line 1341, in __init__
    self._handles = get_handle(
                    ~~~~~~~~~~^
        path, mode, storage_options=storage_options, is_text=False
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\ACER\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 954, in get_handle
    handle = open(handle, ioargs.mode)
PermissionError: [Errno 13] Permission denied: 'students.xlsx'
PS C:\Users\ACER\Desktop\Student_Performance_Project>