
def test_method(num):
    tot = 0
    print("hello world")

    for i in range(num):
        print(f"testing for CI/CD {i}")
        tot += num
    return tot


if __name__ == "__main__":
    test_method(5)
