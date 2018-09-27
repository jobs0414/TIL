score = 128
try:
    assert score <= 100, "점수는 100 이하여야 합니다."
except AssertionError as ex:
    print(ex)
else:
    print(score)