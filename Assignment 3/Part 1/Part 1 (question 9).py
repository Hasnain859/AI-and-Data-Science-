def check_pass_fail(score):
    if score > 60:
        return "Pass"
    else:
        return "Fail"
print(check_pass_fail(75))  # Output: Pass
print(check_pass_fail(45))  # Output: Fail
print(check_pass_fail(60))  # Output: Fail
