{
  """  
BLOCK Exception_Config
ON BLOCK ERROR all
    SET EXCEPTION TO $'''TRUE'''
END
    # FLOW CONFIG
    # EXTRAINDO DADOS DA PLANILHA DE CONFIG
    Excel.LaunchExcel.LaunchAndOpenUnderExistingProcess Path: $'''%UserProfile%\\OneDrive\\%ComputerName%\\Nome_da_pasta\\RPA 004 - Nome_RPA\\Input\\Config.xlsx''' Visible: False ReadOnly: False Instance=> ExcelInstanceConfig
    Excel.ReadFromExcel.ReadAllCells Instance: ExcelInstanceConfig ReadAsText: False FirstLineIsHeader: True RangeValue=> ExcelDataConfig
    Excel.CloseExcel.Close Instance: ExcelInstanceConfig
    # EXTRAINDO DADOS DA CONFIG DATATABLE
    SET PathInput TO ExcelDataConfig[
    0
  ][
    1
  ]
    SET PathOutput TO ExcelDataConfig[
    1
  ][
    1
  ]
    SET fileWorksheetCambioPetroleo TO ExcelDataConfig[
    2
  ][
    1
  ]
    SET UrlBCBR TO ExcelDataConfig[
    3
  ][
    1
  ]
    SET UrlEIA TO ExcelDataConfig[
    4
  ][
    1
  ]
    SET fileLog TO ExcelDataConfig[
    5
  ][
    1
  ]
    Text.Replace Text: fileLog TextToFind: $'''[DATE
  ]''' IsRegEx: False IgnoreCase: False ReplaceWith: DateTimeText ActivateEscapeSequences: False Result=> fileLog
    Folder.Create FolderPath: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%''' FolderName: DateTimeText Folder=> NewFolder
    # CRIAÇÃO DO LOG
    File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''Nome_do_RPA
    %DateTime%
    INICIOU A EXECUÇÃO''' AppendNewLine: True IfFileExists: File.IfFileExists.Overwrite Encoding: File.FileEncoding.Unicode
END
"""
}