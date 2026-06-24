from .common import StaticTestBase


class TestGuardPhi(StaticTestBase):

    def test_phi_merge(self):
        codestr = """
        from __static__ import int64

        def f(flag: bool, a: int64, b: int64):
            if flag:
                x = a
            else:
                x = b
            return x
        """

        code = self.compile(codestr)
        f = self.find_code(code, "f")

        self.assertInBytecode(f, "LOAD_LOCAL")

    def test_loop_phi(self):
        codestr = '''
        from __static__ import int64

        def f():
            i: int64 = 0

            while i < 100:
                i += 1

            return i
        '''
        code = self.compile(codestr)
        f = self.find_code(code, "f")

        self.assertInBytecode(f, "LOAD_LOCAL")
