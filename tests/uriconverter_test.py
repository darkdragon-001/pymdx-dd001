import uriconverter.uriconverter as uriconverter

class TestClass:
    def test_base1(self):
        uri = 'path/invisible/../file.html#fragment'
        base = 'ftp://host/root/currentfile.md#hhh'
        result = 'ftp://host/root/path/file.html#fragment'
        assert uriconverter.urlbase(base, uri) == result

    def test_base2(self):
        uri = 'path/invisible/../file.html#fragment'
        base = 'ignore#hhh'  # filename ignored
        result = 'path/file.html#fragment'
        assert uriconverter.urlbase(base, uri) == result

    def test_base3(self):
        uri = 'path/invisible/../file.html#fragment'
        base = '.'
        result = 'path/file.html#fragment'
        assert uriconverter.urlbase(base, uri) == result

    def test_replace1(self):
        uri = 'a/b/c#fragment'
        search = 'a/b'
        replace = 'x/y'
        result = 'x/y/c#fragment'
        assert uriconverter.urlreplace(search, replace, uri) == result

    def test_replace2(self):
        uri = 'http://host/path/file?query#fragment'
        search = 'http'
        replace = 'https'
        result = 'https://host/path/file?query#fragment'
        assert uriconverter.urlreplace(search, replace, uri) == result

    def test_replace3(self):
        uri = '//host/long/path/file?query#fragment'
        search = '//host/long/path'
        replace = '//other.host/path'
        result = '//other.host/path/file?query#fragment'
        assert uriconverter.urlreplace(search, replace, uri) == result

    def test_relative1(self):
        uri = '/path/to/file1#fragment'
        base = '/path/'  # trailing slash
        result = 'to/file1#fragment'
        assert uriconverter.urlrelative(base, uri) == result

    def test_relative2(self):
        uri = '/path/to/file1#fragment'
        base = '/path/to/other/file2'  # filename ignored
        result = '../file1#fragment'
        assert uriconverter.urlrelative(base, uri) == result
