# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)#使用这个方法打印日志

main()
print('END')#当捕获了异常后，这一句可以被执行，不会直接退出