from ....utils import W3CTestCase

class TestAnonymousInlineWhitespace(W3CTestCase):
    vars().update(W3CTestCase.find_tests(__file__, 'anonymous-inline-whitespace-'))
