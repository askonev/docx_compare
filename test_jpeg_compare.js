builderJS.OpenFile("http://161.35.214.46:9090/files/empty.docx");
    var file = builderJS.OpenTmpFile("http://161.35.214.46:9090/files/docx/docx_with_jpg.docx");
        AscCommonWord.CompareDocuments(Api, file, null);
        file.Close();
builderJS.SaveFile("docx", "Result.docx");
builderJS.CloseFile();
