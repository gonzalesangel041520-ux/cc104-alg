def outer():
    message='Original'
    def inner():
        nonlocal message
        message='Updated inside inner function'
    inner()
    print(message)
outer()
