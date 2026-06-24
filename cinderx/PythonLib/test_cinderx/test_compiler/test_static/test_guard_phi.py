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
        f_code = self.find_code(code, "f")

        self.assertInBytecode(f_code, "LOAD_LOCAL")

        mod = self.in_module(codestr).__enter__()

        self.assertEqual(mod.f(True, 10, 20), 10)
        self.assertEqual(mod.f(False, 10, 20), 20)

    def test_loop_phi(self):
        codestr = """
        from __static__ import int64

        def f():
            i: int64 = 0

            while i < 100:
                i += 1

            return i
        """

        code = self.compile(codestr)
        f_code = self.find_code(code, "f")

        self.assertInBytecode(f_code, "LOAD_LOCAL")
        self.assertInBytecode(f_code, "PRIMITIVE_BINARY_OP")
        self.assertInBytecode(f_code, "PRIMITIVE_COMPARE_OP")

        mod = self.in_module(codestr).__enter__()

        self.assertEqual(mod.f(), 100)

    def test_nested_phi(self):
        codestr = """
        from __static__ import int64

        def f(a: bool, b: bool):
            x: int64 = 42

            if a:
                y = x
            else:
                y = x

            if b:
                z = y
            else:
                z = y

            return z + 1
        """

        code = self.compile(codestr)
        f_code = self.find_code(code, "f")

        self.assertInBytecode(f_code, "LOAD_LOCAL")

        mod = self.in_module(codestr).__enter__()

        self.assertEqual(mod.f(True, True), 43)
        self.assertEqual(mod.f(True, False), 43)
        self.assertEqual(mod.f(False, True), 43)
        self.assertEqual(mod.f(False, False), 43)

    def test_deep_phi_chain(self):
        codestr = """
        from __static__ import int64

        def f(a: bool, b: bool, c: bool):
            x: int64 = 100

            if a:
                p1 = x
            else:
                p1 = x

            if b:
                p2 = p1
            else:
                p2 = p1

            if c:
                p3 = p2
            else:
                p3 = p2

            return p3 + 7
        """

        code = self.compile(codestr)
        f_code = self.find_code(code, "f")

        self.assertInBytecode(f_code, "LOAD_LOCAL")

        mod = self.in_module(codestr).__enter__()

        self.assertEqual(mod.f(True, True, True), 107)
        self.assertEqual(mod.f(True, False, True), 107)
        self.assertEqual(mod.f(False, True, False), 107)
        self.assertEqual(mod.f(False, False, False), 107)
