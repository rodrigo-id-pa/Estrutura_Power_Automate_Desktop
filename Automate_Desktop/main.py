{
    """
    # FLOW MAIN
    # SETANDO EXCEPTION COMO FALSE
    SET EXCEPTION TO $'''FALSE'''
    # PEGANDO USERPROFILE E COMPUTER NAME DE ACORDO COM A MAQUINA QUE ESTA EXECUTANDO
    System.GetEnvironmentVariable.GetEnvironmentVariable Name: $'''USERPROFILE''' Value=> UserProfile
    System.GetEnvironmentVariable.GetEnvironmentVariable Name: $'''COMPUTERNAME''' Value=> ComputerName
    # PEGANDO DATA E HORA DA EXCUÇÃO DO BOT
    DateTime.GetCurrentDateTime.Local DateTimeFormat: DateTime.DateTimeFormat.DateAndTime CurrentDateTime=> DateTime
    Text.ConvertDateTimeToText.FromCustomDateTime DateTime: DateTime CustomFormat: $'''dd-MM-yyyy_hh-mm''' Result=> DateTimeText
    # INICIANDO FLOW CONFIG
    CALL Config
    IF EXCEPTION = $'''FALSE''' THEN
        File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''FLOW CONFIG REALIZADO COM SUCESSO''' AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.Unicode
        DISABLE CALL Nome_subfluxo_rpa
    ELSE
        ERROR => LastError
        File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''ERROR: %LastError%''' AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.Unicode
    END
    IF EXCEPTION = $'''FALSE''' THEN
        File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''FLOW EXTRAIR RPA REALIZADO COM SUCESSO''' AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.Unicode
        DISABLE CALL Nome_subfluxo2_rpa
    ELSE
        ERROR => LastError
        File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''ERROR: %LastError%''' AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.Unicode
    END
    IF EXCEPTION = $'''FALSE''' THEN
        File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''FLOW EXTRAIR PREÇO PETRÓLEO REALIZADO COM SUCESSO''' AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.Unicode
        DISABLE CALL Nome_subfluxo3_rpa
    ELSE
        ERROR => LastError
        File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''ERROR: %LastError%''' AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.Unicode
    END
    IF EXCEPTION = $'''FALSE''' THEN
        File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''FLOW ATUALIZAR PLANILHA REALIZADO COM SUCESSO''' AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.Unicode
    ELSE
        ERROR => LastError
        File.WriteText File: $'''%UserProfile.Trimmed%%PathOutput.Trimmed%\\%DateTimeText%%fileLog%''' TextToWrite: $'''ERROR: %LastError%''' AppendNewLine: True IfFileExists: File.IfFileExists.Append Encoding: File.FileEncoding.Unicode
    END
    SET ErroProcess TO EXCEPTION
END FUNCTION
"""
}
