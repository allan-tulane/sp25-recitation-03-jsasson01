from main import quadratic_multiply, BinaryNumber



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(8)) == 1 * 8
    assert quadratic_multiply(BinaryNumber(20), BinaryNumber(3)) == 20 * 3
    assert quadratic_multiply(BinaryNumber(1111123), BinaryNumber(7869)) == 1111123 *7869
