# Uncommon Python Error: Missed ZeroDivisionError

This example shows a case where a `ZeroDivisionError` in Python might be missed due to conditional logic.  The function `function_with_uncommon_error` only raises the error when called with an input of 0. If this function is not always called with zero, a programmer may never see the actual runtime error.

The solution provides ways to avoid this.