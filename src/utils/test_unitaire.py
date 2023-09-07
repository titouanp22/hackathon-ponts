def test_txt(path):
    filename_test = os.path.join(os.path.dirname(__file__), path)
    document_test = open_text_file(filename_test)
    return document_test


if test_txt("test.txt") == "bonjour filo":
    print(True)
else:
    print(False)
