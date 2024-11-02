from utils import memoize
from unittest.mock import patch

class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches the result of a method call"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)
            self.assertEqual(instance.a_property, 42)
            mock_method.assert_called_once()

if __name__ == "__main__":
    unittest.main()
